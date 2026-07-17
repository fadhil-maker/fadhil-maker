<img width="1280" height="740" alt="banner" src="https://github.com/user-attachments/assets/988120fc-fefc-4efb-9b9c-c79bcfc524ad" />
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="1280" height="740">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#0a0a1a"/>
    <stop offset="50%" stop-color="#12102e"/>
    <stop offset="100%" stop-color="#0d0b20"/>
  </linearGradient>
  <linearGradient id="amberBar" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#f59e0b"/>
    <stop offset="100%" stop-color="#d97706"/>
  </linearGradient>
  <linearGradient id="orbGrad1" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#a855f7" stop-opacity="0.25"/>
    <stop offset="100%" stop-color="#7c3aed" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="orbGrad2" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.18"/>
    <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
  </linearGradient>
  <filter id="neonGlow">
    <feGaussianBlur stdDeviation="6" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="softGlow">
    <feGaussianBlur stdDeviation="3" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="orbBlur">
    <feGaussianBlur stdDeviation="18"/>
  </filter>
  <clipPath id="statsClip1"><rect x="260" y="478" width="0" height="12" rx="6"><animate attributeName="width" from="0" to="360" dur="1.8s" begin="2.5s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/></rect></clipPath>
  <clipPath id="statsClip2"><rect x="260" y="500" width="0" height="12" rx="6"><animate attributeName="width" from="0" to="340" dur="1.8s" begin="2.8s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/></rect></clipPath>
  <clipPath id="statsClip3"><rect x="260" y="522" width="0" height="12" rx="6"><animate attributeName="width" from="0" to="320" dur="1.8s" begin="3.1s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/></rect></clipPath>
</defs>
<style>
  /* ── KEYFRAMES ── */
  @keyframes cursorBlink { 0%,49%{opacity:1}50%,100%{opacity:0} }
  @keyframes fadeInUp { from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)} }
  @keyframes fadeIn { from{opacity:0}to{opacity:1} }
  @keyframes slideInLeft { from{opacity:0;transform:translateX(-30px)}to{opacity:1;transform:translateX(0)} }
  @keyframes pillFade { from{opacity:0;transform:scale(0.85)}to{opacity:1;transform:scale(1)} }
  @keyframes pulseGlow { 0%,100%{opacity:0.5}50%{opacity:1} }
  @keyframes neonFlicker { 0%,19%,21%,23%,25%,54%,56%,100%{opacity:1}20%,24%,55%{opacity:0.4} }
  @keyframes scanLine { 0%{transform:translateY(0)}100%{transform:translateY(740px)} }
  @keyframes floatA { 0%,100%{transform:translate(0,0)}50%{transform:translate(15px,-20px)} }
  @keyframes floatB { 0%,100%{transform:translate(0,0)}50%{transform:translate(-12px,18px)} }
  @keyframes floatC { 0%,100%{transform:translate(0,0)}50%{transform:translate(10px,14px)} }
  @keyframes twinkle { 0%,100%{opacity:0.15;transform:scale(0.8)}50%{opacity:0.9;transform:scale(1.3)} }
  @keyframes spinDiamond { from{transform:rotate(0deg)}to{transform:rotate(360deg)} }
  @keyframes borderPulse { 0%,100%{opacity:0.18}50%{opacity:0.38} }
  @keyframes cornerPulse { 0%,100%{opacity:0.6}50%{opacity:1} }
  @keyframes barGrow1 { from{width:0}to{width:360px} }
  @keyframes barGrow2 { from{width:0}to{width:340px} }
  @keyframes barGrow3 { from{width:0}to{width:320px} }
  @keyframes separatorDraw { from{width:0}to{width:200px} }
  @keyframes separatorDrawV { from{width:0}to{width:60px} }
  @keyframes codeLine { from{opacity:0;transform:translateX(6px)}to{opacity:1;transform:translateX(0)} }
  @keyframes typingReveal { from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)} }

  /* ── BASE ── */
  .mono { font-family:'Consolas','Courier New',monospace }
  .sans { font-family:'Segoe UI',system-ui,-apple-system,sans-serif }

  /* ── CURSOR ── */
  .cursor { animation: cursorBlink 1s step-end infinite }

  /* ── NAME LETTERS ── */
  .nl { opacity:0; animation: fadeInUp 0.5s ease-out both }

  /* ── ROLE ── */
  .role1 { opacity:0; animation: fadeIn 0.8s ease-out 1.2s both }
  .role2 { opacity:0; animation: fadeIn 0.8s ease-out 1.5s both }

  /* ── PILLS ── */
  .pill { opacity:0; animation: pillFade 0.5s ease-out both }
  .pill-glow { animation: pulseGlow 3s ease-in-out infinite }

  /* ── ABOUT ── */
  .about-line { opacity:0; animation: slideInLeft 0.6s ease-out both }

  /* ── CODE ── */
  .code-line { opacity:0; animation: codeLine 0.5s ease-out both }

  /* ── STATS ── */
  .stat-bar { animation-fill-mode: both }
  .sb1 { width:0; animation: barGrow1 1.8s cubic-bezier(0.25,0.1,0.25,1) 2.5s both }
  .sb2 { width:0; animation: barGrow2 1.8s cubic-bezier(0.25,0.1,0.25,1) 2.8s both }
  .sb3 { width:0; animation: barGrow3 1.8s cubic-bezier(0.25,0.1,0.25,1) 3.1s both }

  /* ── NEON ── */
  .neon-text { animation: neonFlicker 4s ease-in-out infinite }

  /* ── SCANNER ── */
  .scanner { animation: scanLine 4s linear infinite }

  /* ── FLOATS ── */
  .orb1 { animation: floatA 7s ease-in-out infinite }
  .orb2 { animation: floatB 9s ease-in-out infinite }
  .orb3 { animation: floatC 8s ease-in-out infinite }

  /* ── SPARKLES ── */
  .sparkle { animation: twinkle 2s ease-in-out infinite }

  /* ── DIAMOND ── */
  .diamond { animation: spinDiamond 12s linear infinite; transform-origin: center }

  /* ── BORDER ── */
  .outer-border { animation: borderPulse 4s ease-in-out infinite }
  .corner-accent { animation: cornerPulse 3s ease-in-out infinite }
