# Generates parts/packs.svg: realistic, brand-free kirana packshots as SVG <symbol>s (viewBox 0 0 100 120).
# Brands are invented for the demo (Gehu Gold, Dudhwala, Suraj, Cruncho, Chai Shakti, Ujla...).

def zz(x0, x1, y, h=2.2, up=True):
    n = max(4, int((x1 - x0) / 3)); s = (x1 - x0) / n; d = -h if up else h
    p = [f"L{x0} {y}"]
    for k in range(n):
        p.append(f"L{x0+s*(k+.5):.1f} {y+d:.1f} L{x0+s*(k+1):.1f} {y}")
    return " ".join(p)

def crimp_rect(x0, x1, y0, y1, top=True, bottom=False):
    """closed path for a band with zigzag top (and optionally bottom)."""
    t = zz(x0, x1, y0) if top else f"L{x0} {y0} L{x1} {y0}"
    b = zz(x1, x0, y1, up=False).replace(f"L{x1} {y1}", f"L{x1} {y1}", 1) if bottom else f"L{x1} {y1} L{x0} {y1}"
    if bottom:
        n = max(4, int((x1 - x0) / 3)); s = (x1 - x0) / n
        b = f"L{x1} {y1} " + " ".join(f"L{x1-s*(k+.5):.1f} {y1+2.2:.1f} L{x1-s*(k+1):.1f} {y1}" for k in range(n))
    return f"M{x0} {y1} " + t[1:].replace("L", "L", 1).join(["", ""]) if False else f"M{x0} {y1} {t} {b} Z"

GROUND = '<ellipse cx="50" cy="112" rx="{rx}" ry="3.6" fill="url(#pk-ground)"/>'
F = 'font-family="Brico,Onest,sans-serif"'
O = 'font-family="Onest,sans-serif"'

defs = '''
<radialGradient id="pk-ground"><stop offset="0" stop-color="#000" stop-opacity=".30"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<linearGradient id="pk-sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".42"/><stop offset=".16" stop-color="#fff" stop-opacity=".06"/><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset=".9" stop-color="#000" stop-opacity=".16"/><stop offset="1" stop-color="#000" stop-opacity=".30"/></linearGradient>
<linearGradient id="pk-shv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".25" stop-color="#fff" stop-opacity="0"/><stop offset=".85" stop-color="#000" stop-opacity=".04"/><stop offset="1" stop-color="#000" stop-opacity=".16"/></linearGradient>
<radialGradient id="pk-pillow" cx=".38" cy=".38" r=".75"><stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/><stop offset=".85" stop-color="#000" stop-opacity=".10"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></radialGradient>
<linearGradient id="pk-gloss" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<pattern id="pt-dal" width="6" height="5" patternUnits="userSpaceOnUse"><rect width="6" height="5" fill="#F4C02E"/><circle cx="1.6" cy="1.4" r="1.45" fill="#F8D45A"/><circle cx="4.6" cy="3.6" r="1.45" fill="#E9AC12"/><circle cx="4.4" cy="1" r=".9" fill="#FBE08A"/></pattern>
<pattern id="pt-chana" width="6" height="5" patternUnits="userSpaceOnUse"><rect width="6" height="5" fill="#E2A53A"/><circle cx="1.6" cy="1.4" r="1.5" fill="#EDBE5C"/><circle cx="4.6" cy="3.6" r="1.5" fill="#D18F22"/><circle cx="4.4" cy="1" r=".8" fill="#F5D287"/></pattern>
<pattern id="pt-sugar" width="5" height="5" patternUnits="userSpaceOnUse"><rect width="5" height="5" fill="#F3F2EE"/><rect x=".6" y=".6" width="1.7" height="1.7" fill="#fff" transform="rotate(15 1.4 1.4)"/><rect x="2.8" y="2.7" width="1.6" height="1.6" fill="#DCDAD3" transform="rotate(-20 3.6 3.5)"/></pattern>
<pattern id="pt-rice" width="7" height="5" patternUnits="userSpaceOnUse"><rect width="7" height="5" fill="#EFE9DA"/><ellipse cx="2" cy="1.5" rx="1.9" ry=".7" fill="#fff" transform="rotate(25 2 1.5)"/><ellipse cx="5.2" cy="3.6" rx="1.9" ry=".7" fill="#FBF8F0" transform="rotate(-30 5.2 3.6)"/></pattern>
'''

