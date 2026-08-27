---
name: postgres-kernel-review
description: "Review PostgreSQL backend/kernel C changes for locking, concurrency, error handling, resource ownership, memory contexts, WAL/recovery, and hot-path performance risks."
---

# PostgreSQL Kernel Code Review

Use this skill when reviewing PostgreSQL backend/kernel C code, PostgreSQL forks, or extensions that use backend internals. It is intended for changes touching areas such as:

- `src/backend/**`, `src/include/**`
- storage, lock manager, buffer manager, WAL/recovery, executor, optimizer, access methods, replication, postmaster, background workers
- PostgreSQL extensions that use `MemoryContext`, `ResourceOwner`, `LWLock`, `SpinLock`, buffer pins, snapshots, hooks, or backend callbacks

This skill adapts PostgreSQL's public development conventions and in-tree design notes, including the PostgreSQL C dialect guidance, memory context README, ResourceOwner semantics, and subsystem README practices. Always prefer the local source tree's README and existing nearby patterns when they conflict with a generic rule.

## Review Mindset

PostgreSQL backend code is not ordinary C. The most important review question is usually:

> What happens if this code is interrupted by `ERROR`, cancellation, process exit, concurrent backend activity, crash recovery, or standby replay?

Review for correctness before style. Prioritize issues that can cause:

1. data corruption
2. deadlock or global stall
3. crash/recovery failure
4. resource leak across transaction or backend lifetime
5. user-visible wrong results
6. serious hot-path regression

## Standard Review Workflow

1. Identify touched subsystem(s) and read nearby code plus relevant in-tree README files.
2. Classify the change:
   - lock/concurrency/shared memory
   - transaction/MVCC/snapshot
   - buffer/storage/WAL/recovery
   - executor/planner
   - extension/hook/background worker
   - error/resource/memory management
3. Trace all normal exits and non-local exits:
   - `ereport(ERROR)`, `elog(ERROR)`, `PG_RE_THROW()`
   - cancel/interrupt points such as `CHECK_FOR_INTERRUPTS()`
   - transaction abort and subtransaction abort
   - process exit callbacks
4. Verify resource ownership:
   - memory belongs to the right `MemoryContext`
   - non-memory resources are released explicitly or owned by `ResourceOwner`
   - locks, buffer pins, files, catcache references, tuple descriptors, snapshots, DSM handles, and callbacks are cleaned up
5. Verify concurrency invariants:
   - lock order
   - shared memory synchronization
   - atomic/barrier usage
   - wait/signal/latch/condition variable protocol
   - recovery/standby behavior if persistent state changes
6. Ask for or inspect tests appropriate to the blast radius:
   - unit/regression tests for functional behavior
   - isolation tests for MVCC/locking changes
   - TAP tests for replication/recovery/postmaster behavior
   - crash/restart or WAL replay coverage for WAL/storage changes
   - stress or repeated runs for race-prone changes

## Output Format for Reviews

Lead with findings. Do not bury bugs in a summary.

For each finding include:

```text
[severity] file:line - concise title
What is wrong:
Why it matters:
Suggested fix:
Evidence / reasoning:
```

Severity guide:

- **Critical**: likely data corruption, recovery failure, security boundary break, or cluster-wide PANIC/deadlock.
- **High**: backend crash, deadlock/hang, leaked lock/pin/file across transaction, wrong query results.
- **Medium**: plausible resource leak, race in unusual path, missing abort cleanup, serious performance regression.
- **Low**: maintainability, diagnostics, missing comments/tests, minor performance issue.

If no issues are found, say so and mention residual risk and tests reviewed or missing.

## High-Signal Blocking Rules

Treat these as likely review blockers unless the patch gives a very strong reason:

- `SpinLock` held across `palloc`, `elog`/`ereport`, I/O, syscalls, sleeps, or complex function calls.
- `LWLock`/regular lock acquired without a guaranteed release on all `ERROR` paths.
- Buffer pin, catcache reference, tuple descriptor, file, snapshot, DSM segment, or lock not tracked by `ResourceOwner` and not explicitly released.
- Shared memory read/write without lock, atomic primitive, or documented memory barrier protocol.
- `PG_TRY` block exits via `return`, `break`, `continue`, or `goto` in a way that skips `PG_END_TRY` or cleanup.
- `PG_CATCH` swallows errors instead of cleanup plus `PG_RE_THROW()` unless this is an intentionally documented soft-failure path.
- Persistent state change without WAL, replay, logical decoding, checkpoint, or crash-recovery consideration.
- New `TopMemoryContext` allocation without bounded lifetime, eviction, or explicit ownership.
- New global lock or shared structure likely to become a scalability hotspot.
- `PANIC` or `FATAL` used for recoverable user/input/state errors.

## Locking Review Rules

### General Locking

- Lock acquisition order must match existing subsystem order and must be documented for new multi-lock protocols.
- Critical sections should be minimal: prepare data before acquiring locks; under the lock do only the state transition.
- Do not call functions that may `ERROR` while holding locks unless the lock is released by a proven cleanup mechanism.
- Do not add lock upgrades unless the existing API explicitly supports them and deadlock behavior is understood.
- For conditional acquisition, verify both success and failure paths release already-held resources.

### Spinlocks

- Use only for tiny shared-memory field updates.
- No memory allocation, logging, I/O, latch waits, condition variable waits, syscache lookups, or callbacks while held.
- No `CHECK_FOR_INTERRUPTS()` while held.
- Confirm every `SpinLockAcquire()` has a structurally obvious `SpinLockRelease()`.

### LWLocks

- Prefer shared mode when the code only reads protected state.
- Avoid waiting for regular locks, condition variables, I/O, or long computations while holding an LWLock.
- New tranches or wait events must be registered and named consistently.
- Consider known hotspots such as `ProcArrayLock`, `WALInsertLock`, `BufferMappingLock`, CLOG/SLRU locks, and lock-manager partition locks.

### Regular Locks and Proc State

- Changes around `ProcSleep`, `GrantLock`, fast-path locks, lock partitions, or `deadlock.c` must preserve deadlock detection assumptions.
- Never wait on another lock partition while holding one unless the existing lock-manager protocol allows it.
- Fields such as `MyProc->waitLock`, `waitProcLock`, `waitStatus`, and lock wait queues must only be manipulated in the expected proc/lock states.

## Concurrency and Shared Memory Rules

- Shared memory state needs a clear synchronization mechanism: lock, `pg_atomic_*`, latch protocol, condition variable protocol, or documented single-writer ownership.
- Do not use `volatile` as a substitute for synchronization.
- For lock-free publication, write payload first, use the required memory barrier, then publish the state/version visible to readers.
- Signal handlers should set flags/latches only; complex work belongs in the main loop.
- Condition variables must follow the prepare/sleep/recheck pattern and tolerate spurious wakeups.
- Latch waits must set/reset latches according to the surrounding loop's protocol.
- Background workers must register appropriate `on_shmem_exit` / `before_shmem_exit` cleanup for shared state.

## Error Handling Rules

PostgreSQL `ERROR` is a non-local jump. Memory contexts usually clean memory; they do not release all non-memory resources.

- User-facing failures should use `ereport(ERROR, (errcode(...), errmsg(...)))` with the correct SQLSTATE.
- Internal invariant failures may use `elog(ERROR, ...)` or `Assert`, but release builds must not rely on `Assert` for correctness.
- Use `FATAL` only when the backend cannot continue; use `PANIC` only for cluster-wide unrecoverable conditions.
- `PG_CATCH` should normally clean up and `PG_RE_THROW()`.
- Avoid complex business logic in `PG_CATCH`.
- Verify callbacks used during abort cannot themselves throw `ERROR`.
- If using soft-error APIs such as `errsave()` / `ereturn()`, verify callers check the return path and do not proceed with invalid state.

## Resource Management Rules

### MemoryContext

