"""Generates high-aesthetic SVG graphics for Paris History Video."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(BASE_DIR, "assets", "icons")
AVATARS_DIR = os.path.join(BASE_DIR, "assets", "avatars")
os.makedirs(ICONS_DIR, exist_ok=True)
os.makedirs(AVATARS_DIR, exist_ok=True)

# 1. Eiffel Tower (Golden glowing architectural icon)
eiffel_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="eiffelGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#eab308" />
      <stop offset="100%" stop-color="#ca8a04" />
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fde047" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#fde047" stop-opacity="0" />
    </radialGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#ca8a04" flood-opacity="0.5"/>
    </filter>
  </defs>
  <circle cx="200" cy="200" r="180" fill="url(#glow)"/>
  <g filter="url(#shadow)" stroke="url(#eiffelGold)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <!-- Spire -->
    <line x1="200" y1="40" x2="200" y2="90" stroke-width="5"/>
    <circle cx="200" cy="38" r="4" fill="#fef08a"/>
    <!-- Top Platform -->
    <rect x="188" y="90" width="24" height="12" rx="3" fill="url(#eiffelGold)" />
    <!-- Section 1 (Top to Mid) -->
    <line x1="192" y1="102" x2="175" y2="175"/>
    <line x1="208" y1="102" x2="225" y2="175"/>
    <!-- Bracing top -->
    <line x1="188" y1="125" x2="212" y2="125"/>
    <line x1="182" y1="150" x2="218" y2="150"/>
    <line x1="188" y1="125" x2="218" y2="150" stroke-width="2"/>
    <line x1="212" y1="125" x2="182" y2="150" stroke-width="2"/>
    <!-- Second Platform -->
    <rect x="160" y="175" width="80" height="18" rx="4" fill="url(#eiffelGold)"/>
    <!-- Section 2 (Mid to Base) -->
    <path d="M 170 193 Q 150 280 115 340" stroke-width="6"/>
    <path d="M 230 193 Q 250 280 285 340" stroke-width="6"/>
    <!-- Center arch -->
    <path d="M 150 340 C 160 265 240 265 250 340" stroke-width="5"/>
    <!-- Cross lattices -->
    <line x1="165" y1="230" x2="235" y2="230"/>
    <line x1="165" y1="230" x2="245" y2="280" stroke-width="2.5"/>
    <line x1="235" y1="230" x2="155" y2="280" stroke-width="2.5"/>
    <line x1="155" y1="280" x2="245" y2="280"/>
    <!-- Base feet -->
    <rect x="100" y="340" width="35" height="12" rx="3" fill="url(#eiffelGold)"/>
    <rect x="265" y="340" width="35" height="12" rx="3" fill="url(#eiffelGold)"/>
  </g>
</svg>"""

# 2. Notre Dame Cathedral (Gothic Rose Window & Towers)
notre_dame_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="stoneGothic" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#93c5fd" />
      <stop offset="50%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1e3a8a" />
    </linearGradient>
    <radialGradient id="roseWindowGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f43f5e" />
      <stop offset="50%" stop-color="#8b5cf6" />
      <stop offset="100%" stop-color="#3b82f6" />
    </radialGradient>
    <filter id="gothicGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#3b82f6" flood-opacity="0.4"/>
    </filter>
  </defs>
  <g filter="url(#gothicGlow)">
    <!-- Main Wall Block -->
    <rect x="100" y="140" width="200" height="210" rx="8" fill="#1e293b" stroke="url(#stoneGothic)" stroke-width="4"/>
    <!-- Left Tower -->
    <rect x="100" y="70" width="60" height="80" rx="6" fill="#0f172a" stroke="url(#stoneGothic)" stroke-width="4"/>
    <path d="M 115 125 L 115 95 C 115 85 145 85 145 95 L 145 125 Z" fill="#3b82f6" opacity="0.3"/>
    <!-- Right Tower -->
    <rect x="240" y="70" width="60" height="80" rx="6" fill="#0f172a" stroke="url(#stoneGothic)" stroke-width="4"/>
    <path d="M 255 125 L 255 95 C 255 85 285 85 285 95 L 285 125 Z" fill="#3b82f6" opacity="0.3"/>
    <!-- Spire center -->
    <path d="M 195 140 L 200 45 L 205 140 Z" fill="#60a5fa"/>
    <!-- Gallery of Kings -->
    <rect x="108" y="152" width="184" height="24" rx="4" fill="#334155"/>
    <circle cx="125" cy="164" r="5" fill="#93c5fd"/>
    <circle cx="150" cy="164" r="5" fill="#93c5fd"/>
    <circle cx="175" cy="164" r="5" fill="#93c5fd"/>
    <circle cx="200" cy="164" r="5" fill="#93c5fd"/>
    <circle cx="225" cy="164" r="5" fill="#93c5fd"/>
    <circle cx="250" cy="164" r="5" fill="#93c5fd"/>
    <circle cx="275" cy="164" r="5" fill="#93c5fd"/>
    <!-- Rose Window -->
    <circle cx="200" cy="225" r="38" fill="url(#roseWindowGlow)" stroke="#f8fafc" stroke-width="4"/>
    <circle cx="200" cy="225" r="26" fill="none" stroke="#f8fafc" stroke-width="2" stroke-dasharray="8 4"/>
    <circle cx="200" cy="225" r="10" fill="#f8fafc"/>
    <!-- Triple Portals -->
    <!-- Left portal -->
    <path d="M 115 350 L 115 305 C 115 285 145 285 145 305 L 145 350 Z" fill="#0f172a" stroke="#60a5fa" stroke-width="3"/>
    <!-- Central portal -->
    <path d="M 175 350 L 175 290 C 175 265 225 265 225 290 L 225 350 Z" fill="#0f172a" stroke="#60a5fa" stroke-width="4"/>
    <!-- Right portal -->
    <path d="M 255 350 L 255 305 C 255 285 285 285 285 305 L 285 350 Z" fill="#0f172a" stroke="#60a5fa" stroke-width="3"/>
  </g>