S = {}

# ---------- big bag (atta / rice), parametric ----------
def bag(id, top, body, body2, ink, brand, line1, line2, kg, art):
    body_path = "M25 16 L75 16 Q79 60 80 104 Q80 110 74 110 L26 110 Q20 110 20 104 Q21 60 25 16 Z"
    return f'''
{GROUND.format(rx=32)}
<defs><clipPath id="c-{id}"><path d="{body_path}"/></clipPath>
<linearGradient id="g-{id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{body}"/><stop offset="1" stop-color="{body2}"/></linearGradient></defs>
<path d="{body_path}" fill="{top}"/>
<g clip-path="url(#c-{id})">
  <path d="M10 58 Q35 48 55 56 T92 52 L92 120 L10 120 Z" fill="url(#g-{id})"/>
  {art}
  <rect x="10" y="10" width="90" height="8" fill="{ink}" opacity=".9"/>
</g>
<path d="M24.5 18 {zz(24.5,75.5,10)[1:]} L75.5 18 Z" fill="{ink}"/>
<text x="50" y="33" text-anchor="middle" {F} font-weight="800" font-size="10" fill="{ink}" letter-spacing="-.3">{brand}</text>
<text x="50" y="41.5" text-anchor="middle" {O} font-weight="600" font-size="3.7" fill="{ink}" opacity=".75" letter-spacing=".4">{line1}</text>
<text x="50" y="68" text-anchor="middle" {O} font-weight="700" font-size="5" fill="#fff" opacity=".9" letter-spacing=".6">{line2.split("|")[0]}</text><text x="50" y="81" text-anchor="middle" {F} font-weight="800" font-size="12.5" fill="#fff" letter-spacing="-.4">{line2.split("|")[1]}</text>
<circle cx="66" cy="98" r="8" fill="#fff"/><text x="66" y="100.4" text-anchor="middle" {F} font-weight="800" font-size="7" fill="{ink}">{kg}</text>
<path d="{body_path}" fill="url(#pk-sh)"/><path d="{body_path}" fill="url(#pk-shv)"/>
'''

wheat = '<g transform="translate(32 102) scale(.8)" fill="#FFE29A">' + "".join(
    f'<ellipse cx="{3*(k%2)-1.5}" cy="{-k*3.2}" rx="1.6" ry="3" transform="rotate({35 if k%2 else -35} {3*(k%2)-1.5} {-k*3.2})"/>' for k in range(6)) + '<path d="M0 6 V-18" stroke="#FFE29A" stroke-width=".9"/></g>'
grains = '<g transform="translate(30 98) scale(.8)">' + "".join(
    f'<ellipse cx="{x}" cy="{y}" rx="2.6" ry="1" fill="#fff" transform="rotate({r} {x} {y})"/>' for x, y, r in [(0,0,20),(5,2,-25),(2,6,40),(8,7,10),(-3,5,-15),(6,-4,30)]) + '</g>'
S["atta"] = bag("atta", "#FFF4DC", "#F28A1E", "#D9530F", "#7A2A0C", "GEHU GOLD", "CHAKKI FRESH · 100% WHEAT", "WHOLE WHEAT|Atta", "5kg", wheat)
S["rice"] = bag("rice", "#F2F7EC", "#1F8E4D", "#0E5C31", "#0D4426", "Dhaanya", "AGED 12 MONTHS", "SONA MASOORI|Rice", "5kg", grains)