</style>

<!-- ══════════ BACKGROUND ══════════ -->
<rect width="1280" height="740" fill="url(#bg)"/>

<!-- ── Grid ── -->
<g opacity="0.04" stroke="#a855f7" stroke-width="0.5">
  <line x1="0" y1="0" x2="0" y2="740"/><line x1="40" y1="0" x2="40" y2="740"/><line x1="80" y1="0" x2="80" y2="740"/>
  <line x1="120" y1="0" x2="120" y2="740"/><line x1="160" y1="0" x2="160" y2="740"/><line x1="200" y1="0" x2="200" y2="740"/>
  <line x1="240" y1="0" x2="240" y2="740"/><line x1="280" y1="0" x2="280" y2="740"/><line x1="320" y1="0" x2="320" y2="740"/>
  <line x1="360" y1="0" x2="360" y2="740"/><line x1="400" y1="0" x2="400" y2="740"/><line x1="440" y1="0" x2="440" y2="740"/>
  <line x1="480" y1="0" x2="480" y2="740"/><line x1="520" y1="0" x2="520" y2="740"/><line x1="560" y1="0" x2="560" y2="740"/>
  <line x1="600" y1="0" x2="600" y2="740"/><line x1="640" y1="0" x2="640" y2="740"/><line x1="680" y1="0" x2="680" y2="740"/>
  <line x1="720" y1="0" x2="720" y2="740"/><line x1="760" y1="0" x2="760" y2="740"/><line x1="800" y1="0" x2="800" y2="740"/>
  <line x1="840" y1="0" x2="840" y2="740"/><line x1="880" y1="0" x2="880" y2="740"/><line x1="920" y1="0" x2="920" y2="740"/>
  <line x1="960" y1="0" x2="960" y2="740"/><line x1="1000" y1="0" x2="1000" y2="740"/><line x1="1040" y1="0" x2="1040" y2="740"/>
  <line x1="1080" y1="0" x2="1080" y2="740"/><line x1="1120" y1="0" x2="1120" y2="740"/><line x1="1160" y1="0" x2="1160" y2="740"/>
  <line x1="1200" y1="0" x2="1200" y2="740"/><line x1="1240" y1="0" x2="1240" y2="740"/><line x1="1280" y1="0" x2="1280" y2="740"/>
  <line x1="0" y1="0" x2="1280" y2="0"/><line x1="0" y1="40" x2="1280" y2="40"/><line x1="0" y1="80" x2="1280" y2="80"/>
  <line x1="0" y1="120" x2="1280" y2="120"/><line x1="0" y1="160" x2="1280" y2="160"/><line x1="0" y1="200" x2="1280" y2="200"/>
  <line x1="0" y1="240" x2="1280" y2="240"/><line x1="0" y1="280" x2="1280" y2="280"/><line x1="0" y1="320" x2="1280" y2="320"/>
  <line x1="0" y1="360" x2="1280" y2="360"/><line x1="0" y1="400" x2="1280" y2="400"/><line x1="0" y1="440" x2="1280" y2="440"/>
  <line x1="0" y1="480" x2="1280" y2="480"/><line x1="0" y1="520" x2="1280" y2="520"/><line x1="0" y1="560" x2="1280" y2="560"/>
  <line x1="0" y1="600" x2="1280" y2="600"/><line x1="0" y1="640" x2="1280" y2="640"/><line x1="0" y1="680" x2="1280" y2="680"/>
  <line x1="0" y1="720" x2="1280" y2="720"/>