- `palloc` into a context whose lifetime matches the object:
  - per-tuple / short scratch: per-tuple or temporary child context
  - per-query: executor/query context
  - per-transaction: transaction context
  - process lifetime: `TopMemoryContext` only with explicit reason and bound
- Always restore the previous context after `MemoryContextSwitchTo()`.
- Prefer deleting/resetting a short-lived context over many individual `pfree()` calls.
- Do not keep pointers into short-lived contexts in longer-lived structs, static variables, shared memory, or caches.
- Review `repalloc` and growth loops for unbounded memory use.

### ResourceOwner and Non-Memory Resources

Resources visible outside memory contexts must be released explicitly or registered with `ResourceOwner`.

Check:

- buffer pins and buffer content locks
- relation opens/closes
- heavyweight locks
- catcache/syscache/listcache references
- tuple descriptors
- snapshots
- temporary/transient files
- DSM/DSA handles
- replication slots, logical decoding contexts, tuplestores, portals, and holdable resources

Resource release ordering matters. Resources visible to other backends generally need cleanup before locks are released, matching ResourceOwner release phases.

### Buffer Manager

- Pin before content lock; unlock before unpin unless nearby code documents a different protocol.
- Do not leave a buffer pinned across operations that can wait indefinitely or `ERROR` unless ownership is intentional.
- Page modifications must occur under the correct buffer lock and be WAL-logged when needed.
- For dirtying a page, check `MarkBufferDirty()` and WAL record ordering.

## WAL, Recovery, and Storage Rules

For persistent page or catalog changes, ask:

- Is there a WAL record?
- Does redo fully reconstruct the change after crash?
- Is the WAL record described and identified for debugging?
- Is full-page-write behavior correct?
- Is logical decoding affected?
- Are standby/recovery restrictions respected?
- Is checksum/page LSN ordering correct?
- Does the change interact with checkpoints, smgr/md files, fsync, or relation forks?

New WAL resource managers or record types need registration, redo, desc/identify support, tests, and documentation.

## MVCC, Snapshot, and Transaction Rules

- Do not bypass snapshot APIs or scan `ProcArray` directly without the correct lock/protocol.
- Tuple visibility changes must preserve `xmin`, `xmax`, infomask, hint-bit, pruning, HOT, and freeze invariants.
- Changes to heap visibility, pruning, vacuum, freezing, or index AM concurrency require isolation and recovery tests.
- Subtransaction behavior must be explicit for resources and visibility state.
- Catalog changes must preserve catcache invalidation ordering and relcache/syscache consistency.

## Planner, Executor, and Node Rules

- New node fields must be handled by copy/equal/out/read helpers where applicable.
- Executor allocations should use the appropriate per-query or per-tuple memory context.
- Per-tuple context reset behavior must not invalidate data needed after the tuple loop.
- Slot ownership and tuple lifetime must be clear.
- Parallel query code must handle DSM lifecycle, worker error paths, and leader cleanup.
- Planner transformations must preserve semantics for NULLs, volatility, collation, security barriers, lateral references, and parameterization.

## Hooks, Extensions, and Background Workers

- Hook installers must chain to previous hooks and restore or preserve hook state on unload when appropriate.
- `shared_preload_libraries` code must handle postmaster/backend process boundaries.
- Background workers need signal/latch loops, clean shutdown, transaction boundaries, and shared-memory cleanup.
- SQL-callable C functions must use `PG_FUNCTION_INFO_V1`, null checks, detoasting rules, and correct `PG_RETURN_*` macros.
- `SECURITY DEFINER` or privileged functions must fix `search_path` and avoid leaking privileged data through errors/logs.

## Performance Review Rules

Prioritize performance review on hot paths such as tuple loops, buffer access, snapshot acquisition, lock acquisition, WAL insertion, syscache lookups, executor inner loops, and planner path enumeration.

Watch for:

- repeated `palloc`/`pfree` in per-tuple loops
- repeated syscache/catcache lookups inside large loops
- unnecessary `snprintf`, string formatting, or logging in hot paths
- added global LWLock/spinlock contention
- large struct copies
- O(N^2) scans over relations, procs, buffers, locks, or paths
- excessive WAL records instead of batched logging
- extra memory growth proportional to query rows without `work_mem` or spill behavior
- timestamp/syscall calls in tight loops