# ---------- clear pouch (dal / sugar / poha) ----------
def pouch(id, fill, band, ink, name, sub, wt):
    p = "M28 16 L72 16 L74 106 Q74 110 70 110 L30 110 Q26 110 26 106 Z"
    return f'''
{GROUND.format(rx=26)}
<path d="{p}" fill="{fill}"/>
<path d="M27.5 18 {zz(27.5,72.5,10)[1:]} L72.5 18 Z" fill="#E9E6DD" opacity=".95"/>
<rect x="27.5" y="17" width="45" height="2" fill="#fff" opacity=".6"/>
<rect x="33" y="48" width="34" height="44" rx="5" fill="#fff"/>
<path d="M33 53 a5 5 0 0 1 5 -5 h24 a5 5 0 0 1 5 5 v6 h-34 Z" fill="{band}"/>
<text x="50" y="56.4" text-anchor="middle" {O} font-weight="700" font-size="3.8" fill="#fff" letter-spacing=".4">{sub}</text>
<text x="50" y="72" text-anchor="middle" {F} font-weight="800" font-size="9" fill="{ink}" letter-spacing="-.3">{name}</text>
<text x="50" y="84" text-anchor="middle" {O} font-weight="700" font-size="6" fill="{ink}" opacity=".7">{wt}</text>
<path d="{p}" fill="url(#pk-sh)"/>
<rect x="31" y="22" width="5" height="84" fill="url(#pk-gloss)" opacity=".8"/>
<path d="{p}" fill="none" stroke="#000" stroke-opacity=".08" stroke-width=".6"/>
'''
S["dal"] = pouch("dal", "url(#pt-dal)", "#14853F", "#14532D", "Toor Dal", "UNPOLISHED", "1 kg")
S["chana"] = pouch("chana", "url(#pt-chana)", "#B5481B", "#5A2A0B", "Chana Dal", "PREMIUM", "1 kg")
S["sugar"] = pouch("sugar", "url(#pt-sugar)", "#E2336B", "#7A1236", "Sugar", "FINE GRAIN", "1 kg")
S["poha"] = pouch("poha", "url(#pt-rice)", "#E07A12", "#6B3407", "Poha", "INDORI", "500 g")

# ---------- milk pouch ----------
mp = "M27 22 Q50 16 73 22 Q77 62 74 102 Q50 108 26 102 Q23 62 27 22 Z"
S["milk"] = f'''
{GROUND.format(rx=28)}
<defs><clipPath id="c-milk"><path d="{mp}"/></clipPath></defs>
<path d="{mp}" fill="#F7F9FC"/>
<g clip-path="url(#c-milk)">
  <path d="M10 10 H90 V52 Q70 60 50 54 T10 56 Z" fill="#1D5BD6"/>
  <path d="M10 56 Q30 50 50 56 T90 52 V58 Q70 64 50 60 T10 62 Z" fill="#8DB4FF"/>
  <rect x="10" y="96" width="90" height="20" fill="#1D5BD6"/>
</g>
<path d="M27 22 Q50 16 73 22 L73 25 Q50 19 27 25 Z" fill="#fff" opacity=".7"/>
<text x="50" y="38" text-anchor="middle" {F} font-weight="800" font-size="9" fill="#fff" letter-spacing="-.3">Dudhwala</text>
<text x="50" y="46" text-anchor="middle" {O} font-weight="600" font-size="3.6" fill="#CFE0FF" letter-spacing=".4">FARM FRESH · PUNE</text>
<text x="50" y="76" text-anchor="middle" {F} font-weight="800" font-size="8.4" fill="#1D3E8F" letter-spacing="-.2">Toned Milk</text>
<text x="50" y="86" text-anchor="middle" {O} font-weight="700" font-size="6" fill="#1D3E8F" opacity=".75">500 ml</text>
<path d="{mp}" fill="url(#pk-pillow)"/>
'''