</g>

<!-- ══════════ OUTER BORDER ══════════ -->
<rect class="outer-border" x="18" y="18" width="1244" height="704" rx="18" ry="18" fill="none" stroke="#7c3aed" stroke-width="1.2"/>

<!-- ── Corner Accents ── -->
<g class="corner-accent" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round">
  <!-- Top-left -->
  <line x1="18" y1="50" x2="18" y2="18"/><line x1="18" y1="18" x2="50" y2="18"/>
  <!-- Top-right -->
  <line x1="1230" y1="18" x2="1262" y2="18"/><line x1="1262" y1="18" x2="1262" y2="50"/>
  <!-- Bottom-left -->
  <line x1="18" y1="690" x2="18" y2="722"/><line x1="18" y1="722" x2="50" y2="722"/>
  <!-- Bottom-right -->
  <line x1="1230" y1="722" x2="1262" y2="722"/><line x1="1262" y1="690" x2="1262" y2="722"/>
</g>

<!-- ══════════ HOLOGRAM SCANNER ══════════ -->
<g class="scanner" opacity="0.15">
  <rect x="18" y="0" width="1244" height="2" rx="1" fill="#a855f7"/>
  <rect x="18" y="2" width="1244" height="6" rx="1" fill="#a855f7" opacity="0.2"/>
</g>

<!-- ══════════ FLOATING ORBS ══════════ -->
<circle class="orb1" cx="120" cy="380" r="80" fill="#a855f7" opacity="0.07" filter="url(#orbBlur)"/>
<circle class="orb2" cx="1150" cy="200" r="65" fill="#f59e0b" opacity="0.06" filter="url(#orbBlur)"/>
<circle class="orb3" cx="900" cy="620" r="55" fill="#7c3aed" opacity="0.08" filter="url(#orbBlur)"/>

<!-- ══════════ SPARKLES ══════════ -->
<circle class="sparkle" cx="200" cy="120" r="1.5" fill="#f59e0b" style="animation-delay:0s"/>
<circle class="sparkle" cx="1050" cy="90" r="1.2" fill="#a855f7" style="animation-delay:0.5s"/>
<circle class="sparkle" cx="950" cy="500" r="1.8" fill="#f59e0b" style="animation-delay:1.2s"/>
<circle class="sparkle" cx="350" cy="650" r="1.3" fill="#a855f7" style="animation-delay:0.8s"/>
<circle class="sparkle" cx="1180" cy="600" r="1.5" fill="#f59e0b" style="animation-delay:1.6s"/>

<!-- ══════════ SPINNING DIAMOND ══════════ -->
<g class="diamond" transform="translate(1190,120)">
  <rect x="-12" y="-12" width="24" height="24" rx="2" fill="none" stroke="#a855f7" stroke-width="1" opacity="0.25" transform="rotate(45)"/>
</g>

<!-- ══════════ 1. TERMINAL LINE ══════════ -->
<g class="mono" transform="translate(55,55)">
  <text fill="#8b8ba7" font-size="14" opacity="0.7">
    <tspan fill="#f59e0b">user@dev</tspan><tspan fill="#8b8ba7">:</tspan><tspan fill="#a855f7">~</tspan><tspan fill="#8b8ba7">$ </tspan><tspan fill="#8b8ba7">cat README.md</tspan>
  </text>
  <text x="196" fill="#f0eef6" font-size="14" class="cursor">█</text>