If performance risk is nontrivial, ask for focused benchmark evidence such as `pgbench`, repeated regression timing, microbenchmark, or representative `EXPLAIN (ANALYZE, BUFFERS, WAL)`.

## Tests to Request by Change Type

- Lock manager / deadlock: isolation tests, stress/repeated tests, wait-event observability.
- MVCC / heap / vacuum / freeze: isolation tests, regress tests, upgrade/recovery-sensitive cases.
- WAL / storage / recovery: TAP restart/recovery tests, standby replay tests, checksums if relevant.
- Buffer manager: cassert build, stress tests, targeted crash/restart if pages are modified.
- Planner: regression tests with NULLs, volatile functions, outer joins, lateral, partitioning, permissions.
- Executor: regression tests plus memory-context and parallel-query variants when applicable.
- Replication/logical decoding: TAP tests, slot cleanup, restart_lsn/WAL retention behavior.
- Background workers/postmaster: TAP tests for start/stop/reload/crash behavior.
- Extension APIs: installcheck against supported PG versions if compatibility is claimed.

## Useful Investigation Commands

Use these when reviewing locally or debugging a suspicious patch:

```bash
git diff --check
make -s check
make -s installcheck
make -C src/test/isolation check
make -C src/test/recovery check
```

Build/debug variants:

```bash
./configure --enable-cassert --enable-debug CFLAGS="-O0 -g3"
./configure --enable-cassert --enable-debug CFLAGS="-O1 -g -fsanitize=address,undefined"
```

GDB snippets:

```gdb
bt full
p *MyProc
p num_held_lwlocks
p held_lwlocks[0]
p *MyProc->waitLock
call MemoryContextStats(TopMemoryContext)
```

Runtime observability:

```sql
SELECT pid, wait_event_type, wait_event, state, query
FROM pg_stat_activity
WHERE wait_event IS NOT NULL;

SELECT pg_blocking_pids(pid), pid, query
FROM pg_stat_activity
WHERE cardinality(pg_blocking_pids(pid)) > 0;
```

## Reference Map

Prefer local in-tree files when present:

- PostgreSQL coding conventions: `doc/src/sgml/source.sgml` / project docs
- Memory contexts: `src/backend/utils/mmgr/README`
- Function manager: `src/backend/utils/fmgr/README`
- Lock manager: `src/backend/storage/lmgr/README`
- Buffer manager: `src/backend/storage/buffer/README`
- Transaction/WAL: `src/backend/access/transam/README`
- Executor: `src/backend/executor/README`
- Planner: `src/backend/optimizer/README`
- Resource ownership: `src/include/utils/resowner.h`, `src/backend/utils/resowner/resowner.c`

Public references worth consulting:

- PostgreSQL wiki: "The PostgreSQL C Dialect"
- PostgreSQL Doxygen for current branch structs and callbacks
- pgsql-hackers discussions for subsystem-specific design decisions

## Final Review Checklist

Use this compact checklist before finalizing a review:

- [ ] Lock acquisition/release and lock order are correct.
- [ ] No blocking, allocation, logging, or error-prone work inside spinlock sections.
- [ ] Shared memory uses locks/atomics/barriers correctly.
- [ ] `ERROR` paths clean non-memory resources.
- [ ] Memory is allocated in a context with the right lifetime.
- [ ] `ResourceOwner` tracks resources that must survive until transaction cleanup.
- [ ] Buffer pins, locks, relation/cache refs, snapshots, files, DSM handles are released.
- [ ] WAL/recovery behavior is correct for persistent changes.
- [ ] MVCC/snapshot/catalog invalidation invariants are preserved.
- [ ] Hot paths avoid avoidable allocation, cache lookups, logging, and global contention.
- [ ] Tests cover functional behavior plus concurrency/recovery where relevant.
