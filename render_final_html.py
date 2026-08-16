from pathlib import Path

ROOT = Path(__file__).parent


def svg(name):
    return (ROOT / "diagrams" / f"{name}.svg").read_text(encoding="utf-8")


SOURCES = {
    "O0": ("Oracle 26ai replaces 23ai", "https://www.oracle.com/database/ai-native-database-26ai/"),
    "O1": ("Oracle 26ai Technical Architecture", "https://docs.oracle.com/en/database/oracle/oracle-database/26/dbiad/all_diagrams.html"),
    "O2": ("Oracle In-Memory Area", "https://docs.oracle.com/en/database/oracle/oracle-database/26/dbiad/db_inmemoryarea.html"),
    "O3": ("Exadata AI Smart Scan", "https://docs.oracle.com/en/engineered-systems/exadata-database-machine/dbmso/ai-vector-search.html"),
    "O4": ("Oracle Select AI Agent", "https://docs.oracle.com/en/database/oracle/oracle-database/26/selai/select-ai-agent2.html"),
    "O5": ("Autonomous AI Database MCP Server", "https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/mcp-server.html"),
    "O6": ("Oracle in-database ONNX/vector/agent example", "https://blogs.oracle.com/database/building-an-autonomous-fraud-detection-pipeline-with-autonomous-ai-database"),
    "O7": ("Oracle Autonomous AI Lakehouse", "https://www.oracle.com/autonomous-database/autonomous-ai-lakehouse/"),
    "O8": ("Oracle customer: Retraced", "https://www.oracle.com/customers/retraced/"),
    "O9": ("Oracle customer: Rappi", "https://www.oracle.com/customers/rappi/"),
    "P1": ("PolarDB IMCI architecture", "https://help.aliyun.com/en/polardb/polardb-for-mysql/user-guide/technical-background-and-architecture-of-column-store-index"),
    "P2": ("PolarDB IMCI technical approach", "https://help.aliyun.com/en/polardb/polardb-for-mysql/htap-based-real-time-data-analysis-in-polardb"),
    "P3": ("PolarDB AutoIndex/Redo synchronization", "https://help.aliyun.com/en/polardb/polardb-for-mysql/user-guide/automatic-non-sense-speed-autoindex"),
    "P4": ("PolarDB for AI and NL2SQL", "https://help.aliyun.com/en/polardb/polardb-for-mysql/polardb-for-ai-nl2sql-commercialized"),
    "P5": ("Enable PolarDB for AI / AI nodes", "https://help.aliyun.com/en/polardb/polardb-for-mysql/enable-the-polardb-for-ai-feature"),
    "P6": ("PolarDB Data-Agent", "https://help.aliyun.com/en/polardb/polardb-for-mysql/db-agent/"),
    "P7": ("PolarDB IMCI RAG implementation", "https://help.aliyun.com/zh/polardb/polardb-for-mysql/building-a-retrieval-enhancement-rag-system-based-on-polardb-imci"),
    "P8": ("PolarDB customer: Yadea", "https://help.aliyun.com/en/polardb/polardb-for-mysql/electric-vehicle-manufacturing-yadi-technology-group-co-ltd"),
    "B1": ("OceanBase AI Database / Lakebase", "https://www.oceanbase.com/solution/ai"),
    "B2": ("OceanBase AI function service", "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005682097"),
    "B3": ("OceanBase AI model registration", "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005682098"),
    "B4": ("OceanBase Iceberg via External Catalog", "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006326202"),
    "B5": ("OceanBase external data access and limits", "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006326199"),
    "B6": ("OceanBase Spark Catalog integration", "https://www.oceanbase.com/docs/common-best-practices-1000000002808478"),
    "B7": ("OceanBase semantic index", "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005682088"),
    "D1": ("Databricks Lakebase architecture", "https://docs.databricks.com/aws/en/oltp/projects/architecture"),
    "D2": ("Databricks Lakebase storage architecture", "https://docs.databricks.com/aws/en/oltp/projects/storage-architecture"),
    "D3": ("Databricks LTAP architecture", "https://docs.databricks.com/aws/en/oltp/projects/ltap-overview"),
    "D4": ("Databricks Unity AI Gateway", "https://docs.databricks.com/aws/en/ai-gateway/"),
    "D5": ("Databricks agents", "https://docs.databricks.com/aws/en/agents/custom-agents/build-agents"),
    "D6": ("Databricks AI Search", "https://docs.databricks.com/aws/en/ai-search/ai-search"),
    "D7": ("Databricks Supervisor Agent", "https://docs.databricks.com/aws/en/agents/agent-bricks/multi-agent-supervisor"),
    "D8": ("Databricks customer: FinThrive", "https://www.databricks.com/customers/finthrive/agent-bricks"),
}


