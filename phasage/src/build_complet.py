"""Plan de phasage complet, option R — Hôpital de Chandler R-657-24.

Neuf planches tabloïd paysage : vue d'ensemble et calendrier ; phases reportées
sur les quatre élévations ; une planche par phase (plan d'implantation avec les
éléments de chantier, plan clé, murs travaillés avec leurs appareils, verrous,
coupures, PCI) ; calendrier et décisions.

Usage : python3 src/build_complet.py [--out phasage/plan-phasage-complet.pdf]
Règles : aucun texte sous 9 pt (12 px à 96 px/po) ; [lecture] = lu sur un plan,
[choix] = proposé par GLCRM, [à confirmer] = non fixé par les documents.
"""
import sys, re, json, pathlib, subprocess, datetime as dt
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_elevations as BE
import elev_geom as G, elev_data as E, complet_data as C, complet_textes as T, zones as Z

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'; BUILD.mkdir(exist_ok=True)
BOT = 1002
box, table, rich, esc = BE.box, BE.table, BE.rich, BE.esc
D5I = BE.D5I
MES = {}            # hauteurs mesurées au premier passage {id: px}

def hr(t):
    """Texte déjà en HTML : seuls les marqueurs `…` sont convertis."""
    return re.sub(r'`([^`]+)`', r'<span class="mk">\1</span>', t)