# ---------- oil bottle ----------
ob = "M42 26 L58 26 Q60 34 70 38 Q76 41 76 50 L76 104 Q76 110 70 110 L30 110 Q24 110 24 104 L24 50 Q24 41 30 38 Q40 34 42 26 Z"
S["oil"] = f'''
{GROUND.format(rx=28)}
<defs><linearGradient id="g-oil" x1="0" x2="1"><stop offset="0" stop-color="#FFD84A"/><stop offset=".5" stop-color="#F6B714"/><stop offset="1" stop-color="#D98A00"/></linearGradient></defs>
<rect x="40" y="10" width="20" height="14" rx="2.5" fill="#1C7A3A"/>
<rect x="40" y="10" width="20" height="14" rx="2.5" fill="url(#pk-sh)"/>
<rect x="38.5" y="22" width="23" height="5" rx="1.5" fill="#15652F"/>
<path d="{ob}" fill="url(#g-oil)"/>
<rect x="24" y="56" width="52" height="38" fill="#fff"/>
<rect x="24" y="56" width="52" height="6" fill="#1C7A3A"/>
<g transform="translate(37 76)">{"".join(f'<ellipse cx="0" cy="-5.2" rx="2" ry="3.6" fill="#FFB800" transform="rotate({a})"/>' for a in range(0,360,30))}<circle r="3.6" fill="#7A4A12"/></g>
<text x="62" y="74" text-anchor="middle" {F} font-weight="800" font-size="8.5" fill="#14532D">Suraj</text>
<text x="62" y="81" text-anchor="middle" {O} font-weight="700" font-size="4.3" fill="#14532D" letter-spacing=".3">SUNFLOWER</text>
<text x="62" y="88.5" text-anchor="middle" {O} font-weight="700" font-size="5.2" fill="#14532D" opacity=".7">1 L</text>
<text x="50" y="60.4" text-anchor="middle" {O} font-weight="700" font-size="3.6" fill="#fff" letter-spacing=".8">REFINED OIL</text>
<path d="{ob}" fill="url(#pk-sh)"/>
<rect x="28" y="40" width="4" height="66" rx="2" fill="#fff" opacity=".45"/>
'''

# ---------- chips pillow pack ----------
cp = "M22 22 L78 22 Q83 64 78 104 L22 104 Q17 64 22 22 Z"
chip = lambda x, y, r, s: f'<ellipse cx="{x}" cy="{y}" rx="{9*s}" ry="{6.5*s}" fill="#F7C548" transform="rotate({r} {x} {y})"/><ellipse cx="{x}" cy="{y}" rx="{9*s}" ry="{6.5*s}" fill="none" stroke="#D99A1C" stroke-width=".8" transform="rotate({r} {x} {y})"/><circle cx="{x-2}" cy="{y-1}" r=".9" fill="#C0491A"/><circle cx="{x+3}" cy="{y+1.5}" r=".8" fill="#C0491A"/>'
S["chips"] = f'''
{GROUND.format(rx=32)}
<defs><linearGradient id="g-chips" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2BB46A"/><stop offset="1" stop-color="#0B6B3A"/></linearGradient><clipPath id="c-chips"><path d="{cp}"/></clipPath></defs>
<path d="{cp}" fill="url(#g-chips)"/>
<path d="M21.5 24 {zz(21.5,78.5,16)[1:]} L78.5 24 Z" fill="#0F7A42"/>
<path d="M21.5 102 L78.5 102 {zz(78.5,21.5,110,up=False)[1:]} Z" fill="#0F7A42"/>
<g clip-path="url(#c-chips)">
  <path d="M10 42 L90 30 L90 52 L10 64 Z" fill="#FFD23F"/>
  {chip(40,84,-20,1.1)}{chip(58,88,15,1.15)}{chip(50,76,5,1)}
</g>
<text x="50" y="52" text-anchor="middle" {F} font-weight="800" font-size="12.5" fill="#0B4D2A" letter-spacing="-.5" transform="rotate(-8 50 50)">Cruncho</text>
<text x="50" y="66" text-anchor="middle" {O} font-weight="700" font-size="5.6" fill="#fff" letter-spacing=".4">MASALA MUNCH</text>
<path d="{cp}" fill="url(#pk-pillow)"/>
'''