def refs(*ids):
    return " ".join(f'<a class="ref" href="{SOURCES[i][1]}" target="_blank">[{i}]</a>' for i in ids)


source_list = "\n".join(
    f'<li id="src-{sid}"><strong>[{sid}]</strong> '
    f'<a href="{url}" target="_blank">{title}</a></li>'
    for sid, (title, url) in SOURCES.items()
)

html = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI 时代数据库内核增强、库仓一体与 Agent 架构证据报告</title>
<style>
:root{{--bg:#f8fafc;--card:#fff;--text:#0f172a;--muted:#475569;--line:#dbe4ef;
--blue:#2563eb;--green:#16a34a;--cyan:#0891b2;--orange:#ea580c;--gray:#64748b}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--text);
font:15px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}}
.page{{max-width:1220px;margin:auto;padding:32px 22px 60px}}
header{{background:#0f172a;color:#fff;border-radius:18px;padding:38px 40px}}
h1{{font-size:30px;margin:0 0 12px}} header p{{color:#cbd5e1;margin:6px 0}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:28px 32px;margin:22px 0}}
h2{{font-size:22px;border-bottom:2px solid var(--line);padding-bottom:10px}}
h3{{font-size:18px;color:#1e3a8a;margin-top:30px}} h4{{font-size:15px;margin:20px 0 8px}}
a{{color:#0369a1;text-decoration:none}} a:hover{{text-decoration:underline}}
.ref{{font-size:12px;font-weight:700;margin-left:2px}}
.fact{{background:#eff6ff;border-left:4px solid var(--blue);padding:14px 18px;border-radius:8px}}
.warn{{background:#fff7ed;border-left:4px solid var(--orange);padding:14px 18px;border-radius:8px}}
.evidence{{background:#f0fdf4;border-left:4px solid var(--green);padding:14px 18px;border-radius:8px}}
.diagram{{border:1px solid var(--line);border-radius:12px;padding:10px;margin:18px 0;background:#fff}}
.caption{{font-size:13px;color:var(--muted);margin:8px 4px}}
.legend{{display:flex;flex-wrap:wrap;gap:8px 18px;padding:10px 14px;background:#f1f5f9;border-radius:8px;font-size:12px}}
.dot{{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px}}
table{{width:100%;border-collapse:collapse;font-size:13.5px;margin:16px 0}}
th,td{{border:1px solid var(--line);padding:10px 12px;vertical-align:top}} th{{background:#f1f5f9;text-align:left}}
code{{background:#f1f5f9;padding:1px 5px;border-radius:4px}} li{{margin:7px 0}}
.status{{display:inline-block;font-size:11px;border-radius:999px;padding:2px 8px;font-weight:700}}
.ga{{background:#dcfce7;color:#166534}} .roadmap{{background:#fef3c7;color:#92400e}}
.unknown{{background:#e2e8f0;color:#334155}} .sources li{{font-size:13px}}
@media(max-width:760px){{header,.card{{padding:22px 17px}}h1{{font-size:24px}}table{{font-size:12px}}}}
</style></head>
<body><main class="page">
<header>
<h1>AI 时代数据库内核增强、库仓一体与 Agent 架构证据报告</h1>
<p>重点厂商：Oracle 23ai/26ai、阿里云 PolarDB、OceanBase、Databricks</p>
<p>原则：厂商事实只采用官方文档、官方产品页和官方客户案例；未披露的内部实现明确标注，不以推断代替事实。</p>
</header>

<section class="card">
<h2>1. 先给结论：四家都在利用既有数据，但实现路径并不相同</h2>
<table>
<tr><th>厂商</th><th>既有数据在哪里</th><th>如何补 AP/仓</th><th>如何补 AI/Agent</th><th>关键区别</th></tr>
<tr><td><strong>Oracle 26ai</strong></td><td>Oracle 行格式业务数据、外部 Iceberg</td>
<td>数据库实例 SGA 内同时维护 Buffer Cache 行格式和 IM Column Store 列格式；优化器透明选择</td>
<td>VECTOR/ONNX/Select AI Agent 在数据库能力体系内；Autonomous DB 提供托管 MCP</td>
<td>最典型的“增强单一数据库内核”路线</td></tr>
<tr><td><strong>PolarDB</strong></td><td>InnoDB 行存与 PolarDB 共享存储</td>
<td>把 IMCI 做成 InnoDB 列存二级索引，在 RO/Standby 通过 Redo/物理复制维护</td>
<td>专属 AI 节点或 Serverless 资源，通过 SQL 提供 MLOps、NL2SQL、Data-Agent</td>
<td>内核 HTAP + 独立 AI 算力节点，资源隔离清晰</td></tr>
<tr><td><strong>OceanBase</strong></td><td>OceanBase 事务数据；OSS/S3/HDFS 中外部数据</td>
<td>现有 HTAP/混合行列能力；External Catalog 把 Iceberg/Hive/文件纳入 SQL；Lakebase 产品路线进一步强调对象存储和开放计算</td>
<td>内核提供向量/全文/语义索引及 SQL AI 函数；模型 endpoint 在外部；上层有 Fork/上下文产品</td>
<td>已发布能力与 Lakebase 方案路线必须分开看</td></tr>
<tr><td><strong>Databricks</strong></td><td>Delta/Iceberg 湖数据和 Lakebase Postgres 数据</td>
<td>LTAP 在 Lakebase 存储物化时把行式 Postgres 转码为 Parquet，让 Postgres 与 Lakehouse//RT 使用单一逻辑副本</td>
<td>AI Search 是独立托管索引；Agent Bricks 是托管 Agent 服务；Unity Catalog/AI Gateway 统一治理</td>
<td>从湖仓向 OLTP 扩展，不是把所有能力塞进一个数据库进程</td></tr>
</table>
<div class="warn"><strong>纠正此前报告中的不严谨表述：</strong>
Oracle MCP 不是客户必须自建的 Sidecar；Oracle IM Column Store 的公开机制是数据库后台进程填充/重填，不应写成 Redo 直灌；
PolarDB AI 节点是官方独立节点/Serverless 资源，不应笼统写成同机 Sidecar；
OceanBase Lakebase 的部分内部进程边界尚未公开，不能自行判定全部位于数据库内核。</div>
</section>

<section class="card">
<h2>2. Oracle 23ai/26ai：真正以数据库内核为中心的“TP + AP + AI + 湖”</h2>
<p>Oracle Database 26ai 是 23ai 的后续长期支持版本，官方说明可通过 2025 年 10 月 Release Update 从 23ai 过渡到 26ai。{refs("O0")}</p>
<div class="diagram">{svg("oracle-26ai-architecture")}</div>
<p class="caption">图中 [O*] 与本报告参考资料一一对应；分类表示公开资料可确认的组件落点，不表示 Oracle 未公开的内部微服务拓扑。</p>

<h3>2.1 通过什么方式把“仓”加进数据库</h3>
<ul>
<li><strong>双格式而非外部复制：</strong>同一数据库实例的 SGA 内，Buffer Cache 保存行格式，IM Column Store 保存列格式。Oracle 会把 OLTP 点查路由到行格式，把扫描、Join、聚合路由到列格式；同一查询还可同时读取两者。{refs("O1","O2")}</li>
<li><strong>列格式维护机制：</strong>DML 修改首先进入 Buffer Cache 和持久化路径；IMCO、SMCO、Wnnn 等数据库后台进程根据 metadata invalidation 与查询请求进行列存填充和重填。公开资料并未把它描述为外部 CDC 或客户部署的复制服务。{refs("O1")}</li>
<li><strong>AP 执行能力：</strong>IM Column Store 支持列式压缩、扫描和 SIMD/deep vectorization，因此是在数据库内核内部增强 AP，而不是另建一个数仓产品。{refs("O2")}</li>
</ul>

<h3>2.2 AI 如何和既有业务数据结合</h3>
<ul>
<li><strong>内核数据类型和执行：</strong>AI Vector Search 与关系、JSON、Graph 等处于 converged database 体系；业务条件过滤和向量相似搜索可在同一数据库查询中完成。{refs("O0","O1")}</li>
<li><strong>Embedding 两种路径：</strong>可以调用外部模型提供商，也可以把 ONNX embedding 模型加载到数据库并在数据库 CPU 上推理。官方反欺诈示例明确说明后者不需要第三方向量库或外部 embedding API。{refs("O6")}</li>
<li><strong>Agent 不是泛泛的外部框架：</strong>Select AI Agent 由 <code>DBMS_CLOUD_AI_AGENT</code> 管理，包含 Planning、Tool Use、Reflection、Memory；工具可以是 NL2SQL、RAG、PL/SQL 或 REST。{refs("O4")}</li>
<li><strong>MCP 部署边界：</strong>Autonomous AI Database 提供每数据库的托管、多租户 MCP Server，客户启用后获得 endpoint，无需自行部署 MCP 服务器基础设施。{refs("O5")}</li>
</ul>

<h3>2.3 如何把“湖”接进来</h3>
<p>Autonomous AI Lakehouse 通过 Apache Iceberg 在数据原位置运行 Oracle SQL、Vector、Graph、Spatial 等能力，并由统一 Catalog 发现外部数据；Data Lake Accelerator 和缓存用于加速。这里是<strong>数据库计算能力访问开放湖表</strong>，不是把所有湖数据先复制进 Oracle。{refs("O7")}</p>

<h3>2.4 已有客户证据</h3>
<ul>
<li><strong>Retraced：</strong>在原有 Autonomous Database 数据上使用 26ai Vector Search 和 Select AI；向量化供应商数据后，官方案例称重复记录减少 80%。{refs("O8")}</li>
<li><strong>Rappi：</strong>选择 Autonomous AI Database 与 AI Vector Search，把 AI 带到现有目录数据所在地，官方案例称搜索响应延迟降低 40%。{refs("O9")}</li>
</ul>
</section>

<section class="card">
<h2>3. 阿里云 PolarDB：内核 IMCI 做 HTAP，独立 AI 节点做 Data+AI</h2>
<div class="diagram">{svg("polardb-imci-ai-architecture")}</div>

<h3>3.1 IMCI 不是旁挂数仓，而是 InnoDB 内的列存二级索引</h3>
<ul>
<li>PolarDB 没有选择实现一个完全分离的列存 Storage Engine，而是在 InnoDB 中实现 Columnar Secondary Index，以复用事务、Redo、物理复制和 MySQL 兼容性。{refs("P1","P2")}</li>
<li>列索引默认驻留 In-Memory Column Store Area，内存不足时可溢写到共享存储。优化器比较行存串行、行存并行和 IMCI 三条路径，选择成本最低者。{refs("P1")}</li>
<li>专用 IMCI RO 节点通过 Redo 和 PolarDB 物理复制在后台构建、恢复和维护列索引；AutoIndex 在 RW 节点只更新字典，真正的列索引构建发生在 RO IMCI 节点。{refs("P1","P3")}</li>
<li>部署可分三种隔离：RW 节点启用 IMCI、专用 AP 型 RO 节点、独立 Standby 节点。它们分别提供从无隔离到 CPU/内存隔离，再到 I/O 也隔离。{refs("P1")}</li>
</ul>

<h3>3.2 AI 为什么是独立节点，而不是塞进数据库主线程</h3>
<ul>
<li>PolarDB for AI 是集成到 PolarDB for MySQL 的分布式机器学习组件，通过 SQL 提供模型创建、训练、评估和推理。{refs("P4")}</li>
<li>官方产品支持向集群增加专属 AI Node；数据、向量表等资源与节点生命周期相关。另有 Serverless 模式，Data-Agent 按 SQL 调用计费。{refs("P5","P6")}</li>
<li>这意味着产品边界是：<strong>SQL 接口和路由与数据库集成，AI 算力由专属节点或 Serverless 资源承载</strong>，而不是未经证实的“数据库内核同步调用外部 Sidecar”。</li>
<li>官方 RAG 架构明确：IMCI 列存节点负责向量索引，AI 节点负责文本向量化和 LLM，应用/Web 服务可在 ECS 等计算环境运行，OSS 保存知识文档。{refs("P7")}</li>
</ul>

<h3>3.3 已有客户证据</h3>
<p><strong>雅迪：</strong>DMS + PolarDB for AI 为云销通 App 提供 NL2SQL 和 RAG，超过 10 万销售人员可用自然语言查询批发、销售和库存，官方案例给出的查询准确率超过 90%。{refs("P8")}</p>
</section>

<section class="card">
<h2>4. OceanBase：现有内核能力、外部湖接入与 Lakebase 产品路线要分层理解</h2>
<div class="diagram">{svg("oceanbase-lakebase-architecture")}</div>

<h3>4.1 已有官方文档可直接证明的数据库能力</h3>
<ul>
<li><strong>SQL AI 函数：</strong><code>AI_SPLIT_DOCUMENT</code>、<code>AI_EMBED</code>、<code>AI_COMPLETE</code>、<code>AI_RERANK</code> 以 SQL 表达式进入数据处理；模型和 endpoint 由 <code>DBMS_AI_SERVICE</code> 注册和监控。{refs("B2","B3")}</li>
<li><strong>模型在哪里：</strong>官方文档要求注册第三方模型服务 endpoint 和 API Key，因此“SQL 函数在 OceanBase，模型推理服务可在数据库外”是有证据的边界。{refs("B3")}</li>
<li><strong>语义索引：</strong>用户可直接在 VARCHAR 列创建语义索引，OceanBase 自动 embedding 并建立向量索引；查询时也可输入原始文本。{refs("B7")}</li>
<li><strong>湖数据访问：</strong>OceanBase 通过 External Catalog 连接 HMS、Iceberg REST、FILESYSTEM、ODPS 等 Catalog，获取 <code>metadata.json</code>、snapshot、manifest 后读取 OSS/S3/HDFS 中的数据文件。{refs("B4","B5")}</li>
<li><strong>重要限制：</strong>当前官方文档明确 External Catalog/湖表访问“以只读为主”，写入能力依版本和 Catalog 类型而异。因此不能把今天的所有能力直接描述成完整双向共享写。{refs("B4","B5")}</li>
</ul>

<h3>4.2 Lakebase 方案页声明的演进方向</h3>
<p>官方方案页把未来形态描述为 S3 兼容对象存储 + Iceberg + 统一 Catalog，并接入 Spark、Ray；同时声明多模表、AI 列、混合搜索、Fork Database 和 Agent 上下文能力。{refs("B1")}</p>
<div class="warn"><strong>证据边界：</strong>方案页说明了能力目标，但没有完整公开多模表、AI 列、Fork Database、统一 Catalog 的进程拓扑、事务协议和跨引擎写入冲突处理。因此本报告不再把这些组件武断标为“全部在内核”或指定为某种 Sidecar；图中按“数据库能力、管控/产品层、开放计算服务、外部存储”标注，并明确未披露部分。</div>

<h3>4.3 既有数据如何被利用</h3>
<ul>
<li>交易数据继续由 OceanBase SQL/事务/HTAP 内核承载；向量、全文和关系过滤进入统一查询路径。{refs("B1","B7")}</li>
<li>外部湖数据通过 External Catalog 纳入 SQL，而不是强制先复制到数据库。{refs("B4","B5")}</li>
<li>Spark 可通过 Catalog/Connector 与 OceanBase 协作；官方最佳实践证明 Spark Catalog 与 OceanBase 的元数据映射和并行读写能力，但这和“Spark 直接共享 OceanBase 内核页格式”不是同一件事。{refs("B6")}</li>
</ul>

<h3>4.4 官方客户案例</h3>
<p>OceanBase 方案页列出蚂蚁阿福、灵光、中国联通、货拉拉等：阿福使用 Fork Database 沙箱，灵光使用逻辑表支撑大量轻应用，中国联通和货拉拉用于 RAG/向量与架构简化。这里的效果数字来源均为 OceanBase 方案页自身披露。{refs("B1")}</p>
</section>

<section class="card">
<h2>5. Databricks：从湖仓补 OLTP，LTAP 与 Agent/AI Search 是两条不同的数据路径</h2>
<div class="diagram">{svg("databricks-agent-bricks-architecture")}</div>

<h3>5.1 Lakebase 存储架构</h3>
<ul>
<li>Lakebase 把标准、无状态 Postgres compute 与 durable storage 分开；存储由 safekeepers、pageservers 和云对象存储组成。Compute 只保留 shared buffers 和本地缓存，不拥有持久数据。{refs("D1","D2")}</li>
<li>这一设计支持 scale-to-zero、instant branches、read replicas 和 failover；分支使用共享存储上的 Copy-on-Write。{refs("D1","D2")}</li>
</ul>

<h3>5.2 LTAP 如何消除 OLTP 到 OLAP 的外部复制</h3>
<ul>
<li>当 Lakebase 存储把数据物化到对象存储时，LTAP 增加存储层转码步骤，将行式 Postgres 数据转为 Parquet 列式布局，并通过 Delta/Iceberg 暴露。{refs("D3")}</li>
<li>Postgres 处理事务，Lakehouse//RT 处理分析；两者读取一个开放存储中的单一逻辑副本。官方明确称这消除了传统外部 CDC、复制和转换管道。{refs("D3")}</li>
<li>Lakebase Change Data Feed 是同一底层数据的变更流表示，用于下游管道和审计；它不是 LTAP 要消除的外部 CDC。{refs("D3")}</li>
</ul>

<h3>5.3 AI Search 和 Agent Bricks 不属于数据库内核</h3>
<ul>
<li><strong>AI Search：</strong>从 Delta Table 创建 Delta Sync index，自动跟随源表变更；它是受 Unity Catalog 治理的托管 Serverless 搜索服务，而不是 Lakebase Postgres 内核中的索引。{refs("D6")}</li>
<li><strong>Agent Bricks：</strong>Supervisor Agent 协调 Genie、AI Search、UC Functions、MCP 和自定义 Agent；需要 Unity Catalog 和 Serverless compute。{refs("D5","D7")}</li>
<li><strong>Unity AI Gateway：</strong>属于控制面，统一治理模型、Agent、MCP Server、工具和运行时请求，Agent 通过 on-behalf-of identity 继承用户权限。{refs("D4")}</li>
</ul>

<h3>5.4 已有客户证据</h3>
<p><strong>FinThrive：</strong>在既有 Databricks 平台、Notebook、代码库和文档上，通过 Unity Catalog 暴露资产，用 Agent Bricks 构建多个知识 Agent 并由 Supervisor 统一编排；官方案例称数小时内上线了可查询管道的助手。{refs("D8")}</p>
</section>

<section class="card">
<h2>6. 对自研数据库的可执行映射：哪些必须进内核，哪些应独立部署</h2>
<table>
<tr><th>目标</th><th>建议落点</th><th>研发工作</th><th>参考证据</th></tr>
<tr><td>利用现有 TP 数据直接做 AP</td><td><strong>数据库内核</strong></td>
<td>列存格式/列索引、向量化执行器、CBO 行列路径选择、资源隔离</td>
<td>Oracle IMCS；PolarDB IMCI {refs("O1","O2","P1","P2")}</td></tr>
<tr><td>保持行列实时一致</td><td><strong>内核后台进程或数据库复制层</strong></td>
<td>选择 Oracle 式后台填充/失效重填，或 PolarDB 式 Redo/物理复制到 RO 列存节点；不要默认引入 Kafka/Flink</td>
<td>{refs("O1","P1","P3")}</td></tr>
<tr><td>向量与业务条件统一查询</td><td><strong>数据库内核</strong></td>
<td>VECTOR 类型、距离算子、ANN 索引、标量过滤与向量路径的优化器整合、RLS 一致执行</td>
<td>{refs("O0","B7")}</td></tr>
<tr><td>Embedding/LLM 推理</td><td><strong>可插拔：库内轻量模型 + 独立 AI 节点/Serverless</strong></td>
<td>轻量 ONNX 可库内；大型模型、GPU、弹性任务放独立 AI Node/服务；SQL 保持统一入口</td>
<td>Oracle local ONNX；PolarDB AI nodes {refs("O6","P4","P5","P6")}</td></tr>
<tr><td>自然语言分析与 Agent</td><td><strong>托管服务/管控面</strong></td>
<td>NL2SQL、Agent 编排、评测、Tracing、模型路由；只把确定性 SQL/工具执行落到内核</td>
<td>Oracle Select AI；PolarDB Data-Agent；Databricks Agent Bricks {refs("O4","P6","D5","D7")}</td></tr>
<tr><td>湖数据接入</td><td><strong>Catalog + Connector + 对象存储</strong></td>
<td>Iceberg REST/HMS、Parquet reader、谓词下推、权限凭据；先支持只读原位查询，再谨慎扩展一致写</td>
<td>{refs("O7","B4","B5","D3")}</td></tr>
</table>
<div class="evidence"><strong>推荐产品结构：</strong>
内核产品负责 TP、列存 AP、向量/全文和统一 SQL；复制层负责行列增量维护；AI Node/Serverless 负责模型算力；
控制面负责语义模型、Agent、权限与审计；湖连接层负责 Iceberg/Catalog。这样既保持“数据库是核心”，又避免把不确定、长延迟、GPU 密集型逻辑塞进核心事务进程。</div>
</section>

<section class="card sources">
<h2>7. 逐项参考资料</h2>
<p>以下全部为厂商官方文档、官方产品页、官方博客或官方客户案例。图中引用编号与此处一致。</p>
<ul>{source_list}</ul>
</section>
</main></body></html>"""

(ROOT / "ob-lakebase-ai-report.html").write_text(html, encoding="utf-8")
print("generated evidence-backed HTML report")