</g>

<!-- ══════════ 2. NAME SECTION ══════════ -->
<g class="sans" text-anchor="middle">
  <!-- Staggered letters: M U H A M M E D   F A D H I L -->
  <text x="510" y="130" font-size="54" font-weight="700" fill="#f0eef6" letter-spacing="5">
    <tspan class="nl" style="animation-delay:0.3s">M</tspan><tspan class="nl" style="animation-delay:0.35s">U</tspan><tspan class="nl" style="animation-delay:0.4s">H</tspan><tspan class="nl" style="animation-delay:0.45s">A</tspan><tspan class="nl" style="animation-delay:0.5s">M</tspan><tspan class="nl" style="animation-delay:0.55s">M</tspan><tspan class="nl" style="animation-delay:0.6s">E</tspan><tspan class="nl" style="animation-delay:0.65s">D</tspan></text>
  <text x="830" y="130" font-size="54" font-weight="700" fill="#f0eef6" letter-spacing="5">
    <tspan class="nl" style="animation-delay:0.75s">F</tspan><tspan class="nl" style="animation-delay:0.8s">A</tspan><tspan class="nl" style="animation-delay:0.85s">D</tspan><tspan class="nl" style="animation-delay:0.9s">H</tspan><tspan class="nl" style="animation-delay:0.95s">I</tspan><tspan class="nl" style="animation-delay:1.0s">L</tspan></text>

  <!-- Separator -->
  <rect x="540" y="148" width="200" height="3" rx="1.5" fill="#f59e0b" opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.1s" fill="freeze"/>
    <animate attributeName="width" from="0" to="200" dur="0.8s" begin="1.1s" fill="freeze"/>
  </rect>
  <rect x="745" y="148" width="60" height="3" rx="1.5" fill="#a855f7" opacity="0">
    <animate attributeName="opacity" from="0" to="0.7" dur="0.5s" begin="1.4s" fill="freeze"/>
    <animate attributeName="width" from="0" to="60" dur="0.6s" begin="1.4s" fill="freeze"/>
  </rect>
</g>

<!-- ══════════ 3. ROLE TITLES ══════════ -->
<text class="sans role1" x="640" y="188" text-anchor="middle" font-size="18" font-weight="700" fill="#f59e0b" letter-spacing="3">FULL-STACK DEVELOPER</text>
<text class="sans role2" x="640" y="214" text-anchor="middle" font-size="15" font-weight="500" fill="#a855f7" letter-spacing="2">PYTHON / DJANGO SPECIALIST</text>

<!-- ══════════ 4. TECH STACK PILLS ══════════ -->
<g transform="translate(260,248)">
  <!-- Python -->
  <g class="pill" style="animation-delay:1.5s">
    <rect x="0" y="0" width="85" height="30" rx="15" fill="#1a1735" stroke="#a855f7" stroke-width="1" class="pill-glow"/>
    <text x="42" y="20" text-anchor="middle" fill="#f0eef6" font-size="12" class="sans">Python</text>
  </g>
  <!-- Django -->
  <g class="pill" style="animation-delay:1.6s">
    <rect x="100" y="0" width="85" height="30" rx="15" fill="#1a1735" stroke="#7c3aed" stroke-width="1" class="pill-glow"/>
    <text x="142" y="20" text-anchor="middle" fill="#f0eef6" font-size="12" class="sans">Django</text>
  </g>
  <!-- React -->
  <g class="pill" style="animation-delay:1.7s">
    <rect x="200" y="0" width="80" height="30" rx="15" fill="#1a1735" stroke="#f59e0b" stroke-width="1" class="pill-glow"/>
    <text x="240" y="20" text-anchor="middle" fill="#f0eef6" font-size="12" class="sans">React</text>
  </g>
  <!-- JS -->
  <g class="pill" style="animation-delay:1.8s">
    <rect x="295" y="0" width="55" height="30" rx="15" fill="#1a1735" stroke="#f59e0b" stroke-width="1" class="pill-glow"/>
    <text x="322" y="20" text-anchor="middle" fill="#f0eef6" font-size="12" class="sans">JS</text>
  </g>
  <!-- PostgreSQL -->
  <g class="pill" style="animation-delay:1.9s">
    <rect x="365" y="0" width="105" height="30" rx="15" fill="#1a1735" stroke="#a855f7" stroke-width="1" class="pill-glow"/>
    <text x="417" y="20" text-anchor="middle" fill="#f0eef6" font-size="12" class="sans">PostgreSQL</text>
  </g>
  <!-- Docker -->
  <g class="pill" style="animation-delay:2.0s">
    <rect x="485" y="0" width="82" height="30" rx="15" fill="#1a1735" stroke="#7c3aed" stroke-width="1" class="pill-glow"/>
    <text x="526" y="20" text-anchor="middle" fill="#f0eef6" font-size="12" class="sans">Docker</text>
  </g>
  <!-- Git -->
  <g class="pill" style="animation-delay:2.1s">
    <rect x="582" y="0" width="60" height="30" rx="15" fill="#1a1735" stroke="#f59e0b" stroke-width="1" class="pill-glow"/>
    <text x="612" y="20" text-anchor="middle" fill="#f0eef6" font-size="12" class="sans">Git</text>
  </g>
  <!-- Node.js -->
  <g class="pill" style="animation-delay:2.2s">
    <rect x="657" y="0" width="82" height="30" rx="15" fill="#1a1735" stroke="#a855f7" stroke-width="1" class="pill-glow"/>
    <text x="698" y="20" text-anchor="middle" fill="#f0eef6" font-size="12" class="sans">Node.js</text>
  </g>
