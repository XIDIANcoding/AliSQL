import os

def get_svg(name):
    with open(f'/workspace/diagrams/{name}.svg', 'r', encoding='utf-8') as f:
        return f.read()

oracle_svg = get_svg('oracle-26ai-architecture')
databricks_svg = get_svg('databricks-agent-bricks-architecture')
snowflake_svg = get_svg('snowflake-cortex-horizon-architecture')
polardb_svg = get_svg('polardb-imci-ai-architecture')

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

    .legend-box {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: #f1f5f9;
      padding: 10px 16px;
      border-radius: 8px;
      margin-bottom: 16px;
      font-size: 12px;
      align-items: center;
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .legend-dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      display: inline-block;
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
      <p><strong>分析核心：</strong>OceanBase 湖库一体、Databricks (Mosaic AI / Agent Bricks)、Oracle 26ai (Autonomous Lakehouse)、Snowflake (Cortex / Horizon)、阿里云 PolarDB (IMCI / Lakebase) 等各大主流厂商具体架构设计、<strong>组件物理落点（内核/管控面/复制管道/外部微服务）</strong>、层间配合数据流与落地客户案例深度拆解。</p>
      <div class="tags">
        <span class="tag">库仓一体</span>
        <span class="tag">湖库一体</span>
        <span class="tag">内核改动标注</span>
        <span class="tag">外部服务部署</span>
        <span class="tag">Database-First</span>
        <span class="tag">Agent Bricks</span>
        <span class="tag">IMCI 列存</span>
        <span class="tag">零 ETL</span>
      </div>
    </header>

    <!-- SECTION 1: Strategic Vision -->
    <section class="card">
      <h2>一、战略共识：利用既有数据，增强内核做“库仓一体+AI”</h2>
      <div class="summary">
        <p>
          <strong>行业演进本质：</strong>当前主流数据库厂商、数仓与湖仓平台（如 Oracle、Databricks、Snowflake、OceanBase、阿里云 PolarDB 等）正在不约而同地走向同一终局——<strong>统一数据底座（Unified Data Foundation）</strong>。
        </p>
        <p>
          你们作为自研数据库团队，所选定的战略路线（<strong>“增强数据库内核，走库仓一体，利用既有数据优势，引入列存仓与 AI 大数据分析能力”</strong>），不仅与 OceanBase 的底层逻辑完全一致，也是数据库龙头 <strong>Oracle（23ai/26ai）</strong> 与 <strong>阿里云 PolarDB</strong> 最核心的成功路径。
        </p>
        <p>
          <strong>核心护城河：</strong>企业最核心、最具价值的业务数据已经在你们的 TP 数据库中。<strong>“计算与模型向既有数据靠近”</strong> 的效率，永远远高于将数百 TB 数据通过繁重的 CDC/ETL 管道搬运到外围系统。
        </p>
      </div>
    </section>

    <!-- SECTION 2: Vendor In-depth with Component Placement -->
    <section class="card">
      <h2>二、各大厂商架构设计、层间配合与【组件物理落点】标注剖析</h2>
      
      <div class="legend-box">
        <strong>架构图组件物理落点与改造分类图例：</strong>
        <span class="legend-item"><span class="legend-dot" style="background:#2563eb;"></span><strong>【数据库内核代码】</strong>：直接修改 C++/Rust 数据面进程（事务/存储/列存/向量/执行器）</span>
        <span class="legend-item"><span class="legend-dot" style="background:#059669;"></span><strong>【管控面 / 控制台】</strong>：独立 Web 管理平台 / 元数据库（语义配置/沙箱管理/安全策略）</span>
        <span class="legend-item"><span class="legend-dot" style="background:#d97706;"></span><strong>【新增外部服务 / 容器化】</strong>：解耦大模型调用、MCP 网关、Worker 进程（K8s/微服务独立部署）</span>
        <span class="legend-item"><span class="legend-dot" style="background:#0284c7;"></span><strong>【复制与同步管道】</strong>：内核后台流式线程 / Redo Log 解析（实现物理零 ETL）</span>
      </div>

      <!-- 1. Oracle -->
      <h3>1. Oracle (Oracle AI Database 26ai &amp; Autonomous AI Lakehouse)</h3>
      <p>
        <span class="badge">技术流派</span><strong>传统数据库内核扩展派（Database-First）</strong><br />
        Oracle 26ai 将事务、列存 AP、向量检索与库内模型推理高度内聚在同一 C++ 数据库内核进程中，上层通过 PL/SQL 与管控面提供 Select AI Agent 编排，底层结合 Exadata 硬件实现算子下推。
      </p>

      <div class="diagram-container">
        <div class="diagram-title">【架构设计图】Oracle 26ai Autonomous AI Lakehouse 三层协同与组件落点 (draw.io 绘制)</div>
        {oracle_svg}
      </div>

      <h4>三层架构的配合关系与组件物理落点：</h4>
      <ul>
        <li><strong>第 1 层：智能交互与 Agent 编排层 (Select AI Agent Framework)  <span style="color:#d97706;font-weight:700;">【落点：管控面微服务 + 库内运行时】</span>：</strong>
          <ul>
            <li><strong>ReAct 编排引擎：</strong>作为外部微服务或库内 PL/SQL 运行时运行，负责 <code>Planning 规划 -&gt; Tool 调用 -&gt; Reflection 反思</code> 循环。</li>
            <li><strong>Select AI (NL2SQL)：</strong>部署在管控面 Agent 模块中，绑定元数据字典与 LLM，将自然语言转为高精度 SQL。</li>
            <li><strong>In-DB Tool &amp; MCP 适配器：</strong>作为外部独立微服务容器化部署，暴露标准 MCP 接口，统一调度库内存储过程与外部 REST API。</li>
            <li><strong>长短期记忆视图：</strong>物理存储在<strong>数据库内核系统表</strong>（<code>USER_CLOUD_AI_CONVERSATION</code>）中，由内核事务保证审计一致性。</li>
          </ul>
        </li>
        <li><strong>第 1 层 ➔ 第 2 层配合链路：</strong>通过库内函数调用（<code>DBMS_CLOUD_AI</code> / In-DB UDF），Agent 将生成的执行计划与事务上下文直接下发给 SQL 计算引擎。</li>
        <li><strong>第 2 层：统一多模 SQL 计算引擎层 (Converged Engine)  <span style="color:#2563eb;font-weight:700;">【落点：数据库内核 C++ 核心进程】</span>：</strong>
          <ul>
            <li><strong>OLTP 事务引擎：</strong>内核核心代码，负责行存、ACID 强一致性、锁管理并生成 Redo Log。</li>
            <li><strong>Database In-Memory (AP)：</strong>内核列存模块，行存数据通过<strong>内核 Redo 流式回放线程</strong>毫秒级同步为双格式内存列存，<strong>物理免去外部 ETL 搬迁</strong>。</li>
            <li><strong>AI Vector Search &amp; ONNX：</strong>内核原生支持 <code>VECTOR</code> 类型与 HNSW 索引；当文本写入时由内核触发同机 ONNX 模型生成向量，保持事务原子性。</li>
            <li><strong>JSON Duality &amp; Graph：</strong>内核多模模块，实现属性图分析以及关系表与文档格式的透明双向映射。</li>
          </ul>
        </li>
        <li><strong>第 2 层 ➔ 第 3 层配合链路：</strong>通过 <strong>Smart Scan 存储硬件算子下推</strong>，向量距离计算与谓词过滤直接在存储层并发完成，仅将 Top-K 结果返回计算层。</li>
        <li><strong>第 3 层：智能存储与开放湖仓加速层  <span style="color:#059669;font-weight:700;">【落点：底层存储节点 + 湖仓连接器】</span>：</strong>
          <ul>
            <li><strong>Exadata Smart Scan：</strong>运行在 Exadata 存储节点底层软件/FPGA 中，硬件级下推计算，节省 90%+ 网络 IO。</li>
            <li><strong>True Cache &amp; Exascale 闪存：</strong>分布式事务一致性中层缓存集群，为高并发查询提供低延迟。</li>
            <li><strong>Autonomous AI Catalog 湖仓连接器：</strong>作为外部连接插件与管控面 Catalog，原位直读外部 S3/Iceberg 表（基于 Delta Sharing），实现跨云数据原位 Join。</li>
          </ul>
        </li>
      </ul>

      <h4>落地客户与成效：</h4>
      <ul>
        <li><strong>全球顶级跨国银行：</strong>在核心交易系统中落地实时反洗钱（AML）与实时风控，利用库内向量检索与事务保障，实现<strong>数据物理不出库</strong>。</li>
        <li><strong>跨国电信巨头：</strong>将数十亿级计费记录与客服通话非结构化工单统一在 Exadata In-Memory 中，提供亚秒级实时经营报表与故障排查。</li>
      </ul>

      <hr style="border:none;border-top:1px dashed var(--line);margin:30px 0;" />

      <!-- 2. Databricks -->
      <h3>2. Databricks (Delta Lake + Unity Catalog + Agent Bricks)</h3>
      <p>
        <span class="badge">技术流派</span><strong>数据湖仓自顶向下派（Lakehouse-First）</strong><br />
        Databricks 依托 Delta Lake 开放存储底座，通过 Unity Catalog 统筹治理，将 Agent 拆分为外部独立的微服务与 Serverless 向量搜索集群。
      </p>

      <div class="diagram-container">
        <div class="diagram-title">【架构设计图】Databricks Mosaic AI Agent Bricks 架构体系与组件落点 (draw.io 绘制)</div>
        {databricks_svg}
      </div>

      <h4>架构协作细节与组件物理落点：</h4>
      <ul>
        <li><strong>第 1 层：Mosaic AI Agent Framework (Agent Bricks)  <span style="color:#d97706;font-weight:700;">【落点：新增外部服务 / Model Serving 容器化部署】</span>：</strong>
          <ul>
            <li><strong>Multi-Agent Supervisor：</strong>新增外部编排微服务，负责意图分类、任务拆解与子 Agent 路由。</li>
            <li><strong>Genie Space (SQL Agent)：</strong>新增外部 AI 服务，针对结构化 Gold 业务表自动生成并执行分析 SQL。</li>
            <li><strong>Knowledge Assistant：</strong>新增外部 RAG 服务，绑定 AI Search 索引，负责非结构化文档检索。</li>
            <li><strong>UC Functions (确定性工具)：</strong>在管控面注册的 Python/SQL 业务函数（如授信审批、风控公式），作为 Agent 调用的工具。</li>
          </ul>
        </li>
        <li><strong>第 1 层 ➔ 第 2 层配合链路：</strong>Agent 严格继承用户身份 Token，通过 Unity Catalog 集中进行 RBAC 鉴权、动态列脱敏与行级过滤（RLS），并由 MLflow 记录端到端 Tracing。</li>
        <li><strong>第 2 层：统一治理控制面 (Unity Catalog)  <span style="color:#059669;font-weight:700;">【落点：管控面独立服务集群 + 元数据库】</span>：</strong>
          提供统一身份继承、行级安全规则引擎、MLflow 自动评估服务以及数据到 Agent 输出的端到端血缘图谱。</li>
        <li><strong>第 2 层 ➔ 第 3 层配合链路：</strong>通过 <strong>Change Data Feed (CDF) 复制管道</strong>捕获数据表变更，异步推送到 Serverless 算力构建向量索引。</li>
        <li><strong>第 3 层：湖仓存储与自动同步索引层  <span style="color:#2563eb;font-weight:700;">【落点：内核引擎 + 复制管道 + 向量检索集群】</span>：</strong>
          <ul>
            <li><strong>既有 Delta Table：</strong>运行在对象存储上的 Bronze/Silver/Gold 分层数据资产。</li>
            <li><strong>Change Data Feed (CDF)：</strong>内核级逻辑复制管道，将行级增删改事件实时广播。</li>
            <li><strong>Databricks AI Search：</strong>作为<strong>独立托管的 Serverless 向量搜索集群</strong>部署，自动调用模型计算 Embedding 并维护 HNSW/BM25 混合索引。</li>
          </ul>
        </li>
      </ul>

      <h4>落地客户与成效：</h4>
      <ul>
        <li><strong>康宁（Corning）：</strong>基于 Delta Lake 专利库构建企业研究助手，由 Agent Bricks 快速装配上线，研发文献检索效率提升数倍。</li>
        <li><strong>洲际交易所（ICE）：</strong>为金融客户提供合规问答助手，凭借 Unity Catalog 严格的行级安全与审计满足合规要求。</li>
        <li><strong>Block (Square) &amp; 巴斯夫 (BASF)：</strong>用于商家自适应运营生成及全球 1000+ 销售代表的智能销售情报辅助。</li>
      </ul>

      <hr style="border:none;border-top:1px dashed var(--line);margin:30px 0;" />

      <!-- 3. Snowflake -->
      <h3>3. Snowflake (Horizon Catalog + Cortex AI &amp; Cortex Agents)</h3>
      <p>
        <span class="badge">技术流派</span><strong>云数仓演进派（Data Cloud &amp; Semantic-First）</strong><br />
        Snowflake 强调 <strong>“管控面语义模型驱动 + 外部 Cortex Agent 服务 + 虚拟数仓弹性算力”</strong> 的协同分工。
      </p>

      <div class="diagram-container">
        <div class="diagram-title">【架构设计图】Snowflake Cortex AI 与 Horizon Catalog 协同体系及组件落点 (draw.io 绘制)</div>
        {snowflake_svg}
      </div>

      <h4>核心技术协同与组件物理落点：</h4>
      <ul>
        <li><strong>第 1 层：Cortex Agents 编排与双驱动工具层  <span style="color:#d97706;font-weight:700;">【落点：新增外部服务 / 容器化 Cortex 运行时】</span>：</strong>
          <ul>
            <li><strong>Cortex Agent：</strong>新增外部编排服务，负责意图分类与 Auto-Routing，原生提供标准 MCP 端点。</li>
            <li><strong>Cortex Analyst：</strong>外部 Text-to-SQL 服务，强制读取 Horizon 语义视图以消除幻觉，准确率达到 90%+。</li>
            <li><strong>Cortex Search &amp; Analytical Search：</strong>结合独立检索集群与库内分析算子（<code>AI_FILTER</code> / <code>AI_AGG</code>），完成非结构化内容的两层深度分析。</li>
          </ul>
        </li>
        <li><strong>第 1 层 ➔ 第 2 层配合链路：</strong>Cortex Analyst 读取语义模型生成标准 SQL，Policy Decision Point (PDP) 实时判定权限并拦截越权请求。</li>
        <li><strong>第 2 层：统一治理控制面 (Horizon Catalog)  <span style="color:#059669;font-weight:700;">【落点：管控面独立服务集群 + 元数据库】</span>：</strong>
          <ul>
            <li><strong>Semantic Views (语义即代码)：</strong>管控面建模模块，统一指标公式、维度关系与同义词定义。</li>
            <li><strong>Policy Decision Point (PDP)：</strong>安全策略引擎，跨 SQL 与向量检索统一执行动态脱敏和行访问控制。</li>
            <li><strong>Cortex AI Guardrails：</strong>内容安全过滤模块，实时拦截 PII 敏感信息。</li>
          </ul>
        </li>
        <li><strong>第 2 层 ➔ 第 3 层配合链路：</strong>将通过安全校验的查询任务下发给无共享架构的虚拟数仓计算节点。</li>
        <li><strong>第 3 层：弹性计算与统一存储层  <span style="color:#2563eb;font-weight:700;">【落点：数据库内核计算节点 + 湖仓连接器 + 对象存储】</span>：</strong>
          <ul>
            <li><strong>虚拟仓库 (Virtual Warehouses)：</strong>C++ 编写的无状态弹性计算集群，按需秒级拉起，执行分布式分析与算子计算。</li>
            <li><strong>双向开放存储 (Open Iceberg REST Catalog)：</strong>外部湖仓连接插件与底层存储，统一读写内部专有表与外部 S3/Azure Iceberg 表。</li>
          </ul>
        </li>
      </ul>

      <h4>落地客户与成效：</h4>
      <ul>
        <li><strong>SRAM：</strong>通过 Cortex Analyst 让非技术员工在 Slack 中直接用自然语言查询多维销售与库存指标，无需 DBA 手工提数。</li>
        <li><strong>拜耳 (Bayer)、Booking.com、DoorDash：</strong>用于供应链智能调度与海量用户全域评论情感洞察。</li>
      </ul>

      <hr style="border:none;border-top:1px dashed var(--line);margin:30px 0;" />

      <!-- 4. 阿里云 PolarDB -->
      <h3>4. 阿里云 PolarDB (PolarDB IMCI + PolarDB for AI + Agent Lakebase)</h3>
      <p>
        <span class="badge">技术流派</span><strong>云原生数据库内核演进派（Cloud-Native DB &amp; HTAP）</strong><br />
        PolarDB 采用一写多读架构，主节点 TP 与列存节点 AP 全在内核数据面完成，AI 模型推理与 Agent 沙箱则通过外部微服务和轻量容器解耦。
      </p>

      <div class="diagram-container">
        <div class="diagram-title">【架构设计图】阿里云 PolarDB IMCI、AI 算子化与 Agent Lakebase 架构及组件落点 (draw.io 绘制)</div>
        {polardb_svg}
      </div>

      <h4>各节点分工、层间配合与组件物理落点：</h4>
      <ul>
        <li><strong>第 1 层：PolarDB 计算集群  <span style="color:#2563eb;font-weight:700;">【落点：数据库内核进程 + AI 算子节点】</span>：</strong>
          <ul>
            <li><strong>主节点 (Primary TP)：</strong>数据库内核代码，负责在线高并发事务写入并生成 Redo Log。</li>
            <li><strong>内核复制管道：</strong>内核后台线程流式解析 Redo Log，毫秒级更新列存与 HGraph 向量索引（<strong>零 ETL 内存流式复制</strong>）。</li>
            <li><strong>只读列存节点 (IMCI AP)：</strong>内核列存模块，支持内存列存加速、SIMD 向量化执行与 HGraph 向量检索算法。</li>
            <li><strong>PolarDB for AI 节点：</strong>作为<strong>外部独立 AI 推理服务 / 同机 Sidecar</strong> 部署，负责大模型推理与 MLOps 特征工程，防止 GPU/模型高延迟拖垮内核。</li>
          </ul>
        </li>
        <li><strong>第 1 层 ➔ 第 2 层配合链路：</strong>SQL 引擎直接下发 <code>AI_PREDICT</code> 与向量检索结果，驱动并挂载 Agent 运行时工作空间。</li>
        <li><strong>第 2 层：Agent Lakebase 工作空间基础设施  <span style="color:#d97706;font-weight:700;">【落点：管控面沙箱管理器 + 容器化挂载工作区】</span>：</strong>
          <ul>
            <li><strong>百万级 Agent 隔离空间：</strong>新增外部沙箱服务，为每个 Agent 提供独立的文件系统与上下文视图。</li>
            <li><strong>嵌入式引擎支持：</strong>沙箱内直接运行嵌入式 SQLite / DuckDB / LanceDB，满足本地快存快取。</li>
            <li><strong>生命周期管理器：</strong>部署在管控面中，负责 Agent 专属秒级快照、克隆与故障回滚。</li>
          </ul>
        </li>
        <li><strong>第 2 层 ➔ 第 3 层配合链路：</strong>通过共享存储底座与 RDMA 高速网络互联，物理上一份数据，行存、列存与对象存储共享底层文件。</li>
        <li><strong>第 3 层：共享分布式存储底座  <span style="color:#059669;font-weight:700;">【落点：底层共享存储系统 + 对象存储】</span>：</strong>
          <ul>
            <li><strong>PolarStore 共享块存储：</strong>共享存储底层系统，支持主节点与只读节点免复制共享数据文件。</li>
            <li><strong>OSS 对象存储 &amp; 湖仓加速：</strong>外部对象存储，通过 Object Table 与 AI Function 自动挂载非结构化图片/音视频并切片向量化。</li>
          </ul>
        </li>
      </ul>

      <h4>落地客户与成效：</h4>
      <ul>
        <li><strong>雅迪科技集团：</strong>在“云销通 App”中集成 PolarDB for AI，服务全国 <strong>10 万+ 销售与经销商人员</strong>，以自然语言口语化提问实时获取库存、批发、销售全域数据，<strong>NL2SQL 准确率超 90%</strong>。</li>
        <li><strong>头部游戏与广告厂商：</strong>用于数亿级用户画像流失预测与广告点击率（CTR）库内实时推理。</li>
      </ul>
    </section>

    <!-- SECTION 3: Main Matrix -->
    <section class="card">
      <h2>三、主流厂商全景矩阵横向对比</h2>
      <table>
        <tr>
          <th>厂商 / 产品</th>
          <th>产品定位与路线</th>
          <th>核心架构与组件物理落点</th>
          <th>AI / Agent 核心能力</th>
          <th>典型代表客户</th>
        </tr>
        <tr>
          <td><strong>OceanBase (OB)</strong></td>
          <td>金融级分布式 TP -&gt; HTAP -&gt; 湖库一体 AI 数据库</td>
          <td>【内核】：多模表 (Multimodal Table) + 混合搜索 (标量/全文/向量)<br>【管控/外部】：Fork Database 沙箱 + DataPilot 语义层</td>
          <td>AI 列 (异步事务一致生成) + seekdb M0 记忆自进化 + 库级数据分支回滚</td>
          <td>蚂蚁阿福 (医疗Agent沙箱)、灵光 (3000万轻应用)、中国联通、货拉拉</td>
        </tr>
        <tr>
          <td><strong>Oracle</strong></td>
          <td>企业关系型数据库龙头 -&gt; 26ai Converged Engine</td>
          <td>【内核】：Database In-Memory 列存 + 原生 Vector 索引<br>【管控/外部】：Select AI Agent 编排微服务 + Exadata 硬件下推</td>
          <td>Select AI Agent (ReAct 循环) + 库内 ONNX 推理 + Autonomous AI Lakehouse 原位读 Iceberg</td>
          <td>全球顶级大型跨国银行、证券核心风控、跨国电信运营商核心计费</td>
        </tr>
        <tr>
          <td><strong>Databricks</strong></td>
          <td>数据湖仓 -&gt; Delta Lake + Unity Catalog 统一数据智能</td>
          <td>【内核/存储】：Delta Table + CDF 复制管道<br>【管控/外部】：Unity Catalog 鉴权集群 + AI Search 向量服务 + Agent Bricks 微服务</td>
          <td>Agent Bricks (一键装配) + Genie Space (SQL Agent) + Databricks AI Search 混合检索</td>
          <td>康宁 (Corning 专利助手)、洲际交易所 (ICE)、Block (Square)、巴斯夫 (BASF)</td>
        </tr>
        <tr>
          <td><strong>Snowflake</strong></td>
          <td>云数仓 -&gt; AI Data Cloud + Apache Polaris 开放治理</td>
          <td>【内核】：C++ 虚拟数仓计算集群<br>【管控/外部】：Horizon Catalog 语义建模 + Cortex Analyst/Search 微服务 + 原生 MCP</td>
          <td>Cortex Analyst (语义驱动 Text-to-SQL) + Cortex Search (文本向量混合) + 原生 MCP Server</td>
          <td>拜耳 (Bayer)、Booking.com、DoorDash、SRAM (Slack 智能 ChatBI)</td>
        </tr>
        <tr>
          <td><strong>阿里云 PolarDB</strong></td>
          <td>云原生分布式数据库 -&gt; IMCI 实时分析 -&gt; Agent Lakebase</td>
          <td>【内核】：主节点 TP + IMCI 内存列存 (Redo 零ETL同步)<br>【管控/外部】：PolarDB for AI 推理 Sidecar + Agent Lakebase 沙箱集群</td>
          <td>PolarDB for AI (库内通义千问推理) + 原生 Vector 类型 + Agent Lakebase 百万级沙箱</td>
          <td>雅迪科技 (10万+销售端智能运营)、头部移动广告与游戏企业</td>
        </tr>
        <tr>
          <td><strong>AWS</strong></td>
          <td>分立式云服务组合 -&gt; Zero-ETL 存储复制与联邦</td>
          <td>【内核/存储】：Aurora TP + Redshift AP<br>【管控/外部】：Zero-ETL 复制管道 + Glue Catalog + SageMaker Unified Studio</td>
          <td>SageMaker Unified Studio + Bedrock 大模型 + Glue REST Catalog 联邦鉴权</td>
          <td>跨国大型企业云上大数据与电商实时分析架构</td>
        </tr>
      </table>
    </section>

    <!-- SECTION 4: Engineering Action Blueprint -->
    <section class="card">
      <h2>四、自研数据库走“库仓一体+AI”的技术路线与研发建议</h2>
      
      <div class="note">
        <strong>核心战略判断：</strong>
        数据库的核心资产是<strong>既有业务数据与事务一致性</strong>。你们的目标应当是<strong>“让数据库内核吞并数仓 AP 与 AI 上下文能力，杜绝用户采购外部 Kafka + ClickHouse + 独立向量库”</strong>。
      </div>

      <h3>研发落地三阶段实施蓝图：</h3>
      <div class="grid">
        <div class="mini">
          <h3>阶段一：筑基 (夯实内核 HTAP 列存仓能力)</h3>
          <ul>
            <li><strong>【数据库内核】：</strong>实现行存旁的内存列存 (IMCI，参考 PolarDB / Oracle In-Memory)。</li>
            <li><strong>【内核流式管道】：</strong>内核后台线程流式解析 Redo Log，毫秒级将行存增量组织为列存 Block，实现物理零 ETL。</li>
            <li><strong>【优化器智能分流】：</strong>CBO 优化器自动识别查询成本，OLTP 短查询走 B-Tree 索引，大聚合与复杂 Join 走 SIMD 向量化 AP 执行器。</li>
            <li><strong>【强资源隔离】：</strong>CPU 核心与内存池物理划分，保障复杂的 AI/大数据分析跑满时核心交易 0 抖动。</li>
          </ul>
        </div>

        <div class="mini">
          <h3>阶段二：融入 AI 核心要素 (混合检索与外部推理代理)</h3>
          <ul>
            <li><strong>【数据库内核】：</strong>原生支持 <code>VECTOR(dim)</code> 类型与 HNSW 索引管理器，实现“标量过滤 + BM25 全文 + 向量”单条 SQL 多路召回。</li>
            <li><strong>【新增外部服务】：</strong>开发同机 Sidecar / Daemon 形式的 <strong>AI 模型推理代理 (Model Gateway)</strong>，通过 UDS/共享内存与内核通信，执行 <code>AI_EMBED()</code> 与 <code>AI_PREDICT()</code>，防止外部网络/GPU 阻塞内核。</li>
            <li><strong>【内核级安全穿透】：</strong>确保行级安全策略（RLS）和列脱敏在扫描算子层对向量检索完全生效。</li>
          </ul>
        </div>

        <div class="mini">
          <h3>阶段三：语义层与 Agent 原生生态 (商业化变现)</h3>
          <ul>
            <li><strong>【管控面平台】：</strong>开发 <strong>Semantic View 语义模型配置中心</strong>（指标公式、同义词声明），将 Text-to-SQL 准确率拉升至 90% 以上。</li>
            <li><strong>【新增外部服务】：</strong>开发独立的 <strong>MCP Server 协议网关</strong>（Go/Node.js），暴露标准 MCP 接口供 Cursor、Claude Code、Dify 一键直连。</li>
            <li><strong>【管控面/存储】：</strong>提供 Copy-on-Write 库级分支（Fork Database），为 Agent 提供秒级沙箱克隆与试错回滚能力。</li>
          </ul>
        </div>

        <div class="mini">
          <h3>商业化客户价值主张 (买点提炼)</h3>
          <ul>
            <li><strong>金融/政企客户：</strong>主打“数据不出库”与金融级审计合规，库内完成交易+风控+智能问答。</li>
            <li><strong>中大型企业客户：</strong>主打“One Database for All”极简架构，替代 MySQL+Kafka+ClickHouse+Milvus，TCO 降低 50% 以上。</li>
            <li><strong>Agent 创新企业：</strong>主打“事务一致性上下文引擎”，一个连接同时完成业务状态变更与知识检索。</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 5: References -->
    <section class="card">
      <h2>五、参考资料与官方文档</h2>
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

print("Report HTML successfully rebuilt with clean integrated diagrams!")
