"""Cahier de phasage graphique — génération des planches (HTML + SVG -> PDF tabloïd paysage).
Usage : python3 src/build_planches.py [--planches 0,1] [--out build/apercu.pdf]
Toute coordonnée relevée sur un plan est une [lecture] (voir src/zones.py)."""
import sys, pathlib, subprocess, html, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from zones import ZONES, FACES_TOUR, ELEV, CROP, OFF, shift
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / 'img'; BUILD = ROOT / 'build'; BUILD.mkdir(exist_ok=True)
W, H = 1632, 1056          # tabloïd paysage, 96 px/po
S = 0.94                   # échelle d'affichage du plan clé (1000 x 540 -> 940 x 508)

# ---------- images dérivées ----------
def prep_images():
    im = Image.open(IMG / 'A010_plan_cle.png').crop(CROP); im.save(BUILD / 'plan.png')
    im = Image.open(IMG / 'A001_implantation.png').crop((400, 200, 3000, 1950)); im.save(BUILD / 'implantation.png')

# ---------- helpers SVG ----------
def pts(poly): return ' '.join(f'{x},{y}' for x, y in shift(poly))
def poly(polyg, fill, op=0.55, stroke='#333', sw=1.2, dash=None, extra=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polygon points="{pts(polyg)}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{d} {extra}/>'
def txt(x, y, s, size=11, anchor='start', weight='normal', fill='#111', italic=False, cls=''):
    st = f'font-size:{size}px;font-weight:{weight};fill:{fill};' + ('font-style:italic;' if italic else '')
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="{st}" class="{cls}">{html.escape(s)}</text>'
def badge(x, y, label, fill='#17324d', r=11, size=12, textfill='#fff'):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#fff" stroke-width="1.5"/>'
            + txt(x, y + size * 0.36, label, size, 'middle', 'bold', textfill))
def tag(x, y, label, fill='#8e24aa', w=None, hgt=15, size=10.5):
    w = w or (len(label) * 6.6 + 8)
    return (f'<rect x="{x - w/2}" y="{y - hgt/2}" width="{w}" height="{hgt}" rx="3" fill="{fill}" stroke="#fff" stroke-width="1"/>'
            + txt(x, y + size * 0.36, label, size, 'middle', 'bold', '#fff'))
def leader(x1, y1, x2, y2, color='#333', dash='3,2'):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1" stroke-dasharray="{dash}"/>'
def dot(x, y, color='#333', r=3.2): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="#fff" stroke-width="1"/>'
def arrow_marker():
    return ('<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">'
            '<path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>'
            '<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="7" stroke="#777" stroke-width="1.2"/></pattern>'
            '<pattern id="hatchm" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="#8e24aa" stroke-width="1.6"/></pattern></defs>')
def view_arrow(letter, anchor, direction, color='#0d47a1'):
    x, y = anchor[0] - OFF[0], anchor[1] - OFF[1]
    dx, dy = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}[direction]
    return (f'<line x1="{x}" y1="{y}" x2="{x + dx*22}" y2="{y + dy*22}" stroke="{color}" stroke-width="2" marker-end="url(#ar)"/>'
            + f'<circle cx="{x}" cy="{y}" r="10" fill="#fff" stroke="{color}" stroke-width="2"/>'
            + txt(x, y + 4.2, letter, 12, 'middle', 'bold', color))

PHASE_FILL = {'1': '#3b7dd8', '2': '#5cb85c', '3': '#f0a830', 'non touché': 'url(#hatch)'}
FACE_FILL = {'2.N': '#1b5e20', '2.E': '#2e7d32', '2.S': '#66bb6a', '2.O': '#00695c'}
P3_FILL = {'3.N': '#e65100', '3.O': '#ef6c00', '3.S': '#ffb300'}

def zone_labels(with_fn=True):
    """Lettres de zone dans les aplats (positions relevées) et, si demandé, fonction courte."""
    pos = {'A': (459, 430), 'B': (486, 333), 'J': (318, 333), 'K': (625, 333), 'O': (256, 430), 'I': (290, 528), 'H': (430, 528),
           'G': (616, 528), 'P': (532, 573), 'D': (790, 440), 'F': (725, 585), 'E': (845, 585), 'L': (952, 530), 'C': (459, 160)}
    out = []
    for k, (x, y) in pos.items():
        x, y = x - OFF[0], y - OFF[1]
        lab = k if k not in ('O', 'P') else ('ouest' if k == 'O' else 'saillie')
        out.append(f'<rect x="{x-9}" y="{y-9}" width="18" height="18" transform="rotate(45 {x} {y})" fill="#fff" stroke="#111" stroke-width="1.2"/>' if k not in ('O', 'P') else '')
        out.append(txt(x, y + 4, lab if k not in ('O', 'P') else '', 11, 'middle', 'bold'))
    return ''.join(out)