</g>

<!-- ══════════ 5. ABOUT ME SECTION (left) ══════════ -->
<g transform="translate(70,320)">
  <text class="sans about-line" style="animation-delay:1.8s" x="0" y="0" fill="#8b8ba7" font-size="11" letter-spacing="2" font-weight="600" text-transform="uppercase">
    <tspan fill="#f59e0b">▸</tspan> ABOUT ME
  </text>
  <line x1="0" y1="10" x2="80" y2="10" stroke="#7c3aed" stroke-width="1" opacity="0.4"/>
  <text class="sans about-line" style="animation-delay:2.0s" x="0" y="38" fill="#f0eef6" font-size="14">🎓  B.Tech CS with Business Systems</text>
  <text class="sans about-line" style="animation-delay:2.15s" x="0" y="62" fill="#f0eef6" font-size="14">💻  Django &amp; Python Full-Stack Dev</text>
  <text class="sans about-line" style="animation-delay:2.3s" x="0" y="86" fill="#f0eef6" font-size="14">⚙️  VPS / Nginx / Cloudflare Infra</text>
  <text class="sans about-line" style="animation-delay:2.45s" x="0" y="110" fill="#f0eef6" font-size="14">🚀  Drug Interaction Tracking System</text>
  <text class="sans about-line" style="animation-delay:2.6s" x="0" y="134" fill="#a855f7" font-size="14">🌐  Muhammedfadhil.vercel.app</text>
</g>

<!-- ══════════ 6. CODE EDITOR CARD (right) ══════════ -->
<g transform="translate(700,310)">
  <!-- Card background -->
  <rect x="0" y="0" width="490" height="155" rx="10" fill="#0f0d1e" stroke="#7c3aed" stroke-width="0.8" opacity="0.9"/>
  <!-- Title bar -->
  <rect x="0" y="0" width="490" height="30" rx="10" fill="#161330"/>
  <rect x="0" y="15" width="490" height="15" fill="#161330"/>
  <!-- Dots -->
  <circle cx="18" cy="15" r="5" fill="#ef4444"/>
  <circle cx="36" cy="15" r="5" fill="#f59e0b"/>
  <circle cx="54" cy="15" r="5" fill="#22c55e"/>
  <!-- File name -->
  <text x="80" y="19" class="mono" font-size="11" fill="#8b8ba7">buildDreams.js</text>

  <!-- Code content -->
  <g class="mono" font-size="13">
    <text class="code-line" style="animation-delay:2.2s" x="18" y="52">
      <tspan fill="#a855f7">const </tspan><tspan fill="#f0eef6">fadhil = {</tspan>
    </text>
    <text class="code-line" style="animation-delay:2.5s" x="36" y="72">
      <tspan fill="#8b8ba7">role</tspan><tspan fill="#f0eef6">: </tspan><tspan fill="#f59e0b">"Full-Stack Dev"</tspan><tspan fill="#f0eef6">,</tspan>
    </text>
    <text class="code-line" style="animation-delay:2.8s" x="36" y="92">
      <tspan fill="#8b8ba7">stack</tspan><tspan fill="#f0eef6">: [</tspan><tspan fill="#f59e0b">"Django"</tspan><tspan fill="#f0eef6">, </tspan><tspan fill="#f59e0b">"React"</tspan><tspan fill="#f0eef6">],</tspan>
    </text>
    <text class="code-line" style="animation-delay:3.1s" x="36" y="112">
      <tspan fill="#8b8ba7">motto</tspan><tspan fill="#f0eef6">: </tspan><tspan fill="#f59e0b">"Ship it!"</tspan><tspan fill="#f0eef6">,</tspan>
    </text>
    <text class="code-line" style="animation-delay:3.4s" x="36" y="132">
      <tspan fill="#8b8ba7">coffee</tspan><tspan fill="#f0eef6">: </tspan><tspan fill="#a855f7">Infinity</tspan>
    </text>
    <text class="code-line" style="animation-delay:3.7s" x="18" y="149">
      <tspan fill="#f0eef6">};</tspan>
    </text>
  </g>
