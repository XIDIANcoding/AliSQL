import os

def get_svg(name):
    with open(f'/workspace/diagrams/{name}.svg', 'r', encoding='utf-8') as f:
        return f.read()

oracle_svg = get_svg('oracle-26ai-architecture')
databricks_svg = get_svg('databricks-agent-bricks-architecture')
snowflake_svg = get_svg('snowflake-cortex-horizon-architecture')
polardb_svg = get_svg('polardb-imci-ai-architecture')
eng_svg = get_svg('engineering-boundary-architecture')

html_content = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>AI 时代数据库湖库/库仓一体与 Agent 架构深度分析报告</title>
  <style>
    :root {{
      --bg: #f8fafc;
      --card: #ffffff;
      --text: #0f172a;
      --muted: #475569;
      --blue: #0284c7;
      --blue-dark: #0369a1;
      --indigo: #4338ca;
      --line: #e2e8f0;
      --soft: #f0f9ff;
      --warn: #fffbeb;
      --tag-bg: #e0f2fe;
      --tag-text: #0369a1;
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
        "Microsoft YaHei", Arial, sans-serif;
      line-height: 1.8;
    }}

    .page {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 36px 24px 64px;
    }}

    header {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0369a1 100%);
      color: #fff;
      padding: 48px 44px;
      border-radius: 24px;
      box-shadow: 0 20px 40px rgba(15, 23, 42, 0.15);
      margin-bottom: 28px;
    }}

    header h1 {{
      margin: 0 0 14px;
      font-size: 32px;
      line-height: 1.3;
      letter-spacing: -0.02em;
    }}

    header p {{
      margin: 6px 0;
      color: rgba(255, 255, 255, 0.88);
      font-size: 15px;
    }}

    .card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 20px;
      padding: 32px 36px;
      margin: 24px 0;
      box-shadow: 0 6px 20px rgba(15, 23, 42, 0.04);
    }}

    h2 {{
      color: #0f172a;
      border-bottom: 2px solid var(--line);
      padding-bottom: 12px;
      margin-top: 4px;
      font-size: 22px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    h3 {{
      color: #1e293b;
      margin-top: 28px;
      font-size: 17px;
      border-left: 4px solid var(--blue);
      padding-left: 12px;
    }}

    h4 {{
      color: #334155;
      margin: 18px 0 8px;
      font-size: 15px;
    }}

    a {{ color: var(--blue); text-decoration: none; font-weight: 500; }}
    a:hover {{ text-decoration: underline; }}

    .summary {{
      background: var(--soft);
      border-left: 5px solid var(--blue);
      padding: 18px 22px;
      border-radius: 12px;
      margin: 20px 0;
    }}

    .note {{
      background: var(--warn);
      border-left: 5px solid #f59e0b;
      padding: 18px 22px;
      border-radius: 12px;
      margin: 20px 0;
    }}

    .tags {{ margin-top: 18px; display: flex; flex-wrap: wrap; gap: 8px; }}
    .tag {{
      display: inline-block;
      background: rgba(255, 255, 255, 0.15);
      color: #fff;
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 12.5px;
    }}

    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 20px 0;
      font-size: 13.5px;
      background: #fff;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }}

    th, td {{
      border: 1px solid var(--line);
      padding: 12px 14px;
      vertical-align: top;
    }}

    th {{
      background: #f1f5f9;
      color: #1e293b;
      text-align: left;
      font-weight: 700;
    }}

    ul {{ padding-left: 24px; }}
    li {{ margin: 8px 0; }}

    .diagram-container {{
      margin: 24px 0;
      padding: 16px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }}

    .diagram-title {{
      font-size: 14px;
      font-weight: 700;
      color: #475569;
      margin-bottom: 12px;
      text-align: center;
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px;
    }}

    .mini {{
      border: 1px solid var(--line);
      background: #f8fafc;
      border-radius: 14px;
      padding: 18px 20px;
    }}

    .mini h3 {{
      margin-top: 0;
      border-left: none;
      padding-left: 0;
      color: #0369a1;
    }}

    footer {{
      color: var(--muted);
      font-size: 13px;
      text-align: center;
      margin-top: 36px;
    }}

    .badge {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 600;
      background: var(--tag-bg);
      color: var(--tag-text);
      margin-right: 6px;
    }}

    .code-badge {{
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 11px;
      font-family: monospace;
      font-weight: 700;
      background: #e2e8f0;
      color: #334155;
    }}

    @media (max-width: 800px) {{
      header {{ padding: 32px 24px; border-radius: 18px; }}
      header h1 {{ font-size: 24px; }}
      .card {{ padding: 22px 18px; }}
      .grid {{ grid-template-columns: 1fr; }}
      table {{ font-size: 12.5px; }}
    }}
  </style>
</head>
<body>
  <main class="page">
    <header>
      <h1>AI 时代数据库湖库/库仓一体与 Agent 架构深度分析报告</h1>
      <p><strong>报告日期：</strong>2026-08-16</p>
      <p><strong>分析核心：</strong>OceanBase 湖库一体、Databricks (Mosaic AI / Agent Bricks)、Oracle 26ai (Autonomous Lakehouse)、Snowflake (Cortex / Horizon)、阿里云 PolarDB (IMCI / Lakebase) 等各大主流厂商具体架构设计、层间配合数据流、真实落地客户案例，以及<strong>自研数据库代码落点、组件物理边界与服务部署形态全景拆解</strong>。</p>
      <div class="tags">
        <span class="tag">库仓一体</span>
        <span class="tag">湖库一体</span>
        <span class="tag">内核改动清单</span>
        <span class="tag">外部服务部署</span>
        <span class="tag">Database-First</span>
        <span class="tag">Agent Bricks</span>
        <span class="tag">IMCI 列存</span>
        <span class="tag">零 ETL</span>
      </div>
    </header>

    <!-- SECTION: Engineering Boundaries -->
    <section class="card" style="border: 2px solid #0284c7;">
      <h2>🌟 自研数据库落地工程指南：组件物理边界、内核代码落点与服务部署形态</h2>
      <div class="summary">
        <p>
          <strong>解决核心疑惑：</strong>要把数据库做成“库仓一体 + AI”，团队研发的<strong>代码到底写在哪里？哪些必须做在数据库内核里？哪些需要独立外部微服务？服务如何部署通信？</strong>
        </p>
        <p>
          为了避免大模型秒级延迟、GPU 故障或复杂协议拖垮数据库内核，工程架构必须将系统严格划分为 <strong>4 大物理边界</strong>：
          <strong>1. 管控面 Web 中心</strong>、<strong>2. 外部独立微服务矩阵</strong>、<strong>3. 数据库内核进程 (C++/Rust)</strong>、<strong>4. 底层混合存储</strong>。
        </p>
      </div>

      <div class="diagram-container">
        <div class="diagram-title">【自研工程全景架构图】组件物理边界、内核代码落点与服务部署形态 (draw.io 绘制)</div>
        {eng_svg}
      </div>

      <h3>1. 必须做在【数据库内核 (DB Kernel)】里的工作（C++/Rust 数据面核心）</h3>
      <table>
        <tr>
          <th>内核模块</th>
          <th>内核代码落点 / 改造内容</th>
          <th>具体实现细节与技术选型</th>
        </tr>
        <tr>
          <td><strong>数据类型扩展</strong></td>
          <td><span class="code-badge">SQL Parser &amp; Type System</span></td>
          <td>新增原生 <code>VECTOR(dim)</code> 类型（支持 768/1536 维 float 数组）与高效二进制 <code>JSON</code> 存储格式。</td>
        </tr>
        <tr>
          <td><strong>原生向量索引与算子</strong></td>
          <td><span class="code-badge">Storage Engine &amp; Index Manager</span></td>
          <td>在存储层内置 <strong>HNSW / IVF-Flat</strong> 索引管理器。利用 <strong>AVX-512 / ARM Neon SIMD 指令集</strong> 硬件加速距离计算算子（L2、Cosine、Inner Product）。</td>
        </tr>
        <tr>
          <td><strong>内存列存引擎 (AP)</strong></td>
          <td><span class="code-badge">Columnar Storage Engine</span></td>
          <td>实现行存旁的<strong>双格式内存列存 (IMCI)</strong>。支持字典编码压缩、Bit-Packing、按列裁剪与 SIMD 向量化扫表。</td>
        </tr>
        <tr>
          <td><strong>混合查询优化器</strong></td>
          <td><span class="code-badge">Cost-Based Optimizer (CBO)</span></td>
          <td>代价模型升级：<br>1. 智能分流 TP 短查询（走 B-Tree 点查）与 AP 复杂查询（走列存）；<br>2. <strong>标量条件先过滤，再做向量 KNN 近似搜索</strong>，避免全表暴力计算。</td>
        </tr>
        <tr>
          <td><strong>混合执行器</strong></td>
          <td><span class="code-badge">Execution Engine</span></td>
          <td>实现向量化执行流水线，单条 SQL 闭环支持“标量过滤 + BM25 全文倒排 + HNSW 向量检索”多路融合召回。</td>
        </tr>
        <tr>
          <td><strong>SQL 级 AI 语法</strong></td>
          <td><span class="code-badge">SQL Functions &amp; UDFs</span></td>
          <td>内置注册 <code>AI_EMBED(text)</code>、<code>AI_PREDICT(model, input)</code>、<code>AI_EXTRACT(schema, text)</code> 等函数，通过内部 IPC 调用外部代理。</td>
        </tr>
        <tr>
          <td><strong>内核级统一权限</strong></td>
          <td><span class="code-badge">Security &amp; Policy Checker</span></td>
          <td>将行级安全（RLS）和列脱敏策略下沉至 Scan 算子层，<strong>保证向量检索和 SQL 查询看到同一份受控数据</strong>。</td>
        </tr>
        <tr>
          <td><strong>内核流式同步管道</strong></td>
          <td><span class="code-badge">WAL / Redo Engine (In-Kernel)</span></td>
          <td>内核后台流式线程解析 Redo Log，毫秒级将行存增量转换并刷入内存列存区（零 ETL 物理免复制）。</td>
        </tr>
      </table>

      <h3>2. 需要【新开发的外部独立服务 (External Services)】及部署形态</h3>
      <div class="grid">
        <div class="mini">
          <h3>① AI 模型推理代理 (Model Gateway)</h3>
          <p><strong>部署形态：</strong>同机 Sidecar 容器 或 独立 Daemon 进程 (Python / C++ / Go 实现)。</p>
          <p><strong>通信方式：</strong>与内核通过 <strong>Unix Domain Socket (UDS) / 共享内存 IPC / gRPC</strong> 高速通信。</p>
          <p><strong>职责：</strong>接收内核 SQL 函数调用，负责大模型连接池管理、超时重试、熔断降级，统一调度外部 API (OpenAI/Qwen) 或本地私有 vLLM/ONNX 引擎。</p>
        </div>

        <div class="mini">
          <h3>② 异步 Embedding 与向量回填 Worker</h3>
          <p><strong>部署形态：</strong>独立无状态微服务集群 (K8s Deployment / Worker 进程，可水平伸缩)。</p>
          <p><strong>通信方式：</strong>消费数据库变更日志流 (CDF)，通过专用批量通道将结果写回数据表。</p>
          <p><strong>职责：</strong>监听大文本/多模态数据变更，自动执行文档切片 (Chunking)、并发计算向量，并回填到表的 AI 列中。</p>
        </div>

        <div class="mini">
          <h3>③ 数据库 MCP Server 协议网关</h3>
          <p><strong>部署形态：</strong>独立轻量级微服务 (Go / Node.js / Python FastMCP 编写)，暴露 SSE / HTTP 端点。</p>
          <p><strong>通信方式：</strong>标准 MCP 协议对接外部 Client，内部使用连接池直连数据库内核与管控面。</p>
          <p><strong>职责：</strong>将数据库的元数据字典、受控查询工具、事务沙箱操作标准化暴露给 Cursor、Claude Code、Dify 等 Agent 平台。</p>
        </div>

        <div class="mini">
          <h3>④ 外部湖仓连接器 (Lake Connector)</h3>
          <p><strong>部署形态：</strong>动态共享库插件 (.so) 或独立 Arrow Flight 服务。</p>
          <p><strong>通信方式：</strong>S3 API / Iceberg REST Catalog 协议。</p>
          <p><strong>职责：</strong>原位挂载外部 S3 / OSS 对象存储中的 Iceberg / Parquet 冷数据，实现与库内表原位 Join。</p>
        </div>
      </div>

      <h3>3. 必须做在【管控面 / 控制台 (Control Plane)】里的功能（独立 Web 平台）</h3>
      <ul>
        <li><strong>Semantic Views 语义模型配置中心（学习 Snowflake）：</strong>提供可视化 Web 界面，供 DBA/业务人员配置指标公式（如“净利润 = 营收 - 成本”）、同义词与业务关系，输出标准化语义字典供 Text-to-SQL 使用。</li>
        <li><strong>Agent 沙箱与分支管理器（学习 OB / PolarDB）：</strong>提供 Copy-on-Write 库级分支（Fork Database）可视化调度，支持海量 Agent 秒级快照创建、配额限制与回滚。</li>
        <li><strong>Model &amp; Key Vault 秘钥中心：</strong>统一安全托管企业大模型 API Key（OpenAI、通义千问、Claude 等）或本地私有端点，提供 Token 消耗与限流统计。</li>
        <li><strong>全链路 AI 审计与 Tracing 日志：</strong>完整记录自然语言提问、生成的 SQL、执行耗时、召回文档块及用户操作轨迹，满足金融合规。</li>
      </ul>
    </section>

    <!-- SECTION: Vendor In-depth -->
    <section class="card">
      <h2>一、各大厂商架构设计与技术细节剖析 (含 draw.io 原生架构图)</h2>

      <!-- 1. Oracle -->
      <h3>1. Oracle (Oracle AI Database 26ai &amp; Autonomous AI Lakehouse)</h3>
      <p>
        <span class="badge">技术流派</span><strong>传统数据库内核扩展派（Database-First）</strong><br />
        Oracle 26ai 的设计哲学是 <strong>“多模汇聚（Converged Database）与计算硬件下推”</strong>。它将事务、列存 AP、向量检索、大模型交互与外部 Iceberg 湖仓融合为一套三层紧密协同架构。
      </p>

      <div class="diagram-container">
        <div class="diagram-title">【架构设计图】Oracle 26ai Autonomous AI Lakehouse 三层协同体系</div>
        {oracle_svg}
      </div>

      <h4>三层架构的配合关系：</h4>
      <ul>
        <li><strong>第 1 层：智能交互与 Agent 编排层 (Select AI &amp; Select AI Agent)：</strong>
          在 26ai 中，Agent 成为库内一等公民。内置 <code>DBMS_CLOUD_AI_AGENT</code> 实现了 <strong>ReAct（Reasoning &amp; Acting）</strong> 循环：
          <code>用户自然语言 -&gt; Planning 任务规划 -&gt; Tool Use (调用 PL/SQL、库内 RAG 或外部 REST) -&gt; Reflection 评估反思 -&gt; 更新记忆</code>。
          整个过程直接使用数据库的 <code>USER_CLOUD_AI_CONVERSATION</code> 等系统视图审计，<strong>杜绝了外部 LangChain 框架带来的安全漏洞</strong>。
        </li>
        <li><strong>第 2 层：统一多模 SQL 计算引擎层 (Converged Engine)：</strong>
          单条 SQL 可以同时调度：OLTP 强一致行存、<strong>Database In-Memory 双格式内存列存（SIMD 向量化 AP）</strong>、<strong>原生 VECTOR 类型</strong>与 ONNX 库内模型推理引擎。当新数据写入时，库内自动触发 ONNX 模型生成向量，事务保持原子性。
        </li>
        <li><strong>第 3 层：智能存储与开放湖仓加速层 (Exadata AI Storage &amp; Autonomous Lakehouse)：</strong>
          <strong>Smart Scan 硬件下推：</strong>Exadata 存储节点硬件级并发执行向量距离计算和列裁剪，仅将 Top-K 结果返回计算节点，网络 IO 降低 90%。
          同时，通过 Autonomous AI Catalog 直接原位挂载外部 S3/Iceberg 表（利用 Delta Sharing 协议），实现库内核心交易数据与外部大数据无缝 Join。
        </li>
      </ul>

      <h4>落地客户与成效：</h4>
      <ul>
        <li><strong>全球顶级金融机构与跨国银行：</strong>在核心交易系统中落地实时欺诈检测与投研智能问答，满足严苛的 PCI-DSS 与金融监管合规要求，实现<strong>数据物理不出库</strong>。</li>
        <li><strong>大型电信运营商：</strong>将数十亿级通话账单与工单非结构化文本统一在 Exadata In-Memory 中，提供亚秒级经营分析与网络故障排查。</li>
      </ul>

      <hr style="border:none;border-top:1px dashed var(--line);margin:30px 0;" />

      <!-- 2. Databricks -->
      <h3>2. Databricks (Delta Lake + Unity Catalog + Agent Bricks)</h3>
      <p>
        <span class="badge">技术流派</span><strong>数据湖仓自顶向下派（Lakehouse-First）</strong><br />
        Databricks 凭借 <strong>“在既有 Delta Lake 上一键启动 Agent（Agent Bricks）”</strong> 成为 AI Agent 基础设施标杆。
      </p>

      <div class="diagram-container">
        <div class="diagram-title">【架构设计图】Databricks Mosaic AI Agent Bricks 架构体系</div>
        {databricks_svg}
      </div>

      <h4>架构协作细节与“一键启动 Agent”机制：</h4>
      <ul>
        <li><strong>既有数据自动增量同步（AI Search）：</strong>
          用户无需搭建任何 ETL 管道，只需对既有的 Delta Table 声明创建 <code>AI Search Index</code>。
          底层的 <strong>Change Data Feed (CDF)</strong> 自动监听数据增删改，Serverless 算力自动调用 Embedding 模型，实时维护 HNSW 向量与 BM25 全文混合索引。
        </li>
        <li><strong>Agent Bricks 快速装配（Multi-Agent Supervisor）：</strong>
          Databricks 将 Agent 生产化抽象为三大标准组件，通过监督器（MAS）自动协调：
          <ol>
            <li><strong>Genie Space（SQL Agent）：</strong>绑定结构化 Gold 业务表，负责高精度自然语言转 SQL 指标分析；</li>
            <li><strong>Knowledge Assistant：</strong>绑定 AI Search 索引，负责文档 RAG 与非结构化检索；</li>
            <li><strong>Unity Catalog Functions：</strong>将 Python/SQL 函数注册为确定性工具（如信用额度审批、风险评级算法）。</li>
          </ol>
        </li>
        <li><strong>Unity Catalog 全链路治理：</strong>
          Agent 严格继承发起用户的 Identity。若某用户在 Unity Catalog 中被配置了列脱敏或行级安全（RLS），Genie 生成的 SQL 与 Knowledge Assistant 检索结果会自动过滤，并由 MLflow 记录完整输入输出血缘。
        </li>
      </ul>

      <h4>落地客户与成效：</h4>
      <ul>
        <li><strong>康宁（Corning）：</strong>利用 Mosaic AI 构建企业级研究助手，索引数十万份专利与实验记录，研发检索效率提升数倍。</li>
        <li><strong>洲际交易所（ICE - Intercontinental Exchange）：</strong>为金融客户提供基于市场数据的合规问答助手，凭借 Unity Catalog 满足金融审计要求。</li>
        <li><strong>Block（原 Square）：</strong>用于自动化商家运营（如智能菜单自适应生成与销售趋势分析）。</li>
        <li><strong>巴斯夫（BASF Coatings）：</strong>构建 Marketmind 销售情报 Agent，服务全球 1000 多名销售代表。</li>
      </ul>

      <hr style="border:none;border-top:1px dashed var(--line);margin:30px 0;" />

      <!-- 3. Snowflake -->
      <h3>3. Snowflake (Horizon Catalog + Cortex AI &amp; Cortex Agents)</h3>
      <p>
        <span class="badge">技术流派</span><strong>云数仓演进派（Data Cloud &amp; Semantic-First）</strong><br />
        Snowflake 强调 <strong>“语义层（Semantic Views）驱动 + 两层 Analytical Search 闭环”</strong>。
      </p>

      <div class="diagram-container">
        <div class="diagram-title">【架构设计图】Snowflake Cortex AI 与 Horizon Catalog 协同体系</div>
        {snowflake_svg}
      </div>

      <h4>核心技术协同机制：</h4>
      <ul>
        <li><strong>Horizon Semantic Views（语义即代码）：</strong>
          解决 LLM 直连数仓表容易产生“幻觉 SQL”的痛点。在 Horizon Catalog 中声明指标口径（如“净利润 = 营业收入 - 营业成本 - 税金”）、同义词与维度关联。
          <strong>Cortex Analyst</strong> 读取语义视图生成 SQL，将企业级 Text-to-SQL 准确率从通用大模型的 60% 提升至 <strong>90% 以上</strong>。
        </li>
        <li><strong>两层分析检索（Analytical Search Loop）：</strong>
          针对大规模非结构化文档分析，采用 <code>Layer 1 剪枝召回 (Cortex Search 动态深度搜索) + Layer 2 库内语义算子 (AI_FILTER / AI_EXTRACT / AI_AGG)</code>，并在 SQL 中直接与结构化数据做 <code>GROUP BY</code> 关联聚合。
        </li>
        <li><strong>原生 MCP Server 对象：</strong>
          通过 <code>CREATE MCP SERVER</code> 语句，直接将数仓内的 Cortex Agent 暴露为标准 MCP 端点，供外部 Claude Desktop、Cursor 或企业自建应用安全调用。
        </li>
      </ul>

      <h4>落地客户与成效：</h4>
      <ul>
        <li><strong>拜耳（Bayer）、Booking.com、DoorDash、SRAM：</strong>广泛应用于供应链智能调度、用户评论全域洞察。SRAM 员工可直接在 Slack 中用自然语言查询实时库存与多维销售 KPI。</li>
      </ul>

      <hr style="border:none;border-top:1px dashed var(--line);margin:30px 0;" />

      <!-- 4. 阿里云 PolarDB -->
      <h3>4. 阿里云 PolarDB (PolarDB IMCI + PolarDB for AI + Agent Lakebase)</h3>
      <p>
        <span class="badge">技术流派</span><strong>云原生数据库内核演进派（Cloud-Native DB &amp; HTAP）</strong><br />
        PolarDB 从计算存储分离的 TP 数据库出发，通过 <strong>只读列存节点（IMCI）</strong> 和 <strong>In-DB AI 算子</strong> 实现了数据库与实时分析、智能推理的深度内聚。
      </p>

      <div class="diagram-container">
        <div class="diagram-title">【架构设计图】阿里云 PolarDB IMCI、AI 算子化与 Agent Lakebase 架构</div>
        {polardb_svg}
      </div>

      <h4>各节点分工与配合：</h4>
      <ul>
        <li><strong>TP 事务与 IMCI 列存节点的毫秒级零 ETL 同步：</strong>
          主节点处理写入并生成 Redo Log。只读列存节点（IMCI）通过内存流式解析 Redo Log，毫秒级更新列存与 HGraph 向量索引，<strong>底层共享同一份 PolarStore 文件，物理上彻底免去数据搬迁</strong>。
        </li>
        <li><strong>PolarDB for AI 算子化：</strong>
          通过扩展标准 SQL（如 <code>SELECT AI_PREDICT(...) WHERE VECTOR_DISTANCE(...) &lt; 0.2</code>），将通义千问大模型与 MLOps 推理能力内嵌在数据库执行计划中。
        </li>
        <li><strong>2026 年全新组件：Agent Lakebase：</strong>
          为海量智能体提供隔离的工作空间视图，支持直接嵌入 SQLite/DuckDB/LanceDB，并在底层由 PolarDB 元数据驱动，提供百万级 Agent 秒级快照、克隆与挂载回滚。
        </li>
      </ul>

      <h4>落地客户与成效：</h4>
      <ul>
        <li><strong>雅迪科技集团（电动车制造巨头）：</strong>
          在“云销通 App”中集成基于 PolarDB for AI 的智能查询与营销助手，赋能全国 <strong>10 万+ 销售与经销商人员</strong>，以口语化提问实时获取批发、销售、库存全域数据多模态分析结果，<strong>NL2SQL 准确率超 90%</strong>。
        </li>
        <li><strong>某头部游戏与移动广告厂商：</strong>用于数亿级用户画像流失预测与广告点击率（CTR）库内实时推理。</li>
      </ul>
    </section>

    <!-- SECTION: Matrix Comparison -->
    <section class="card">
      <h2>二、主流厂商全景矩阵横向对比</h2>
      <table>
        <tr>
          <th>厂商 / 产品</th>
          <th>产品定位与路线</th>
          <th>核心架构与技术配合</th>
          <th>AI / Agent 核心能力</th>
          <th>典型代表客户</th>
        </tr>
        <tr>
          <td><strong>OceanBase (OB)</strong></td>
          <td>金融级分布式 TP -&gt; HTAP -&gt; 湖库一体 AI 数据库</td>
          <td>存算分离 + 多模表 (Multimodal Table) + 混合搜索 (标量/全文/向量) + Fork Database 沙箱</td>
          <td>AI 列 (异步事务一致生成) + seekdb M0 记忆自进化 + DataPilot 语义层</td>
          <td>蚂蚁阿福 (医疗Agent沙箱)、灵光 (3000万轻应用)、中国联通、货拉拉</td>
        </tr>
        <tr>
          <td><strong>Oracle</strong></td>
          <td>企业关系型数据库龙头 -&gt; 26ai Converged Engine</td>
          <td>三层协同：Select AI 编排 + Database In-Memory 列存与原生向量 + Exadata Smart Scan 硬件下推</td>
          <td>Select AI Agent (ReAct 循环) + 库内 ONNX 推理 + Autonomous AI Lakehouse 原位读 Iceberg</td>
          <td>全球顶级大型跨国银行、证券核心风控、跨国电信运营商核心计费</td>
        </tr>
        <tr>
          <td><strong>Databricks</strong></td>
          <td>数据湖仓 -&gt; Delta Lake + Unity Catalog 统一数据智能</td>
          <td>CDF 自动增量索引 + Unity Catalog 统一身份继承与 RLS + MAS 监督器编排</td>
          <td>Agent Bricks (一键装配) + Genie Space (SQL Agent) + Databricks AI Search 混合检索</td>
          <td>康宁 (Corning 专利助手)、洲际交易所 (ICE)、Block (Square)、巴斯夫 (BASF)</td>
        </tr>
        <tr>
          <td><strong>Snowflake</strong></td>
          <td>云数仓 -&gt; AI Data Cloud + Apache Polaris 开放治理</td>
          <td>Horizon Catalog 语义视图 + 虚拟数仓弹性算力 + 两层 Analytical Search 闭环</td>
          <td>Cortex Analyst (语义驱动 Text-to-SQL) + Cortex Search (文本向量混合) + 原生 MCP Server</td>
          <td>拜耳 (Bayer)、Booking.com、DoorDash、SRAM (Slack 智能 ChatBI)</td>
        </tr>
        <tr>
          <td><strong>阿里云 PolarDB</strong></td>
          <td>云原生分布式数据库 -&gt; IMCI 实时分析 -&gt; Agent Lakebase</td>
          <td>共享存储 PolarStore + 主节点 TP + 只读列存 IMCI (零ETL) + 库内 AI 算子节点</td>
          <td>PolarDB for AI (库内通义千问推理) + 原生 Vector 类型 + Agent Lakebase 百万级沙箱</td>
          <td>雅迪科技 (10万+销售端智能运营)、头部移动广告与游戏企业</td>
        </tr>
        <tr>
          <td><strong>AWS</strong></td>
          <td>分立式云服务组合 -&gt; Zero-ETL 存储复制与联邦</td>
          <td>Aurora TP 存储日志秒级复制 -&gt; Redshift AP 托管存储 / S3 Tables (Iceberg)</td>
          <td>SageMaker Unified Studio + Bedrock 大模型 + Glue REST Catalog 联邦鉴权</td>
          <td>跨国大型企业云上大数据与电商实时分析架构</td>
        </tr>
      </table>
    </section>

    <!-- SECTION: Reference Links -->
    <section class="card">
      <h2>三、参考资料与官方文档</h2>
      <ul>
        <li><a href="https://zhuanlan.zhihu.com/p/2055689544582817505" target="_blank">OceanBase 湖库一体，重新定义 AI 数据库 (知乎专栏)</a></li>
        <li><a href="https://www.oceanbase.com/solution/ai" target="_blank">OceanBase AI 数据库官方解决方案</a></li>
        <li><a href="https://www.oracle.com/database/ai-native-database-26ai/" target="_blank">Oracle AI Database 26ai 发布与技术概览</a></li>
        <li><a href="https://docs.oracle.com/en/database/oracle/oracle-database/26/selai/select-ai-agent2.html" target="_blank">Oracle Select AI Agent (Autonomous Agent Framework) 官方文档</a></li>
        <li><a href="https://www.databricks.com/product/artificial-intelligence/ai-search" target="_blank">Databricks AI Search 官方产品主页</a></li>
        <li><a href="https://docs.databricks.com/aws/en/ai-search/ai-search" target="_blank">Databricks Mosaic AI Agent Framework 官方指南</a></li>
        <li><a href="https://docs.snowflake.com/en/user-guide/snowflake-horizon" target="_blank">Snowflake Horizon Catalog 2026 治理架构</a></li>
        <li><a href="https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents" target="_blank">Snowflake Cortex Agents 官方开发文档</a></li>
        <li><a href="https://help.aliyun.com/zh/polardb/polardb-for-mysql/what-is-polardb-agent-lakebase" target="_blank">阿里云 PolarDB Agent LakeBase 产品文档</a></li>
        <li><a href="https://help.aliyun.com/zh/polardb/polardb-for-mysql/electric-vehicle-manufacturing-yadi-technology-group-co-ltd" target="_blank">阿里云 PolarDB for AI 雅迪科技集团落地案例</a></li>
      </ul>
    </section>

    <footer>
      本报告由自研数据库架构与 AI 演进分析团队整理出品 · 支持浏览器本地离线与云端直接渲染
    </footer>
  </main>
</body>
</html>
"""

with open('/workspace/ob-lakebase-ai-report.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Report HTML with engineering boundaries updated successfully!")
