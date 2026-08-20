#!/usr/bin/env python3
"""Generate editable draw.io and SVG diagrams from evidence-backed specs."""

from __future__ import annotations

import html
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring

OUT = Path(__file__).parent

CATEGORY = {
    "kernel": ("数据库内核/数据库节点", "#dbeafe", "#2563eb"),
    "control": ("管控面/托管控制服务", "#dcfce7", "#16a34a"),
    "sync": ("复制/同步/转码路径", "#cffafe", "#0891b2"),
    "service": ("独立计算或托管服务", "#ffedd5", "#ea580c"),
    "storage": ("存储/Catalog/开放格式", "#f1f5f9", "#64748b"),
}


def spec_oracle():
    return {
        "name": "Oracle 26ai：从数据库内核扩展 AI 与湖仓",
        "file": "oracle-26ai-architecture",
        "nodes": [
            ("agent", 60, 45, 290, 90, "control",
             "Select AI Agent\n数据库内框架（DBMS_CLOUD_AI_AGENT）\nPlanning / Tool / Reflection / Memory\n[O4]"),
            ("mcp", 410, 45, 290, 90, "control",
             "Autonomous AI Database MCP Server\n每数据库托管、多租户 MCP 服务\n无需客户另建 MCP 基础设施\n[O5]"),
            ("llm", 760, 45, 300, 90, "service",
             "模型来源\n外部 LLM Provider（可选）\n或数据库内加载 ONNX Embedding\n[O4][O6]"),
            ("sql", 60, 210, 235, 105, "kernel",
             "OLTP 行格式\nBuffer Cache / ACID / SQL\n适合点查与更新\n[O1]"),
            ("im", 325, 210, 235, 105, "kernel",
             "Database In-Memory\nSGA 内 IM Column Store\n后台 IMCO/SMCO/Wnnn 填充与重填\n不是外部 CDC\n[O1][O2]"),
            ("vector", 590, 210, 235, 105, "kernel",
             "AI Vector Search\nVECTOR 类型 / 向量池 / 索引\n关系条件与向量检索同 SQL\n[O1][O3]"),
            ("multi", 855, 210, 205, 105, "kernel",
             "Converged Engine\nJSON / Graph / Spatial / Relational\n统一安全与事务\n[O1]"),
            ("exadata", 60, 420, 300, 95, "storage",
             "Exadata AI Smart Scan\n存储服务器执行距离计算与 Top-K\n减少网络与 DB Server 处理\n[O3]"),
            ("iceberg", 420, 420, 300, 95, "storage",
             "Autonomous AI Lakehouse\n外部 Apache Iceberg 表原位查询\n统一 Catalog / Data Lake Accelerator\n[O7]"),
            ("object", 780, 420, 280, 95, "storage",
             "对象存储 / Iceberg 数据\nOCI / AWS / Azure / GCP\n开放数据保留在原位置\n[O7]"),
        ],
        "edges": [
            ("agent", "sql", "生成/执行 SQL、调用 PL/SQL 工具"),
            ("mcp", "agent", "暴露 Select AI Agent tools"),
            ("llm", "agent", "模型推理（按配置）"),
            ("llm", "vector", "Embedding：外部模型或本地 ONNX"),
            ("sql", "im", "同一数据库对象：后台填充/重填列格式"),
            ("sql", "vector", "同 SQL 执行计划"),
            ("im", "exadata", "扫描/谓词下推"),
            ("vector", "exadata", "距离计算与 Top-K 下推"),
            ("iceberg", "object", "Iceberg/Catalog 解析"),
            ("sql", "iceberg", "SQL 原位关联查询"),
        ],
        "note": "公开资料可确认：Select AI Agent 是数据库内框架；MCP Server 是 Autonomous AI Database 托管能力；IM Column Store 位于数据库实例 SGA。公开资料不支持“客户自建 Sidecar MCP”或“Redo 直接同步 IMCS”的表述。",
    }


