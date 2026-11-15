"""Generates a rich pack of modern 3D & neon SVG icons for Claude Video Studio."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(BASE_DIR, "assets", "icons")
os.makedirs(ICONS_DIR, exist_ok=True)

icons = {
    # 1. Startup Rocket
    "rocket.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="rocketBody" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="60%" stop-color="#e2e8f0" />
      <stop offset="100%" stop-color="#94a3b8" />
    </linearGradient>
    <linearGradient id="flameGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="40%" stop-color="#f97316" />
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0" />
    </linearGradient>
    <filter id="rocketGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#f97316" flood-opacity="0.6"/>
    </filter>
  </defs>
  <g filter="url(#rocketGlow)" transform="rotate(-45 200 200)">
    <!-- Fire Flame -->
    <path d="M 180 280 Q 200 380 200 390 Q 200 380 220 280 Z" fill="url(#flameGrad)" />
    <path d="M 190 280 Q 200 340 200 350 Q 200 340 210 280 Z" fill="#fef08a" />
    <!-- Left Fin -->
    <path d="M 155 250 L 120 290 L 160 275 Z" fill="#ef4444"/>
    <!-- Right Fin -->
    <path d="M 245 250 L 280 290 L 240 275 Z" fill="#ef4444"/>
    <!-- Rocket Fuselage -->
    <path d="M 160 270 C 160 170 180 70 200 40 C 220 70 240 170 240 270 Z" fill="url(#rocketBody)" stroke="#cbd5e1" stroke-width="3"/>
    <!-- Nosecone tip -->
    <path d="M 185 90 C 190 60 200 40 200 40 C 200 40 210 60 215 90 Z" fill="#ef4444"/>
    <!-- Porthole Window -->
    <circle cx="200" cy="140" r="24" fill="#0284c7" stroke="#38bdf8" stroke-width="4"/>
    <circle cx="200" cy="140" r="16" fill="#38bdf8" opacity="0.6"/>
    <circle cx="194" cy="134" r="5" fill="#ffffff"/>
    <!-- Thruster base ring -->
    <rect x="175" y="265" width="50" height="12" rx="3" fill="#475569"/>
  </g>
</svg>""",

    # 2. Money Stack / Cash
    "cash_stack.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="moneyGreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4ade80" />
      <stop offset="50%" stop-color="#22c55e" />
      <stop offset="100%" stop-color="#15803d" />
    </linearGradient>
    <filter id="moneyGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="15" flood-color="#22c55e" flood-opacity="0.45"/>
    </filter>
  </defs>
  <g filter="url(#moneyGlow)">
    <!-- Bottom bill -->
    <rect x="70" y="240" width="240" height="80" rx="14" fill="#14532d" stroke="#166534" stroke-width="3" transform="rotate(-6 190 280)"/>
    <!-- Middle bill -->
    <rect x="80" y="200" width="240" height="80" rx="14" fill="#166534" stroke="#22c55e" stroke-width="3" transform="rotate(4 200 240)"/>
    <!-- Top bill -->
    <rect x="80" y="150" width="240" height="90" rx="16" fill="url(#moneyGreen)" stroke="#86efac" stroke-width="4"/>
    <rect x="95" y="162" width="210" height="66" rx="10" fill="none" stroke="#bbf7d0" stroke-width="2" stroke-dasharray="8 6"/>
    <circle cx="200" cy="195" r="24" fill="#15803d" stroke="#86efac" stroke-width="3"/>
    <text x="200" y="206" font-family="Arial, sans-serif" font-size="32" font-weight="900" fill="#ffffff" text-anchor="middle">$</text>
  </g>