def plan_svg(inner, width=940):
    return (f'<svg viewBox="0 0 1000 540" width="{width}" height="{round(width*0.54)}" style="position:absolute;left:0;top:0" '
            f'xmlns="http://www.w3.org/2000/svg">{arrow_marker()}{inner}</svg>')

def plan_figure(left, top, inner, width=940, dim=0.0):
    """Plan clé 010 rendu (200 ppp) + calque SVG."""
    h = round(width * 0.54)
    veil = f'<div style="position:absolute;left:0;top:0;width:{width}px;height:{h}px;background:rgba(255,255,255,{dim})"></div>' if dim else ''
    return (f'<div style="position:absolute;left:{left}px;top:{top}px;width:{width}px;height:{h}px;overflow:hidden;border:1px solid #b8c4d0;background:#fff">'
            f'<img src="plan.png" style="position:absolute;left:0;top:0;width:{width}px;height:{h}px">{veil}{plan_svg(inner, width)}</div>')

def box(left, top, width, height, inner, title=None, style=''):
    t = f'<div class="bt">{html.escape(title)}</div>' if title else ''
    return f'<div class="box" style="left:{left}px;top:{top}px;width:{width}px;height:{height}px;{style}">{t}{inner}</div>'

def table(rows, widths, header=True, size=9.5, cls=''):
    out = [f'<table class="t {cls}" style="font-size:{size}px"><colgroup>' + ''.join(f'<col style="width:{w}">' for w in widths) + '</colgroup>']
    for i, r in enumerate(rows):
        tg = 'th' if header and i == 0 else 'td'
        out.append('<tr>' + ''.join(f'<{tg}>{c}</{tg}>' for c in r) + '</tr>')
    return ''.join(out) + '</table>'

def header(num, title, sub):
    return (f'<div class="hdr"><div class="h1">Planche {num} — {html.escape(title)}</div><div class="h2">{html.escape(sub)}</div>'
            f'<div class="proj">Hôpital de Chandler — Réfection de l\'enveloppe · CISSS de la Gaspésie · AOC-077221 · Dossier GLCRM R-657-24 · Cahier de phasage graphique</div></div>')
def footer(num, total, sources):
    return (f'<div class="ftr"><span><b>Sources :</b> {html.escape(sources)}</span>'
            f'<span class="conv"><b>Conventions :</b> [lecture] = position ou correspondance lue graphiquement sur un plan, non écrite ; [à confirmer] = localisation que les documents ne fixent pas ; identifiants AR-DEV-, AR-PLN-, ME-, ST-, CI- = lignes du registre analyse/02-contraintes.md ; C-, Z-, R- = contradictions, zones d\'ombre, renvois. Document de travail, non contractuel : aucune durée n\'est proposée.</span>'
            f'<span class="pg">{num + 1} / {total}</span></div>')

