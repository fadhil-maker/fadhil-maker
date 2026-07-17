import base64
import os
import urllib.request
import re

def generate_stats_svg(stars, commits, repos, followers, projects, rank="S"):
    # Fetch Orbitron font
    font_b64 = ""
    try:
        css_url = "https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap"
        req = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
        css_data = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r"url\((https://[^)]+\.woff2)\)", css_data)
        if match:
            woff2_url = match.group(1)
            font_data = urllib.request.urlopen(woff2_url).read()
            font_b64 = base64.b64encode(font_data).decode('utf-8')
            font_face_css = f"""@font-face {{
      font-family: 'Orbitron';
      src: url(data:font/woff2;charset=utf-8;base64,{font_b64}) format('woff2');
    }}"""
        else:
            font_face_css = ""
    except Exception:
        font_face_css = ""


    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 232" width="500" height="232" role="img" aria-label="Muhammed Fadhil's GitHub stats">
<defs><style><![CDATA[
{font_face_css}
text{{font-family:'Segoe UI', system-ui, sans-serif}}
.title{{font-family:'Orbitron', 'Segoe UI', sans-serif}}
@keyframes fadeSlide{{from{{opacity:0;transform:translateX(-14px)}}to{{opacity:1;transform:translateX(0)}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes rankPulse{{0%,100%{{opacity:.85;transform:scale(1)}}50%{{opacity:1;transform:scale(1.05)}}}}
@keyframes shineX{{0%{{transform:translateX(-160px) skewX(-15deg)}}60%,100%{{transform:translateX(560px) skewX(-15deg)}}}}
.row{{opacity:0;animation:fadeSlide .5s ease forwards}}
.rk{{animation:rankPulse 2.4s ease-in-out infinite; transform-box:fill-box; transform-origin:center}}
.sh{{animation:shineX 4.5s ease-in-out 2.4s infinite}}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#06b6d4;#3b82f6;#0284c7;#06b6d4" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#0284c7;#06b6d4;#3b82f6;#0284c7" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="ringg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#06b6d4"/><stop offset="100%" stop-color="#3b82f6"/>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".07"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#020617"/>
</linearGradient>
<clipPath id="cc"><rect x="1" y="1" width="498" height="230" rx="14"/></clipPath>
<filter id="g"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="g2"><feGaussianBlur stdDeviation="1.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>

<!-- Background -->
<rect x="1" y="1" width="498" height="230" rx="14" fill="url(#bg)" stroke="#1e293b" stroke-width="1.5"/>

<!-- Title -->
<text class="title" x="24" y="38" font-size="16" font-weight="bold" fill="#f8fafc">Muhammed Fadhil's GitHub Stats</text>
<text class="title" x="24" y="38" font-size="16" font-weight="bold" fill="url(#tg)" filter="url(#g2)">Muhammed Fadhil's GitHub Stats</text>

  <!-- Rows -->
  <g class="row" style="animation-delay:0.50s">
    <text x="24" y="74" font-size="14">⭐</text>
    <text x="52" y="74" font-size="13.5" fill="#e2e8f0" font-weight="600">Total Stars Earned:</text>
    <text x="316" y="74" text-anchor="end" font-size="14" font-weight="bold" fill="#f59e0b">{stars}</text>
  </g>
  <g class="row" style="animation-delay:0.72s">
    <text x="24" y="105" font-size="14">💻</text>
    <text x="52" y="105" font-size="13.5" fill="#e2e8f0" font-weight="600">Total Commits:</text>
    <text x="316" y="105" text-anchor="end" font-size="14" font-weight="bold" fill="#06b6d4">{commits}</text>
  </g>
  <g class="row" style="animation-delay:0.94s">
    <text x="24" y="136" font-size="14">📦</text>
    <text x="52" y="136" font-size="13.5" fill="#e2e8f0" font-weight="600">Public Repos:</text>
    <text x="316" y="136" text-anchor="end" font-size="14" font-weight="bold" fill="#3b82f6">{repos}</text>
  </g>
  <g class="row" style="animation-delay:1.16s">
    <text x="24" y="167" font-size="14">👥</text>
    <text x="52" y="167" font-size="13.5" fill="#e2e8f0" font-weight="600">Followers:</text>
    <text x="316" y="167" text-anchor="end" font-size="14" font-weight="bold" fill="#a855f7">{followers}</text>
  </g>
  <g class="row" style="animation-delay:1.38s">
    <text x="24" y="198" font-size="14">🚀</text>
    <text x="52" y="198" font-size="13.5" fill="#e2e8f0" font-weight="600">Projects Deployed:</text>
    <text x="316" y="198" text-anchor="end" font-size="14" font-weight="bold" fill="#10b981">{projects}</text>
  </g>

<!-- Rank ring -->
<g transform="translate(408,138)">
  <circle r="52" fill="none" stroke="#1e293b" stroke-width="9"/>
  <!-- Stroke array for S rank (almost full circle) -->
  <circle r="52" fill="none" stroke="url(#ringg)" stroke-width="9" stroke-linecap="round"
    stroke-dasharray="290 326.7" stroke-dashoffset="290" transform="rotate(-90)">
    <animate attributeName="stroke-dashoffset" from="290" to="0" dur="1.6s" begin=".6s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
  </circle>
  <text class="rk title" y="16" text-anchor="middle" font-size="46" font-weight="bold" fill="#06b6d4" filter="url(#g)">{rank}</text>
  <text class="rk title" y="16" text-anchor="middle" font-size="46" font-weight="bold" fill="#f8fafc">{rank}</text>
  <text y="76" text-anchor="middle" font-size="10.5" fill="#94a3b8" opacity="0" font-weight="bold" letter-spacing="2" style="animation:fadeIn .5s ease 1.8s forwards">RANK</text>
</g>

<!-- Shine effect -->
<g clip-path="url(#cc)"><rect class="sh" x="0" y="0" width="120" height="232" fill="url(#shg)"/></g>
</svg>
"""

    with open('stats.svg', 'w', encoding='utf-8') as f:
        f.write(svg_template)

    print("Generated stats.svg successfully!")

if __name__ == "__main__":
    generate_stats_svg("40+", "1.2K+", "25+", "15+", "12+", "S")