# ---------- biscuits (flow wrap, slightly tilted) ----------
bw = "M14 46 L86 38 L88 74 L16 82 Z"
S["biscuit"] = f'''
{GROUND.format(rx=36)}
<defs><linearGradient id="g-bis" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD84D"/><stop offset="1" stop-color="#F2AE12"/></linearGradient></defs>
<g transform="translate(0 18)">
<path d="{bw}" fill="url(#g-bis)"/>
<path d="M14 46 L10 44 L12 48 L9 51 L12 54 L9 58 L12 62 L9 66 L12 70 L9 74 L12 78 L13 82 L16 82 Z" fill="#E9A10C"/>
<path d="M86 38 L90 36 L88 40 L91 44 L88 48 L91 52 L88 56 L91 60 L88 64 L91 68 L88 72 L91 75 L88 74 Z" fill="#D99208"/>
<path d="M15 64 L87 56 L87.6 66 L15.6 74 Z" fill="#D7261E"/>
<text x="50" y="66" text-anchor="middle" {F} font-weight="800" font-size="7" fill="#fff" transform="rotate(-6.3 50 66)">Glucose+ Biscuits</text>
<text x="34" y="56" text-anchor="middle" {F} font-weight="800" font-size="9" fill="#9A1C14" transform="rotate(-6.3 34 56)">Bachpan</text>
<g transform="rotate(-6.3 70 50)"><circle cx="68" cy="50" r="7" fill="#E1A04A"/><circle cx="68" cy="50" r="7" fill="none" stroke="#B87424" stroke-width=".8"/>{"".join(f'<circle cx="{68+dx}" cy="{50+dy}" r=".7" fill="#A8641C"/>' for dx,dy in [(-3,-2),(0,-3),(3,-1),(-2,2),(2,3)])}</g>
<path d="{bw}" fill="url(#pk-shv)"/>
<path d="M14 46 L86 38 L86.3 42 L14.3 50 Z" fill="#fff" opacity=".35"/>
</g>
'''

# ---------- tea box (3D carton) ----------
S["tea"] = f'''
{GROUND.format(rx=30)}
<defs><linearGradient id="g-tea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#A3231F"/><stop offset="1" stop-color="#6E1210"/></linearGradient></defs>
<path d="M24 26 L66 26 L80 18 L38 18 Z" fill="#C2413A"/>
<path d="M66 26 L80 18 L80 100 L66 108 Z" fill="#5A0E0C"/>
<rect x="24" y="26" width="42" height="82" fill="url(#g-tea)"/>
<rect x="27" y="30" width="36" height="74" rx="2" fill="none" stroke="#E8B84A" stroke-width=".7"/>
<text x="45" y="44" text-anchor="middle" {F} font-weight="800" font-size="7.6" fill="#F7D27A" letter-spacing="-.2">Chai</text>
<text x="45" y="53" text-anchor="middle" {F} font-weight="800" font-size="7.6" fill="#F7D27A" letter-spacing="-.2">Shakti</text>
<path d="M36 72 h18 v4 a9 9 0 0 1 -18 0 Z" fill="#fff"/><path d="M54 74 a3 3 0 0 1 0 6" fill="none" stroke="#fff" stroke-width="1.6"/>
<path d="M40 70 q2 -4 0 -7 M45 70 q2 -4 0 -7 M50 70 q2 -4 0 -7" stroke="#F7D27A" stroke-width=".9" fill="none" stroke-linecap="round"/>
<text x="45" y="96" text-anchor="middle" {O} font-weight="700" font-size="3.7" fill="#fff" letter-spacing=".3">STRONG · 250 g</text>
<rect x="24" y="26" width="42" height="82" fill="url(#pk-sh)" opacity=".7"/>
'''

