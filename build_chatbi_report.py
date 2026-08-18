#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the comprehensive ChatBI Industry Architecture Report:
chatbi-industry-architecture-report.html
"""

import html
import os
import sys

def generate_svg_pipeline():
    """Generates the End-to-End ChatBI Architecture and Pipeline SVG diagram."""
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1160 760" width="100%" height="auto">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#2563EB"/>
    </marker>
    <marker id="arrow-green" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#16A34A"/>
    </marker>
    <marker id="arrow-orange" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#EA580C"/>
    </marker>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1160" height="760" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>

  <!-- Title Banner -->
  <rect x="20" y="20" width="1120" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="40" y="46" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="15" font-weight="700" fill="#0F172A">
    现代企业级 ChatBI 端到端技术架构与 Pipeline 执行链路全景
  </text>
  <text x="860" y="46" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="12" fill="#64748B">
    核心模式：Text2DSL + 语义指标层 + Agent 自愈循环
  </text>

  <!-- Layer 1: User & Interface Layer -->
  <rect x="30" y="80" width="200" height="640" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.2" filter="url(#shadow)"/>
  <rect x="30" y="80" width="200" height="32" rx="8" fill="#0284C7"/>
  <text x="130" y="101" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">1. 交互与多轮会话层</text>
  
  <rect x="45" y="125" width="170" height="75" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="55" y="147" font-size="12" font-weight="700" fill="#0369A1">多端交互入口</text>
  <text x="55" y="167" font-size="11" fill="#475569">• Web/移动端 BI 门户</text>
  <text x="55" y="185" font-size="11" fill="#475569">• 飞书 / 企微 / 钉钉机器人</text>

  <rect x="45" y="215" width="170" height="95" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="55" y="237" font-size="12" font-weight="700" fill="#0369A1">意图识别与分流</text>
  <text x="55" y="257" font-size="11" fill="#475569">• 闲聊/知识问答 (RAG)</text>
  <text x="55" y="275" font-size="11" fill="#475569">• 报表问数 (Text2DSL)</text>
  <text x="55" y="293" font-size="11" fill="#475569">• 归因与预测分析 Agent</text>

  <rect x="45" y="325" width="170" height="105" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="55" y="347" font-size="12" font-weight="700" fill="#0369A1">多轮上下文会话管理</text>
  <text x="55" y="367" font-size="11" fill="#475569">• 历史指代消解 (Coreference)</text>
  <text x="55" y="385" font-size="11" fill="#475569">• 筛选继承与下钻追问</text>
  <text x="55" y="403" font-size="11" fill="#475569">• 对话状态跟踪 (DST)</text>

  <rect x="45" y="445" width="170" height="95" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="55" y="467" font-size="12" font-weight="700" fill="#0369A1">模糊澄清与反问</text>
  <text x="55" y="487" font-size="11" fill="#475569">• 缺省槽位主动追问</text>
  <text x="55" y="505" font-size="11" fill="#475569">• 歧义指标/维度候选推荐</text>
  <text x="55" y="523" font-size="11" fill="#475569">• 联想推荐引导词</text>

  <!-- Layer 2: Semantic & Knowledge Layer -->
  <rect x="250" y="80" width="200" height="640" rx="8" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.2" filter="url(#shadow)"/>
  <rect x="250" y="80" width="200" height="32" rx="8" fill="#7C3AED"/>
  <text x="350" y="101" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">2. 语义与知识索引层</text>

  <rect x="265" y="125" width="170" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="275" y="147" font-size="12" font-weight="700" fill="#6D28D9">企业指标语义层</text>
  <text x="275" y="167" font-size="11" fill="#475569">• 原子指标 / 衍生指标定义</text>
  <text x="275" y="185" font-size="11" fill="#475569">• 业务维度与修饰词字典</text>
  <text x="275" y="203" font-size="11" fill="#475569">• 同义词与别名映射表</text>
  <text x="275" y="221" font-size="11" fill="#475569">• 维度表与事实表关联模型</text>

  <rect x="265" y="250" width="170" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="275" y="272" font-size="12" font-weight="700" fill="#6D28D9">Schema Linking 检索</text>
  <text x="275" y="292" font-size="11" fill="#475569">• 向量相似度检索 (Dense)</text>
  <text x="275" y="310" font-size="11" fill="#475569">• BM25 关键词倒排 (Sparse)</text>
  <text x="275" y="328" font-size="11" fill="#475569">• 混合 Rerank 动态重排</text>
  <text x="275" y="346" font-size="11" fill="#475569">• 上下文 Schema 剪枝过滤</text>

  <rect x="265" y="375" width="170" height="100" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="275" y="397" font-size="12" font-weight="700" fill="#6D28D9">ICL 动态样本库</text>
  <text x="275" y="417" font-size="11" fill="#475569">• 行业标准问答 Few-Shot</text>
  <text x="275" y="435" font-size="11" fill="#475569">• 用户高频采纳黄金案例</text>
  <text x="275" y="453" font-size="11" fill="#475569">• 专家修正样例沉淀</text>

  <!-- Layer 3: Agentic Generation Layer -->
  <rect x="470" y="80" width="210" height="640" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.2" filter="url(#shadow)"/>
  <rect x="470" y="80" width="210" height="32" rx="8" fill="#2563EB"/>
  <text x="575" y="101" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">3. DSL/SQL 生成引擎</text>

  <rect x="485" y="125" width="180" height="120" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="495" y="147" font-size="12" font-weight="700" fill="#1D4ED8">Multi-Agent 协作生成</text>
  <text x="495" y="167" font-size="11" fill="#475569">• 选表与模型定位 Agent</text>
  <text x="495" y="185" font-size="11" fill="#475569">• 维度与度量选择 Agent</text>
  <text x="495" y="203" font-size="11" fill="#475569">• 筛选与过滤条件 Agent</text>
  <text x="495" y="221" font-size="11" fill="#475569">• 高级计算 (同环比/LOD) Agent</text>

  <rect x="485" y="260" width="180" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="495" y="282" font-size="12" font-weight="700" fill="#1D4ED8">中间表示 (Text2DSL)</text>
  <text x="495" y="302" font-size="11" fill="#475569">• 结构化 JSON/AST 协议</text>
  <text x="495" y="320" font-size="11" fill="#475569">• 规避模型直接写物理 SQL</text>
  <text x="495" y="338" font-size="11" fill="#475569">• 算子化：聚合/切片/排序</text>
  <text x="495" y="356" font-size="11" fill="#475569">• 白盒可视化：用户可干预</text>

  <rect x="485" y="385" width="180" height="100" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="495" y="407" font-size="12" font-weight="700" fill="#1D4ED8">大模型基座与微调</text>
  <text x="495" y="427" font-size="11" fill="#475569">• 通用大模型 (DeepSeek/千问)</text>
  <text x="495" y="445" font-size="11" fill="#475569">• 领域微调专用小模型</text>
  <text x="495" y="463" font-size="11" fill="#475569">• 大小模型双通道路由分发</text>

  <!-- Layer 4: Validation, Security & Compiler Layer -->
  <rect x="700" y="80" width="210" height="640" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.2" filter="url(#shadow)"/>
  <rect x="700" y="80" width="210" height="32" rx="8" fill="#059669"/>
  <text x="805" y="101" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">4. 校验自愈与安全编译</text>

  <rect x="715" y="125" width="180" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="725" y="147" font-size="12" font-weight="700" fill="#047857">AST 语法与语义静态校验</text>
  <text x="725" y="167" font-size="11" fill="#475569">• 字段存在性与类型检查</text>
  <text x="725" y="185" font-size="11" fill="#475569">• 聚合维度一致性验证</text>
  <text x="725" y="203" font-size="11" fill="#475569">• 时间范围与常量格式检验</text>
  <text x="725" y="221" font-size="11" fill="#475569">• 防注入与危险操作拦截</text>

  <rect x="715" y="250" width="180" height="110" rx="6" fill="#FFFFFF" stroke="#EA580C" stroke-width="1.2"/>
  <text x="725" y="272" font-size="12" font-weight="700" fill="#C2410C">Self-Reflection 反思自愈</text>
  <text x="725" y="292" font-size="11" fill="#475569">• 编译/执行报错捕获</text>
  <text x="725" y="310" font-size="11" fill="#475569">• 结构化 Error Prompt 回传</text>
  <text x="725" y="328" font-size="11" fill="#475569">• 模型自动重试纠错 (≤3次)</text>
  <text x="725" y="346" font-size="11" fill="#475569">• 无法自愈时转人工澄清</text>

  <rect x="715" y="375" width="180" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="725" y="397" font-size="12" font-weight="700" fill="#047857">行/列级权限动态注入</text>
  <text x="725" y="417" font-size="11" fill="#475569">• AST 层注入租户/组织过滤</text>
  <text x="725" y="435" font-size="11" fill="#475569">• 敏感字段脱敏与列权限拦截</text>
  <text x="725" y="453" font-size="11" fill="#475569">• 无法被自然语言指令绕过</text>
  <text x="725" y="471" font-size="11" fill="#475569">• 审计日志与追溯记录</text>

  <rect x="715" y="500" width="180" height="85" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="725" y="522" font-size="12" font-weight="700" fill="#047857">多方言 SQL 编译下推</text>
  <text x="725" y="542" font-size="11" fill="#475569">• ClickHouse / StarRocks</text>
  <text x="725" y="560" font-size="11" fill="#475569">• MySQL / PolarDB / OB</text>
  <text x="725" y="578" font-size="11" fill="#475569">• Presto / Spark / Doris</text>

  <!-- Layer 5: Execution & Insights Layer -->
  <rect x="930" y="80" width="200" height="640" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.2" filter="url(#shadow)"/>
  <rect x="930" y="80" width="200" height="32" rx="8" fill="#D97706"/>
  <text x="1030" y="101" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">5. 极速执行与洞察呈现</text>

  <rect x="945" y="125" width="170" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="955" y="147" font-size="12" font-weight="700" fill="#B45309">底层计算与加速</text>
  <text x="955" y="167" font-size="11" fill="#475569">• MPP/HTAP 向量化执行</text>
  <text x="955" y="185" font-size="11" fill="#475569">• 查询结果智能缓存 (Cache)</text>
  <text x="955" y="203" font-size="11" fill="#475569">• 物化视图与预聚合 Cube</text>
  <text x="955" y="221" font-size="11" fill="#475569">• 秒级/毫秒级交互式返回</text>

  <rect x="945" y="250" width="170" height="100" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="955" y="272" font-size="12" font-weight="700" fill="#B45309">智能图表推荐</text>
  <text x="955" y="292" font-size="11" fill="#475569">• Chart Advisor 规则与算法</text>
  <text x="955" y="310" font-size="11" fill="#475569">• 趋势/占比/分布/对比适配</text>
  <text x="955" y="328" font-size="11" fill="#475569">• AntV / ECharts 一键切换</text>

  <rect x="945" y="365" width="170" height="110" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="955" y="387" font-size="12" font-weight="700" fill="#B45309">深度归因与数据洞察</text>
  <text x="955" y="407" font-size="11" fill="#475569">• 指标异动波动归因分析</text>
  <text x="955" y="425" font-size="11" fill="#475569">• 贡献度拆解 (Shapley/决策树)</text>
  <text x="955" y="443" font-size="11" fill="#475569">• 自然语言经营总结摘要</text>
  <text x="955" y="461" font-size="11" fill="#475569">• 智能决策行动建议</text>

  <!-- Flow Arrows between Layers -->
  <path d="M230 160 L250 160" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M230 300 L250 300" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow)"/>
  
  <path d="M450 180 L470 180" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M450 310 L470 310" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow)"/>

  <path d="M680 200 L700 200" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M680 315 L700 315" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Reflection Loop Arrow -->
  <path d="M715 305 C680 305 680 340 665 340" fill="none" stroke="#EA580C" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arrow-orange)"/>
  <text x="685" y="365" font-size="10" font-weight="700" fill="#EA580C">报错自愈反馈</text>

  <path d="M910 180 L930 180" fill="none" stroke="#16A34A" stroke-width="2" marker-end="url(#arrow-green)"/>
  <path d="M910 420 L930 420" fill="none" stroke="#16A34A" stroke-width="2" marker-end="url(#arrow-green)"/>

  <!-- Footer annotation -->
  <rect x="30" y="660" width="1100" height="45" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="45" y="688" font-size="11.5" fill="#334155">
    💡 <strong>核心技术共识：</strong>业界头部厂商（阿里、腾讯、字节、帆软）均已放弃“大模型直接端到端直出物理 SQL”的脆弱路线，全面收敛至<strong>「语义层/指标模型 + Text2DSL 结构化生成 + AST 静态校验与权限拦截 + 引擎编译下推」</strong>的稳健工业架构。
  </text>
</svg>'''

def generate_svg_comparison_matrix():
    """Generates the Technical Route Comparison Matrix SVG."""
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1160 480" width="100%" height="auto">
  <defs>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>
  <rect width="1160" height="480" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>

  <!-- Title -->
  <text x="30" y="38" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="16" font-weight="700" fill="#0F172A">
    三代 ChatBI 技术路线演进与对比（从纯 Text2SQL 到 Text2DSL + Agent 架构）
  </text>

  <!-- Route 1: 1.0 Pure Text2SQL -->
  <rect x="30" y="60" width="350" height="395" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.2" filter="url(#shadow2)"/>
  <rect x="30" y="60" width="350" height="36" rx="8" fill="#EF4444"/>
  <text x="205" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">第一代：纯 Text2SQL 路线（黑盒直出）</text>
  
  <text x="45" y="120" font-size="12" font-weight="700" fill="#991B1B">【实现链路】</text>
  <text x="45" y="140" font-size="11.5" fill="#334155">用户自然语言 → Prompt 拼 DDL → LLM 直出 SQL → 数据库执行</text>
  
  <text x="45" y="175" font-size="12" font-weight="700" fill="#991B1B">【核心缺陷（企业落地失败根因）】</text>
  <text x="45" y="198" font-size="11" fill="#475569">❌ <strong>复杂口径无法表达：</strong>同环比、留存、LOD 等无法从单表映射</text>
  <text x="45" y="222" font-size="11" fill="#475569">❌ <strong>方言难以穷尽：</strong>无法准确掌握数十种 OLAP 引擎专有函数</text>
  <text x="45" y="246" font-size="11" fill="#475569">❌ <strong>黑盒不可干预：</strong>业务人员看不懂复杂 SQL，无法纠错</text>
  <text x="45" y="270" font-size="11" fill="#475569">❌ <strong>安全风险极高：</strong>无法可靠注入租户行级安全（RLS）</text>
  <text x="45" y="294" font-size="11" fill="#475569">❌ <strong>幻觉率居高不下：</strong>字段名捏造、JOIN 关系错误、聚合笛卡尔积</text>

  <rect x="45" y="325" width="320" height="115" rx="6" fill="#FFFFFF" stroke="#FCA5A5"/>
  <text x="55" y="348" font-size="11.5" font-weight="700" fill="#B91C1C">⚠️ 工业界结论：</text>
  <text x="55" y="370" font-size="11" fill="#475569">适合学术 Benchmark（如 Spider），在表数量 > 50、指标计算复杂的企业真实场景中，真实可用准确率通常 &lt; 40%，无法独立支撑严肃业务分析。</text>

  <!-- Route 2: 2.0 Text2DSL -->
  <rect x="405" y="60" width="350" height="395" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.2" filter="url(#shadow2)"/>
  <rect x="405" y="60" width="350" height="36" rx="8" fill="#10B981"/>
  <text x="580" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">第二代：Text2DSL + 语义层（主流基线）</text>

  <text x="420" y="120" font-size="12" font-weight="700" fill="#065F46">【实现链路】</text>
  <text x="420" y="140" font-size="11.5" fill="#334155">用户输入 → 语义层映射 → LLM 生成 DSL JSON → BI 引擎编译下推 SQL</text>

  <text x="420" y="175" font-size="12" font-weight="700" fill="#065F46">【核心优势（帆软、阿里、腾讯共同基底）】</text>
  <text x="420" y="198" font-size="11" fill="#475569">✅ <strong>口径收敛在语义层：</strong>指标、维度、同义词在元数据中集中治理</text>
  <text x="420" y="222" font-size="11" fill="#475569">✅ <strong>算子化抽象：</strong>大模型只需决定“查什么维度和度量”，不写 SQL</text>
  <text x="420" y="246" font-size="11" fill="#475569">✅ <strong>白盒可干预：</strong>用户前端可直接勾选、修改识别错误的维度/过滤项</text>
  <text x="420" y="270" font-size="11" fill="#475569">✅ <strong>引擎层统一安全：</strong>BI 引擎根据用户身份强制注入行/列权限</text>
  <text x="420" y="294" font-size="11" fill="#475569">✅ <strong>多方言无缝适配：</strong>由 BI 翻译器生成对应数据库的高性能 SQL</text>

  <rect x="420" y="325" width="320" height="115" rx="6" fill="#FFFFFF" stroke="#86EFAC"/>
  <text x="430" y="348" font-size="11.5" font-weight="700" fill="#047857">🎯 工业界现状：</text>
  <text x="430" y="370" font-size="11" fill="#475569">当前国内主流商业 BI（Quick BI、FineChatBI、腾讯云 BI）的标准底座，准确率可提升至 85%~92%，有效实现“可控生成、可信查数”。</text>

  <!-- Route 3: 3.0 Agentic Hybrid -->
  <rect x="780" y="60" width="350" height="395" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.2" filter="url(#shadow2)"/>
  <rect x="780" y="60" width="350" height="36" rx="8" fill="#3B82F6"/>
  <text x="955" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">第三代：Data Agent 智能体（前沿演进）</text>

  <text x="795" y="120" font-size="12" font-weight="700" fill="#1E40AF">【实现链路】</text>
  <text x="795" y="140" font-size="11.5" fill="#334155">复杂业务目标 → Agent 任务拆解 → ReAct 工具调用 → 深度归因与报告</text>

  <text x="795" y="175" font-size="12" font-weight="700" fill="#1E40AF">【核心能力突破（火山引擎 2.0、阿里小Q）】</text>
  <text x="795" y="198" font-size="11" fill="#475569">🚀 <strong>从查数跃迁到深度分析：</strong>不仅回答“是多少”，还能回答“为什么”</text>
  <text x="795" y="222" font-size="11" fill="#475569">🚀 <strong>自动异动归因与诊断：</strong>基于下钻树、Shapley 贡献度定位根因</text>
  <text x="795" y="246" font-size="11" fill="#475569">🚀 <strong>动态规划与工具路由：</strong>按需调度 Text2DSL、Python 沙箱、RAG</text>
  <text x="795" y="270" font-size="11" fill="#475569">🚀 <strong>闭环自愈机制：</strong>编译失败自动 Reflection，多次重试修正 Prompt</text>
  <text x="795" y="294" font-size="11" fill="#475569">🚀 <strong>端到端报告自动化：</strong>一键组装完整 Dashboard 与图文经营周报</text>

  <rect x="795" y="325" width="320" height="115" rx="6" fill="#FFFFFF" stroke="#93C5FD"/>
  <text x="805" y="348" font-size="11.5" font-weight="700" fill="#1D4ED8">🌟 未来趋势：</text>
  <text x="805" y="370" font-size="11" fill="#475569">将 BI 从被动的“取数工具”转变为主动的“AI 数据分析师”，融合湖仓算力、MCP 标准协议与企业工作流协同平台。</text>
</svg>'''

def generate_svg_vendor_matrix():
    """Generates the 4 Vendors Architectural Mapping SVG."""
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1160 520" width="100%" height="auto">
  <defs>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>
  <rect width="1160" height="520" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>

  <!-- Title -->
  <text x="30" y="38" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="16" font-weight="700" fill="#0F172A">
    国内四大头部厂商 ChatBI 技术栈与核心组件落点全景
  </text>

  <!-- Vendor 1: Alibaba Quick BI -->
  <rect x="25" y="60" width="265" height="435" rx="8" fill="#F8FAFC" stroke="#E2E8F0" filter="url(#shadow3)"/>
  <rect x="25" y="60" width="265" height="38" rx="8" fill="#EA580C"/>
  <text x="157" y="85" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">阿里云 Quick BI (智能小Q)</text>

  <rect x="35" y="110" width="245" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="45" y="130" font-size="11.5" font-weight="700" fill="#C2410C">核心架构路线</text>
  <text x="45" y="148" font-size="10.5" fill="#475569">• NL2DSL → NL2SQL2DSL 混合</text>
  <text x="45" y="163" font-size="10.5" fill="#475569">• 抽象 SQL 算子扩展 (时间/LOD)</text>

  <rect x="35" y="185" width="245" height="75" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="45" y="205" font-size="11.5" font-weight="700" fill="#C2410C">模型与中间层</text>
  <text x="45" y="223" font-size="10.5" fill="#475569">• 通义千问 Qwen 数据微调大模型</text>
  <text x="45" y="238" font-size="10.5" fill="#475569">• 轻量小模型快速意图响应</text>
  <text x="45" y="253" font-size="10.5" fill="#475569">• AI 中间层链接 Agent 与算子</text>

  <rect x="35" y="270" width="245" height="70" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="45" y="290" font-size="11.5" font-weight="700" fill="#C2410C">BI 底座与引擎</text>
  <text x="45" y="308" font-size="10.5" fill="#475569">• 经典星型/雪花模型建模层</text>
  <text x="45" y="323" font-size="10.5" fill="#475569">• 40+ 数据源方言翻译下推</text>

  <rect x="35" y="350" width="245" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="45" y="370" font-size="11.5" font-weight="700" fill="#C2410C">可视化与生态</text>
  <text x="45" y="388" font-size="10.5" fill="#475569">• 蚂蚁 AntV 智能图表推荐</text>
  <text x="45" y="403" font-size="10.5" fill="#475569">• 钉钉智能助理 / 阿里云 RAM</text>

  <rect x="35" y="425" width="245" height="55" rx="6" fill="#FFF7ED" stroke="#FDBA74"/>
  <text x="45" y="445" font-size="10.5" font-weight="700" fill="#9A3412">代表案例：</text>
  <text x="45" y="463" font-size="10" fill="#7C2D12">雅迪电动车 (10万+销售/NL2SQL>90%)</text>

  <!-- Vendor 2: Tencent Cloud BI -->
  <rect x="305" y="60" width="265" height="435" rx="8" fill="#F8FAFC" stroke="#E2E8F0" filter="url(#shadow3)"/>
  <rect x="305" y="60" width="265" height="38" rx="8" fill="#0284C7"/>
  <text x="437" y="85" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">腾讯云 BI (智能小腾 / ChatBI)</text>

  <rect x="315" y="110" width="245" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="325" y="130" font-size="11.5" font-weight="700" fill="#0369A1">核心架构路线</text>
  <text x="325" y="148" font-size="10.5" fill="#475569">• Text2DSL + Multi-Agent 架构</text>
  <text x="325" y="163" font-size="10.5" fill="#475569">• DSL + Python 联合计算引擎</text>

  <rect x="315" y="185" width="245" height="75" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="325" y="205" font-size="11.5" font-weight="700" fill="#0369A1">Agent 协同与调优</text>
  <text x="325" y="223" font-size="10.5" fill="#475569">• 选表/维度/指标/条件 Agent 协作</text>
  <text x="325" y="238" font-size="10.5" fill="#475569">• ES + LLM 意图澄清机制</text>
  <text x="325" y="253" font-size="10.5" fill="#475569">• In-Context Learning (ICL) 场景调优</text>

  <rect x="315" y="270" width="245" height="70" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="325" y="290" font-size="11.5" font-weight="700" fill="#0369A1">数据安全与模型</text>
  <text x="325" y="308" font-size="10.5" fill="#475569">• 仅读表头元数据，数据不离本地</text>
  <text x="325" y="323" font-size="10.5" fill="#475569">• 适配腾讯混元、DeepSeek-V3/R1</text>

  <rect x="315" y="350" width="245" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="325" y="370" font-size="11.5" font-weight="700" fill="#0369A1">可视化与生态</text>
  <text x="325" y="388" font-size="10.5" fill="#475569">• 智能多轮追问与指标联想</text>
  <text x="325" y="403" font-size="10.5" fill="#475569">• 企微应用嵌出 / H5 多端轻量访问</text>

  <rect x="315" y="425" width="245" height="55" rx="6" fill="#F0F9FF" stroke="#BAE6FD"/>
  <text x="325" y="445" font-size="10.5" font-weight="700" fill="#0369A1">主要特色：</text>
  <text x="325" y="463" font-size="10" fill="#0C4A6E">公有云+私有化+混元生态多端嵌出</text>

  <!-- Vendor 3: ByteDance Volcano Engine -->
  <rect x="585" y="60" width="265" height="435" rx="8" fill="#F8FAFC" stroke="#E2E8F0" filter="url(#shadow3)"/>
  <rect x="585" y="60" width="265" height="38" rx="8" fill="#2563EB"/>
  <text x="717" y="85" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">火山引擎 (DataWind / Data Agent)</text>

  <rect x="595" y="110" width="245" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="605" y="130" font-size="11.5" font-weight="700" fill="#1D4ED8">核心架构路线</text>
  <text x="605" y="148" font-size="10.5" fill="#475569">• Data Agent 2.0 智能调度站</text>
  <text x="605" y="163" font-size="10.5" fill="#475569">• 围绕 ByteHouse 重抽取极速计算</text>

  <rect x="595" y="185" width="245" height="75" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="605" y="205" font-size="11.5" font-weight="700" fill="#1D4ED8">深度分析与归因</text>
  <text x="605" y="223" font-size="10.5" fill="#475569">• 异常指标自动检测与下钻归因</text>
  <text x="605" y="238" font-size="10.5" fill="#475569">• 深度研究 Agent 端到端报告生成</text>
  <text x="605" y="253" font-size="10.5" fill="#475569">• 豆包 (Doubao) 大模型专属适配</text>

  <rect x="595" y="270" width="245" height="70" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="605" y="290" font-size="11.5" font-weight="700" fill="#1D4ED8">底座与工具集成</text>
  <text x="605" y="308" font-size="10.5" fill="#475569">• ByteHouse MPP 向量化秒级查询</text>
  <text x="605" y="323" font-size="10.5" fill="#475569">• Python/SQL 动态沙箱执行环境</text>

  <rect x="595" y="350" width="245" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="605" y="370" font-size="11.5" font-weight="700" fill="#1D4ED8">协作与生态</text>
  <text x="605" y="388" font-size="10.5" fill="#475569">• 飞书卡片问答 / 看板订阅推送</text>
  <text x="605" y="403" font-size="10.5" fill="#475569">• 开放 OpenAPI 与 MCP 协议支持</text>

  <rect x="595" y="425" width="245" height="55" rx="6" fill="#EFF6FF" stroke="#BFDBFE"/>
  <text x="605" y="445" font-size="10.5" font-weight="700" fill="#1E40AF">主要特色：</text>
  <text x="605" y="463" font-size="10" fill="#172554">极速 ByteHouse 算力 + 飞书闭环协同</text>

  <!-- Vendor 4: FanRuan FineChatBI -->
  <rect x="865" y="60" width="265" height="435" rx="8" fill="#F8FAFC" stroke="#E2E8F0" filter="url(#shadow3)"/>
  <rect x="865" y="60" width="265" height="38" rx="8" fill="#059669"/>
  <text x="997" y="85" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">帆软 (FineChatBI / FineBI)</text>

  <rect x="875" y="110" width="245" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="885" y="130" font-size="11.5" font-weight="700" fill="#047857">核心架构路线</text>
  <text x="885" y="148" font-size="10.5" fill="#475569">• 坚守 Text2DSL “可控生成/可信查数”</text>
  <text x="885" y="163" font-size="10.5" fill="#475569">• fine-chat-bi-parser 语义解析模型</text>

  <rect x="875" y="185" width="245" height="75" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="885" y="205" font-size="11.5" font-weight="700" fill="#047857">企业语义与治理</text>
  <text x="885" y="223" font-size="10.5" fill="#475569">• 沉淀 20 年企业级指标中心与字典</text>
  <text x="885" y="238" font-size="10.5" fill="#475569">• 极速模式（免改写）与智能改写双模</text>
  <text x="885" y="253" font-size="10.5" fill="#475569">• FineAI 算法供给与大模型转发中枢</text>

  <rect x="875" y="270" width="245" height="70" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="885" y="290" font-size="11.5" font-weight="700" fill="#047857">安全与权限穿透</text>
  <text x="885" y="308" font-size="10.5" fill="#475569">• 深度集成 FineBI 中国式复杂权限树</text>
  <text x="885" y="323" font-size="10.5" fill="#475569">• 行级/列级/模板级细粒度隔离</text>

  <rect x="875" y="350" width="245" height="65" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="885" y="370" font-size="11.5" font-weight="700" fill="#047857">交互与白盒化</text>
  <text x="885" y="388" font-size="10.5" fill="#475569">• 问答结果业务逻辑全流程白盒可干预</text>
  <text x="885" y="403" font-size="10.5" fill="#475569">• 一键沉淀为 FineBI 仪表板/看板组件</text>

  <rect x="875" y="425" width="245" height="55" rx="6" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="885" y="445" font-size="10.5" font-weight="700" fill="#065F46">主要特色：</text>
  <text x="885" y="463" font-size="10" fill="#064E3B">私有化能力极强，契合大型政企复杂报表</text>
</svg>'''

def build_full_html():
    svg_pipeline = generate_svg_pipeline()
    svg_comparison = generate_svg_comparison_matrix()
    svg_vendors = generate_svg_vendor_matrix()

    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>业界主流 ChatBI 深度技术架构与实现方案对比分析报告（阿里/腾讯/字节/帆软）</title>
  <style>
    :root {{
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #eff6ff;
      --text-main: #0f172a;
      --text-muted: #475569;
      --border: #e2e8f0;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --sidebar-w: 280px;
      --ali: #ea580c;
      --tencent: #0284c7;
      --byte: #2563eb;
      --fanruan: #059669;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.65;
      font-size: 15px;
    }}
    a {{
      color: var(--primary);
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    
    /* Layout */
    .layout {{
      display: flex;
      min-height: 100vh;
    }}
    .sidebar {{
      width: var(--sidebar-w);
      background: #ffffff;
      border-right: 1px solid var(--border);
      position: sticky;
      top: 0;
      height: 100vh;
      overflow-y: auto;
      padding: 24px 16px;
      flex-shrink: 0;
    }}
    .sidebar-title {{
      font-size: 14px;
      font-weight: 700;
      color: #0f172a;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
      padding-left: 8px;
    }}
    .nav-list {{
      list-style: none;
    }}
    .nav-item {{
      margin-bottom: 4px;
    }}
    .nav-link {{
      display: block;
      padding: 7px 12px;
      font-size: 13.5px;
      color: var(--text-muted);
      border-radius: 6px;
      transition: all 0.15s ease;
    }}
    .nav-link:hover {{
      background: var(--primary-light);
      color: var(--primary);
      text-decoration: none;
    }}
    .nav-sub {{
      list-style: none;
      padding-left: 14px;
      margin-top: 2px;
    }}
    .nav-sub .nav-link {{
      font-size: 12.5px;
      padding: 5px 10px;
    }}

    .main-content {{
      flex: 1;
      max-width: 1200px;
      margin: 0 auto;
      padding: 40px 48px 80px 48px;
    }}

    /* Header Banner */
    .header-banner {{
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      color: #ffffff;
      padding: 36px 40px;
      border-radius: 12px;
      margin-bottom: 36px;
      box-shadow: 0 4px 20px rgba(15, 23, 42, 0.15);
    }}
    .header-badge {{
      display: inline-block;
      background: rgba(37, 99, 235, 0.35);
      border: 1px solid rgba(96, 165, 250, 0.4);
      color: #93c5fd;
      font-size: 12px;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 20px;
      margin-bottom: 12px;
    }}
    .header-title {{
      font-size: 26px;
      font-weight: 800;
      line-height: 1.3;
      margin-bottom: 10px;
      letter-spacing: -0.3px;
    }}
    .header-desc {{
      font-size: 14.5px;
      color: #94a3b8;
      max-width: 900px;
      line-height: 1.6;
    }}
    .meta-tags {{
      display: flex;
      gap: 16px;
      margin-top: 18px;
      font-size: 12.5px;
      color: #cbd5e1;
    }}

    /* Sections */
    section {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 32px;
      margin-bottom: 32px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
    }}
    h2 {{
      font-size: 20px;
      font-weight: 700;
      color: #0f172a;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 10px;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    h2::before {{
      content: "";
      display: inline-block;
      width: 4px;
      height: 20px;
      background: var(--primary);
      border-radius: 2px;
    }}
    h3 {{
      font-size: 16.5px;
      font-weight: 700;
      color: #1e293b;
      margin: 24px 0 12px 0;
    }}
    h4 {{
      font-size: 14.5px;
      font-weight: 700;
      color: #334155;
      margin: 16px 0 8px 0;
    }}
    p {{
      margin-bottom: 14px;
      color: #334155;
      text-align: justify;
    }}

    /* Diagrams */
    .diagram-container {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 16px;
      margin: 20px 0;
      box-shadow: inset 0 0 4px rgba(0,0,0,0.02);
    }}
    .diagram-caption {{
      text-align: center;
      font-size: 12.5px;
      font-weight: 600;
      color: #64748B;
      margin-top: 8px;
    }}

    /* Tables */
    .table-wrapper {{
      overflow-x: auto;
      margin: 20px 0;
      border: 1px solid var(--border);
      border-radius: 8px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
      background: #ffffff;
      text-align: left;
    }}
    th {{
      background: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      white-space: nowrap;
    }}
    td {{
      padding: 12px 14px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
      vertical-align: top;
      line-height: 1.5;
    }}
    tr:last-child td {{
      border-bottom: none;
    }}
    tr:hover td {{
      background: #f8fafc;
    }}
    .highlight-col {{
      background: #faf5ff;
      font-weight: 600;
    }}

    /* Vendor Badges */
    .badge {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11.5px;
      font-weight: 600;
    }}
    .badge-ali {{ background: #ffedd5; color: #c2410c; border: 1px solid #fed7aa; }}
    .badge-tencent {{ background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }}
    .badge-byte {{ background: #dbeafe; color: #1d4ed8; border: 1px solid #bfdbfe; }}
    .badge-fanruan {{ background: #d1fae5; color: #047857; border: 1px solid #a7f3d0; }}
    .badge-primary {{ background: var(--primary-light); color: var(--primary-dark); }}

    /* Cards Grid */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 20px 0;
    }}
    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin: 20px 0;
    }}
    .card {{
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 18px;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }}
    .card-title {{
      font-size: 14.5px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Code Blocks */
    pre {{
      background: #0f172a;
      color: #e2e8f0;
      padding: 16px;
      border-radius: 8px;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 12.5px;
      line-height: 1.5;
      overflow-x: auto;
      margin: 14px 0;
    }}
    code {{
      font-family: inherit;
    }}
    .inline-code {{
      background: #f1f5f9;
      color: #0f172a;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 12.5px;
      font-family: monospace;
      border: 1px solid #e2e8f0;
    }}

    /* Callouts */
    .callout {{
      padding: 16px 20px;
      border-left: 4px solid var(--primary);
      background: var(--primary-light);
      border-radius: 0 8px 8px 0;
      margin: 18px 0;
      font-size: 13.5px;
    }}
    .callout-warning {{
      border-left-color: #f59e0b;
      background: #fffbeb;
      color: #92400e;
    }}
    .callout-success {{
      border-left-color: #10b981;
      background: #ecfdf5;
      color: #065f46;
    }}

    /* Footer */
    footer {{
      text-align: center;
      padding: 30px;
      font-size: 13px;
      color: #94a3b8;
      border-top: 1px solid var(--border);
      margin-top: 40px;
    }}

    /* Responsive */
    @media (max-width: 900px) {{
      .layout {{ flex-direction: column; }}
      .sidebar {{ width: 100%; height: auto; position: static; }}
      .main-content {{ padding: 20px; }}
      .grid-2 {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
<div class="layout">
  <!-- Sidebar Navigation -->
  <aside class="sidebar">
    <div class="sidebar-title">📑 报告目录索引</div>
    <ul class="nav-list">
      <li class="nav-item"><a class="nav-link" href="#section-1">1. 宏观背景与技术演进史</a>
        <ul class="nav-sub">
          <li><a class="nav-link" href="#sec-1-1">1.1 传统 BI 痛点与 AI 范式重塑</a></li>
          <li><a class="nav-link" href="#sec-1-2">1.2 ChatBI 技术演进三代史</a></li>
          <li><a class="nav-link" href="#sec-1-3">1.3 Text2SQL vs Text2DSL 路线之争</a></li>
        </ul>
      </li>
      <li class="nav-item"><a class="nav-link" href="#section-2">2. 端到端架构与 Pipeline</a>
        <ul class="nav-sub">
          <li><a class="nav-link" href="#sec-2-1">2.1 整体分层技术架构图</a></li>
          <li><a class="nav-link" href="#sec-2-2">2.2 核心 Pipeline 六步法执行链路</a></li>
        </ul>
      </li>
      <li class="nav-item"><a class="nav-link" href="#section-3">3. 四大头部厂商方案深度剖析</a>
        <ul class="nav-sub">
          <li><a class="nav-link" href="#sec-3-1">3.1 阿里 Quick BI (智能小Q)</a></li>
          <li><a class="nav-link" href="#sec-3-2">3.2 腾讯云 BI (智能小腾)</a></li>
          <li><a class="nav-link" href="#sec-3-3">3.3 字节跳动 (DataWind / Data Agent)</a></li>
          <li><a class="nav-link" href="#sec-3-4">3.4 帆软 (FineChatBI)</a></li>
        </ul>
      </li>
      <li class="nav-item"><a class="nav-link" href="#section-4">4. 厂商横向多维对比矩阵</a></li>
      <li class="nav-item"><a class="nav-link" href="#section-5">5. 企业自研落地实操指南</a>
        <ul class="nav-sub">
          <li><a class="nav-link" href="#sec-5-1">5.1 语义指标层规范定义</a></li>
          <li><a class="nav-link" href="#sec-5-2">5.2 AST 级行级权限注入机制</a></li>
          <li><a class="nav-link" href="#sec-5-3">5.3 报错自愈循环状态机设计</a></li>
          <li><a class="nav-link" href="#sec-5-4">5.4 工业级评测基准与演进路线</a></li>
        </ul>
      </li>
      <li class="nav-item"><a class="nav-link" href="#section-6">6. 总结与战略建议</a></li>
    </ul>
  </aside>

  <!-- Main Content Body -->
  <main class="main-content">
    <!-- Header Banner -->
    <div class="header-banner">
      <span class="header-badge">AI + 商业智能 (BI) 深度技术调研报告</span>
      <h1 class="header-title">业界主流 ChatBI 深度技术架构与实现方案对比分析</h1>
      <p class="header-desc">
        全面拆解阿里（Quick BI / 智能小Q）、腾讯（腾讯云 BI / 智能小腾）、字节跳动（火山引擎 DataWind / Data Agent）、帆软（FineChatBI）等头部厂商的对话式 BI 底层技术方案、语义层建模、Text2DSL 编译器、自愈校验与权限治理体系，为自研数据库与湖仓一体落地 ChatBI 提供工程级参考规范。
      </p>
      <div class="meta-tags">
        <span>📅 发布日期：2026 年 8 月</span>
        <span>🏷️ 涵盖厂商：阿里 / 腾讯 / 字节跳动 / 帆软</span>
        <span>🔍 关键技术：Text2DSL · 语义指标层 · Multi-Agent · Self-Reflection · AST 权限注入</span>
      </div>
    </div>

    <!-- Section 1 -->
    <section id="section-1">
      <h2>1. 宏观背景与技术演进路线</h2>
      
      <div id="sec-1-1">
        <h3>1.1 传统 BI 痛点与大模型带来的范式重塑</h3>
        <p>
          在传统商业智能（BI）体系中，企业数据消费存在显著的<strong>“供给-需求剪刀差”</strong>。业务人员产生一个临时分析需求（Ad-hoc Query），通常需要经历“提出需求 → 数据开发排期 → 建立数仓中间模型（DWS/ADS） → BI 工程师拖拉拽报表 → 业务验收”的漫长链路，交付周期往往以<strong>数天甚至数周</strong>计。
        </p>
        <p>
          大语言模型（LLM）的兴起推动了 BI 从<strong>“人适应工具（学习 SQL / 复杂报表配置）”</strong>向<strong>“工具理解人（自然语言对话即席获取洞察）”</strong>的范式转移，即 <strong>ChatBI（Conversational BI / Data Agent）</strong>。
        </p>
      </div>

      <div id="sec-1-2">
        <h3>1.2 ChatBI 技术演进三代史</h3>
        <p>
          回顾对话式数据分析的技术演进，经历了三个关键发展阶段：
        </p>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>演进阶段</th>
                <th>代表技术 / 架构</th>
                <th>核心实现机制</th>
                <th>工业落地瓶颈 / 局限性</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1.0 规则与模式匹配时代</strong><br><span style="color:#64748B;">(2015-2020)</span></td>
                <td>NLIDB / 关键词解析 / 槽位填充 / 语法规则树</td>
                <td>基于词法句法分析器（Jieba/NLTK/Stanford CoreNLP），手工配置大量同义词、意图模板与正则表达式进行意图槽位提取。</td>
                <td>泛化能力极弱，冷启动和维护成本巨大；业务语言稍有变化即无法识别；无法支持复杂的多表关联与多维下钻。</td>
              </tr>
              <tr>
                <td><strong>2.0 深度学习与端到端 Text2SQL</strong><br><span style="color:#64748B;">(2020-2023)</span></td>
                <td>Seq2Seq / IRNet / RAT-SQL / RESDSQL / Spider 基准</td>
                <td>利用预训练模型（BERT/T5）编码自然语言与数据库 DDL Schema，端到端直接生成目标物理 SQL 语句。</td>
                <td>在公开 Benchmark（如 Spider）表现优异，但在<strong>企业真实场景中迅速崩溃</strong>：Schema 庞大时 Context 溢出、无法理解同环比等复杂业务计算、多方言适配成本极高、容易产生严重幻觉。</td>
              </tr>
              <tr>
                <td><strong>3.0 语义层 + Text2DSL + Agentic 时代</strong><br><span style="color:#64748B;">(2023-至今)</span></td>
                <td>LLM + 语义指标层 (Metric Store) + Text2DSL + Reflection 闭环 + Agent 工具调用</td>
                <td>构建独立的<strong>企业语义层（指标/维度/关系）</strong>，大模型输出结构化中间领域特定语言（DSL JSON），经 AST 静态校验与行级权限注入后，由 BI 引擎编译下推至底座数据库。</td>
                <td><strong>已成为阿里、腾讯、字节、帆软等全行业的共同标准基底</strong>。兼顾了大模型的泛化理解能力与企业数据消费的确定性、安全性、可解释性。</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div id="sec-1-3">
        <h3>1.3 核心技术争论：为什么纯 Text2SQL 无法在企业生产环境直接落地？</h3>
        <p>
          许多初学者尝试直接让大模型输入 <code>DDL + 用户问题</code> 直出 SQL，但在严肃的企业级生产环境中，这种纯 Text2SQL 路线几乎不可行。主要原因如下：
        </p>
        <div class="grid-2">
          <div class="card" style="border-left: 4px solid #ef4444;">
            <div class="card-title" style="color: #b91c1c;">🚫 纯 Text2SQL 的致命缺陷</div>
            <ul style="padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.6;">
              <li><strong>业务计算逻辑丢失：</strong>企业指标如“近30天GMV环比增长率”、“高价值活跃用户留存率”无法由物理表结构推导，单表 DDL 缺乏业务语义。</li>
              <li><strong>多数据库方言差异：</strong>ClickHouse、StarRocks、Presto、MySQL、Oracle 等各自函数体系迥异（如时间开窗、数组处理），通用 LLM 难以全量准确覆盖。</li>
              <li><strong>黑盒不可干预：</strong>生成的 SQL 嵌套数十行，业务用户看不懂也无法在前端修正某个错误字段或过滤条件。</li>
              <li><strong>权限无法可靠注入：</strong>大模型无法保证在生成的 SQL 每一个子查询中都严格添加 <code>tenant_id = X AND org_id IN (...)</code>，存在数据越权泄露隐患。</li>
              <li><strong>严重幻觉与笛卡尔积：</strong>多表关联时极易推导错误的 JOIN 路径，导致数据库跑出天量重复数据甚至崩溃。</li>
            </ul>
          </div>
          <div class="card" style="border-left: 4px solid #10b981;">
            <div class="card-title" style="color: #047857;">✅ Text2DSL + 语义层（Semantic Layer）解法</div>
            <ul style="padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.6;">
              <li><strong>大模型降维：</strong>大模型从“写代码（SQL）”转变为“语义参数抽取”（选哪个指标、哪个维度、什么时间切片、什么过滤条件）。</li>
              <li><strong>口径集中治理：</strong>指标口径、同义词映射、关联关系定义在语义层（Cube/Metric Catalog）中，一处修改全局生效。</li>
              <li><strong>白盒化可视化干预：</strong>前端以“指标胶囊、维度标签、过滤器”形式呈现，用户可直接点击修改错误项。</li>
              <li><strong>引擎层统一安全：</strong>BI 编译引擎在将 DSL 翻译为物理 SQL 时，自动、强制在 AST 语法树中注入行级/列级安全过滤器。</li>
              <li><strong>多方言自动适配：</strong>BI 原生引擎原生支持 30~50 种数据库方言，由编译器负责生成极致优化的物理 SQL。</li>
            </ul>
          </div>
        </div>

        <div class="diagram-container">
          {svg_comparison}
          <div class="diagram-caption">图 1.1：三代 ChatBI 技术路线演进与核心机制对比</div>
        </div>
      </div>
    </section>

    <!-- Section 2 -->
    <section id="section-2">
      <h2>2. 企业级 ChatBI 端到端技术架构与 Pipeline 详解</h2>
      
      <div id="sec-2-1">
        <h3>2.1 整体分层技术架构全景</h3>
        <p>
          一个达到生产可用级别（准确率 &gt; 85%）的企业级 ChatBI 架构，通常由<strong>交互会话层、语义知识索引层、DSL/SQL 生成引擎、校验自愈与权限编译层、极速执行与洞察呈现层</strong>五大核心层级组成：
        </p>
        <div class="diagram-container">
          {svg_pipeline}
          <div class="diagram-caption">图 2.1：现代企业级 ChatBI 端到端分层架构与核心执行 Pipeline</div>
        </div>
      </div>

      <div id="sec-2-2">
        <h3>2.2 核心 Pipeline 六步法执行链路全解析</h3>
        
        <div class="card" style="margin-bottom: 16px;">
          <div class="card-title"><span class="badge badge-primary">Step 1</span> 意图识别与多轮上下文指代消解 (Multi-turn Context & Intent)</div>
          <p style="font-size: 13.5px; color: #475569;">
            接收用户自然语言输入后，首先进过轻量意图分类器。若为“产品使用说明/制度咨询”，分流至企业文档 <strong>RAG 知识库</strong>；若为“报表与数据查询”，进入 ChatBI 流水线。针对多轮会话（如“那浙江省呢？”、“按月份再拆开看”），系统利用<strong>指代消解（Coreference Resolution）与对话状态跟踪（DST）</strong>，将历史会话中的已选指标、时间范围与上轮过滤条件与当前提问合并，生成语义完备的当前查询请求。
          </p>
        </div>

        <div class="card" style="margin-bottom: 16px;">
          <div class="card-title"><span class="badge badge-primary">Step 2</span> 语义检索与 Schema Linking (动态上下文剪枝)</div>
          <p style="font-size: 13.5px; color: #475569;">
            面对企业成百上千张数据表与数万字段，直接将全部元数据塞入 Prompt 会导致上下文超长与幻觉激增。系统采用<strong>向量检索（Dense Retrieval） + BM25 关键词倒排（Sparse Retrieval）</strong>的混合检索策略，从企业指标中心、业务同义词库中检索与用户问题最匹配的 Top-K 个候选指标、维度及对应数据集，完成 <strong>Schema Linking</strong> 并将无关元数据动态剪枝过滤。
          </p>
        </div>

        <div class="card" style="margin-bottom: 16px;">
          <div class="card-title"><span class="badge badge-primary">Step 3</span> 结构化 DSL 生成与 Multi-Agent 协作 (Text-to-DSL)</div>
          <p style="font-size: 13.5px; color: #475569;">
            将提炼后的精简 Schema、同义词映射表、Few-Shot ICL 样例及用户会话输入大模型。在进阶架构中，采用 <strong>Multi-Agent 分工协作模式</strong>：由“选表 Agent”定位模型、“维度度量 Agent”确定统计粒度、“过滤条件 Agent”解析时间与枚举值、“高级计算 Agent”处理同环比/占比逻辑，最终组装成统一的 <strong>JSON 格式 DSL 抽象语法树</strong>。
          </p>
        </div>

        <div class="card" style="margin-bottom: 16px;">
          <div class="card-title"><span class="badge badge-primary">Step 4</span> AST 静态校验与 Self-Reflection 反思自愈循环</div>
          <p style="font-size: 13.5px; color: #475569;">
            生成的 DSL 进入确定性编译器进行语法与语义合规性检查（如：度量字段是否存在、维度与度量是否支持关联聚合、时间格式是否合法）。若校验失败或在沙箱 Dry-Run 时报错，触发 <strong>Self-Reflection 机制</strong>：将详细的错误 Traceback、失败的 DSL 及纠错建议拼装成反馈 Prompt，回传给大模型进行定向修正（通常限制重试 2~3 次）。自愈失败时，主动向用户发起澄清式反问。
          </p>
        </div>

        <div class="card" style="margin-bottom: 16px;">
          <div class="card-title"><span class="badge badge-primary">Step 5</span> 企业级行/列权限动态注入 (AST-Level Security Injection)</div>
          <p style="font-size: 13.5px; color: #475569;">
            在将校验通过的 DSL 翻译为物理 SQL 之前，编译器根据当前登录用户的企业身份（组织架构、部门、角色、数据权限策略），<strong>在 AST 语法树层面强制插入行级过滤条件（RLS）</strong>（例如：<code>WHERE org_id = 'D001' AND region = 'East'</code>），并对无权访问的敏感列进行脱敏或阻断，确保数据安全<strong>不受大模型幻觉与 Prompt 注入攻击影响</strong>。
          </p>
        </div>

        <div class="card">
          <div class="card-title"><span class="badge badge-primary">Step 6</span> 底座引擎下推执行、智能图表推荐与深度归因</div>
          <p style="font-size: 13.5px; color: #475569;">
            编译器将最终 SQL 下推至底座计算引擎（ClickHouse/StarRocks/PolarDB/ByteHouse/OceanBase），通过向量化执行秒级返回明细与聚合结果。前端 <strong>Chart Advisor 引擎</strong>根据返回数据的维度类型（时间、分类、地理、数值）与基数自动推荐最优图表（折线图、柱状图、透视表、地图），并由大模型自动生成 3~5 条<strong>关键业务洞察摘要与波动归因结论</strong>。
          </p>
        </div>
      </div>
    </section>

    <!-- Section 3 -->
    <section id="section-3">
      <h2>3. 四大头部厂商方案深度剖析</h2>
      
      <div class="diagram-container">
        {svg_vendors}
        <div class="diagram-caption">图 3.1：阿里、腾讯、字节跳动、帆软 ChatBI 核心技术架构映射</div>
      </div>

      <!-- 3.1 Alibaba -->
      <div id="sec-3-1">
        <h3>3.1 阿里云 Quick BI（智能小Q / PolarDB Data-Agent）</h3>
        <div class="callout">
          <strong>产品定位：</strong>国内唯一连续多年进入 Gartner ABI 魔力象限的产品，定位于企业级全场景智能 BI 平台，深度整合阿里云数据湖仓（MaxCompute/Hologres/PolarDB）与通义千问大模型生态。
        </div>

        <h4>技术架构与核心实现机制：</h4>
        <ul style="padding-left: 20px; line-height: 1.7; color: #334155;">
          <li>
            <strong>技术路线演进：</strong>从早期的纯 NL2DSL 升级为 <strong>NL2SQL2DSL 混合模型</strong>。为了解决市面 40+ 数据源方言难以穷尽的问题，Quick BI 定义了一套可识别的<strong>增强型抽象 SQL 语言</strong>，对标准 SQL 在时间算子、高级计算、LOD（详细级别表达式）和抽象函数四大维度进行了算子化扩展。
          </li>
          <li>
            <strong>分层多智能体协同：</strong>架构自下而上划分为 <code>BI 基座引擎层 → 领域自研大模型层 → AI 中间层 → 交互应用层</code>。采用<strong>轻量小模型</strong>处理基础意图路由与快速问答，关键复杂分析节点调用<strong>通义千问微调大模型</strong>进行深度多步逻辑推理。
          </li>
          <li>
            <strong>数据建模下推：</strong>将复杂的星型/雪花模型、多表关联与复合指标计算下推至 Quick BI 既有建模层，大模型不需要感知底层表物理 JOIN 细节，大幅降低了 Prompt 复杂度和出错率。
          </li>
          <li>
            <strong>可视化工程支撑：</strong>依托阿里开源的 <strong>AntV（G2/S2/L7）</strong> 可视化底座，实现强大的 Chart Advisor 智能图表推荐，支持自然语言改图、换色、指标高亮与一键生成仪表板。
          </li>
        </ul>

        <h4>典型落地客户与表现：</h4>
        <p>
          在<strong>雅迪电动车（云销通 App）</strong>案例中，DMS + PolarDB for AI / Quick BI 支撑全国超过 <strong>10 万销售与经销商</strong>通过手机端自然语言实时查询批发、销售、库存与应收账款数据，官方披露 NL2SQL 综合查询准确率超过 <strong>90%</strong>。
        </p>
      </div>

      <!-- 3.2 Tencent -->
      <div id="sec-3-2" style="margin-top: 32px;">
        <h3>3.2 腾讯云 BI（智能小腾 / ChatBI / 腾讯微分析）</h3>
        <div class="callout" style="border-left-color: var(--tencent); background: #f0f9ff; color: #0c4a6e;">
          <strong>产品定位：</strong>基于腾讯混元大模型与数据分析引擎打造的下一代智能数据助手，主打“免运维、高准确率、数据不离本地、企微生态无缝集成”。
        </div>

        <h4>技术架构与核心实现机制：</h4>
        <ul style="padding-left: 20px; line-height: 1.7; color: #334155;">
          <li>
            <strong>坚决转向 Text2DSL：</strong>在早期上线 Text2SQL 发现方言和复杂计算瓶颈后，全面重构为 <strong>Text2DSL + Python 联合计算方案</strong>。大模型生成符合 BI 拖拽协议的 DSL 指令，原生支持同环比、组内排名、区间聚合等复杂分析。
          </li>
          <li>
            <strong>Multi-Agent 多模型分工：</strong>针对 DSL 包含维度、度量、过滤、排序等复杂约束，拆解为四大专用 Agent（<code>选表 Agent</code>、<code>维度生成 Agent</code>、<code>指标生成 Agent</code>、<code>条件生成 Agent</code>），大幅降低单个模型的生成复杂度。
          </li>
          <li>
            <strong>ES + LLM 意图澄清机制：</strong>当用户提问模糊或存在歧义时，结合 Elasticsearch 模糊检索与 LLM 进行场景细分，主动向用户反问并推荐候选指标，消除歧义后再执行计算。
          </li>
          <li>
            <strong>数据隐私与安全设计：</strong>默认<strong>仅读取数据表的元数据与表头结构</strong>，绝不将客户真实数据内容上传至大模型；生成的 DSL/SQL 直接下发至用户私有数据库或云上计算引擎（ClickHouse/MySQL/StarRocks 等）执行并返回图表。
          </li>
        </ul>

        <h4>部署与生态特性：</h4>
        <p>
          支持公有云 SaaS、私有化部署及混合云模式；适配腾讯混元、DeepSeek-V3/R1、通义千问等主流底座；提供强大的 <strong>H5 / 企微微分析嵌出能力</strong>，业务人员在企微聊天窗口即可完成即席问数。
        </p>
      </div>

      <!-- 3.3 ByteDance -->
      <div id="sec-3-3" style="margin-top: 32px;">
        <h3>3.3 字节跳动火山引擎（DataWind / Data Agent / ByteHouse）</h3>
        <div class="callout" style="border-left-color: var(--byte); background: #eff6ff; color: #1e3a8a;">
          <strong>产品定位：</strong>字节跳动数智平台 VeDI 旗下的增强型 ABI 平台，融合自研极速分析型数据库 ByteHouse 与豆包（Doubao）大模型，主打高性能交互式洞察、异常指标自动归因与飞书深度协同。
        </div>

        <h4>技术架构与核心实现机制：</h4>
        <ul style="padding-left: 20px; line-height: 1.7; color: #334155;">
          <li>
            <strong>Data Agent 2.0 智能调度站：</strong>架构从 1.0 时期的固定流水线升级为 2.0 <strong>“工具包 + 动态调度站”</strong>模式。将数据集选择、图表洞察、SQL/Python 沙箱等拆解为独立工具（Tools），由豆包大模型基于 ReAct 范式根据提问自主规划工具链并自我优化。
          </li>
          <li>
            <strong>围绕 ByteHouse 的极速计算链路：</strong>为了保证秒级响应，在企业内部和公有云上主推<strong>“重抽取到 ByteHouse”</strong>架构，将分析数据集中加载至自研 ByteHouse 向量化 MPP 引擎中，支持 PB 级数据明细秒级 Ad-hoc 分析。
          </li>
          <li>
            <strong>智能波动归因与下钻：</strong>不仅能回答“当前数据是多少”，更内置自动化归因算法，自动检测异动指标并沿维度树下钻，计算各维度的贡献度（如地区、渠道、品类对 GMV 下跌的贡献率）。
          </li>
          <li>
            <strong>深度研究 Agent (Deep Research)：</strong>支持由智能体自主执行多轮数据探查，将多张图表与文字洞察自动拼装为完整的<strong>结构化分析日报/周报</strong>，并支持一键固化与飞书定时推送。
          </li>
        </ul>

        <h4>生态与特色：</h4>
        <p>
          深度整合<strong>飞书协作生态</strong>，支持飞书群机器人直接交互问数、飞书消息卡片交互式图表操作、订阅看板推送；提供标准 OpenAPI 与 MCP 协议接入，支持企业作为 Agent 插件直接调用。
        </p>
      </div>

      <!-- 3.4 FanRuan -->
      <div id="sec-3-4" style="margin-top: 32px;">
        <h3>3.4 帆软（FineChatBI / FineBI 6.0 Copilot / FineAI）</h3>
        <div class="callout" style="border-left-color: var(--fanruan); background: #ecfdf5; color: #064e3b;">
          <strong>产品定位：</strong>中国 BI 市场占有率第一的传统龙头，在 FineBI 20 年企业级数据建模与报表底座之上打造的“可控生成、可信查数”对话式 BI 产品，深度贴合国内大型政企复杂报表与多级权限体系。
        </div>

        <h4>技术架构与核心实现机制：</h4>
        <ul style="padding-left: 20px; line-height: 1.7; color: #334155;">
          <li>
            <strong>坚决杜绝黑盒 Text2SQL：</strong>帆软认为大模型“黑盒”直出 SQL 存在无法克服的幻觉与安全漏洞。FineChatBI 全面基于 <strong>Text2DSL 架构</strong>，由专用语义解析模型（<code>fine-chat-bi-parser</code>）将自然语言解析为符合 FineBI 协议的结构化指令。
          </li>
          <li>
            <strong>双模式切换设计：</strong>提供<strong>“极速模式”</strong>（提问默认不经过改写，毫秒级快速匹配标准指标）与<strong>“智能模式”</strong>（引入 FineAI 与大模型进行语义纠偏、意图改写与复杂业务思路拆解）。
          </li>
          <li>
            <strong>全流程白盒可干预：</strong>系统将自然语言解析的结果以“选中的数据集、指标名称、聚合方式、过滤维度”清晰呈现在界面上。业务人员若发现模型理解偏差，可<strong>直接手动调整任一算子</strong>，从根源上保障取数结果 100% 可信。
          </li>
          <li>
            <strong>中国式复杂权限与组织架构穿透：</strong>深度继承 FineBI 的企业级权限树体系，支持精细到“行级条件、列级字段掩码、多层级部门继承”的数据权限过滤，确保私有化部署时的数据安全合规。
          </li>
        </ul>

        <h4>典型业务价值：</h4>
        <p>
          官方披露帮助制造、金融、零售等典型企业客户将“从业务问题定位到数据报表”的平均流转时间从 <strong>5 小时缩短至 3 分钟</strong>，显著降低了业务人员找 IT 取数的沟通壁垒。
        </p>
      </div>
    </section>

    <!-- Section 4 -->
    <section id="section-4">
      <h2>4. 四大头部厂商多维度横向对比矩阵</h2>
      <p>
        以下汇总阿里、腾讯、字节跳动、帆软四大厂商在 12 个核心维度的详细技术实现与能力对比：
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>对比维度</th>
              <th style="background:#ffedd5; color:#c2410c;">阿里云 Quick BI (智能小Q)</th>
              <th style="background:#e0f2fe; color:#0369a1;">腾讯云 BI (智能小腾)</th>
              <th style="background:#dbeafe; color:#1d4ed8;">火山引擎 (DataWind / Data Agent)</th>
              <th style="background:#d1fae5; color:#047857;">帆软 (FineChatBI)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>核心技术路线</strong></td>
              <td>NL2DSL → NL2SQL2DSL 混合<br>(增强抽象 SQL 算子)</td>
              <td>Text2DSL + Python 联合计算<br>(兼容 BI 拖拽协议)</td>
              <td>Data Agent 2.0 智能调度站<br>(ReAct 工具调度 + DSL/SQL)</td>
              <td>纯粹 Text2DSL 架构<br>(强调“可控生成、可信查数”)</td>
            </tr>
            <tr>
              <td><strong>大模型底座与协同</strong></td>
              <td>通义千问 (Qwen) 领域微调<br>+ 轻量小模型双通道协同</td>
              <td>腾讯混元大模型<br>+ 深度适配 DeepSeek-V3/R1</td>
              <td>字节豆包 (Doubao) 大模型<br>+ 内部分析大模型深度微调</td>
              <td>FineAI 算法中枢<br>+ fine-chat-bi-parser 专用模型</td>
            </tr>
            <tr>
              <td><strong>语义指标层 (Semantic Layer)</strong></td>
              <td>原生星型/雪花模型建模层<br>统一封装复杂多表关联与复合度量</td>
              <td>多模型选表与指标映射字典<br>支持多事实表与维表关联配置</td>
              <td>指标库与数据资产集市打通<br>支持多数据集协同查询与预加载</td>
              <td>20 年沉淀的企业级指标中心<br>同义词、业务词典与元数据治理</td>
            </tr>
            <tr>
              <td><strong>意图识别与澄清机制</strong></td>
              <td>轻量模型意图分类<br>支持多轮会话继承与追问下钻</td>
              <td>ES + LLM 双重意图澄清<br>模糊提问主动反问与联想推荐</td>
              <td>多轮会话状态跟踪 (DST)<br>支持问题推荐、收藏与自动追问</td>
              <td>极速模式 vs 智能改写双模式<br>支持模糊字段自动联想提示</td>
            </tr>
            <tr>
              <td><strong>防幻觉与自愈修复 (Self-Correction)</strong></td>
              <td>AI 中间层算子约束校验<br>结合业务 SQL 映射与执行纠偏</td>
              <td>Multi-Agent 多层约束隔离<br>In-Context Learning (ICL) 场景调优</td>
              <td>Agent 动态 ReAct 自我修正<br>沙箱执行报错拦截与反馈重试</td>
              <td>全流程白盒可视化可干预<br>用户可在前端直接点击修改算子</td>
            </tr>
            <tr>
              <td><strong>企业级权限与安全隔离</strong></td>
              <td>深度集成阿里云 RAM 体系<br>行级权限与列级脱敏自动注入</td>
              <td>仅读表头元数据，数据不离本地<br>SQL 携带租户条件由本地库执行</td>
              <td>火山引擎多租户安全体系<br>支持行列级权限与数据集级隔离</td>
              <td>继承 FineBI 复杂组织架构树<br>支持精细到人/岗位的行列级权限</td>
            </tr>
            <tr>
              <td><strong>底层计算引擎与加速</strong></td>
              <td>深度适配 MaxCompute / Hologres / PolarDB / MySQL 等 40+ 数据源</td>
              <td>适配 ClickHouse / StarRocks / MySQL / Oracle 等 20+ 数据源</td>
              <td>强依赖自研 ByteHouse 极速 MPP<br>支持 PB 级数据明细秒级查询</td>
              <td>依托 FineBI Direct/抽取双引擎<br>支持主流关系型与 OLAP 数据库</td>
            </tr>
            <tr>
              <td><strong>数据深度洞察与归因</strong></td>
              <td>智能数据洞察 (趋势/占比/异常)<br>提供文字总结与决策辅助</td>
              <td>波动归因智能工具模块<br>自动计算异动幅度并拆解归因</td>
              <td>深度研究 Agent (Deep Research)<br>自动化归因下钻树 + 生成完整研报</td>
              <td>波动归因分析 + 趋势预测<br>基于假设检验拆解业务影响因子</td>
            </tr>
            <tr>
              <td><strong>图表智能推荐与渲染</strong></td>
              <td>阿里 AntV (G2/S2/L7) 引擎<br>智能匹配最优图表，一键换图</td>
              <td>内置智能绘制图表模块<br>柱/线/饼/表一键平滑无缝切换</td>
              <td>DataWind 丰富可视化库<br>支持大屏、看板组件与飞书卡片</td>
              <td>FineBI 强大图表与中国式复杂报表<br>一键固化为正式仪表板组件</td>
            </tr>
            <tr>
              <td><strong>协同生态与部署形态</strong></td>
              <td>公有云 SaaS / 专属云<br>深度打通钉钉智能助理</td>
              <td>公有云 / 私有化 / 混合云<br>深度打通企业微信 / H5 嵌出</td>
              <td>火山公有云 / 私有化部署<br>深度集成飞书协作与消息卡片</td>
              <td>本地私有化部署能力极强<br>广泛集成企业微信/钉钉/自有 OA</td>
            </tr>
            <tr>
              <td><strong>核心优势</strong></td>
              <td>ABI 连续入选 Gartner 实力雄厚，算子库完善，多数据源方言支持极佳</td>
              <td>多 Agent 架构解耦清晰，数据不离本地安全性高，企微生态体验丝滑</td>
              <td>ByteHouse 极速查询性能强悍，Data Agent 2.0 归因与自动化研报领先</td>
              <td>私有化与中国式报表底座极深，白盒可干预性最高，客户信任度高</td>
            </tr>
            <tr>
              <td><strong>潜在局限 / 适用建议</strong></td>
              <td>高度依赖阿里系云生态配合效果最佳，私有化定制门槛相对较高</td>
              <td>在极端复杂的跨多事实表复杂嵌套关联建模上需较强前置配置</td>
              <td>需要较重的 ByteHouse 抽取链路才能发挥最佳极速性能</td>
              <td>更侧重传统报表与指标统计，偏前沿的自由代码沙箱分析相对克制</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Section 5 -->
    <section id="section-5">
      <h2>5. 企业自研 / 数据库厂商 ChatBI 落地实操指南</h2>
      
      <div id="sec-5-1">
        <h3>5.1 语义指标层 (Semantic Metric Layer) 核心规范与定义示例</h3>
        <p>
          自研 ChatBI 必须先建立<strong>独立的语义层（Semantic Layer）</strong>。以下为一个标准的企业级指标模型 YAML 定义范例（可被 Schema Linking 向量化检索与 LLM 直接理解）：
        </p>
        <pre><code class="language-yaml"># semantic_model_sales.yaml
semantic_model:
  name: "ecommerce_sales_model"
  description: "电商核心销售与履约主题模型，涵盖订单、商品、用户及履约数据"
  base_table: "dws_trade_order_di"
  primary_key: ["order_id"]
  
  # 维度定义（支持同义词与枚举值映射）
  dimensions:
    - name: "order_date"
      type: "time"
      column: "order_time"
      description: "下单日期，支持按日/周/月/年聚合"
      synonyms: ["日期", "时间", "下单时间", "成交日期"]
      
    - name: "region"
      type: "categorical"
      column: "delivery_province"
      description: "收货省份/大区"
      synonyms: ["地区", "省份", "大区", "区域", "目的地"]
      allowed_values: ["华东", "华北", "华南", "西南", "华中", "西北", "东北"]

    - name: "channel"
      type: "categorical"
      column: "traffic_source"
      description: "推广与流量渠道"
      synonyms: ["渠道", "来源", "流量渠道", "端"]

  # 指标度量定义（包含计算表达式与聚合规则）
  measures:
    - name: "gmv"
      type: "additive"
      column: "pay_amount"
      aggregation: "SUM"
      description: "实际支付总金额 (GMV)"
      synonyms: ["销售额", "流水", "收入", "GMV", "营收", "成交额"]
      unit: "元"

    - name: "order_count"
      type: "additive"
      column: "order_id"
      aggregation: "COUNT_DISTINCT"
      description: "独立成交订单数"
      synonyms: ["单量", "订单量", "笔数", "成交单数"]

  # 复合/衍生指标计算逻辑
  derived_metrics:
    - name: "avg_order_value"
      expression: "gmv / order_count"
      description: "客单价 (AOV)"
      synonyms: ["客单价", "笔均价", "平均每单金额"]</code></pre>
      </div>

      <div id="sec-5-2">
        <h3>5.2 AST 级别行级权限（Row-Level Security）动态注入机制</h3>
        <p>
          为了彻底防止大模型生成 SQL 时漏掉权限条件，必须在<strong>抽象语法树（AST）编译阶段</strong>进行强制重写拦截：
        </p>
        <pre><code class="language-python"># rls_ast_rewriter.py (示例：基于 SQLGlot 进行 AST 级行权限强制注入)
import sqlglot
from sqlglot import exp

def inject_row_level_security(raw_sql: str, user_context: dict) -> str:
    """
    在生成的 SQL AST 根节点处强制合并注入行级权限过滤器
    user_context = {{'tenant_id': 'T1001', 'allowed_orgs': ['D01', 'D02']}}
    """
    expression = sqlglot.parse_one(raw_sql)
    
    # 构造必须满足的权限断言表达式
    tenant_cond = exp.EQ(
        this=exp.Column(this=exp.Identifier(this="tenant_id")),
        expression=exp.Literal.string(user_context["tenant_id"])
    )
    
    org_values = [exp.Literal.string(o) for o in user_context["allowed_orgs"]]
    org_cond = exp.In(
        this=exp.Column(this=exp.Identifier(this="org_id")),
        expressions=org_values
    )
    
    security_filter = exp.And(this=tenant_cond, expression=org_cond)
    
    # 递归遍历所有 SELECT 查询块，在 WHERE 子句中与既有条件进行 AND 合并
    for select in expression.find_all(exp.Select):
        existing_where = select.args.get("where")
        if existing_where:
            # 既有 WHERE (condition) 变为 WHERE ((condition) AND (security_filter))
            combined = exp.And(this=existing_where.this, expression=security_filter)
            select.set("where", exp.Where(this=combined))
        else:
            select.set("where", exp.Where(this=security_filter))
            
    return expression.sql(dialect="clickhouse")</code></pre>
      </div>

      <div id="sec-5-3">
        <h3>5.3 Agent 报错自愈反思循环（Self-Correction Loop）设计</h3>
        <div class="grid-2">
          <div class="card">
            <div class="card-title">🔄 状态机流转控制</div>
            <ol style="padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.6;">
              <li><strong>State 1:</strong> 接收用户提问，初次生成 DSL。</li>
              <li><strong>State 2:</strong> 静态校验（语法/度量存在性）。若通过进入 State 4，若失败进入 State 3。</li>
              <li><strong>State 3:</strong> 组装 <code>Error Correction Prompt</code>，带上失败原因让模型重写（计数器 +1）。</li>
              <li><strong>State 4:</strong> 沙箱 Dry-Run（试执行 <code>LIMIT 1</code>）。若引擎报错进入 State 3。</li>
              <li><strong>State 5:</strong> 若重试次数 &gt; 3 次仍未解决，触发 Fallback 状态，向用户发出主动澄清。</li>
            </ol>
          </div>
          <div class="card">
            <div class="card-title">📝 反思纠错 Prompt 模板</div>
            <pre style="margin:0; font-size: 11.5px;"><code class="language-markdown">### 纠错反馈任务 (Correction Prompt)
上一步生成的 DSL 在执行时发生了以下错误：
【错误类型】：SEMANTIC_ERROR_UNKNOWN_COLUMN
【错误详情】：度量 "sales_profit" 在当前模型中不存在，当前模型可用度量仅包含：["gmv", "order_count", "cost_amount"]。
【用户原问题】：查询上个月各省份的利润情况

请反思失败原因，并重新生成符合规范的 DSL：
1. 若业务无直接利润指标，请判断是否可用 (gmv - cost_amount) 表达；
2. 仅输出最终合法的 JSON DSL，不要包含多余闲聊。</code></pre>
          </div>
        </div>
      </div>

      <div id="sec-5-4">
        <h3>5.4 工业级评测基准 (Benchmark) 与四阶段建设路线图</h3>
        <p>
          不能仅用学术 Spider 数据集来评测企业 ChatBI。企业必须构建<strong>私域黄金评测集（Golden Test Suite）</strong>，监控以下 4 大核心指标：
        </p>
        <div class="grid-4">
          <div class="card" style="text-align: center;">
            <div style="font-size: 24px; font-weight: 800; color: #2563eb;">≥ 95%</div>
            <div style="font-size: 13px; font-weight: 700; color: #0f172a; margin-top: 4px;">意图与 Schema 召回率</div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 4px;">候选指标/维度是否在 Top-3 中</div>
          </div>
          <div class="card" style="text-align: center;">
            <div style="font-size: 24px; font-weight: 800; color: #16a34a;">≥ 88%</div>
            <div style="font-size: 13px; font-weight: 700; color: #0f172a; margin-top: 4px;">DSL 语法执行准确率</div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 4px;">生成的 DSL/SQL 能否无报错运行</div>
          </div>
          <div class="card" style="text-align: center;">
            <div style="font-size: 24px; font-weight: 800; color: #ea580c;">≥ 85%</div>
            <div style="font-size: 13px; font-weight: 700; color: #0f172a; margin-top: 4px;">结果业务一致率 (EX Rate)</div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 4px;">查询结果与人工专家答案完全一致</div>
          </div>
          <div class="card" style="text-align: center;">
            <div style="font-size: 24px; font-weight: 800; color: #7c3aed;">≤ 1.5s</div>
            <div style="font-size: 13px; font-weight: 700; color: #0f172a; margin-top: 4px;">端到端 P90 响应耗时</div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 4px;">包含 LLM 推理与底座 SQL 执行</div>
          </div>
        </div>

        <h4>自研落地四阶段演进路线图：</h4>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>阶段</th>
                <th>建设重点</th>
                <th>交付产物与关键技术</th>
                <th>解决的核心问题</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Phase 1: 语义与算力筑基</strong></td>
                <td>统一数仓宽表 + 语义指标层 (Metric Layer) + HTAP/MPP 计算底座</td>
                <td>定义 YAML/JSON 指标字典，梳理高频 100 个指标与维度同义词，打通底层 PolarDB/ClickHouse/StarRocks 极速引擎。</td>
                <td>解决“口径不统一”、“物理表杂乱”、“大模型理解不了业务术语”的根本痛点。</td>
              </tr>
              <tr>
                <td><strong>Phase 2: Text2DSL 编译闭环</strong></td>
                <td>Schema Linking + Text2DSL 映射器 + AST 校验器 + 静态权限注入</td>
                <td>向量+BM25 混合检索，微调/Prompt 驱动输出 JSON DSL，由编译器下推物理 SQL 并强制注入 RLS 租户安全条件。</td>
                <td>实现“可控生成、可信查数”，问数准确率跨越至 80%~85%，消除严重 SQL 幻觉。</td>
              </tr>
              <tr>
                <td><strong>Phase 3: 体验与自愈增强</strong></td>
                <td>Multi-Agent 协作 + 报错反思自愈 (Self-Correction) + 智能图表推荐</td>
                <td>多轮指代消解，歧义反问澄清，执行报错自动反馈重试，AntV 智能图表与关键数据洞察摘要。</td>
                <td>提升交互丝滑度与容错能力，降低业务用户学习门槛，端到端问答体验媲美专业分析师。</td>
              </tr>
              <tr>
                <td><strong>Phase 4: Agent 深度洞察与协同</strong></td>
                <td>波动归因分析 + 自动化研报生成 + 飞书/钉钉/企微办公协同打通</td>
                <td>Shapley 贡献度归因下钻树，Deep Research 自动化组装日报周报，开放 MCP/REST API 赋能上层业务 Agent。</td>
                <td>从“被动查数”升级为“主动业务诊断与行动建议”，实现数据智能业务闭环。</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Section 6 -->
    <section id="section-6">
      <h2>6. 总结与战略建议</h2>
      <p>
        通过对阿里、腾讯、字节跳动、帆软等业界标杆的深入剖析，我们可以得出以下明确的技术趋势与战略结论：
      </p>
      <div class="grid-2">
        <div class="card" style="border-top: 4px solid var(--primary);">
          <div class="card-title">💡 关键技术共识</div>
          <p style="font-size: 13.5px; color: #475569;">
            1. <strong>告别纯 Text2SQL 幻想：</strong>在企业级场景中，<strong>Text2DSL + 语义指标层</strong>是唯一被工业界验证可信、可控、高准确率的技术路线。<br>
            2. <strong>算力底座是决胜底牌：</strong>没有毫秒级响应的 MPP/HTAP 数据库（如 ByteHouse/PolarDB/StarRocks/OceanBase），多轮交互式 ChatBI 将因延迟过高而失去实用价值。<br>
            3. <strong>权限不能靠 Prompt：</strong>行级、列级安全必须在编译器 AST 层面做确定性物理注入，坚决不信任大模型的自然语言自觉性。
          </p>
        </div>
        <div class="card" style="border-top: 4px solid var(--fanruan);">
          <div class="card-title">🎯 建设与选型建议</div>
          <p style="font-size: 13.5px; color: #475569;">
            1. <strong>对于自研数据库团队：</strong>优先将内核的高并发 AP 向量化执行能力与 AI Agent 算子（AI Function / MCP / 向量索引）打通，提供标准的抽象 SQL/DSL 编译能力。<br>
            2. <strong>对于企业 IT 与数据团队：</strong>先做指标治理与语义层沉淀，再做大模型接入；“垃圾进垃圾出”在 ChatBI 尤为致命。<br>
            3. <strong>对于 SaaS / 垂直应用：</strong>优先通过轻量 H5 / 企微 / 钉钉 / 飞书卡片嵌出问数能力，从核心高频指标切入，逐步扩展到深度归因。
          </p>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <p>业界主流 ChatBI 深度技术架构与实现方案对比分析报告 · 阿里 / 腾讯 / 字节 / 帆软 · 2026</p>
    </footer>
  </main>
</div>
</body>
</html>'''

    output_path = os.path.join(os.path.dirname(__file__), "chatbi-industry-architecture-report.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated HTML report at: {output_path}")

if __name__ == "__main__":
    build_full_html()
