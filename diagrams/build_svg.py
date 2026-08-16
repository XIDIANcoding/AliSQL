import re
import html
from xml.etree import ElementTree as ET

def render_drawio_svg(drawio_path):
    tree = ET.parse(drawio_path)
    root = tree.getroot()
    cells = root.findall('.//mxCell')
    
    # Dimensions
    max_w = 1140
    max_h = 590
    
    elems = []
    
    # Base background card
    elems.append(f'<rect x="0" y="0" width="{max_w}" height="{max_h}" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" />')
    
    # 1. First render swimlanes / containers
    for c in cells:
        style = c.get('style', '')
        geo = c.find('mxGeometry')
        if geo is None or c.get('edge') == '1':
            continue
        if 'swimlane' not in style:
            continue
            
        x = float(geo.get('x', '0'))
        y = float(geo.get('y', '0'))
        w = float(geo.get('width', '0'))
        h = float(geo.get('height', '0'))
        
        fill = '#f8fafc'
        stroke = '#64748b'
        m_fill = re.search(r'fillColor=([^;]+)', style)
        if m_fill:
            fill = m_fill.group(1)
        m_stroke = re.search(r'strokeColor=([^;]+)', style)
        if m_stroke:
            stroke = m_stroke.group(1)
            
        val = html.unescape(c.get('value', ''))
        title = val.split('\n')[0].split('&#xa;')[0]
        
        elems.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.8" />')
        elems.append(f'<path d="M {x} {y+10} A 10 10 0 0 1 {x+10} {y} L {x+w-10} {y} A 10 10 0 0 1 {x+w} {y+10} L {x+w} {y+32} L {x} {y+32} Z" fill="{stroke}" opacity="0.12" />')
        elems.append(f'<text x="{x+18}" y="{y+21}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="{stroke}">{html.escape(title)}</text>')

    # 2. Render children items and normal shapes
    for c in cells:
        style = c.get('style', '')
        geo = c.find('mxGeometry')
        if geo is None or c.get('edge') == '1':
            continue
        if 'swimlane' in style:
            continue
            
        x = float(geo.get('x', '0'))
        y = float(geo.get('y', '0'))
        w = float(geo.get('width', '0'))
        h = float(geo.get('height', '0'))
        parent = c.get('parent')
        
        if parent and parent not in ('0', '1'):
            pcell = root.find(f".//mxCell[@id='{parent}']")
            if pcell is not None:
                pgeo = pcell.find('mxGeometry')
                if pgeo is not None:
                    x += float(pgeo.get('x', '0'))
                    y += float(pgeo.get('y', '0'))
                    
        val = html.unescape(c.get('value', ''))
        lines = [l.strip() for l in val.replace('&#xa;', '\n').split('\n') if l.strip()]
        
        fill = '#ffffff'
        stroke = '#94a3b8'
        m_fill = re.search(r'fillColor=([^;]+)', style)
        if m_fill:
            fill = m_fill.group(1)
        m_stroke = re.search(r'strokeColor=([^;]+)', style)
        if m_stroke:
            stroke = m_stroke.group(1)
            
        is_arrow = 'shape=flexArrow' in style
        if is_arrow:
            elems.append(f'<path d="M {x} {y+h*0.25} L {x+w-18} {y+h*0.25} L {x+w-18} {y} L {x+w} {y+h*0.5} L {x+w-18} {y+h} L {x+w-18} {y+h*0.75} L {x} {y+h*0.75} Z" fill="{fill}" stroke="{stroke}" stroke-width="1.5" />')
            for idx, line in enumerate(lines):
                elems.append(f'<text x="{x + (w-18)/2}" y="{y + 20 + idx*15}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="10.5" font-weight="700" fill="#0f172a" text-anchor="middle">{html.escape(line)}</text>')
            continue
            
        rx = '8' if 'rounded=1' in style else '4'
        elems.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.4" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.04))" />')
        
        total_lines = len(lines)
        line_height = 16
        start_y = y + (h - (total_lines * line_height)) / 2 + 13
        
        for idx, line in enumerate(lines):
            is_title = (idx == 0)
            weight = "700" if is_title else "400"
            font_size = "11.5" if is_title else "10.5"
            color = stroke if is_title and stroke not in ('#666666', '#94a3b8') else ("#0f172a" if is_title else "#475569")
            elems.append(f'<text x="{x+w/2}" y="{start_y + idx*line_height}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="{font_size}" font-weight="{weight}" fill="{color}" text-anchor="middle">{html.escape(line)}</text>')

    svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {max_w} {max_h}" width="100%" height="auto">
      {''.join(elems)}
    </svg>'''
    return svg_code

for name in ['oracle-26ai-architecture', 'databricks-agent-bricks-architecture', 'snowflake-cortex-horizon-architecture', 'polardb-imci-ai-architecture']:
    svg = render_drawio_svg(f'/workspace/diagrams/{name}.drawio')
    with open(f'/workspace/diagrams/{name}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'Rendered SVG for {name}')
