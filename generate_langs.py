import base64
import os
import urllib.request
import re

def generate_langs_svg(langs):
    """
    langs: list of dicts [{'name': 'Python', 'pct': 45.0, 'color': '#3b82f6'}, ...]
    Must have exactly 4 items for this template.
    """
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

    python_pct = langs[0]['pct']
    django_pct = langs[1]['pct']
    react_pct = langs[2]['pct']
    docker_pct = langs[3]['pct']

    bar_width = 380.0
    py_w = bar_width * (python_pct / 100.0)
    dj_w = bar_width * (django_pct / 100.0)
    re_w = bar_width * (react_pct / 100.0)
    do_w = bar_width * (docker_pct / 100.0)

    c_py = langs[0]['color']
    c_dj = langs[1]['color']
    c_re = langs[2]['color']
    c_do = langs[3]['color']

    n_py = langs[0]['name']
    n_dj = langs[1]['name']
    n_re = langs[2]['name']
    n_do = langs[3]['name']

    max_sub_w = 268.0
    py_sw = max_sub_w * (python_pct / 100.0)
    dj_sw = max_sub_w * (django_pct / 100.0)
    re_sw = max_sub_w * (react_pct / 100.0)
    do_sw = max_sub_w * (docker_pct / 100.0)

    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 282" width="420" height="282" role="img" aria-label="Top languages">
<defs><style><![CDATA[
{font_face_css}
text{{font-family:'Segoe UI', system-ui, sans-serif}}
.title{{font-family:'Orbitron', 'Segoe UI', sans-serif}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes shineX{{0%{{transform:translateX(-140px)}}60%,100%{{transform:translateX(460px)}}}}
.row{{opacity:0;animation:fadeUp .5s ease forwards}}
.sh{{animation:shineX 4s ease-in-out 2.2s infinite}}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#06b6d4;#3b82f6;#0284c7;#06b6d4" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#0284c7;#06b6d4;#3b82f6;#0284c7" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".08"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#020617"/>
</linearGradient>

<clipPath id="cardc"><rect x="1" y="1" width="418" height="280" rx="14"/></clipPath>
<clipPath id="stackc"><rect x="20" y="58" width="0" height="11" rx="5.5"><animate attributeName="width" from="0" to="380" dur="1.4s" begin=".4s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/></rect></clipPath>
<filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>

<!-- Background -->
<rect x="1" y="1" width="418" height="280" rx="14" fill="url(#bg)" stroke="#1e293b" stroke-width="1.5"/>

<!-- Title -->
<text class="title" x="20" y="34" font-size="16" font-weight="bold" fill="#f8fafc">Top Languages</text>
<text class="title" x="20" y="34" font-size="16" font-weight="bold" fill="url(#tg)" filter="url(#glow)">Top Languages</text>

<!-- Top Bar -->
<g clip-path="url(#stackc)">
  <rect x="20.0" y="58" width="{py_w}" height="11" fill="{c_py}"/>
  <rect x="{20.0 + py_w}" y="58" width="{dj_w}" height="11" fill="{c_dj}"/>
  <rect x="{20.0 + py_w + dj_w}" y="58" width="{re_w}" height="11" fill="{c_re}"/>
  <rect x="{20.0 + py_w + dj_w + re_w}" y="58" width="{do_w}" height="11" fill="{c_do}"/>
</g>

  <!-- Lang 1 -->
  <g class="row" style="animation-delay:0.90s">
    <circle cx="26" cy="91" r="5" fill="{c_py}" filter="url(#glow)"/>
    <circle cx="26" cy="91" r="5" fill="{c_py}"/>
    <text x="40" y="96" font-size="13" fill="#e2e8f0" font-weight="bold">{n_py}</text>
    <text x="396" y="96" text-anchor="end" font-size="13" fill="{c_py}" font-weight="bold">{python_pct:.1f}%</text>
    <rect x="40" y="104" width="268" height="9" rx="4.5" fill="#1e293b"/>
    <rect class="bar" x="40" y="104" width="{py_sw}" height="9" rx="4.5" fill="{c_py}" style="animation-delay:1.05s">
      <animate attributeName="width" from="0" to="{py_sw}" dur="1.1s" begin="1.05s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Lang 2 -->
  <g class="row" style="animation-delay:1.25s">
    <circle cx="26" cy="133" r="5" fill="{c_dj}" filter="url(#glow)"/>
    <circle cx="26" cy="133" r="5" fill="{c_dj}"/>
    <text x="40" y="138" font-size="13" fill="#e2e8f0" font-weight="bold">{n_dj}</text>
    <text x="396" y="138" text-anchor="end" font-size="13" fill="{c_dj}" font-weight="bold">{django_pct:.1f}%</text>
    <rect x="40" y="146" width="268" height="9" rx="4.5" fill="#1e293b"/>
    <rect class="bar" x="40" y="146" width="{dj_sw}" height="9" rx="4.5" fill="{c_dj}" style="animation-delay:1.40s">
      <animate attributeName="width" from="0" to="{dj_sw}" dur="1.1s" begin="1.40s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Lang 3 -->
  <g class="row" style="animation-delay:1.60s">
    <circle cx="26" cy="175" r="5" fill="{c_re}" filter="url(#glow)"/>
    <circle cx="26" cy="175" r="5" fill="{c_re}"/>
    <text x="40" y="180" font-size="13" fill="#e2e8f0" font-weight="bold">{n_re}</text>
    <text x="396" y="180" text-anchor="end" font-size="13" fill="{c_re}" font-weight="bold">{react_pct:.1f}%</text>
    <rect x="40" y="188" width="268" height="9" rx="4.5" fill="#1e293b"/>
    <rect class="bar" x="40" y="188" width="{re_sw}" height="9" rx="4.5" fill="{c_re}" style="animation-delay:1.75s">
      <animate attributeName="width" from="0" to="{re_sw}" dur="1.1s" begin="1.75s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Lang 4 -->
  <g class="row" style="animation-delay:1.95s">
    <circle cx="26" cy="217" r="5" fill="{c_do}" filter="url(#glow)"/>
    <circle cx="26" cy="217" r="5" fill="{c_do}"/>
    <text x="40" y="222" font-size="13" fill="#e2e8f0" font-weight="bold">{n_do}</text>
    <text x="396" y="222" text-anchor="end" font-size="13" fill="{c_do}" font-weight="bold">{docker_pct:.1f}%</text>
    <rect x="40" y="230" width="268" height="9" rx="4.5" fill="#1e293b"/>
    <rect class="bar" x="40" y="230" width="{do_sw}" height="9" rx="4.5" fill="{c_do}" style="animation-delay:2.10s">
      <animate attributeName="width" from="0" to="{do_sw}" dur="1.1s" begin="2.10s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

<g clip-path="url(#cardc)"><rect class="sh" x="0" y="0" width="100" height="282" fill="url(#shg)" transform="skewX(-15)"/></g>
</svg>
"""

    with open('langs.svg', 'w', encoding='utf-8') as f:
        f.write(svg_template)

    print("Generated langs.svg successfully!")

if __name__ == "__main__":
    generate_langs_svg([
        {'name': 'Python', 'pct': 45.0, 'color': '#3b82f6'},
        {'name': 'Django', 'pct': 30.0, 'color': '#0ea5e9'},
        {'name': 'React', 'pct': 15.0, 'color': '#06b6d4'},
        {'name': 'Docker', 'pct': 10.0, 'color': '#f59e0b'}
    ])
