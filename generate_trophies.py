import base64
import os
import urllib.request
import re

def generate_trophies_svg(stars, commits, repos, followers):
    # Determine Ranks
    r_stars = "S" if stars >= 100 else ("A" if stars >= 40 else "B")
    r_commits = "S" if commits >= 1000 else ("A" if commits >= 500 else "B")
    r_repos = "S" if repos >= 25 else ("A" if repos >= 10 else "B")
    r_followers = "S" if followers >= 50 else ("A" if followers >= 15 else "B")

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


    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1092 168" width="1092" height="168" role="img" aria-label="GitHub trophies">
<defs><style><![CDATA[
{font_face_css}
text{{font-family:'Segoe UI', system-ui, sans-serif}}
.title{{font-family:'Orbitron', 'Segoe UI', sans-serif}}
@keyframes popCell{{0%{{opacity:0;transform:translateY(16px) scale(.85)}}70%{{opacity:1;transform:translateY(-3px) scale(1.03)}}100%{{opacity:1;transform:translateY(0) scale(1)}}}}
@keyframes rankGlow{{0%,100%{{opacity:.75;transform:scale(1)}}50%{{opacity:1;transform:scale(1.08)}}}}
@keyframes shineX2{{0%{{transform:translateX(-200px) skewX(-15deg)}}60%,100%{{transform:translateX(1172px) skewX(-15deg)}}}}
.cell{{opacity:0;animation:popCell .55s cubic-bezier(.2,.8,.3,1.2) forwards;transform-box:fill-box;transform-origin:center}}
.rk{{animation:rankGlow 2.2s ease-in-out infinite; transform-box:fill-box; transform-origin:center}}
.sh2{{animation:shineX2 5s ease-in-out 2s infinite}}
]]></style>
<linearGradient id="shg2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".07"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#020617"/>
</linearGradient>
<clipPath id="tc"><rect x="0" y="0" width="1092" height="168" rx="14"/></clipPath>
<filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>

  <!-- Cell 1 -->
  <g class="cell" style="animation-delay:0.30s">
    <rect x="12" y="12" width="168" height="144" rx="14" fill="url(#bg)" stroke="#06b6d4" stroke-opacity=".7" stroke-width="1.5"/>
    <text x="96.0" y="52" text-anchor="middle" font-size="30">⚙️</text>
    <text class="rk title" x="164" y="40" text-anchor="end" font-size="24" font-weight="bold" fill="#06b6d4" filter="url(#glow)" style="animation-delay:0.70s">SSS</text>
    <text class="rk title" x="164" y="40" text-anchor="end" font-size="24" font-weight="bold" fill="#f8fafc" style="animation-delay:0.70s">SSS</text>
    <text x="96.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#f8fafc">Architect</text>
    <text x="96.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8" font-weight="600">Full-Stack Dev</text>
    <rect x="30" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="30" y="124" width="0" height="5" rx="2.5" fill="#06b6d4">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.60s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  
  <!-- Cell 2 -->
  <g class="cell" style="animation-delay:0.48s">
    <rect x="192" y="12" width="168" height="144" rx="14" fill="url(#bg)" stroke="#f59e0b" stroke-opacity=".7" stroke-width="1.5"/>
    <text x="276.0" y="52" text-anchor="middle" font-size="30">🌟</text>
    <text class="rk title" x="344" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#f59e0b" filter="url(#glow)" style="animation-delay:0.88s">S</text>
    <text class="rk title" x="344" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#f8fafc" style="animation-delay:0.88s">S</text>
    <text x="276.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#f8fafc">Open Source</text>
    <text x="276.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8" font-weight="600">GitHub Badge</text>
    <rect x="210" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="210" y="124" width="0" height="5" rx="2.5" fill="#f59e0b">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.78s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  
  <!-- Cell 3 -->
  <g class="cell" style="animation-delay:0.66s">
    <rect x="372" y="12" width="168" height="144" rx="14" fill="url(#bg)" stroke="#3b82f6" stroke-opacity=".7" stroke-width="1.5"/>
    <text x="456.0" y="52" text-anchor="middle" font-size="30">⭐</text>
    <text class="rk title" x="524" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#3b82f6" filter="url(#glow)" style="animation-delay:1.06s">{r_stars}</text>
    <text class="rk title" x="524" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#f8fafc" style="animation-delay:1.06s">{r_stars}</text>
    <text x="456.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#f8fafc">Stargazer</text>
    <text x="456.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8" font-weight="600">Stars {stars}</text>
    <rect x="390" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="390" y="124" width="0" height="5" rx="2.5" fill="#3b82f6">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.96s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  
  <!-- Cell 4 -->
  <g class="cell" style="animation-delay:0.84s">
    <rect x="552" y="12" width="168" height="144" rx="14" fill="url(#bg)" stroke="#a855f7" stroke-opacity=".7" stroke-width="1.5"/>
    <text x="636.0" y="52" text-anchor="middle" font-size="30">💜</text>
    <text class="rk title" x="704" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#a855f7" filter="url(#glow)" style="animation-delay:1.24s">{r_followers}</text>
    <text class="rk title" x="704" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#f8fafc" style="animation-delay:1.24s">{r_followers}</text>
    <text x="636.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#f8fafc">Rising Star</text>
    <text x="636.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8" font-weight="600">Followers {followers}</text>
    <rect x="570" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="570" y="124" width="0" height="5" rx="2.5" fill="#a855f7">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.14s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  
  <!-- Cell 5 -->
  <g class="cell" style="animation-delay:1.02s">
    <rect x="732" y="12" width="168" height="144" rx="14" fill="url(#bg)" stroke="#10b981" stroke-opacity=".7" stroke-width="1.5"/>
    <text x="816.0" y="52" text-anchor="middle" font-size="30">💻</text>
    <text class="rk title" x="884" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#10b981" filter="url(#glow)" style="animation-delay:1.42s">{r_commits}</text>
    <text class="rk title" x="884" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#f8fafc" style="animation-delay:1.42s">{r_commits}</text>
    <text x="816.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#f8fafc">Committer</text>
    <text x="816.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8" font-weight="600">Commits {commits}</text>
    <rect x="750" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="750" y="124" width="0" height="5" rx="2.5" fill="#10b981">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.32s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  
  <!-- Cell 6 -->
  <g class="cell" style="animation-delay:1.20s">
    <rect x="912" y="12" width="168" height="144" rx="14" fill="url(#bg)" stroke="#0ea5e9" stroke-opacity=".7" stroke-width="1.5"/>
    <text x="996.0" y="52" text-anchor="middle" font-size="30">📦</text>
    <text class="rk title" x="1064" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#0ea5e9" filter="url(#glow)" style="animation-delay:1.60s">{r_repos}</text>
    <text class="rk title" x="1064" y="40" text-anchor="end" font-size="28" font-weight="bold" fill="#f8fafc" style="animation-delay:1.60s">{r_repos}</text>
    <text x="996.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#f8fafc">Creator</text>
    <text x="996.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8" font-weight="600">Repos {repos}</text>
    <rect x="930" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="930" y="124" width="0" height="5" rx="2.5" fill="#0ea5e9">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.50s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  
<g clip-path="url(#tc)"><rect class="sh2" x="0" y="0" width="140" height="168" fill="url(#shg2)"/></g>
</svg>
"""

    with open('trophies.svg', 'w', encoding='utf-8') as f:
        f.write(svg_template)

    print("Generated trophies.svg successfully!")

if __name__ == "__main__":
    generate_trophies_svg(40, 1200, 25, 15)