# ---------- Planche 0 ----------
POINTS_FIXES = [
 # no, libellé, localisation écrite, IDs, marque, (x,y) image 200 ppp, (lx,ly) position du numéro
 ('1', 'Prise d\'air frais du bloc opératoire — 24/7, conduits temporaires', '« Façade ouest (tour) », « toiture ouest »', 'ME-042 à 048', '[à confirmer] tour ou basilaire', (272, 440), (205, 465)),
 ('2', 'Évents de vapeur des autoclaves (sous-sol) — 24/7, relocalisés avant la façade ouest ; temporaires jusqu\'au coin sud-ouest', '« Façade ouest », toiture', 'ME-075 à 079', '', (257, 475), (205, 495)),
 ('3', 'Centrale d\'air médical — 24/7 ; prise temporaire sur la façade ouest pendant la façade nord', '« Toiture nord-ouest » ; façades nord et ouest', 'ME-064 à 068', '[à confirmer] tour ou basilaire', (300, 335), (205, 335)),
 ('4', 'Unité de ventilation hémodialyse / laboratoire, niveau 200 — conduits temporaires avant démolition ; coupures dimanche hors été', '« Façades nord/ouest » de la tour', 'ME-049 à 054', '[à confirmer] locaux 202-237', (380, 356), (330, 292)),
 ('5', 'IRM — interdiction de métal quand l\'IRM est en service ; volets coupe-feu R16/R34/R36', 'Zone F (RC)', 'AR-PLN-009, 010 ; ME-010, 109, 110', '', (705, 560), (705, 613)),
 ('6', 'Urgence (RC, zone H) et quai des ambulances — gicleurs 2 × 2 h ; enseigne ; caméra', '« Entrée ambulance sud » (D4, D5) ; « Zone ambulance (nord) » (AR-PLN-004)', 'ME-006 à 008, 145 à 147 ; AR-PLN-004, 014, 018 ; CI-TAB-016', '[lecture] garage ▲▼, saillie sud', (532, 556), (585, 613)),
 ('7', 'Entrée principale et marquise — accès maintenu en trois configurations', 'Zone H ; détail 2 de la feuille 002', 'AR-PLN-008, 019 ; CI-TAB-014', '[lecture] marquise au sud (002)', (420, 550), (450, 613)),
 ('8', 'Nouvelle issue permanente du laboratoire (niveau 100) — jalon obligatoire ; escalier no 7 des plans de structure', 'Zone B ; « basilaire nord-ouest » (ST-039)', 'AR-DEV-058, 198 ; AR-PLN-064 ; ST-039 ; CI-TAB-019', '[à confirmer] escalier no 7 = issue (Z-12)', (470, 320), (590, 235)),
 ('9', 'Chambres à pression négative 216 (nord) et 307 (sud) ; soins intensifs 315', 'Façade nord ; façade sud ; ligne D5 N-F-V-009', 'ME-056 à 058', '', (560, 356), (650, 235)),
 ('10', 'Hotte de médecine nucléaire — conduit modifié sur toute la hauteur ; arrêt vendredi-dimanche', '« Tour est »', 'ME-117 à 119', '', (662, 445), (735, 300)),
 ('11', 'Prises d\'air et registres du service alimentaire, sous-sol — classe IV, horaire « S »', 'Niveau SS, locaux S41/S42/S44M, « zone A »', 'CI-TAB-005 ; ME-025, 029', '[à confirmer] SS non zoné', (520, 480), (600, 480)),
 ('12', 'Local R-22 — renforts des colonnes A4, A5, A6 en entreplafond (classe IV, J/S)', '« Secteur IRM / local R-22 (RC) » ; zone C au tableau CISSS', 'ME-108, 111 ; CI-TAB-010 ; C-40 ; Z-25', '[à confirmer]', (690, 525), (790, 613)),
 ('13', 'Salle des serveurs RC (arrêt court, semaine, hors été) ; bi-bloc LG 18 MBH', '« Façade est »', 'ME-086, 088', '', (930, 440), (985, 470)),
 ('14', 'Persienne UT-2 (chirurgie d\'un jour) — coupure rapide nuit ou fin de semaine', '« Façade sud »', 'ME-055', '', (380, 548), (320, 613)),
 ('15', 'Stationnement de l\'IRM mobile — sorties d\'arrosage à conserver, alcôve dans le revêtement', '« Coin nord-est » (D4) ; lignes D5 sud et nord', 'ME-116 ; CI-TAB-017', '[à confirmer]', (928, 372), (985, 345)),
 ('16', 'Évents de la chaufferie (porte-à-faux) — 24/7 ; soffite et toiture du coin nord-ouest', '« Porte-à-faux », « coin nord-ouest »', 'ME-080, 096, 120 à 123', '[à confirmer] face (C-28)', (262, 340), (205, 300)),
]