def spec_polardb():
    return {
        "name": "PolarDB：InnoDB IMCI + AI 节点的库仓一体与 Data+AI",
        "file": "polardb-imci-ai-architecture",
        "nodes": [
            ("rw", 60, 45, 275, 95, "kernel",
             "RW 主节点 / InnoDB 行存\nOLTP 写入、事务与 Redo\n列存索引以 InnoDB Secondary Index 实现\n[P1][P2]"),
            ("redo", 410, 45, 270, 95, "sync",
             "PolarDB 物理复制 / Redo 回放\nRO/Standby 节点从 Redo 重建与维护 IMCI\n不是 Kafka/Flink 外部 ETL\n[P1][P2][P3]"),
            ("imci", 755, 45, 305, 95, "kernel",
             "RO AP 节点 / IMCI\n压缩列存：默认内存，不足时落共享存储\n行存串行/并行/IMCI 三路径成本选择\n[P1][P2]"),
            ("shared", 60, 235, 300, 90, "storage",
             "PolarDB 共享存储\n一写多读；IMCI 可部署 RW、专用 AP RO\n或独立 Standby，隔离级别不同\n[P1]"),
            ("ainode", 410, 235, 300, 90, "service",
             "PolarDB for AI 节点\n独立计费计算节点；可含 GPU\n隔离 AI/ML 训练与推理负载\n[P4][P5]"),
            ("serverless", 760, 235, 300, 90, "service",
             "PolarDB for AI Serverless / VNode\nData-Agent 可选 Serverless 调用计费\nGPU VNode 以 Pod 调度到托管资源池\n[P5][P6]"),
            ("sqlai", 60, 420, 300, 95, "control",
             "SQL / Data-Agent 接口\nPolarDB for AI 通过 SQL 提供 MLOps、\nNL2SQL、NL2Chart、Summary\n[P4][P6]"),
            ("rag", 420, 420, 300, 95, "kernel",
             "IMCI 向量/RAG 数据路径\n列存节点构建向量索引并检索\nAI 节点提供向量化与 LLM 能力\n[P7]"),
            ("dms", 780, 420, 280, 95, "control",
             "DMS + PolarDB for AI\n面向业务用户的自然语言分析入口\n雅迪 10万+ 销售、准确率超90%\n[P8]"),
        ],
        "edges": [
            ("rw", "redo", "提交后复制 Redo"),
            ("redo", "imci", "后台构建/增量维护列存索引"),
            ("shared", "rw", "共享数据文件"),
            ("shared", "imci", "列存溢写/共享 I/O"),
            ("sqlai", "ainode", "SQL 路由模型训练/推理"),
            ("sqlai", "serverless", "按模式选择专属或 Serverless"),
            ("ainode", "rag", "Embedding / LLM"),
            ("imci", "rag", "向量索引与检索"),
            ("dms", "sqlai", "自然语言请求"),
        ],
        "note": "公开资料可确认：IMCI 是 InnoDB 的列存二级索引，借助 Redo 与物理复制在 RO/Standby 维护；AI 能力有专属 AI 节点和 Serverless 两种模式。不能笼统称为“同机 Sidecar”。",
    }