# ---------- ghee jar ----------
S["ghee"] = f'''
{GROUND.format(rx=30)}
<defs><linearGradient id="g-ghee" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE38A"/><stop offset="1" stop-color="#EDB52C"/></linearGradient>
<linearGradient id="g-lid" x1="0" x2="1"><stop offset="0" stop-color="#F6D27A"/><stop offset=".45" stop-color="#C9932C"/><stop offset="1" stop-color="#8C5F14"/></linearGradient></defs>
<rect x="24" y="34" width="52" height="76" rx="10" fill="url(#g-ghee)"/>
<rect x="27" y="20" width="46" height="16" rx="3" fill="url(#g-lid)"/>
{"".join(f'<rect x="{29+k*3}" y="22" width="1" height="12" fill="#000" opacity=".12"/>' for k in range(14))}
<rect x="24" y="54" width="52" height="38" fill="#fff"/>
<rect x="24" y="54" width="52" height="5" fill="#B3261E"/><rect x="24" y="87" width="52" height="5" fill="#B3261E"/>
<text x="50" y="72" text-anchor="middle" {F} font-weight="800" font-size="8" fill="#7A1A12" letter-spacing="-.3">Gaon Ghee</text>
<text x="50" y="80" text-anchor="middle" {O} font-weight="700" font-size="3.7" fill="#7A1A12" opacity=".8" letter-spacing=".3">PURE COW · 500 ml</text>
<rect x="24" y="34" width="52" height="76" rx="10" fill="url(#pk-sh)"/>
<rect x="29" y="38" width="4" height="66" rx="2" fill="#fff" opacity=".5"/>
'''

# ---------- bread ----------
br = "M22 46 Q22 22 50 22 Q78 22 78 46 L78 104 Q78 110 72 110 L28 110 Q22 110 22 104 Z"
S["bread"] = f'''
{GROUND.format(rx=30)}
<defs><linearGradient id="g-br" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9A5524"/><stop offset=".35" stop-color="#C98446"/><stop offset="1" stop-color="#B26D33"/></linearGradient></defs>
<path d="{br}" fill="url(#g-br)"/>
<rect x="22" y="58" width="56" height="26" fill="#fff"/>
<rect x="22" y="58" width="56" height="4" fill="#C2271E"/>
<text x="50" y="73" text-anchor="middle" {F} font-weight="800" font-size="7.4" fill="#7A1A12" letter-spacing="-.3">Brown Bread</text>
<text x="50" y="80" text-anchor="middle" {O} font-weight="700" font-size="3.6" fill="#7A1A12" opacity=".75" letter-spacing=".3">100% ATTA · 400 g</text>
<path d="{br}" fill="url(#pk-sh)"/>
<path d="{br}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="1.2"/>
<rect x="27" y="34" width="4" height="70" rx="2" fill="#fff" opacity=".35"/>
'''

# ---------- curd cup ----------
S["curd"] = f'''
{GROUND.format(rx=30)}
<path d="M22 40 L78 40 L72 106 Q50 112 28 106 Z" fill="#fff"/>
<path d="M23.2 54 L76.8 54 L75.7 66 L24.3 66 Z" fill="#1D5BD6"/>
<ellipse cx="50" cy="40" rx="28" ry="8" fill="#C9D6EA"/>
<ellipse cx="50" cy="38.5" rx="28" ry="8" fill="#E7EEF8"/>
<ellipse cx="50" cy="38.5" rx="20" ry="5" fill="none" stroke="#1D5BD6" stroke-width=".8" opacity=".5"/>
<text x="50" y="62.5" text-anchor="middle" {O} font-weight="700" font-size="5.2" fill="#fff" letter-spacing=".8">DUDHWALA</text>
<text x="50" y="84" text-anchor="middle" {F} font-weight="800" font-size="12" fill="#1D3E8F" letter-spacing="-.4">Dahi</text>
<text x="50" y="94" text-anchor="middle" {O} font-weight="700" font-size="5.4" fill="#1D3E8F" opacity=".7">400 g</text>
<path d="M22 40 L78 40 L72 106 Q50 112 28 106 Z" fill="url(#pk-sh)"/>
'''