def planche0(total):
    inner = [zone_outline_layer(), zone_labels()]
    for l, (anc, d, name) in ELEV.items(): inner.append(view_arrow(l, anc, d))
    for no, lib, loc, ids, marque, (px, py), (lx, ly) in POINTS_FIXES:
        x, y = px - OFF[0], py - OFF[1]; bx, by = lx - OFF[0], ly - OFF[1]
        inner += [leader(bx, by, x, y, '#8e24aa', '2,2'), dot(x, y, '#8e24aa'), badge(bx, by, no, '#8e24aa', 10, 11)]
    plan = plan_figure(40, 96, ''.join(inner), 940) + '<div class="cap" style="left:40px;top:606px;width:940px">Fond : feuille 010 (D2), plan clé « Zones des travaux », couleurs des architectes (bleu phase 1, vert phase 2, orange phase 3, hachures « secteur non touché »), nord en haut à droite. Contours des zones, repères d\'élévation A à I (feuille 011) et points fixes 1 à 16 : superposés [lecture]. Le numéro pointe l\'emplacement écrit ou lu ; la colonne « Marque » du tableau dit ce qui reste à confirmer.</div>'
    # tableau des zones
    rows = [['Zone', 'Fonction (légende 010, via 01 §8.5)', 'Phase du plan clé [lecture]']]
    for k in 'ABCDEFGHIJKL':
        p, short, fn, ph = ZONES[k]; rows.append([f'<b>{k}</b>', fn, {'1': 'Phase 1 — basilaire est', '2': 'Phase 2 — tour', '3': 'Phase 3 — basilaires nord, ouest, sud', 'non touché': 'Secteur non touché'}[ph]])
    rows.append(['—', 'Basilaire ouest (1 étage) : aucune lettre sur le plan clé ; angles J et I', 'Phase 3 [lecture]'])
    rows.append(['—', 'Saillie sud avec portes de garage (▲▼) : quai des ambulances', 'Phase 3 [lecture] ; C-34, §6 de 03'])
    zones_tab = box(40, 634, 940, 282, table(rows, ['48px', '640px', '250px'], size=9.5), 'Zones A à L et parties de bâtiment')
    # élévations
    rows = [['Élév.', 'Titre (feuille 011)', 'Face vue [lecture]']]
    faces = {'A': 'sud (basilaire sud et tour)', 'B': 'ouest (basilaire ouest et tour)', 'C': 'ouest, partielle — jonction basilaire est / saillie', 'D': 'est, partielle — saillie sud (G)', 'E': 'ouest, partielle — angle sud-ouest (I)', 'F': 'nord (basilaire nord, tour, archives)', 'G': 'est (basilaire est et tour)', 'H': 'nord, partielle — près des archives / K', 'I': 'ouest, partielle — près des archives / K'}
    for l, (anc, d, name) in ELEV.items(): rows.append([f'<b>{l}</b>', name, faces[l]])
    elev_tab = box(1000, 312, 592, 182, table(rows, ['40px', '200px', '352px'], size=9.5), 'Repères d\'élévation A à I (plan clé de la feuille 011)')
    # implantation
    impl = (f'<div class="box" style="left:1000px;top:96px;width:592px;height:210px"><div class="bt">Implantation existante (feuille 001) : issues et accès repérés par les architectes</div>'
            f'<img src="implantation.png" style="position:absolute;left:8px;top:22px;width:576px;height:auto;max-height:140px">'
            f'<div style="position:absolute;left:8px;top:164px;font-size:8.6px;color:#333;line-height:1.2">Légende 001/002 : ▲ issue ou accès au bâtiment (protection durant le chantier, AR-PLN-016) ; △ porte de garage ; borne-fontaine accessible en tout temps (AR-PLN-001) ; issues et chemins d\'évacuation maintenus, 1650 mm (AR-PLN-006) ; portes mises hors service repérées au plan (AR-PLN-007) ; plan d\'action avant tout travail près d\'une issue (AR-PLN-011).</div></div>')
    # points fixes
    rows = [['No', 'Point fixe ou accès à maintenir', 'Localisation écrite', 'Registre', 'Marque']]
    for no, lib, loc, ids, marque, _, _ in POINTS_FIXES: rows.append([f'<b>{no}</b>', lib, loc, ids, marque])
    pf = box(1000, 500, 592, 512, table(rows, ['24px', '222px', '142px', '108px', '84px'], size=8.4), 'Points fixes 24/7, unités critiques et accès (registre 02)')
    return ('<section class="planche">' + header(0, 'Lecture du site', 'Zones A à L, repères d\'élévation A à I, points fixes 24/7 et accès à maintenir — planche commune à toutes les options')
            + plan + zones_tab + impl + elev_tab + pf + footer(0, total, 'D2 feuilles 001, 002, 010, 011 (rendus 200 ppp) ; analyse/01-inventaire.md §8.5 ; analyse/02-contraintes.md ; analyse/03-phasage.md §2.1, §6.') + '</section>')

def zone_outline_layer():
    out = []
    for k, (p, short, fn, ph) in ZONES.items():
        out.append(poly(p, 'none', 0, '#111', 1.3))
    return ''.join(out)