def spec_oceanbase():
    return {
        "name": "OceanBase：数据库内多模/搜索 + External Catalog + 开放计算",
        "file": "oceanbase-lakebase-architecture",
        "nodes": [
            ("sql", 60, 45, 300, 100, "kernel",
             "OceanBase SQL / 事务 / HTAP 内核\n关系、JSON、全文、向量与混合搜索\n语义索引自动把 VARCHAR 转向量并建索引\n[B1][B2]"),
            ("aifunc", 420, 45, 300, 100, "kernel",
             "AI 函数服务（SQL 表达式）\nAI_SPLIT_DOCUMENT / AI_EMBED /\nAI_COMPLETE / AI_RERANK\n[B2]"),
            ("model", 780, 45, 280, 100, "service",
             "第三方模型服务端点\n通过 DBMS_AI_SERVICE 注册模型和 endpoint\n需 API Key；具体模型服务在数据库外\n[B2][B3]"),
            ("catalog", 60, 245, 300, 100, "control",
             "External Catalog\nHMS / Iceberg REST / FILESYSTEM / ODPS\n读取表定义、snapshot、manifest\n[B4][B5]"),
            ("exttable", 420, 245, 300, 100, "kernel",
             "OceanBase 外部表/目录访问层\n解析 Parquet/ORC/CSV 与 Iceberg 元数据\n纳入 OceanBase SQL 查询\n[B4][B5]"),
            ("lake", 780, 245, 280, 100, "storage",
             "外部湖存储\nOSS / S3 / HDFS + Parquet/Iceberg\n当前文档：External Catalog 以只读为主\n[B4][B5]"),
            ("spark", 60, 445, 300, 95, "service",
             "开放计算引擎\nSpark / Ray（官方产品路线）\n通过开放格式/Catalog 或连接器协作\n[B1][B6]"),
            ("fork", 420, 445, 300, 95, "control",
             "Fork Database / Agent 沙箱\n官方方案页声明：克隆、隔离、Diff/回滚\n内部进程与实现细节未公开\n[B1]"),
            ("ctx", 780, 445, 280, 95, "control",
             "上下文/应用层\nPowerMem / DataPilot / Agent 应用\n属于产品与服务层，不等同数据库内核\n[B1]"),
        ],
        "edges": [
            ("sql", "aifunc", "同 SQL 执行"),
            ("aifunc", "model", "调用已注册模型 endpoint"),
            ("catalog", "exttable", "提供 schema/snapshot/manifest"),
            ("exttable", "lake", "按元数据读取数据文件"),
            ("sql", "exttable", "联邦/外部表查询"),
            ("spark", "lake", "开放格式访问"),
            ("fork", "sql", "数据库克隆与隔离控制"),
            ("ctx", "sql", "结构化查询/混合检索"),
            ("ctx", "aifunc", "Embedding/生成/Rerank"),
        ],
        "note": "公开文档已经证明 AI 函数、语义索引、External Catalog 与外部表；官方方案页描述 Lakebase、Spark/Ray、多模表、Fork Database。对这些新 Lakebase 能力，公开资料未完整披露进程边界和写入一致性实现，图中明确标为产品层或“未公开”，不做内核臆测。",
    }


def spec_databricks():
    return {
        "name": "Databricks：Lakebase LTAP + Lakehouse + Agent Bricks",
        "file": "databricks-agent-bricks-architecture",
        "nodes": [
            ("pg", 60, 45, 285, 100, "kernel",
             "Lakebase Postgres Compute\n无状态标准 Postgres 计算层\n仅持有 shared buffers 与本地缓存\n[D1][D2]"),
            ("keeper", 405, 45, 300, 100, "storage",
             "Lakebase Durable Storage\nSafekeepers + Pageservers + Cloud Object Storage\n提交持久化，计算与存储分离\n[D1][D2]"),
            ("transcode", 765, 45, 295, 100, "sync",
             "LTAP Storage Transcoding\n行式 Postgres 数据落湖时转为 Parquet 列式\n不是外部 CDC/复制管道\n[D3]"),
            ("olap", 60, 250, 285, 100, "kernel",
             "Lakehouse//RT / OLAP Engine\n直接查询 live Lakebase 当前状态\n与 Postgres 各用专门引擎\n[D3]"),
            ("open", 405, 250, 300, 100, "storage",
             "单一逻辑副本 / 开放格式\n对象存储中的 Parquet，通过 Delta/Iceberg 读取\nOLTP 与 OLAP 共用存储基础\n[D3]"),
            ("uc", 765, 250, 295, 100, "control",
             "Unity Catalog / Unity AI Gateway\n权限、血缘、审计；模型/Agent/MCP/工具\n统一作为 securable objects 管理\n[D4][D5]"),
            ("aisearch", 60, 455, 285, 100, "service",
             "Databricks AI Search\n独立托管 Serverless 搜索服务\nDelta Sync index 自动同步源 Delta Table\n[D6]"),
            ("agent", 405, 455, 300, 100, "service",
             "Agent Bricks / Supervisor Agent\n托管 Agent 运行时；协调 Genie、AI Search、\nUC Functions、MCP 与自定义 Agent\n[D5][D7]"),
            ("apps", 765, 455, 295, 100, "service",
             "Databricks Apps / Model Serving\n应用与 Agent 服务部署入口\nFinThrive 在数小时内上线多 Agent 助手\n[D8]"),
        ],
        "edges": [
            ("pg", "keeper", "WAL/页面持久化"),
            ("keeper", "transcode", "存储物化时转码"),
            ("transcode", "open", "Parquet + Delta/Iceberg"),
            ("open", "olap", "直接分析单一逻辑副本"),
            ("uc", "olap", "治理分析访问"),
            ("uc", "agent", "身份/权限/工具治理"),
            ("open", "aisearch", "Delta Sync 派生搜索索引"),
            ("aisearch", "agent", "检索工具"),
            ("agent", "apps", "部署与调用"),
        ],
        "note": "需要区分两条路径：LTAP 用存储层转码让 OLTP/OLAP 共享单一逻辑副本；AI Search 仍是从 Delta Table 同步出的独立服务索引。Agent Bricks 是托管 Agent 服务，不是数据库内核。",
    }