# ---------- paneer ----------
S["paneer"] = f'''
{GROUND.format(rx=36)}
<rect x="14" y="44" width="72" height="56" rx="9" fill="#DCE6F2"/>
<rect x="19" y="49" width="62" height="46" rx="6" fill="#FBFAF4"/>
{"".join(f'<circle cx="{x}" cy="{y}" r=".9" fill="#E8E4D4"/>' for x,y in [(26,56),(40,62),(58,54),(70,66),(34,86),(64,88),(48,78),(74,82)])}
<rect x="28" y="60" width="44" height="24" rx="4" fill="#1D5BD6"/>
<text x="50" y="72" text-anchor="middle" {F} font-weight="800" font-size="6.6" fill="#fff" letter-spacing="-.2">Malai Paneer</text>
<text x="50" y="79.5" text-anchor="middle" {O} font-weight="700" font-size="4.6" fill="#CFE0FF">200 g</text>
<rect x="14" y="44" width="72" height="56" rx="9" fill="url(#pk-shv)"/>
<path d="M18 48 L50 48" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".8"/>
'''

# ---------- detergent stand-up pouch ----------
dp = "M24 18 L76 18 L78 100 Q78 110 68 110 L32 110 Q22 110 22 100 Z"
S["detergent"] = f'''
{GROUND.format(rx=30)}
<defs><linearGradient id="g-det" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2F86FF"/><stop offset="1" stop-color="#0A3FA8"/></linearGradient><clipPath id="c-det"><path d="{dp}"/></clipPath></defs>
<path d="{dp}" fill="url(#g-det)"/>
<path d="M23.5 20 {zz(23.5,76.5,12)[1:]} L76.5 20 Z" fill="#0A3FA8"/>
<g clip-path="url(#c-det)"><circle cx="50" cy="86" r="26" fill="#fff" opacity=".14"/><circle cx="50" cy="86" r="17" fill="#fff" opacity=".18"/>
<path d="M10 100 Q30 92 50 98 T92 94 L92 120 L10 120 Z" fill="#FFD23F"/></g>
<text x="50" y="44" text-anchor="middle" {F} font-weight="800" font-size="15" fill="#fff" letter-spacing="-.6">Ujla</text>
<text x="50" y="53" text-anchor="middle" {O} font-weight="700" font-size="5" fill="#CFE0FF" letter-spacing=".8">MATIC POWDER</text>
<path d="M66 30 l1.4 3.6 3.6 1.4 -3.6 1.4 -1.4 3.6 -1.4 -3.6 -3.6 -1.4 3.6 -1.4Z" fill="#FFE47A"/>
<text x="50" y="107" text-anchor="middle" {O} font-weight="800" font-size="6" fill="#0A3FA8">1 kg</text>
<path d="{dp}" fill="url(#pk-sh)"/>
'''

# ---------- noodles ----------
S["noodles"] = f'''
{GROUND.format(rx=34)}
<defs><linearGradient id="g-nd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF8A2A"/><stop offset="1" stop-color="#E25A0C"/></linearGradient></defs>
<path d="M16 42 L84 42 L86 98 L14 98 Z" fill="url(#g-nd)"/>
<path d="M16 42 {zz(16,84,42)[1:]} Z" fill="#C24A08"/>
<path d="M14 98 L86 98 {zz(86,14,98,up=False)[1:]} Z" fill="#C24A08"/>
<text x="50" y="58" text-anchor="middle" {F} font-weight="800" font-size="11" fill="#fff" letter-spacing="-.4">Zaika</text>
<text x="50" y="65" text-anchor="middle" {O} font-weight="700" font-size="3.9" fill="#FFE2C8" letter-spacing=".4">MASALA NOODLES</text>
<path d="M32 76 h36 a18 10 0 0 1 -36 0 Z" fill="#fff"/>
<path d="M36 76 q4 -6 8 0 t8 0 t8 0 t8 0" fill="none" stroke="#F7C548" stroke-width="2" stroke-linecap="round"/>
<circle cx="44" cy="74" r="1.6" fill="#3E9C47"/><circle cx="57" cy="73" r="1.4" fill="#D7261E"/>
<path d="M16 42 L84 42 L86 98 L14 98 Z" fill="url(#pk-shv)"/>
<path d="M16 42 L84 42 L86 98 L14 98 Z" fill="url(#pk-sh)" opacity=".7"/>
'''