# ---------- Planche 1 : option R (référence, V-A1) ----------
ORDER_R = [('1', 'Phase 1 — basilaire est (D, E, F)', (790, 470)), ('2', '2.N — tour, face nord', (459, 360)), ('3', '2.E — tour, face est', (662, 395)),
           ('4', '2.S — tour, face sud', (459, 500)), ('5', '2.O — tour, face ouest', (278, 430)), ('6', '3.N — basilaire nord (K, J, B)', (450, 335)),
           ('7', '3.O — basilaire ouest', (256, 470)), ('8', '3.S — basilaire sud (H, G, I)', (370, 528))]
CALLOUTS_R = [
 # code, sous-phase, quoi, IDs, (x,y) point, (lx,ly) étiquette
 ('T1', '1', 'IRM : volets coupe-feu de fenêtre, gicleur R-34 remplacé, entreplafond libéré ; métal interdit quand l\'IRM est en service', 'ME-010, 109, 110 ; AR-PLN-009, 058 ; CI-TAB-009', (712, 580), (820, 613)),
 ('T2', '1', 'Local R-22 : conduits EMT relocalisés avant les renforts A4-A6 (classe IV, J/S)', 'ME-108, 111 ; CI-TAB-010', (692, 522), (720, 613)),
 ('T3', '1', 'Salle des serveurs RC : arrêt court, semaine, hors été ; bi-bloc LG : récupération du réfrigérant, remise en marche', 'ME-088, 086', (930, 445), (985, 470)),
 ('T4', '1', 'IRM mobile : sorties d\'arrosage protégées, alcôve dans le revêtement', 'ME-116', (928, 372), (985, 320)),
 ('T5', '2.N', 'Conduits temporaires d\'alimentation et de retour hémodialyse / labo niv. 200 AVANT démolition ; coupures un conduit à la fois, dimanche hors été', 'ME-049 à 051', (380, 352), (330, 292)),
 ('T6', '2.N', 'Chambre 216 : conduit RAV prolongé hors échafaudages', 'ME-057', (540, 352), (640, 235)),
 ('T7', '2.E', 'Hotte de médecine nucléaire : conduit modifié sur toute la hauteur, supports temporaires, arrêt vendredi-dimanche', 'ME-118, 119', (676, 445), (870, 347)),
 ('T8', '2.S', 'Chambre 307 : démantèlement si inoccupée, conduit prolongé, grillage aviaire ; sectionneurs de thermopompes déposés', 'ME-056, 107', (540, 508), (600, 580)),
 ('T9', '2.O', 'PAF bloc opératoire : 2 conduits temporaires 900 x 900 sous le soffite AVANT démantèlement ; nouveau conduit APRÈS revêtement ; glycol déposé', 'ME-042 à 048 ; ME-084 ; [à confirmer] tour/basilaire', (272, 440), (140, 460)),
 ('T10', '3.N', 'Prise d\'air médical et boîtier HEPA temporaires SUR LA FAÇADE OUEST pendant 3.N ; bonbonnes ; 1re certification ; réinstallation après revêtement nord', 'ME-064 à 069, 072, 073', (272, 345), (205, 300)),
 ('T11', '3.N', 'Nouvelle issue du laboratoire et escalier no 7 : jalon ; classe IV « J » ; câbles souterrains protégés ; deux issues minimum maintenues', 'AR-DEV-058 ; AR-DEV-198 ; AR-PLN-013, 064 ; ST-039 ; CI-TAB-019', (470, 318), (530, 235)),
 ('T12', '3.N', 'Laboratoire : sortie d\'air par conduit temporaire hors échafaudages ; filtration V-53 ; échelle de toiture', 'ME-059 à 061 ; CI-TAB-023', (600, 318), (730, 250)),
 ('T13', '3.O', 'Évents d\'autoclaves relocalisés AVANT 3.O, tuyauteries temporaires en toiture jusqu\'au coin sud-ouest ; fenêtre nuit / avant 10 h ; câbles chauffants hors hiver', 'ME-075 à 083', (256, 480), (140, 500)),
 ('T14', '3.S', 'Quai des ambulances : gicleurs hors service 2 x 2 h, glycol ; enseigne ; caméra ; deux configurations d\'accès (détail 1, 002)', 'ME-006 à 008 ; ME-145 à 147 ; AR-PLN-014, 018', (532, 560), (560, 613)),
 ('T15', '3.S', 'Entrée principale : trois configurations autour de la marquise (détail 2, 002) ; plan d\'action d\'évacuation', 'AR-PLN-008, 019 ; CI-TAB-014', (420, 548), (450, 613)),
 ('T16', '3.S', 'Persienne UT-2 : coupure rapide nuit ou fin de semaine, filtration et grillage temporaires ; bi-bloc GREE de l\'urgence', 'ME-055, 085, 090', (360, 548), (330, 613)),
]