def make_drawio(spec):
    mxfile = Element("mxfile", host="drawio", version="26.0.0")
    diagram = SubElement(mxfile, "diagram", id=spec["file"], name=spec["name"])
    model = SubElement(diagram, "mxGraphModel", dx="1200", dy="800", grid="1",
                       gridSize="10", guides="1", page="1", pageWidth="1200",
                       pageHeight="900")
    root = SubElement(model, "root")
    SubElement(root, "mxCell", id="0")
    SubElement(root, "mxCell", id="1", parent="0")
    node_map = {}
    for i, (nid, x, y, w, h, cat, label) in enumerate(spec["nodes"], start=2):
        node_map[nid] = str(i)
        _, fill, stroke = CATEGORY[cat]
        cell = SubElement(root, "mxCell", id=str(i), value=label.replace("\n", "&#xa;"),
                          style=f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};"
                                f"strokeColor={stroke};fontSize=11;",
                          vertex="1", parent="1")
        SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w),
                   height=str(h), **{"as": "geometry"})
    eid = 100
    for edge_num, (src, dst, label) in enumerate(spec["edges"], start=1):
        cell = SubElement(root, "mxCell", id=str(eid), value=str(edge_num),
                          style="edgeStyle=orthogonalEdgeStyle;rounded=1;"
                                "orthogonalLoop=1;jettySize=auto;html=1;"
                                "strokeColor=#334155;fontSize=10;fontStyle=1;"
                                "labelBackgroundColor=#ffffff;",
                          edge="1", parent="1", source=node_map[src],
                          target=node_map[dst])
        SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
        eid += 1
    # Full connector descriptions live in a dedicated two-column legend.
    # Keeping only numbers on edges prevents labels from covering nodes.
    for edge_num, (_, _, label) in enumerate(spec["edges"], start=1):
        col = 0 if edge_num <= 5 else 1
        row = edge_num - 1 if col == 0 else edge_num - 6
        x = 60 + col * 530
        y = 610 + row * 34
        cell = SubElement(
            root, "mxCell", id=str(eid), value=f"{edge_num}. {label}",
            style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;"
                  "strokeColor=#cbd5e1;fontSize=10;align=left;spacingLeft=8;",
            vertex="1", parent="1"
        )
        SubElement(cell, "mxGeometry", x=str(x), y=str(y), width="490",
                   height="28", **{"as": "geometry"})
        eid += 1
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + tostring(mxfile, encoding="unicode")
    (OUT / f"{spec['file']}.drawio").write_text(xml, encoding="utf-8")