</g>

<!-- ══════════ 7. STATS BARS ══════════ -->
<g transform="translate(70,478)">
  <text class="sans" x="0" y="0" fill="#8b8ba7" font-size="11" letter-spacing="2" font-weight="600">
    <tspan fill="#f59e0b">▸</tspan> SKILL LEVELS
  </text>
  <line x1="0" y1="10" x2="80" y2="10" stroke="#7c3aed" stroke-width="1" opacity="0.4"/>

  <!-- Python -->
  <text class="sans" x="0" y="36" fill="#f0eef6" font-size="13">Python</text>
  <text class="sans" x="170" y="36" fill="#8b8ba7" font-size="11">90%</text>
  <rect x="195" y="26" width="400" height="11" rx="5.5" fill="#1a1735"/>
  <rect x="195" y="26" height="11" rx="5.5" fill="url(#amberBar)" class="sb1"/>

  <!-- Django -->
  <text class="sans" x="0" y="58" fill="#f0eef6" font-size="13">Django</text>
  <text class="sans" x="170" y="58" fill="#8b8ba7" font-size="11">85%</text>
  <rect x="195" y="48" width="400" height="11" rx="5.5" fill="#1a1735"/>
  <rect x="195" y="48" height="11" rx="5.5" fill="url(#amberBar)" class="sb2"/>

  <!-- JavaScript -->
  <text class="sans" x="0" y="80" fill="#f0eef6" font-size="13">JavaScript</text>
  <text class="sans" x="170" y="80" fill="#8b8ba7" font-size="11">80%</text>
  <rect x="195" y="70" width="400" height="11" rx="5.5" fill="#1a1735"/>
  <rect x="195" y="70" height="11" rx="5.5" fill="url(#amberBar)" class="sb3"/>
</g>

<!-- ══════════ 8. NEON SIGN ══════════ -->
<g transform="translate(640,610)" text-anchor="middle">
  <!-- Glow layer -->
  <text class="sans neon-text" x="0" y="0" font-size="28" font-weight="800" fill="#f59e0b" letter-spacing="6" filter="url(#neonGlow)" opacity="0.7">KEEP CODING KEEP GROWING</text>
  <!-- Solid layer -->
  <text class="sans neon-text" x="0" y="0" font-size="28" font-weight="800" fill="#f59e0b" letter-spacing="6">KEEP CODING KEEP GROWING</text>
</g>

<!-- ══════════ 9. TAGLINE ══════════ -->
<text class="mono" x="640" y="660" text-anchor="middle" fill="#8b8ba7" font-size="13" letter-spacing="1" opacity="0.7">"Code. Deploy. Scale. Repeat."</text>

<!-- ══════════ STATUS / FOOTER ══════════ -->
<g transform="translate(640,700)" text-anchor="middle">
  <circle cx="-80" cy="-4" r="4" fill="#22c55e" filter="url(#softGlow)"/>
  <text class="sans" x="-65" y="0" fill="#8b8ba7" font-size="11" text-anchor="start">Available for collaboration</text>
  <text class="mono" x="105" y="0" fill="#7c3aed" font-size="11">@fadhil-maker</text>
</g>

</svg>