def planche1(total):
    inner = []
    # aplats par phase et sous-phase
    for k, (p, short, fn, ph) in ZONES.items():
        if ph == '1': inner.append(poly(p, PHASE_FILL['1'], 0.6, '#0d3b75', 1.5))
        elif ph == 'non touché': inner.append(poly(p, 'url(#hatch)', 0.9, '#666', 1))
    inner.append(poly(ZONES['A'][0], '#a5d6a7', 0.35, '#1b5e20', 1.5))
    for f, p in FACES_TOUR.items(): inner.append(poly(p, FACE_FILL[f], 0.85, '#fff', 0.8))
    for k in ('J', 'B', 'K'): inner.append(poly(ZONES[k][0], P3_FILL['3.N'], 0.7, '#7a3300', 1.2))
    inner.append(poly(ZONES['O'][0], P3_FILL['3.O'], 0.7, '#7a3300', 1.2))
    for k in ('I', 'H', 'G', 'P'): inner.append(poly(ZONES[k][0], P3_FILL['3.S'], 0.7, '#7a3300', 1.2))
    inner.append(zone_labels())
    for l, (anc, d, name) in ELEV.items(): inner.append(view_arrow(l, anc, d, '#555'))
    # ordre
    for no, lab, (x, y) in ORDER_R:
        inner.append(badge(x - OFF[0], y - OFF[1], no, '#111', 13, 14, '#fff'))
    # installations temporaires : hachures magenta sur les faces concernées
    inner.append(poly([(268,352),(272,352),(272,508),(268,508)], '#8e24aa', 0.9, 'none', 0))   # face ouest de la tour : PAF BO temporaire
    inner.append(poly([(243,335),(272,335),(272,352),(243,352)], 'url(#hatchm)', 1, '#8e24aa', 1.2))  # prise d'air médical temporaire, angle nord-ouest, façade ouest
    inner.append(poly([(243,352),(250,352),(250,548),(243,548)], 'url(#hatchm)', 1, '#8e24aa', 1))  # tuyauteries temporaires d'évents jusqu'au coin sud-ouest
    for code, sp, quoi, ids, (px, py), (lx, ly) in CALLOUTS_R:
        x, y = px - OFF[0], py - OFF[1]; bx, by = lx - OFF[0], ly - OFF[1]
        inner += [leader(bx, by, x, y, '#8e24aa', '2,2'), dot(x, y, '#8e24aa'), tag(bx, by, code, '#8e24aa', 30, 15, 10.5)]
        if bx > 900: inner.append(txt(bx - 18, by + 4, ids.split(' ;')[0], 8.5, 'end', 'normal', '#5e1a75'))
        else: inner.append(txt(bx + 18, by + 4, ids.split(' ;')[0], 8.5, 'start', 'normal', '#5e1a75'))
    plan = plan_figure(40, 96, ''.join(inner), 940, dim=0.55) + '<div class="cap" style="left:40px;top:606px;width:940px">Aplats : phase 1 en bleu ; tour en vert clair avec ses faces 2.N, 2.E, 2.S, 2.O en bandes vertes ; 3.N, 3.O, 3.S en oranges ; hachures grises = secteur non touché. Numéros noirs = ordre de référence [choix]. Étiquettes T1 à T16 (magenta) = installations et mesures temporaires, listées à droite avec leurs identifiants ; hachures magenta = emplacement écrit des installations temporaires de la façade ouest (T9, T10, T13).</div>'
    # séquence en une ligne
    seq = ('<div class="seq"><span class="s0">0 Préalables et mobilisation</span> → <span class="s1">1 Basilaire est</span> → '
           '<span class="s2">2 Tour : N → E → S → O</span> → <span class="s3">3 Basilaires : nord → ouest ; sud en parallèle</span> → <span class="s4">4 Clôture</span>'
           '<div class="seqn">Ordre 1 → 2 → 3 : numérotation du plan clé [lecture], aucun texte ne l\'impose (Z-23). Nord avant ouest : lecture de ME-065/067 (prise d\'air médical temporaire sur la façade ouest pendant la façade nord). Ordre des faces de la tour : [choix], seules règles écrites ME-049 (conduits temporaires avant démolition nord/ouest) et ME-118 (conduit de médecine nucléaire modifié pour permettre les façades). Correction des anomalies avant chaque phase suivante (AR-DEV-275). Repères des architectes, feuille 010 : phase 1 « ±5 mois », phase 2 « ±8 mois », phase 3 « ±4 mois » (C-34) — aucun calendrier n\'en est déduit.</div></div>')
    seqbox = box(40, 634, 940, 74, seq)
    # élévations concernées par sous-phase
    elev_map = [('1', 'G (est) ; C (ouest partielle, jonction) ; D (est partielle) ?', '#3b7dd8'), ('2.N', 'F (nord), partie haute', FACE_FILL['2.N']), ('2.E', 'G (est), partie haute', FACE_FILL['2.E']),
                ('2.S', 'A (sud), partie haute', FACE_FILL['2.S']), ('2.O', 'B (ouest), partie haute', FACE_FILL['2.O']), ('3.N', 'F (nord) partie basse ; H, I (partielles)', P3_FILL['3.N']),
                ('3.O', 'B (ouest) partie basse ; E (ouest partielle)', P3_FILL['3.O']), ('3.S', 'A (sud) partie basse ; D (est partielle) ; C ?', P3_FILL['3.S'])]
    rows = [['Sous-phase', 'Élévations de la feuille 011 concernées [lecture]']]
    for sp, el, col in elev_map: rows.append([f'<span class="sw" style="background:{col}"></span><b>{sp}</b>', el])
    elev_tab = box(40, 712, 460, 200, table(rows, ['90px', '360px'], size=9.5), 'Élévations par sous-phase (correspondance zones ↔ élévations non écrite, Z-24)')
    # vignettes des élévations
    thumbs = ''.join(f'<div class="th"><img src="../img/A011_elev_{l}.png"><div>{l} — {html.escape(ELEV[l][2])}</div></div>' for l in 'ABFG')
    thumbs2 = ''.join(f'<div class="th s"><img src="../img/A011_elev_{l}.png"><div>{l} — {html.escape(ELEV[l][2])}</div></div>' for l in 'CDEHI')
    elev_box = box(508, 712, 472, 200, f'<div class="ths">{thumbs}</div><div class="ths">{thumbs2}</div>', 'Élévations A à I (feuille 011, rendus)')
    # tableau des mesures temporaires
    rows = [['Code', 'Sous-phase', 'Installation ou mesure temporaire dessinée', 'Registre']]
    for code, sp, quoi, ids, _, _ in CALLOUTS_R: rows.append([f'<b>{code}</b>', sp, quoi, ids])
    call_tab = box(1000, 96, 592, 438, table(rows, ['32px', '44px', '350px', '166px'], size=8.6), 'Installations temporaires électromécaniques et mesures propres à chaque sous-phase (registre 02, fiches de 03 §2.2 à §2.4)')
    # 002 : configurations
    det = (f'<div class="box" style="left:1000px;top:540px;width:592px;height:280px"><div class="bt">3.S — configurations successives des accès (feuille 002) : ambulances en deux configurations (AR-PLN-018), entrée principale en trois (AR-PLN-019) ; les chiffres « phase 1/2/3 » sont propres à la feuille 002 (C-34)</div>'
           f'<img src="../img/A002_det1.png" style="position:absolute;left:8px;top:36px;height:238px"><img src="../img/A002_det2.png" style="position:absolute;left:222px;top:44px;width:362px">'
           f'<div style="position:absolute;left:222px;top:178px;width:362px;font-size:9px;color:#333;line-height:1.28">Orientation du détail 1 non écrite : « entrée ambulance sud » selon D4/D5 (ME-006, ME-147), « zone ambulance (nord) » selon AR-PLN-004 — voir 03 §6. Un panneau temporaire par configuration (AR-PLN-014) ; préavis de 3 semaines avant tout déplacement de voie (AR-DEV-139) ; durée devant les portes de garage limitée (R-20).</div></div>')
    issues = box(1000, 826, 592, 186, '<div style="font-size:10px;line-height:1.32">Nouvelle issue permanente au laboratoire (zone B, niveau 100) : jalon du calendrier (AR-DEV-058), classe IV horaire « J » (CI-TAB-019), percements hors heures d\'occupation (ME-020). Deux issues minimum et capacité d\'évacuation maintenue dans les secteurs occupés (AR-DEV-198). <b>Aucune issue condamnée n\'est écrite</b> : à chaque issue touchée par une sous-phase, plan d\'action préalable (AR-PLN-011), maintien du chemin d\'évacuation à 1650 mm (AR-PLN-006) ou escalier d\'issue temporaire modulaire incombustible (AR-DEV-311, 195), repérage des portes hors service (AR-PLN-007). Ordre nouvelle issue / condamnation : non écrit (Z-12, K4 ; variantes V-K4a/b/c).</div>', 'Issues : nouvelle issue, issues touchées et compensation')
    return ('<section class="planche">' + header(1, 'Option R (référence) — plan', 'Découpage A par secteurs du plan clé ; ordre 0 → 1 → 2 (N, E, S, O) → 3 (N → O ; S) → 4 ; installations temporaires au bon endroit et au bon moment')
            + plan + seqbox + elev_tab + elev_box + call_tab + det + issues + footer(1, total, 'D2 feuilles 002, 010, 011 ; D4/D5 via le registre (ME-…) ; analyse/03-phasage.md §2.2 à §2.7 (V-A1), §6 ; analyse/04-verification.md §8.') + '</section>')