def svgtxt(x, y, s, size, anchor='start', weight='normal', fill='#111'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" style="font-size:{size:.2f}px;font-weight:{weight};fill:{fill}">{esc(s)}</text>'

def header(num, total, titre, sous):
    return (f'<div class="hdr"><div class="h1">Planche {num} / {total} — {esc(titre)}</div><div class="h2">{rich(sous)}</div>'
            f'<div class="proj">Hôpital de Chandler — Réfection de l\'enveloppe · CISSS de la Gaspésie · AOC-077221 · GLCRM R-657-24<br>'
            f'Plan de phasage complet, option R — document de travail ; dates [choix] à confirmer</div></div>')

def footer(num, total, sources):
    return (f'<div class="ftr"><div><b>Sources :</b> {rich(sources)}</div>'
            f'<div><b>Conventions :</b> [lecture] lu sur un plan ; [choix] proposé par GLCRM ; [à confirmer] non fixé par les documents ; '
            f'N-F-V-005 : ligne du tableau de WSP ; AR-, ME-, ST-, CI- : registre analyse/02-contraintes.md ; C-, Z- : contradictions et zones d\'ombre.</div>'
            f'<span class="pg">page {num} / {total}</span></div>')

def badge(x, y, s, col, k, size=12):
    w = (7.2 * len(s) + 10) / k; h = 18 / k
    return (f'<rect x="{x - w/2:.1f}" y="{y - h/2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{3/k:.1f}" fill="{col}" stroke="#fff" stroke-width="{1/k:.2f}"/>'
            + svgtxt(x, y + 4.6 / k, s, size / k, 'middle', 'bold', '#fff'))

# ------------------------------------------------------------------ plan clé
POS_PH = {'1': (720, 400), '2.N': (459, 374), '2.S': (459, 494), '2.O': (292, 432), '2.E': (628, 440),
          '3.N': (330, 305), '3.S': (418, 566), '3.O': (205, 500)}
def plan_cle(width, actifs=None, phases=None):
    vb = (30, 85, 1000, 540); k = width / vb[2]; h = round(width * vb[3] / vb[2])
    s = [f'<svg viewBox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}" width="{width}" height="{h}" xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:0;top:0">',
         '<image href="../img/A010_plan_cle.png" x="0" y="0" width="1057" height="946"/>',
         f'<rect x="30" y="625" width="1000" height="20" fill="#fff"/>']
    if actifs:
        for lettre, (poly, *_r) in Z.ZONES.items():
            if lettre not in actifs:
                pts = ' '.join(f'{x},{y}' for x, y in poly)
                s.append(f'<polygon points="{pts}" fill="#fff" opacity="0.72"/>')
    for ph, (x, y) in POS_PH.items():
        if phases is None or ph in phases:
            s.append(badge(x, y, ph, C.COUL[C.famille(ph)], k))
    s.append('</svg>')
    return ''.join(s), h

# ------------------------------------------------------------------ plan d'implantation
def site(width, cle):
    k = width / 1900; h = round(width * 840 / 1900)
    s = [f'<svg viewBox="0 0 1900 840" width="{width}" height="{h}" xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:0;top:0">',
         '<defs><pattern id="hb" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         '<line x1="0" y1="0" x2="0" y2="14" stroke="#795548" stroke-width="5" opacity="0.45"/></pattern>'
         '<marker id="fl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
         '<path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs>',
         '<image href="../img/A001_chantier.png" x="0" y="0" width="1900" height="840"/>']
    legende, n = [], 0
    for el in C.SITE[cle]:
        typ, geo, col, *rest = el
        lab = rest[-1] if rest else ''
        if typ == 'zone' or typ == 'bande':
            pts = ' '.join(f'{x},{y}' for x, y in geo)
            if typ == 'bande':
                s.append(f'<polygon points="{pts}" fill="{col}" opacity="0.55" stroke="{col}" stroke-width="3"/>')
            else:
                fill = 'url(#hb)' if rest[0] == 'hachure' else 'none'
                s.append(f'<polygon points="{pts}" fill="{fill}" stroke="{col}" stroke-width="4" stroke-dasharray="{"" if rest[0] != "trait" else "12,7"}"/>')
            cx = sum(x for x, y in geo) / len(geo); cy = sum(y for x, y in geo) / len(geo)
        elif typ == 'rect':
            x0, y0, x1, y1 = geo; style = rest[0]
            if style == 'plein':
                s.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="{col}" opacity="0.6" stroke="{col}" stroke-width="3"/>')
            else:
                s.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="none" stroke="{col}" stroke-width="5" stroke-dasharray="{"14,8" if style == "tirets" else ""}"/>')
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        elif typ == 'fleche':
            x0, y0, x1, y1 = geo
            s.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{col}" stroke-width="7" marker-end="url(#fl)"/>')
            cx, cy = x0, y0
        elif typ == 'ligne':
            pts = ' '.join(f'{x},{y}' for x, y in geo)
            s.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="6" stroke-dasharray="10,6"/>')
            cx, cy = geo[0]
        elif typ == 'point':
            cx, cy = geo
            s.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="{col}" stroke="#fff" stroke-width="3"/>')
        elif typ == 'croix':
            cx, cy = geo; d = 16
            s.append(f'<line x1="{cx-d}" y1="{cy-d}" x2="{cx+d}" y2="{cy+d}" stroke="{col}" stroke-width="7"/>'
                     f'<line x1="{cx-d}" y1="{cy+d}" x2="{cx+d}" y2="{cy-d}" stroke="{col}" stroke-width="7"/>')
        if lab:
            n += 1
            bx = min(max(cx, 20 / k), 1900 - 20 / k); by = min(max(cy - 26, 14 / k), 840 - 14 / k)
            s.append(f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="{10.5/k:.1f}" fill="#111" stroke="#fff" stroke-width="{1.5/k:.1f}"/>'
                     + svgtxt(bx, by + 4.4 / k, str(n), 12 / k, 'middle', 'bold', '#fff'))
            legende.append((n, col, lab))
    s.append('</svg>')
    leg = '<div class="lgc">' + ''.join(f'<div class="lg"><span class="nb">{i}</span><span class="sw" style="background:{c}"></span>{rich(l)}</div>' for i, c, l in legende) + '</div>'
    return ''.join(s), h, leg

# ------------------------------------------------------------------ élévations
def _bande_svg(g, b, focus, k):
    ph, a0, a1, z0, z1, lab = b
    xa, xb = sorted((g.ax(a0), g.ax(a1))); ya, yb = sorted((g.niv(z1), g.niv(z0)))
    xa, xb = max(xa, 0), min(xb, g.largeur); ya, yb = max(ya, 0), min(yb, g.hauteur)
    if xb - xa < 1 or yb - ya < 1: return '', None
    fam = C.famille(ph); col = C.COUL[fam]
    actif = focus is None or ph in focus
    if fam == 'NT':
        r = f'<rect x="{xa:.1f}" y="{ya:.1f}" width="{xb-xa:.1f}" height="{yb-ya:.1f}" fill="url(#hg)" stroke="#757575" stroke-width="{1/k:.2f}"/>'
    elif actif:
        r = f'<rect x="{xa:.1f}" y="{ya:.1f}" width="{xb-xa:.1f}" height="{yb-ya:.1f}" fill="{col}" fill-opacity="0.26" stroke="{col}" stroke-width="{2/k:.2f}"/>'
    else:
        r = f'<rect x="{xa:.1f}" y="{ya:.1f}" width="{xb-xa:.1f}" height="{yb-ya:.1f}" fill="#fff" fill-opacity="0.55" stroke="none"/>'
    pos = ((xa + xb) / 2, ya + 14 / k) if actif and fam != 'NT' and (xb - xa) * k > 46 else None
    return r, (pos, ph, col, xb - xa) if pos else None

def _appareils_svg(g, apps, k, bornes, fixes=()):
    """Étiquettes des appareils : écartement en x et en y, sans recouvrir les pastilles de phase (fixes)."""
    bx0, by0, bx1, by1 = bornes
    et = []
    for app in apps:
        code, etat, lib, rep, a, mm, (dx, dy), v = app
        if rep.startswith('non repéré'): continue
        x, y = g.ax(a), g.niv(mm)
        if not (bx0 - 2 <= x <= bx1 + 2 and by0 - 2 <= y <= by1 + 2): continue
        labl = code if code != '—' else 'ME ' + rep.split('—')[0].strip()
        et.append({'x': x, 'y': y, 'w': (7.0 * len(labl) + 8) / k, 'h': 18 / k, 'c': E.ETATS[etat][0], 't': labl,
                   'lx': x + dx / k, 'ly': y + dy / k})
    # placement glouton : chaque étiquette prend la position libre la plus proche de sa position voulue,
    # sans recouvrir une étiquette déjà posée, une pastille de phase ni le point d'un autre appareil
    m = 2 / k; pas = 6 / k
    obst = [(fx, fy, fw, fh) for fx, fy, fw, fh in fixes] + [(e['x'], e['y'], 9 / k, 9 / k) for e in et]
    def libre(cx, cy, w, h, lst):
        return all(abs(cx - ox) >= (w + ow) / 2 + m or abs(cy - oy) >= (h + oh) / 2 + m for ox, oy, ow, oh in lst)
    voisins = lambda e: sum(1 for f in et if abs(f['x'] - e['x']) < 140 / k and abs(f['y'] - e['y']) < 80 / k)
    for e in sorted(et, key=lambda e: -voisins(e)):
        xa, xb = bx0 + e['w'] / 2 + 2 / k, bx1 - e['w'] / 2 - 2 / k
        ya, yb = by0 + e['h'] / 2 + 2 / k, by1 - e['h'] / 2 - 2 / k
        x0_, y0_ = min(max(e['lx'], xa), xb), min(max(e['ly'], ya), yb)
        autres = [o for o in obst if not (o[0] == e['x'] and o[1] == e['y'] and o[2] == 9 / k)]
        best = None
        nx, ny = int((xb - xa) / pas) + 1, int((yb - ya) / pas) + 1
        for j in range(ny):
            cy = ya + j * pas
            for i in range(nx):
                cx = xa + i * pas
                c = (cx - x0_) ** 2 * 0.5 + (cy - y0_) ** 2
                if best is not None and c >= best[0]: continue
                if libre(cx, cy, e['w'], e['h'], autres): best = (c, cx, cy)
        e['lx'], e['ly'] = (best[1], best[2]) if best else (x0_, y0_)
        obst.append((e['lx'], e['ly'], e['w'], e['h']))
    # traits de rappel, puis points, puis étiquettes : aucun trait ne passe sur une étiquette
    s = [f'<line x1="{e["lx"]:.1f}" y1="{e["ly"]:.1f}" x2="{e["x"]:.1f}" y2="{e["y"]:.1f}" stroke="{e["c"]}" stroke-width="{1.1/k:.2f}" stroke-dasharray="{2/k:.1f},{2/k:.1f}"/>' for e in et]
    s += [f'<circle cx="{e["x"]:.1f}" cy="{e["y"]:.1f}" r="{4/k:.1f}" fill="{e["c"]}" stroke="#fff" stroke-width="{1.2/k:.2f}"/>' for e in et]
    s += [f'<rect x="{e["lx"]-e["w"]/2:.1f}" y="{e["ly"]-e["h"]/2:.1f}" width="{e["w"]:.1f}" height="{e["h"]:.1f}" rx="{3/k:.1f}" fill="{e["c"]}" stroke="#fff" stroke-width="{1/k:.2f}"/>'
          + svgtxt(e['lx'], e['ly'] + 5 / k, e['t'], 12 / k, 'middle', 'bold', '#fff') for e in et]
    return ''.join(s), len(et)

def elevation(fac, width=None, height=None, a0=None, a1=None, z0=None, z1=None, focus=None, apps=None):
    """Élévation (ou segment) avec les bandes de phase ; appareils en option."""
    g = G.GEOMS[fac]
    x0, x1 = 0, g.largeur
    if a0 is not None:
        xa, xb = sorted((g.ax(a0), g.ax(a1))); x0, x1 = max(0, xa), min(g.largeur, xb)
    y0, y1 = 0, g.hauteur
    if z0 is not None:
        y0, y1 = max(0, g.niv(z1)), min(g.hauteur, g.niv(z0))
    vw, vh = x1 - x0, y1 - y0
    if width is None: width = round(height * vw / vh)
    k = width / vw; h = round(width * vh / vw)
    s = [f'<svg viewBox="{x0:.1f} {y0:.1f} {vw:.1f} {vh:.1f}" width="{width}" height="{h}" xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:0;top:0">',
         f'<defs><pattern id="hg" width="{8/k:.1f}" height="{8/k:.1f}" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<line x1="0" y1="0" x2="0" y2="{8/k:.1f}" stroke="#757575" stroke-width="{2/k:.2f}" opacity="0.5"/></pattern></defs>',
         f'<image href="../img/{g.img}" x="0" y="0" width="{g.largeur}" height="{g.hauteur}"/>']
    etiq = []
    for b in C.BANDES[fac]:
        r, e = _bande_svg(g, b, focus, k)
        s.append(r)
        if e: etiq.append(e)
    # une pastille par phase et par élévation, sur la bande visible la plus large
    meilleure = {}
    for (x, y), ph, col, larg in etiq:
        if not (x0 <= x <= x1 and y0 <= y <= y1): continue
        vis = min(x + larg / 2, x1) - max(x - larg / 2, x0)
        xc = (max(x - larg / 2, x0) + min(x + larg / 2, x1)) / 2
        if ph not in meilleure or vis > meilleure[ph][0]: meilleure[ph] = (vis, xc, y, col)
    fixes = []
    for ph, (vis, x, y, col) in meilleure.items():
        yb = max(y, y0 + 12 / k)
        s.append(badge(x, yb, ph, col, k)); fixes.append((x, yb, (7.2 * len(ph) + 10) / k, 18 / k))
    n = 0
    if apps:
        a_svg, n = _appareils_svg(g, apps, k, (x0, y0, x1, y1), fixes); s.append(a_svg)
    s.append('</svg>')
    return ''.join(s), width, h, n

def plan_div(left, top, w, h, inner, cls='plan'):
    return f'<div class="{cls}" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px">{inner}</div>'

def cap(left, top, w, html_):
    return f'<div class="cap" style="left:{left}px;top:{top}px;width:{w}px">{html_}</div>'

# ------------------------------------------------------------------ calendrier
MOIS = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.']
MOIS1 = 'JFMAMJJASOND'
def gantt(width, rowh=36, repere=True):
    lab = 360; cw = width - lab - 6
    tot = (C.FIN_CAL - C.DEBUT_CAL).days + 1
    X = lambda d: lab + (d - C.DEBUT_CAL).days / tot * cw
    top = 44; n = len(C.PHASES); h = top + n * rowh + 8
    s = [f'<svg viewBox="0 0 {width} {h}" width="{width}" height="{h}" xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:0;top:0">']
    for a, b in C.HIVERS:
        s.append(f'<rect x="{X(a):.1f}" y="{top-20}" width="{X(b)-X(a)+cw/790:.1f}" height="{h-top+20}" fill="#cfd8dc" opacity="0.55"/>')
    for a, b in C.ETES:
        s.append(f'<rect x="{X(a):.1f}" y="{top-20}" width="{X(b)-X(a):.1f}" height="{h-top+20}" fill="#ffe082" opacity="0.85"/>')
    # années et mois
    y, m = 2026, 11
    while (y, m) <= (2028, 12):
        d = dt.date(y, m, 1)
        nx = dt.date(y + (m == 12), m % 12 + 1, 1)
        s.append(f'<line x1="{X(d):.1f}" y1="{top-20}" x2="{X(d):.1f}" y2="{h}" stroke="#90a4ae" stroke-width="{1.2 if m == 1 else 0.5}"/>')
        s.append(svgtxt((X(d) + X(nx)) / 2, top - 6, MOIS1[m - 1], 12, 'middle', 'normal', '#37474f'))
        if m == 1 or (y, m) == (2026, 11):
            s.append(svgtxt(X(d) + 3, 13, str(y), 13, 'start', 'bold', '#17324d'))
        y, m = (y + (m == 12), m % 12 + 1)
    for i, (code, titre, d0, d1, pourquoi) in enumerate(C.PHASES):
        yy = top + i * rowh
        fam = C.famille(code) if code != 'P2' else '2'
        col = C.COUL['H'] if code == 'H28' else C.COUL[fam]
        s.append(f'<line x1="0" y1="{yy+rowh:.1f}" x2="{width}" y2="{yy+rowh:.1f}" stroke="#eceff1"/>')
        s.append(svgtxt(4, yy + 15, titre, 12.5, 'start', 'bold' if code in ('0', '1', '4') else 'normal', '#17324d'))
        s.append(svgtxt(4, yy + 30, f'{d0.day} {MOIS[d0.month-1]} {d0.year} – {d1.day} {MOIS[d1.month-1]} {d1.year}', 12, 'start', 'normal', '#546e7a'))
        op = '0.55' if code in ('P2', 'H28') else '1'
        s.append(f'<rect x="{X(d0):.1f}" y="{yy+4:.1f}" width="{max(X(d1)-X(d0), 4):.1f}" height="{rowh-8}" rx="3" fill="{col}" opacity="{op}"/>')
    if repere:
        lignes = {p[0]: i for i, p in enumerate(C.PHASES)}
        for code, ph, d, ecrit, verdict in C.REPERES_SAISON:
            yy = top + lignes[ph] * rowh + rowh / 2; x = X(d)
            col = '#c62828' if verdict.startswith('à trancher') else '#1b5e20'
            s.append(f'<path d="M{x:.1f},{yy-8:.1f} L{x+8:.1f},{yy:.1f} L{x:.1f},{yy+8:.1f} L{x-8:.1f},{yy:.1f} z" fill="#fff" stroke="{col}" stroke-width="2.4"/>')
    s.append('</svg>')
    return ''.join(s), h

CSS_PLUS = """
.lgc { column-count: 2; column-gap: 14px; }
.lg { break-inside: avoid; font-size: 12px; line-height: 1.3; margin-bottom: 3px; display: flex; align-items: flex-start; gap: 5px; }
.lg .nb { display: inline-block; min-width: 18px; height: 18px; border-radius: 9px; background: #111; color: #fff; font-weight: bold; text-align: center; line-height: 18px; font-size: 12px; flex: none; }
.lg .sw { display: inline-block; width: 14px; height: 14px; margin-top: 2px; flex: none; border: 1px solid #fff; outline: 1px solid #ccc; }
.quand { font-size: 12px; line-height: 1.34; }
.quand .dt { font-size: 15px; font-weight: bold; color: #17324d; margin-bottom: 4px; }
.lgd { font-size: 12px; line-height: 1.35; }
.proj { width: 640px; }
.lgd span.k { display: inline-block; width: 18px; height: 12px; vertical-align: -1px; margin: 0 4px 0 10px; border: 1px solid #999; }
"""

# ------------------------------------------------------------------ planches
def P_ensemble(num, total):
    pc, h = plan_cle(580)
    a = plan_div(40, 96, 580, h, pc) + cap(40, 96 + h + 4, 580, hr('Plan clé de la feuille 010, couleurs des architectes. Pastilles : sous-phases par face proposées `[choix]`.'))
    b = box(636, 96, 956, h + 30, f'<div class="txt">{hr(T.ENSEMBLE)}</div>', 'Le plan en une page', 'en-txt')
    gy = 96 + h + 42
    gs, gh = gantt(1538)
    leg = ('<div class="lgd" style="margin-top:4px"><span class="k" style="background:#cfd8dc"></span>Novembre à avril (bâti isolé, AR-PLN-042)'
           '<span class="k" style="background:#ffe082"></span>Période estivale, 24 juin au 15 août (définition de travail GLCRM)'
           '<span class="k" style="background:#fff;border:2px solid #1b5e20;transform:rotate(45deg);width:10px;height:10px"></span>Ligne saisonnière du tableau de WSP respectée'
           '<span class="k" style="background:#fff;border:2px solid #c62828;transform:rotate(45deg);width:10px;height:10px"></span>Ligne à trancher (planche 9)</div>')
    g = box(40, gy, 1552, BOT - gy, f'<div style="position:relative;height:{gh}px">{gs}</div>{leg}', 'Calendrier proposé `[choix]` — novembre 2026 à décembre 2028', 'en-gantt')
    return ('<section class="planche">' + header(num, total, 'Vue d\'ensemble — l\'ordre et le calendrier', 'Option R : basilaire est, tour face par face, basilaires sud, nord et ouest ; durées du plan clé placées dans la fenêtre de travail GLCRM')
            + a + b + g + footer(num, total, 'D2 feuille 010 (plan clé, durées ±5, ±8, ±4 mois) ; D5 tableau de coordination, lignes saisonnières ; cahier de phasage en plan, planche 13 (option R recommandée) ; Z-10, C-14.') + '</section>')

def P_elevations(num, total):
    out = []
    W = 760
    sn, wn, hn, _ = elevation('nord', width=W)
    ss, ws, hs, _ = elevation('sud', width=W)
    out.append(plan_div(40, 96, wn, hn, sn) + cap(40, 96 + hn + 3, wn, '<b>Élévation nord (F)</b> — l\'est à gauche, l\'ouest à droite.'))
    out.append(plan_div(832, 96, ws, hs, ss) + cap(832, 96 + hs + 3, ws, '<b>Élévation sud (A)</b> — l\'ouest à gauche, l\'est à droite.'))
    y2 = 96 + max(hn, hs) + 30
    go, ge = G.GEOMS['ouest'], G.GEOMS['est']
    hh = round((1552 - 16) / (go.largeur / go.hauteur + ge.largeur / ge.hauteur))
    so, wo, ho, _ = elevation('ouest', height=hh)
    se, we, he, _ = elevation('est', height=hh)
    out.append(plan_div(40, y2, wo, ho, so) + cap(40, y2 + ho + 3, wo, '<b>Élévation ouest (B)</b> — le nord à gauche, le sud à droite.'))
    out.append(plan_div(56 + wo, y2, we, he, se) + cap(56 + wo, y2 + he + 3, we, '<b>Élévation est (G)</b> — le sud à gauche, le nord à droite.'))
    y3 = y2 + max(ho, he) + 28
    leg = ('<div class="lgd"><span class="k" style="background:' + C.COUL['1'] + ';opacity:.6"></span>Phase 1'
           '<span class="k" style="background:' + C.COUL['2'] + ';opacity:.6"></span>Phase 2 (tour)'
           '<span class="k" style="background:' + C.COUL['3'] + ';opacity:.6"></span>Phase 3'
           '<span class="k" style="background:repeating-linear-gradient(45deg,#9e9e9e 0 2px,#fff 2px 6px)"></span>Non touché</div>')
    out.append(box(40, y3, 1552, BOT - y3, f'<div class="txt">{hr(T.ELEVATIONS)}</div>{leg}', 'Les phases reportées sur les élévations `[lecture]`', 'el-txt'))
    return ('<section class="planche">' + header(num, total, 'Les phases sur les quatre élévations', 'Chaque façade est partagée entre deux ou trois phases ; bandes reportées depuis le plan clé, axe par axe')
            + ''.join(out) + footer(num, total, 'D2 feuilles 010 (plan clé), 011 (élévations, zones de travaux), 201 et 202 (élévations A, B, F, G) ; chaînes d\'axes et de niveaux des feuilles 201 et 202.') + '</section>')

def _ligne_appareils(phases):
    lst = []
    for ph in phases: lst += C.appareils_de(ph)
    cpt = {}
    for fac, app, m in lst: cpt[app[1]] = cpt.get(app[1], 0) + 1
    noms = {'coupe': 'interrompus', 'deplace': 'déplacés', 'retire': 'retirés', 'maintenu': 'maintenus sans interruption', 'intact': 'non touchés'}
    resume = ', '.join(f'{v} {noms[k]}' for k, v in sorted(cpt.items(), key=lambda x: -x[1]))
    part = [app[0] for fac, app, m in lst if any(app[0].startswith(p) for p in ('O-C-', 'O-I-', 'O-E-', 'E-H-', 'E-D-'))]
    nonrep = [app[0] for fac, app, m in lst if app[3].startswith('non repéré')]
    txt = f'<b>{len(lst)} appareils</b> rattachés à cette période : {resume}.'
    if part: txt += f' Sur les élévations partielles, non dessinés ici : {", ".join(part)}.'
    if nonrep: txt += f' Sans repère sur les dessins : {", ".join(nonrep)}.'
    return txt, lst

def P_phase(num, total, titre, sous, cle_site, actifs, phases_pc, quand, segs, phases, F, sources, sw=980):
    out = []
    sv, sh, leg = site(sw, cle_site)
    out.append(plan_div(40, 96, sw, sh, sv))
    xr = 40 + sw + 14; wr = 1592 - xr
    pcw = 262
    pc, pch = plan_cle(pcw, actifs, phases_pc)
    out.append(plan_div(xr, 96, pcw, pch, pc))
    hq = max(pch, MES.get(f'q{num}') or 150)
    out.append(box(xr + pcw + 10, 96, wr - pcw - 10, hq, f'<div class="quand">{quand}</div>', None, f'q{num}'))
    yl = 96 + hq + 10
    ncol = 3 if wr > 800 else 2
    if ncol == 3: leg = leg.replace('class="lgc"', 'class="lgc" style="column-count:3"', 1)
    hleg = MES.get(f'lg{num}') or (-(-leg.count('class="lg"') // ncol) * 34 + 34)
    hleg = max(hleg, 96 + sh - yl)
    out.append(box(xr, yl, wr, hleg, leg, 'Sur le plan d\'implantation', f'lg{num}'))
    # segments d'élévation
    y = max(96 + sh, yl + hleg) + 10
    apps_ph = {}
    for ph in phases:
        for fac, app, m in C.appareils_de(ph): apps_ph.setdefault(fac, []).append(app)
    def asp(sg):
        g = G.GEOMS[sg[0]]
        xa, xb = sorted((g.ax(sg[1]), g.ax(sg[2]))); xa, xb = max(0, xa), min(g.largeur, xb)
        ya, yb = (max(0, g.niv(sg[4])), min(g.hauteur, g.niv(sg[3]))) if sg[3] is not None else (0, g.hauteur)
        return (xb - xa) / (yb - ya)
    wbox = (1552 - 3 * 12) / 4
    besoin = max((MES.get(f'f{num}{c}') or BE.hauteur_txt(F[c], wbox - 16) + 22) for c in ('quoi', 'avant', 'coupures', 'chantier') if c in F) + 4
    y3 = BOT - besoin
    dispo = y3 - y - 22 - 46
    hseg = min(dispo, (1552 - 14 * (len(segs) - 1)) / sum(asp(sg) for sg in segs))
    x = 40
    for sg in segs:
        fac, a0, a1, z0, z1, legd = sg
        principaux = [a for a in apps_ph.get(fac, []) if not any(a[0].startswith(p) for p in ('O-C-', 'O-I-', 'O-E-', 'E-H-', 'E-D-'))]
        sv2, w2, h2, n = elevation(fac, height=hseg, a0=a0, a1=a1, z0=z0, z1=z1, focus=set(phases), apps=principaux)
        out.append(plan_div(x, y, w2, h2, sv2) + f'<div class="cap" style="left:{x}px;top:{y + h2 + 2}px;width:{w2}px;white-space:nowrap;overflow:hidden"><b>{legd}</b></div>')
        x += w2 + 14
    reste = 1592 - x
    if reste > 380:
        rows = [['Ligne', '&nbsp;', 'Appareil', 'Fenêtre écrite']]
        tous = []
        for ph in phases: tous += C.appareils_de(ph)
        Wt = ['80px', '18px', f'{round((reste - 120) * 0.56)}px', f'{round((reste - 120) * 0.44)}px']
        hmax = hseg + 18
        for fac, app, m in tous:
            r = D5I.get(app[0])
            per = ' '.join((r['periode'] if r else '').split()) or '—'
            if len(per) > 44: per = per[:44].rsplit(' ', 1)[0] + ' …'
            if r and r['arret'].strip().lower().startswith('n/a'): per = 'non touché'
            row = [f'<b>{esc(app[0])}</b>', f'<span class="dot" style="background:{E.ETATS[app[1]][0]}"></span>', esc(app[2]), esc(per)]
            if BE.hauteur_table(rows + [row], Wt) > hmax - 26: break
            rows.append(row)
        manque = len(tous) - (len(rows) - 1)
        note = f'<div class="note">… et {manque} autres : voir le cahier de phasage par élévation.</div>' if manque > 0 else ''
        out.append(box(x, y, reste, round(hseg) + 18, table(rows, Wt) + note, None, f'ap{num}'))
    y2 = y + round(hseg) + 22
    ligne, lst = _ligne_appareils(phases)
    out.append(cap(40, y2, 1552, ligne))
    y3 = max(y3, y2 + 42)
    trou = y3 - (y2 + 42) - 8
    if trou > 64:
        noms = [('coupe', 'Interrompus'), ('deplace', 'Déplacés puis réinstallés'), ('retire', 'Retirés'), ('maintenu', 'Maintenus sans interruption'), ('intact', 'Non touchés')]
        cols = []
        for etat, nom in noms:
            codes = [app[0] if app[0] != '—' else 'hors tableau : ' + app[2] for fac, app, m in lst if app[1] == etat]
            if codes:
                cols.append(f'<div style="break-inside:avoid;margin-bottom:4px"><span class="dot" style="background:{E.ETATS[etat][0]}"></span> <b>{nom} ({len(codes)})</b> : {esc(", ".join(codes))}</div>')
        out.append(box(40, y2 + 40, 1552, trou, '<div class="txt" style="column-count:2;column-gap:18px">' + ''.join(cols) + '</div>', None, f'et{num}'))
    for i, cle in enumerate(('quoi', 'avant', 'coupures', 'chantier')):
        if cle in F:
            out.append(box(round(40 + i * (wbox + 12)), y3, round(wbox), BOT - y3, f'<div class="txt">{hr(F[cle])}</div>', None, f'f{num}{cle}'))
    return ('<section class="planche">' + header(num, total, titre, sous) + ''.join(out)
            + footer(num, total, sources) + '</section>'), lst

def P_phase0(num, total):
    out = []
    sw = 1256
    sv, sh, leg = site(sw, '0')
    leg = leg.replace('class="lgc"', 'class="lgc" style="column-count:1"', 1)
    out.append(plan_div(40, 96, sw, sh, sv))
    out.append(box(40 + sw + 16, 96, 1552 - sw - 16, sh, leg + '<div class="note" style="margin-top:8px">' + hr('La clôture épaisse en tirets et les cadres des détails 1 à 5 sont ceux de la feuille 001 (note 23) ; tout le reste est ajouté `[choix]`.') + '</div>', 'Sur le plan d\'implantation', 'lg0'))
    y3 = 96 + sh + 14
    wbox = (1552 - 3 * 12) / 4
    for i, cle in enumerate(('quoi', 'avant', 'chantier', 'valider')):
        out.append(box(round(40 + i * (wbox + 12)), y3, round(wbox), BOT - y3, f'<div class="txt">{hr(T.F0[cle])}</div>', None, f'f0{cle}'))
    return ('<section class="planche">' + header(num, total, 'Phase 0 — mobilisation et préalables', 'Novembre-décembre 2026 `[choix]` : installation de chantier et tout ce que les documents exigent « avant le début »')
            + ''.join(out) + footer(num, total, 'D2 feuilles 001 et 002 ; D1 01 14 00, 01 32 16.19, 01 51 00, 01 52 00, 01 56 00, 01 56 50 ; D8 ; analyse/03-phasage.md §1.1.') + '</section>')

def P_calendrier(num, total):
    """Calendrier et décisions sur une planche : ce qui commande, lignes saisonnières, ce qui peut bouger, décisions."""
    wl = 620; xr = 40 + wl + 14; wr = 1592 - xr
    ht = max(MES.get('ca-txt') or 260, MES.get('ca-rep') or 300)
    a = box(40, 96, wl, ht, f'<div class="txt">{hr(T.CALENDRIER)}</div>', 'Ce qui commande le calendrier', 'ca-txt')
    rows = [['Ligne', 'Phase', 'Ce que le tableau écrit', 'Dans le calendrier proposé']]
    for code, ph, d, ecrit, verdict in C.REPERES_SAISON:
        v = f'<b style="color:#c62828">{esc(verdict)}</b>' if verdict.startswith('à trancher') else esc(verdict)
        rows.append([f'<b>{code}</b>', ph if ph != 'P2' else 'avant 2', esc(ecrit), v])
    b_ = box(xr, 96, wr, ht, table(rows, ['84px', '58px', '330px', f'{wr - 84 - 58 - 330 - 18}px']), 'Les lignes saisonnières du tableau de WSP, posées sur le calendrier', 'ca-rep')
    y2 = 96 + ht + 12
    hb = MES.get('ca-bou') or 300
    c = box(40, y2, wl, hb, table(T.BOUGER, ['250px', f'{wl - 250 - 18}px']), 'Ce qui peut faire bouger le calendrier', 'ca-bou')
    jj = lambda d: f'{d.day} {MOIS[d.month-1]} {d.year}'
    PH = C.PH
    jal = [['Date', 'Jalon'],
           [jj(PH['0'][2]), 'Mobilisation et installation de chantier (phase 0)'],
           [jj(PH['1'][2]), 'Début des travaux : basilaire est (phase 1)'],
           ['avril 2027', 'Tracé des conduits temporaires de l\'hémodialyse écrit par WSP (Z-29)'],
           [jj(PH['P2'][2]), 'Début des contournements électromécaniques de la tour'],
           [jj(PH['2.S'][2]), 'Début de la tour, face sud'],
           [jj(PH['P2'][3]), 'Conduits temporaires posés, avant la période estivale'],
           [jj(PH['2.E'][3]), 'Tour fermée : fin de la face est'],
           ['24 juin 2028', 'Ambulances : entrée et sortie par la porte sud jusqu\'au 15 août'],
           [jj(PH['3.O'][3]), 'Fin des travaux d\'enveloppe (basilaire ouest)'],
           [jj(PH['4'][3]), 'Fin de la clôture : mise en service et réception']]
    yj = y2 + hb + 12
    c += box(40, yj, wl, BOT - yj, table(jal, ['120px', f'{wl - 120 - 18}px']), 'Jalons du calendrier proposé `[choix]`', 'ca-jal')
    d = box(xr, y2, wr, BOT - y2, table(T.DECISIONS, ['330px', '118px', '96px', f'{wr - 330 - 118 - 96 - 18}px'])
            + '<div class="note" style="margin-top:6px">« Avant » : date à laquelle la décision doit être prise pour que le calendrier proposé tienne. '
              'Les seize défauts documentaires relevés en lisant les élévations sont détaillés dans le cahier de phasage par élévation, planche 14.</div>',
            'Décisions à obtenir pour figer ce plan', 'de')
    return ('<section class="planche">' + header(num, total, 'Calendrier et décisions', 'Ce qui commande le calendrier, ce qui peut le faire bouger, et qui doit trancher quoi avant quand')
            + a + b_ + c + d + footer(num, total, 'D2 feuilles 010 et 505 (AR-PLN-042) ; D5 ; analyse/02-contraintes.md (C-01, C-02, C-14, C-34, Z-01, Z-10, Z-12, Z-27, Z-29) ; analyse/03-phasage.md §4 K3 ; analyse/05-phasage-elevations.md.') + '</section>')

def main():
    args = sys.argv[1:]
    out = pathlib.Path(args[args.index('--out') + 1]) if '--out' in args else ROOT / 'plan-phasage-complet.pdf'
    Q = lambda code, extra='': (f'<div class="dt">{C.PH[code][2].day} {MOIS[C.PH[code][2].month-1]} {C.PH[code][2].year} – {C.PH[code][3].day} {MOIS[C.PH[code][3].month-1]} {C.PH[code][3].year}</div>'
                                f'{rich(C.PH[code][4])}{extra}')
    q1 = Q('1', '<br><br>Durée indicative du plan clé : ±5 mois. Zones D, E, F ; oncologie de 2023 (L) non touchée.')
    def QQ(*items):
        out = []
        for code, nom in items:
            a, b = C.PH[code][2], C.PH[code][3]
            out.append(f'<div style="margin-bottom:5px"><b>{nom}</b><br><span style="font-size:13px;font-weight:bold;color:#17324d">{a.day} {MOIS[a.month-1]} {a.year} – {b.day} {MOIS[b.month-1]} {b.year}</span></div>')
        return ''.join(out)
    q2a = QQ(('P2', 'Contournements de la tour'), ('2.S', 'Face sud'), ('2.O', 'Face ouest'))
    q2b = QQ(('2.N', 'Face nord'), ('2.E', 'Face est'), ('H28', 'Fenêtres de la tour par l\'intérieur'))
    q3a = QQ(('3.S', 'Basilaires sud — ambulances par la porte nord'), ('3.N', 'Basilaire nord — ambulances par la porte sud dès le 24 juin'))
    q3b = QQ(('3.O', 'Basilaire ouest'), ('4', 'Clôture et réception'))
    lst_total = []
    def ph(*a):
        html_, l = P_phase(*a); lst_total.extend(l); return html_
    pages = [
     lambda n, t: P_ensemble(n, t),
     lambda n, t: P_elevations(n, t),
     lambda n, t: P_phase0(n, t),
     lambda n, t: ph(n, t, 'Phase 1 — basilaire est', 'Zones D, E et F ; faces nord, est et sud du basilaire est', '1', {'D', 'E', 'F'}, {'1'}, q1,
                     [('nord', 9.3, 16.4, 8500, 20500, 'Élévation nord, axes 10 à 16'), ('est', 12.5, 1.6, 8500, 20500, 'Élévation est, axes I à B\''), ('sud', 9.3, 16.4, 8500, 20500, 'Élévation sud, axes 10 à 16')],
                     ['1'], T.F1, 'D2 feuilles 001, 002, 010, 201, 202, 505 ; D4 ME001(D) à ME003(D) ; D5 ; D11 ; analyse/03-phasage.md §2.2.'),
     lambda n, t: ph(n, t, 'Phase 2 — la tour : préalables, faces sud et ouest', 'Mai à septembre 2027 : contournements électromécaniques, puis les faces sud et ouest', '2a', {'A'}, {'2.S', '2.O'}, q2a,
                     [('sud', 0.6, 9.3, None, None, 'Élévation sud, axes 1 à 9'), ('ouest', -0.4, 9.6, None, None, 'Ouest, axes A à F\'')],
                     ['P2', '2.S', '2.O'], T.F2A, 'D2 feuilles 201, 301 ; D4 ME001(D), ME002(D), ME010, ME011, ME014 ; D5 ; D6 S201 à S204, S303 ; analyse/03-phasage.md §2.3.', 640),
     lambda n, t: ph(n, t, 'Phase 2 — la tour : faces nord et est, puis l\'hiver 2028', 'Août 2027 à avril 2028 : faces nord et est, puis les fenêtres de la tour par l\'intérieur', '2b', {'A'}, {'2.N', '2.E'}, q2b,
                     [('nord', 0.4, 9.9, None, None, 'Élévation nord, axes 9 à 1'), ('est', 8.6, 0.4, None, None, 'Élévation est, axes F à A')],
                     ['2.N', '2.E'], T.F2B, 'D2 feuilles 202, 504, 505 ; D4 ME001(D), ME002(D), ME003(D), ME014 ; D5 ; D11 ; analyse/03-phasage.md §2.3.', 640),
     lambda n, t: ph(n, t, 'Phase 3 — basilaires sud et nord', 'Mai à août 2028 : façades sud (I, H, G) et nord (J, B, K) ; les ambulances changent de porte le 24 juin', '3a', {'I', 'H', 'G', 'P', 'J', 'B', 'K'}, {'3.S', '3.N'}, q3a,
                     [('sud', -0.2, 9.8, 8500, 20500, 'Élévation sud, axes 1 à 9'), ('nord', -0.2, 9.3, 8500, 20500, 'Élévation nord, axes 9 à 1')],
                     ['3.S', '3.N'], T.F3A, 'D2 feuilles 001, 002 (détails 1 et 2), 705 ; D4 ME004, ME008, ME009 ; D5 ; D11 ; analyse/03-phasage.md §2.4.'),
     lambda n, t: ph(n, t, 'Phase 3 — basilaire ouest, puis la clôture', 'Août-septembre 2028 : façade ouest du basilaire ; octobre-décembre 2028 : mise en service et réception', '3b', {'O', 'J', 'I'}, {'3.O'}, q3b,
                     [('ouest', -0.8, 12.4, 5000, 20500, 'Élévation ouest, du nord (gauche) au sud (droite)')],
                     ['3.O'], T.F3B, 'D2 feuilles 001, 703 ; D4 ME001(D), ME003(D), ME010 ; D5 ; analyse/03-phasage.md §1.4 et §2.4.2.', 760),
     lambda n, t: P_calendrier(n, t),
    ]
    total = len(pages)
    css = BE.CSS + CSS_PLUS
    htmlp = BUILD / 'complet.html'; mesp = BUILD / 'mes_complet.json'
    for passage in (1, 2):
        body = ''.join(f(i + 1, total) for i, f in enumerate(pages))
        doc = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Plan de phasage complet — Hôpital de Chandler R-657-24</title>'
               f'<style>{css}</style></head><body>{body}</body></html>')
        htmlp.write_text(doc, encoding='utf-8')
        r = subprocess.run(['node', str(ROOT / 'src' / 'topdf.cjs'), str(htmlp), str(out), str(BUILD / 'deb_complet.json'), str(mesp)],
                           capture_output=True, text=True)
        if r.returncode: print(r.stdout, r.stderr[-1500:]); return
        if passage == 1: MES.update(json.loads(mesp.read_text()))
    print(r.stdout.strip(), r.stderr[-1500:])

if __name__ == '__main__':
    main()