def make_svg(spec):
    nodes = {n[0]: n for n in spec["nodes"]}
    legend_rows = min(5, len(spec["edges"]))
    canvas_h = 650 + legend_rows * 34
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 {canvas_h}" width="100%" height="auto">',
        '<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" '
        'orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#334155"/></marker></defs>',
        f'<rect width="1120" height="{canvas_h}" rx="14" fill="#fff" stroke="#e2e8f0"/>',
    ]
    # Edges first.
    for edge_num, (src, dst, label) in enumerate(spec["edges"], start=1):
        _, sx, sy, sw, sh, _, _ = nodes[src]
        _, dx, dy, dw, dh, _, _ = nodes[dst]
        if abs(dy - sy) < 120:
            # Horizontal links stay in the gap between adjacent boxes.
            x1, y1 = sx + sw, sy + sh / 2
            x2, y2 = dx, dy + dh / 2
            if x2 < x1:
                x1, y1 = sx, sy + sh / 2
                x2, y2 = dx + dw, dy + dh / 2
            path = f"M{x1},{y1} L{x2},{y2}"
            tx, ty = (x1 + x2) / 2, (y1 + y2) / 2
        else:
            # Vertical links get a small deterministic channel offset.
            if dy > sy:
                x1, y1 = sx + sw / 2, sy + sh
                x2, y2 = dx + dw / 2, dy
            else:
                x1, y1 = sx + sw / 2, sy
                x2, y2 = dx + dw / 2, dy + dh
            channel_offset = ((edge_num - 1) % 5 - 2) * 7
            midy = (y1 + y2) / 2 + channel_offset
            path = f"M{x1},{y1} L{x1},{midy} L{x2},{midy} L{x2},{y2}"
            tx, ty = (x1 + x2) / 2, midy
        parts.append(f'<path d="{path}" fill="none" stroke="#334155" stroke-width="1.5" '
                     'marker-end="url(#arr)"/>')
        # A compact numbered badge replaces the full edge label.
        parts.append(f'<circle cx="{tx}" cy="{ty}" r="9" fill="#ffffff" '
                     'stroke="#334155" stroke-width="1.2"/>')
        parts.append(f'<text x="{tx}" y="{ty + 3.5}" text-anchor="middle" '
                     'font-size="9" font-weight="700" font-family="system-ui" '
                     f'fill="#334155">{edge_num}</text>')
    # Nodes.
    for _, x, y, w, h, cat, label in spec["nodes"]:
        cat_label, fill, stroke = CATEGORY[cat]
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
                     f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        parts.append(f'<rect x="{x+8}" y="{y+7}" width="{min(150, w-16)}" height="18" rx="9" '
                     f'fill="{stroke}"/>')
        parts.append(f'<text x="{x+16}" y="{y+20}" font-size="10" font-weight="700" '
                     f'font-family="system-ui" fill="#fff">{html.escape(cat_label)}</text>')
        lines = label.splitlines()
        start = y + 43
        for idx, line in enumerate(lines):
            size = 11 if idx == 0 else 9.5
            weight = "700" if idx == 0 else "400"
            color = stroke if idx == 0 else "#334155"
            parts.append(f'<text x="{x+w/2}" y="{start+idx*14}" text-anchor="middle" '
                         f'font-size="{size}" font-weight="{weight}" font-family="system-ui" '
                         f'fill="{color}">{html.escape(line)}</text>')
    # Legend and caveat.
    lx = 60
    for cat in ("kernel", "control", "sync", "service", "storage"):
        label, fill, stroke = CATEGORY[cat]
        parts.append(f'<rect x="{lx}" y="575" width="12" height="12" rx="2" fill="{fill}" '
                     f'stroke="{stroke}"/>')
        parts.append(f'<text x="{lx+17}" y="585" font-size="9.5" font-family="system-ui" '
                     f'fill="#334155">{html.escape(label)}</text>')
        lx += 205
    parts.append('<text x="60" y="619" font-size="11" font-weight="700" '
                 'font-family="system-ui" fill="#0f172a">连接关系</text>')
    for edge_num, (_, _, label) in enumerate(spec["edges"], start=1):
        col = 0 if edge_num <= 5 else 1
        row = edge_num - 1 if col == 0 else edge_num - 6
        x = 60 + col * 530
        y = 628 + row * 34
        parts.append(f'<rect x="{x}" y="{y}" width="490" height="27" rx="5" '
                     'fill="#f8fafc" stroke="#cbd5e1"/>')
        parts.append(f'<circle cx="{x+16}" cy="{y+13.5}" r="8" fill="#ffffff" '
                     'stroke="#334155"/>')
        parts.append(f'<text x="{x+16}" y="{y+17}" text-anchor="middle" '
                     'font-size="8.5" font-weight="700" font-family="system-ui" '
                     f'fill="#334155">{edge_num}</text>')
        parts.append(f'<text x="{x+31}" y="{y+17}" font-size="9.2" '
                     f'font-family="system-ui" fill="#334155">{html.escape(label)}</text>')
    parts.append("</svg>")
    (OUT / f"{spec['file']}.svg").write_text("".join(parts), encoding="utf-8")


if __name__ == "__main__":
    for factory in (spec_oracle, spec_polardb, spec_oceanbase, spec_databricks):
        spec = factory()
        make_drawio(spec)
        make_svg(spec)
        print(f"generated {spec['file']}.drawio/.svg")