</svg>""",

    # 3. Exponential Growth Chart
    "growth_chart.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="chartLine" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="60%" stop-color="#4ade80" />
      <stop offset="100%" stop-color="#a3e635" />
    </linearGradient>
    <linearGradient id="areaFill" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4ade80" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#4ade80" stop-opacity="0.0" />
    </linearGradient>
    <filter id="chartGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#4ade80" flood-opacity="0.55"/>
    </filter>
  </defs>
  <g filter="url(#chartGlow)">
    <!-- Base card -->
    <rect x="50" y="60" width="300" height="280" rx="24" fill="#0f172a" stroke="rgba(255,255,255,0.12)" stroke-width="3"/>
    <!-- Grid lines -->
    <line x1="80" y1="130" x2="320" y2="130" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>
    <line x1="80" y1="190" x2="320" y2="190" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>
    <line x1="80" y1="250" x2="320" y2="250" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>
    <!-- Fill Area -->
    <path d="M 80 280 Q 180 270 240 180 T 310 90 L 310 280 Z" fill="url(#areaFill)"/>
    <!-- Exponential Line -->
    <path d="M 80 280 Q 180 270 240 180 T 310 90" fill="none" stroke="url(#chartLine)" stroke-width="6" stroke-linecap="round"/>
    <!-- Peak Arrow point -->
    <circle cx="310" cy="90" r="9" fill="#ffffff" stroke="#4ade80" stroke-width="4"/>
    <!-- Metric tag -->
    <rect x="235" y="75" width="60" height="26" rx="6" fill="#22c55e"/>
    <text x="265" y="93" font-family="Arial, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">+940%</text>
  </g>
</svg>""",

    # 4. Futuristic AI Robot Head
    "robot_head.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="robotMetal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <filter id="robotGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#06b6d4" flood-opacity="0.5"/>
    </filter>
  </defs>
  <g filter="url(#robotGlow)">
    <!-- Ears / side antennas -->
    <rect x="80" y="170" width="30" height="60" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
    <rect x="290" y="170" width="30" height="60" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
    <!-- Head Body -->
    <rect x="100" y="110" width="200" height="180" rx="36" fill="url(#robotMetal)" stroke="#38bdf8" stroke-width="4"/>
    <!-- Top Antenna -->
    <line x1="200" y1="110" x2="200" y2="60" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
    <circle cx="200" cy="55" r="10" fill="#38bdf8"/>
    <!-- Visor Eye Screen -->
    <rect x="125" y="150" width="150" height="55" rx="16" fill="#030712" stroke="#06b6d4" stroke-width="2"/>
    <!-- Glowing Visor Slit -->
    <rect x="140" y="172" width="120" height="12" rx="6" fill="#38bdf8"/>
    <!-- Mouth grill -->
    <line x1="160" y1="245" x2="240" y2="245" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    <line x1="175" y1="258" x2="225" y2="258" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
  </g>
</svg>""",

    # 5. Cyber Lightning Bolt
    "lightning.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="boltGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#facc15" />
      <stop offset="100%" stop-color="#eab308" />
    </linearGradient>
    <filter id="boltGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="18" flood-color="#facc15" flood-opacity="0.65"/>
    </filter>
  </defs>
  <g filter="url(#boltGlow)">
    <polygon points="220,40 110,210 190,210 150,360 290,170 210,170"
             fill="url(#boltGrad)" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"/>
  </g>
</svg>""",

    # 6. Trending Viral Fire
    "fire_viral.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="fireOuter" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#dc2626" />
      <stop offset="50%" stop-color="#f97316" />
      <stop offset="100%" stop-color="#facc15" />
    </linearGradient>
    <linearGradient id="fireInner" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#f97316" />
      <stop offset="100%" stop-color="#fef08a" />
    </linearGradient>
    <filter id="fireGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#f97316" flood-opacity="0.6"/>
    </filter>
  </defs>
  <g filter="url(#fireGlow)">
    <path d="M 200 40 C 230 110 310 160 310 250 C 310 320 260 360 200 360 C 140 360 90 320 90 250 C 90 190 140 140 160 80 C 170 120 190 130 200 110 C 210 80 200 40 200 40 Z"
          fill="url(#fireOuter)" />
    <!-- Inner Flame -->
    <path d="M 200 170 C 220 210 260 240 260 280 C 260 320 230 340 200 340 C 170 340 140 320 140 280 C 140 240 170 210 180 180 Z"
          fill="url(#fireInner)" />
  </g>
</svg>"""
}

for name, svg_text in icons.items():
    path = os.path.join(ICONS_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_text.strip())
    print(f"Created: {path}")

print("Extra icon library ready!")