</svg>"""

# 3. Louvre Glass Pyramid
louvre_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="glassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#0284c7" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.9" />
    </linearGradient>
    <linearGradient id="palaceBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#78350f" />
    </linearGradient>
    <filter id="pyramidGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#38bdf8" flood-opacity="0.5"/>
    </filter>
  </defs>
  <!-- Background historic palace colonnade -->
  <rect x="50" y="160" width="300" height="180" rx="8" fill="#1e1e24" stroke="url(#palaceBg)" stroke-width="3"/>
  <line x1="50" y1="210" x2="350" y2="210" stroke="#d97706" stroke-width="2" opacity="0.6"/>
  <line x1="90" y1="210" x2="90" y2="340" stroke="#d97706" stroke-width="4" opacity="0.5"/>
  <line x1="130" y1="210" x2="130" y2="340" stroke="#d97706" stroke-width="4" opacity="0.5"/>
  <line x1="270" y1="210" x2="270" y2="340" stroke="#d97706" stroke-width="4" opacity="0.5"/>
  <line x1="310" y1="210" x2="310" y2="340" stroke="#d97706" stroke-width="4" opacity="0.5"/>
  <!-- The Famous Glass Pyramid -->
  <g filter="url(#pyramidGlow)">
    <polygon points="200,90 70,340 330,340" fill="url(#glassGrad)" stroke="#7dd3fc" stroke-width="3.5"/>
    <!-- Glass Facet Lines -->
    <line x1="200" y1="90" x2="200" y2="340" stroke="#ffffff" stroke-width="2.5" opacity="0.8"/>
    <line x1="200" y1="90" x2="135" y2="340" stroke="#7dd3fc" stroke-width="2" opacity="0.7"/>
    <line x1="200" y1="90" x2="265" y2="340" stroke="#7dd3fc" stroke-width="2" opacity="0.7"/>
    <!-- Horizontal glass tiers -->
    <line x1="174" y1="140" x2="226" y2="140" stroke="#7dd3fc" stroke-width="2" opacity="0.7"/>
    <line x1="148" y1="190" x2="252" y2="190" stroke="#7dd3fc" stroke-width="2" opacity="0.7"/>
    <line x1="122" y1="240" x2="278" y2="240" stroke="#7dd3fc" stroke-width="2" opacity="0.7"/>
    <line x1="96" y1="290" x2="304" y2="290" stroke="#7dd3fc" stroke-width="2" opacity="0.7"/>
    <!-- Diamond internal braces -->
    <polygon points="200,140 187,165 200,190 213,165" fill="#fef08a" opacity="0.5"/>
    <polygon points="200,190 174,215 200,240 226,215" fill="#fef08a" opacity="0.6"/>
    <polygon points="200,240 161,265 200,290 239,265" fill="#fef08a" opacity="0.7"/>
  </g>
</svg>"""