CSS = """
@page { size: 17in 11in; margin: 0; }
body { margin: 0; font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif; color: #1a1a1a; }
.planche { position: relative; width: 1632px; height: 1056px; overflow: hidden; page-break-after: always; background: #fff; }
.planche:last-child { page-break-after: auto; }
.hdr { position: absolute; left: 40px; top: 26px; right: 40px; height: 62px; border-bottom: 2px solid #17324d; }
.h1 { font-size: 22px; font-weight: bold; color: #17324d; }
.h2 { font-size: 12px; color: #24486b; margin-top: 3px; }
.proj { position: absolute; right: 0; top: 2px; font-size: 10px; color: #444; text-align: right; width: 520px; }
.ftr { position: absolute; left: 40px; right: 40px; bottom: 16px; font-size: 8.3px; color: #444; border-top: 1px solid #b8c4d0; padding-top: 4px; display: flex; gap: 16px; }
.ftr .conv { flex: 1; } .ftr .pg { font-weight: bold; color: #17324d; white-space: nowrap; }
.box { position: absolute; border: 1px solid #b8c4d0; background: #fff; box-sizing: border-box; overflow: hidden; padding: 4px 6px; }
.bt { font-size: 10.5px; font-weight: bold; color: #17324d; margin-bottom: 3px; }
table.t { border-collapse: collapse; width: 100%; table-layout: fixed; }
table.t th, table.t td { border: 1px solid #c9d1da; padding: 1.5px 3px; vertical-align: top; text-align: left; line-height: 1.22; overflow-wrap: break-word; }
table.t th { background: #e8edf2; }
.sw { display: inline-block; width: 10px; height: 10px; margin-right: 4px; vertical-align: middle; border: 1px solid #555; }
.seq { font-size: 12px; font-weight: bold; color: #17324d; }
.seq span { padding: 2px 6px; border-radius: 3px; color: #fff; }
.s0 { background: #607d8b; } .s1 { background: #3b7dd8; } .s2 { background: #2e7d32; } .s3 { background: #ef6c00; } .s4 { background: #455a64; }
.cap { position: absolute; font-size: 9.3px; color: #333; line-height: 1.25; }
.seqn { font-size: 9.3px; font-weight: normal; color: #333; margin-top: 6px; line-height: 1.3; }
.ths { display: flex; gap: 6px; margin-top: 2px; }
.th { flex: 1; font-size: 8px; color: #333; text-align: center; }
.th img { width: 100%; height: 52px; object-fit: contain; border: 1px solid #ddd; background: #fff; }
.th.s img { height: 60px; }
"""

def main():
    args = sys.argv[1:]
    which = [0, 1]
    if '--planches' in args: which = [int(x) for x in args[args.index('--planches') + 1].split(',')]
    out = pathlib.Path(args[args.index('--out') + 1]) if '--out' in args else BUILD / 'apercu.pdf'
    prep_images()
    builders = {0: planche0, 1: planche1}
    total = len(which)
    body = ''.join(builders[n](total) for n in which)
    doc = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Cahier de phasage graphique</title><style>{CSS}</style></head><body>{body}</body></html>'
    htmlp = BUILD / 'planches.html'; htmlp.write_text(doc, encoding='utf-8')
    r = subprocess.run(['node', str(ROOT / 'src' / 'topdf.cjs'), str(htmlp), str(out)], capture_output=True, text=True)
    print(r.stdout, r.stderr[-1500:])

if __name__ == '__main__':
    main()