# ---------- eggs (6 in tray) ----------
egg = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="9" ry="10.5" fill="url(#g-egg)"/><ellipse cx="{x-3}" cy="{y-4}" rx="2.4" ry="3.2" fill="#fff" opacity=".55"/>'
S["eggs"] = f'''
{GROUND.format(rx=38)}
<defs><radialGradient id="g-egg" cx=".38" cy=".32" r=".8"><stop offset="0" stop-color="#FFF6EA"/><stop offset=".55" stop-color="#F1D3AE"/><stop offset="1" stop-color="#C9945E"/></radialGradient></defs>
<path d="M10 70 L90 70 L86 104 Q50 110 14 104 Z" fill="#B9C3CF"/>
<path d="M10 70 L90 70 L86 104 Q50 110 14 104 Z" fill="url(#pk-sh)"/>
{egg(28,58)}{egg(50,56)}{egg(72,58)}
<path d="M8 66 Q20 74 28 68 Q39 76 50 68 Q61 76 72 68 Q80 74 92 66 L92 74 L8 74 Z" fill="#CDD5DF"/>
{egg(30,74)}{egg(50,76)}{egg(70,74)}
<path d="M6 80 Q18 90 30 84 Q40 92 50 86 Q60 92 70 84 Q82 90 94 80 L90 96 Q50 104 10 96 Z" fill="#D9E0E8"/>
<rect x="31" y="88" width="38" height="9" rx="2" fill="#E07A12"/>
<text x="50" y="95" text-anchor="middle" {O} font-weight="800" font-size="4.2" fill="#fff" letter-spacing=".3">FARM EGGS · 6</text>
'''

out = ['<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>', defs]
for k, v in S.items():
    out.append(f'<symbol id="pk-{k}" viewBox="0 0 100 120">{v}</symbol>')
out.append('</defs></svg>')
open('parts/packs.svg', 'w').write("\n".join(out))

# contact sheet for review
cells = "".join(f'<div class="c"><svg viewBox="0 0 100 120"><use href="#pk-{k}"/></svg><span>{k}</span></div>' for k in S)
open('/tmp/claude-0/-home-user-team/6058c3e9-0250-52ec-82b0-061138e3122a/scratchpad/packs_sheet.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Onest;font-weight:600;src:url(/home/user/team/design/kirana-app/src/fonts/onest-latin-600-normal.woff2)}}
@font-face{{font-family:Onest;font-weight:700;src:url(/home/user/team/design/kirana-app/src/fonts/onest-latin-700-normal.woff2)}}
@font-face{{font-family:Onest;font-weight:800;src:url(/home/user/team/design/kirana-app/src/fonts/onest-latin-800-normal.woff2)}}
@font-face{{font-family:Brico;font-weight:800;src:url(/home/user/team/design/kirana-app/src/fonts/bricolage-grotesque-latin-800-normal.woff2)}}
body{{margin:0;font-family:Onest;background:#fff;display:flex;flex-wrap:wrap;gap:10px;padding:12px;width:390px}}
.c{{width:118px;height:150px;background:#F6F6F8;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center}}
.c svg{{width:100px;height:120px}}span{{font-size:10px;color:#888}}</style></head><body>{"".join(out)}{cells}</body></html>''')
print(len(S), "packs")