# 4. Paris Celtic Ancient Boat (Coat of arms of Paris on the Seine)
paris_boat_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a" />
      <stop offset="50%" stop-color="#b91c1c" />
      <stop offset="100%" stop-color="#7f1d1d" />
    </linearGradient>
    <filter id="boatGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="15" flood-color="#f59e0b" flood-opacity="0.4"/>
    </filter>
  </defs>
  <!-- Heraldic Shield -->
  <path d="M 90 70 L 310 70 L 310 230 C 310 320 200 360 200 360 C 200 360 90 320 90 230 Z"
        fill="url(#shieldGrad)" stroke="#f59e0b" stroke-width="6"/>
  <!-- Ancient Silver Galley (Ship of Paris) -->
  <g filter="url(#boatGlow)" fill="#f8fafc" stroke="#f59e0b" stroke-width="3">
    <!-- Waves -->
    <path d="M 110 270 Q 155 250 200 270 T 290 270 L 280 295 Q 200 310 120 295 Z" fill="#38bdf8" stroke="#bae6fd"/>
    <!-- Hull -->
    <path d="M 125 240 C 140 275 260 275 275 240 L 290 200 L 110 200 Z" fill="#ffffff"/>
    <!-- Mast & Sail -->
    <line x1="200" y1="100" x2="200" y2="200" stroke="#f59e0b" stroke-width="5"/>
    <path d="M 200 110 Q 255 140 200 180 Z" fill="#ffffff" stroke="#f59e0b" stroke-width="3"/>
    <path d="M 195 120 Q 145 150 195 180 Z" fill="#f1f5f9" stroke="#f59e0b" stroke-width="2.5"/>
    <!-- Flag -->
    <polygon points="200,100 230,108 200,116" fill="#ef4444"/>
    <!-- Fleur de Lis on top -->
    <circle cx="150" cy="115" r="8" fill="#fbbf24"/>
    <circle cx="200" cy="85" r="6" fill="#fbbf24"/>
    <circle cx="250" cy="115" r="8" fill="#fbbf24"/>
  </g>
</svg>"""

# 5. Gustave Eiffel Avatar Card
eiffel_avatar_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 440" width="340" height="440">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <radialGradient id="faceLight" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#fed7aa" />
      <stop offset="80%" stop-color="#fdba74" />
      <stop offset="100%" stop-color="#fb923c" />
    </radialGradient>
  </defs>
  <!-- Background Card -->
  <rect width="340" height="440" rx="32" fill="url(#cardBg)" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
  <!-- Victorian Oval Frame -->
  <ellipse cx="170" cy="180" rx="100" ry="125" fill="#1e293b" stroke="#eab308" stroke-width="4"/>
  <!-- Shoulders & Suit -->
  <path d="M 85 340 Q 170 300 255 340 L 270 420 L 70 420 Z" fill="#090d16"/>
  <!-- White Collar & Bowtie -->
  <polygon points="170,270 150,290 190,290" fill="#f8fafc"/>
  <polygon points="160,290 180,290 170,305" fill="#b91c1c"/>
  <!-- Head & Ears -->
  <circle cx="112" cy="185" r="16" fill="#fdba74"/>
  <circle cx="228" cy="185" r="16" fill="#fdba74"/>
  <ellipse cx="170" cy="180" rx="58" ry="72" fill="url(#faceLight)"/>
  <!-- Graying Hair -->
  <path d="M 112 165 C 110 110 230 110 228 165 C 215 130 125 130 112 165 Z" fill="#94a3b8"/>
  <!-- Eyes & Eyebrows -->
  <path d="M 135 160 Q 148 156 160 160" stroke="#475569" stroke-width="3" fill="none"/>
  <path d="M 180 160 Q 192 156 205 160" stroke="#475569" stroke-width="3" fill="none"/>
  <circle cx="148" cy="170" r="5" fill="#1e293b"/>
  <circle cx="192" cy="170" r="5" fill="#1e293b"/>
  <!-- Nose -->
  <path d="M 170 168 L 167 195 L 175 195" stroke="#ea580c" stroke-width="2.5" fill="none"/>
  <!-- Distinguished Victorian Beard & Mustache -->
  <path d="M 135 198 Q 170 190 205 198 Q 220 225 200 255 Q 170 270 140 255 Q 120 225 135 198 Z" fill="#cbd5e1"/>
  <!-- Monocle with golden chain -->
  <circle cx="192" cy="170" r="14" fill="none" stroke="#eab308" stroke-width="2.5"/>
  <path d="M 205 174 Q 225 210 215 285" fill="none" stroke="#eab308" stroke-width="1.5" stroke-dasharray="3 2"/>
  <!-- Badge on chest -->
  <circle cx="120" cy="360" r="8" fill="#eab308"/>
</svg>"""

# Save all SVGs
assets = [
    (eiffel_svg, os.path.join(ICONS_DIR, "eiffel.svg")),
    (notre_dame_svg, os.path.join(ICONS_DIR, "notre_dame.svg")),
    (louvre_svg, os.path.join(ICONS_DIR, "louvre.svg")),
    (paris_boat_svg, os.path.join(ICONS_DIR, "paris_boat.svg")),
    (eiffel_avatar_svg, os.path.join(AVATARS_DIR, "eiffel_person.svg")),
]

for content, path in assets:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {path}")

print("All Paris assets generated successfully!")
