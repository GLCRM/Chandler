"""Cahier de phasage graphique — 14 planches tabloïd paysage (HTML + SVG -> PDF via Chromium).
Usage : python3 src/build_planches.py [--out phasage/plan-phasage-graphique.pdf]
Règles : aucun texte sous 9 pt (12 px à 96 px/po ; 13 unités dans le calque SVG du plan) ; toute position lue sur un plan est [lecture]."""
import sys, pathlib, subprocess, html, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from zones import ZONES, FACES_TOUR, ELEV, CROP, OFF, shift
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
IMG = ROOT / 'img'; BUILD = ROOT / 'build'; BUILD.mkdir(exist_ok=True)
S = 0.94  # 1000 x 540 unités SVG -> 940 x 508 px
BOT = 1002  # bas commun des boîtes ; le pied de page occupe 1008-1044 px
FSCALE = 1.0  # multiplicateur des tailles de texte SVG, fixé par plan_figure selon la largeur d'affichage

def prep_images():
    Image.open(IMG / 'A010_plan_cle.png').crop(CROP).save(BUILD / 'plan.png')
    Image.open(IMG / 'A001_implantation.png').crop((400, 200, 3000, 1950)).save(BUILD / 'implantation.png')

# ------------------------------------------------------------------ SVG
def pts(poly): return ' '.join(f'{x},{y}' for x, y in shift(poly))
def poly(polyg, fill, op=0.55, stroke='#333', sw=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polygon points="{pts(polyg)}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def txt(x, y, s, size=13, anchor='start', weight='normal', fill='#111'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="font-size:{round(size * FSCALE, 1)}px;font-weight:{weight};fill:{fill}">{html.escape(s)}</text>'
def badge(x, y, label, fill='#111', r=14, size=14):
    r = r * FSCALE
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#fff" stroke-width="2"/>' + txt(x, y + size * 0.36, label, size, 'middle', 'bold', '#fff')
def tag(x, y, label, fill='#8e24aa', w=36, h=19, size=13):
    w, h = w * FSCALE, h * FSCALE
    return f'<rect x="{x - w/2}" y="{y - h/2}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="#fff" stroke-width="1"/>' + txt(x, y + size * 0.36, label, size, 'middle', 'bold', '#fff')
def leader(x1, y1, x2, y2, color='#333', dash='3,2'): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.2" stroke-dasharray="{dash}"/>'
def dot(x, y, color='#333', r=3.5): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="#fff" stroke-width="1"/>'
def diverg(x, y, size=13):
    """Pictogramme « localisation divergente » : triangle orange avec point d'exclamation."""
    return (f'<polygon points="{x},{y-size} {x+size*0.95},{y+size*0.7} {x-size*0.95},{y+size*0.7}" fill="#f57c00" stroke="#7a3300" stroke-width="1.2"/>'
            + txt(x, y + size * 0.55, '!', max(size + 1, 14), 'middle', 'bold', '#fff'))
DEFS = ('<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>'
        '<marker id="arb" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#17324d"/></marker>'
        '<marker id="arm" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#8e24aa"/></marker>'
        '<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="#777" stroke-width="1.2"/></pattern>'
        '<pattern id="hatchm" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#8e24aa" stroke-width="1.8"/></pattern>'
        '<pattern id="hatchb" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="#1565c0" stroke-width="1.4"/></pattern></defs>')
def view_arrow(letter, anchor, direction, color='#0d47a1'):
    x, y = anchor[0] - OFF[0], anchor[1] - OFF[1]
    dx, dy = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}[direction]
    return (f'<line x1="{x}" y1="{y}" x2="{x + dx*24}" y2="{y + dy*24}" stroke="{color}" stroke-width="2.2" marker-end="url(#ar)"/>'
            f'<circle cx="{x}" cy="{y}" r="12" fill="#fff" stroke="{color}" stroke-width="2"/>' + txt(x, y + 5, letter, 14, 'middle', 'bold', color))
ZPOS = {'A': (459, 430), 'B': (486, 333), 'J': (318, 333), 'K': (625, 333), 'O': (256, 430), 'I': (290, 528), 'H': (430, 528), 'G': (616, 528), 'D': (790, 440), 'F': (725, 585), 'E': (845, 585), 'L': (952, 530), 'C': (459, 160)}
def zone_labels():
    out = []
    for k, (x, y) in ZPOS.items():
        x, y = x - OFF[0], y - OFF[1]
        if k == 'O':
            out.append(f'<rect x="{x-11}" y="{y-11}" width="22" height="22" fill="#fff" stroke="#111" stroke-width="1.3" stroke-dasharray="3,2"/>' + txt(x, y + 5, 'O', 14, 'middle', 'bold'))
        else:
            out.append(f'<rect x="{x-10}" y="{y-10}" width="20" height="20" transform="rotate(45 {x} {y})" fill="#fff" stroke="#111" stroke-width="1.3"/>' + txt(x, y + 5, k, 13, 'middle', 'bold'))
    return ''.join(out)
def outlines(): return ''.join(poly(p, 'none', 0, '#111', 1.4) for p, *_ in ZONES.values())
def set_scale(width):
    global FSCALE; FSCALE = round(940 / width, 3)
def plan_figure(left, top, inner, width=940, dim=0.0):
    h = round(width * 0.54)
    veil = f'<div style="position:absolute;left:0;top:0;width:{width}px;height:{h}px;background:rgba(255,255,255,{dim})"></div>' if dim else ''
    return (f'<div class="plan" style="left:{left}px;top:{top}px;width:{width}px;height:{h}px"><img src="plan.png" style="position:absolute;left:0;top:0;width:{width}px;height:{h}px">{veil}'
            f'<svg viewBox="0 0 1000 540" width="{width}" height="{h}" style="position:absolute;left:0;top:0" xmlns="http://www.w3.org/2000/svg">{DEFS}{inner}</svg></div>')

# ------------------------------------------------------------------ HTML
def box(left, top, width, height, inner, title=None, id=''):
    t = f'<div class="bt">{title}</div>' if title else ''
    return f'<div class="box" id="{id}" style="left:{left}px;top:{top}px;width:{width}px;height:{height}px">{t}{inner}</div>'
def table(rows, widths, header=True, cls=''):
    out = [f'<table class="t {cls}"><colgroup>' + ''.join(f'<col style="width:{w}">' for w in widths) + '</colgroup>']
    for i, r in enumerate(rows):
        tg = 'th' if header and i == 0 else 'td'
        out.append('<tr>' + ''.join(f'<{tg}>{c}</{tg}>' for c in r) + '</tr>')
    return ''.join(out) + '</table>'
def header(num, title, sub):
    return (f'<div class="hdr"><div class="h1">Planche {num - 1} — {title}</div><div class="h2">{sub}</div>'
            f'<div class="proj">Hôpital de Chandler — Réfection de l\'enveloppe · CISSS de la Gaspésie · AOC-077221 · Dossier GLCRM R-657-24<br>Cahier de phasage graphique — document de travail, non contractuel, sans durée</div></div>')
def footer(num, total, sources):
    return (f'<div class="ftr"><div><b>Sources :</b> {sources}</div>'
            f'<div><b>Conventions :</b> [lecture] = lu sur un plan, non écrit ; [à confirmer] = non fixé par les documents ; <span class="picto">!</span> = localisation divergente entre documents ; AR-DEV-, AR-PLN-, ME-, ST-, CI- = lignes du registre 02 ; C-, Z-, R-, K- = contradictions, zones d\'ombre, renvois, conflits de 03.</div>'
            f'<span class="pg">page {num} / {total}</span></div>')

# ------------------------------------------------------------------ données
FILL = {'1': '#3b7dd8', '2': '#a5d6a7', '3': '#f0a830'}
FACE_FILL = {'2.N': '#1b5e20', '2.E': '#2e7d32', '2.S': '#66bb6a', '2.O': '#00695c'}
P3_FILL = {'3.N': '#e65100', '3.O': '#ef6c00', '3.S': '#ffb300'}
SP_LABEL = {'0': 'Phase 0 — préalables', '1': 'Phase 1 — basilaire est (D, E, F)', '2.N': '2.N — tour, face nord', '2.E': '2.E — tour, face est', '2.S': '2.S — tour, face sud', '2.O': '2.O — tour, face ouest',
            '3.N': '3.N — basilaire nord (K, J, B)', '3.O': '3.O — basilaire ouest (O ; angles J, I)', '3.S': '3.S — basilaire sud (H, G, I)', '4': 'Phase 4 — clôture',
            'B-A': 'B-A — rez-de-chaussée (A.1 à A.7)', 'B-B': 'B-B — niveau 1 et sous-sol (B.1.2, B.1.3, B.2.1, B.2.2)', 'B-C': 'B-C — tour, niveaux 2 à 4 (C.2, C.4, C.5)'}
BADGE_POS = {'1': (790, 470), '2.N': (459, 360), '2.E': (662, 395), '2.S': (459, 500), '2.O': (278, 430), '3.N': (450, 335), '3.O': (256, 470), '3.S': (370, 528)}
OPTIONS = {
 'R': dict(nom='Option R — référence', ordre=['1', '2.N', '2.E', '2.S', '2.O', '3.N', '3.O', '3.S'], chips=['0 Préalables', '1 Basilaire est', '2 Tour : N → E → S → O', '3 Basilaires : nord → ouest ; sud en parallèle', '4 Clôture'],
             fondement='Numérotation du plan clé 010 [lecture] ; nord avant ouest déduit de ME-065/067 [lecture] ; ordre des faces de la tour [choix] (seules règles écrites : ME-049, ME-118).'),
 'A2': dict(nom='Option A2 — basilaires avant la tour', ordre=['1', '3.N', '3.O', '3.S', '2.N', '2.E', '2.S', '2.O'], chips=['0 Préalables', '1 Basilaire est', '3 Basilaires : nord → ouest ; sud', '2 Tour : N → E → S → O', '4 Clôture'],
              fondement='Regrouper les deux basilaires avant la tour [choix] ; aucun texte ne lie la tour aux basilaires ; nord avant ouest [lecture] de ME-065/067.'),
 'A3': dict(nom='Option A3 — tour d\'abord', ordre=['2.N', '2.E', '2.S', '2.O', '1', '3.N', '3.O', '3.S'], chips=['0 Préalables', '2 Tour : N → E → S → O', '1 Basilaire est', '3 Basilaires : nord → ouest ; sud', '4 Clôture'],
              fondement='Tour d\'abord [choix] ; prototype de fenêtre et de mur-rideau alors dans la tour (AR-PLN-050) ; échafaudage de la tour sur des toitures non refaites [lecture].'),
 'B': dict(nom='Option B — par niveaux (tableau CISSS)', ordre=['B-A', 'B-B', 'B-C'], chips=['0 Préalables', 'B-A Rez-de-chaussée : A.1 → A.7', 'B-B Niveau 1 et sous-sol : B.1.2 → B.2.2', 'B-C Tour : C.2 → C.4 → C.5', '4 Clôture'],
             fondement='Sous-phases du tableau des contraintes du CISSS (D11) reprises telles qu\'écrites ; leur ordre numérique est une [lecture] (C-30, Z-02).'),
}
# étiquettes T : code, sous-phase (découpage A), sous-phase (découpage B), texte court, registre, point (x,y), étiquette (x,y), face écrite
CALLOUTS = [
 ('T1', '1', 'A.6', 'IRM : volets coupe-feu de fenêtre, gicleur R-34 remplacé ; métal interdit quand l\'IRM est en service', 'ME-010, 109, 110 ; AR-PLN-009 ; CI-TAB-009', (712, 580), (820, 613), 'est'),
 ('T2', '1', 'A.6', 'Local R-22 : conduits EMT relocalisés avant les renforts A4-A6 (classe IV, J/S)', 'ME-108, 111 ; CI-TAB-010', (692, 522), (720, 613), 'est'),
 ('T3', '1', 'A', 'Salle des serveurs RC : arrêt court, semaine, hors été ; bi-bloc LG remis en marche', 'ME-088, 086', (930, 445), (985, 470), 'est'),
 ('T4', '1', 'A.1', 'IRM mobile : sorties d\'arrosage protégées, alcôve dans le revêtement', 'ME-116', (928, 372), (985, 320), 'est'),
 ('T5', '2.N', 'C.2', 'Hémodialyse / labo niv. 200 : conduits temporaires AVANT démolition ; coupures dimanche hors été', 'ME-049 à 051', (380, 352), (330, 292), 'nord'),
 ('T6', '2.N', 'C.2', 'Chambre 216 : conduit RAV prolongé hors échafaudages', 'ME-057', (540, 352), (640, 235), 'nord'),
 ('T7', '2.E', 'C', 'Hotte de médecine nucléaire : conduit modifié sur toute la hauteur ; arrêt vendredi-dimanche', 'ME-118, 119', (676, 445), (870, 347), 'est'),
 ('T8', '2.S', 'C.4', 'Chambre 307 : démantèlement si inoccupée, conduit prolongé, grillage ; sectionneurs de thermopompes déposés', 'ME-056, 107', (540, 508), (600, 580), 'sud'),
 ('T9', '2.O', 'B-C', 'PAF bloc opératoire : 2 conduits temporaires AVANT démantèlement ; nouveau conduit APRÈS revêtement ; glycol déposé', 'ME-042 à 048, 084', (272, 440), (140, 460), 'ouest'),
 ('T10', '3.N', 'B', 'Air médical : prise et HEPA temporaires SUR LA FAÇADE OUEST pendant la façade nord ; bonbonnes ; 1re certification', 'ME-064 à 069, 072, 073', (272, 345), (205, 300), 'ouest'),
 ('T11', '3.N', 'B.1.2', 'Nouvelle issue du laboratoire, escalier no 7 : jalon ; classe IV « J » ; deux issues minimum maintenues', 'AR-DEV-058, 198 ; AR-PLN-064 ; ST-039 ; CI-TAB-019', (470, 318), (530, 235), 'nord'),
 ('T12', '3.N', 'B', 'Laboratoire : sortie d\'air par conduit temporaire hors échafaudages ; filtration V-53', 'ME-059 à 061', (600, 318), (730, 250), 'nord'),
 ('T13', '3.O', 'B', 'Évents d\'autoclaves relocalisés AVANT la façade ouest, temporaires en toiture jusqu\'au coin sud-ouest ; nuit ou avant 10 h', 'ME-075 à 083', (256, 480), (140, 500), 'ouest'),
 ('T14', '3.S', 'A.1', 'Quai des ambulances : gicleurs hors service 2 x 2 h, glycol ; enseigne ; caméra', 'ME-006 à 008, 145 à 147', (532, 560), (560, 613), 'sud'),
 ('T15', '3.S', 'A.1', 'Entrée principale : trois configurations autour de la marquise ; plan d\'action d\'évacuation', 'AR-PLN-008, 019 ; CI-TAB-014', (420, 548), (450, 613), 'sud'),
 ('T16', '3.S', 'B', 'Persienne UT-2 : coupure rapide nuit ou fin de semaine ; bi-bloc GREE de l\'urgence', 'ME-055, 085, 090', (360, 548), (330, 613), 'sud'),
]
FN_COURT = {'A': 'Tour des chambres, niveaux 200 à 400 (1974)', 'B': 'Laboratoire, niveau 100 (1990) — basilaire nord', 'C': 'Archives, RC (2001)', 'D': 'Administration niv. 100 et cliniques externes RC — basilaire est', 'E': 'Oncologie, RC (1974)', 'F': 'IRM, RC (2007)', 'G': 'Basilaire sud-est, 1 étage', 'H': 'Chirurgie d\'un jour niv. 100 et urgence RC — basilaire sud', 'I': 'Basilaire sud-ouest, 1 étage', 'J': 'Basilaire nord-ouest, 1 étage', 'K': 'Basilaire nord-est, 1 étage', 'L': 'Oncologie, RC (2023)'}
POINTS_FIXES = [
 ('1', 'Prise d\'air frais du bloc opératoire — 24/7, conduits temporaires', '« Façade ouest (tour) », « toiture ouest » — [à confirmer] tour ou basilaire', 'ME-042 à 048', (272, 440), (205, 465)),
 ('2', 'Évents des autoclaves (sous-sol) — 24/7, relocalisés avant la façade ouest', '« Façade ouest », toiture ; temporaires jusqu\'au coin sud-ouest', 'ME-075 à 079', (257, 475), (205, 495)),
 ('3', 'Centrale d\'air médical — 24/7 ; prise temporaire sur la façade ouest', '« Toiture nord-ouest » — [à confirmer] tour ou basilaire', 'ME-064 à 068', (300, 335), (205, 335)),
 ('4', 'Ventilation hémodialyse / laboratoire, niveau 200 — conduits temporaires', '« Façades nord/ouest » de la tour — [à confirmer] locaux 202-237', 'ME-049 à 054', (380, 356), (330, 292)),
 ('5', 'IRM — métal interdit quand l\'IRM est en service ; volets coupe-feu', 'Zone F (RC)', 'AR-PLN-009 ; ME-010, 109, 110', (705, 560), (705, 613)),
 ('6', 'Urgence (RC, zone H) et quai des ambulances — gicleurs 2 × 2 h', '« Entrée ambulance sud » (D4, D5) contre « zone ambulance (nord) » (D2) — [lecture] garage ▲▼', 'ME-006 à 008, 145 à 147 ; AR-PLN-004, 018', (532, 556), (585, 613)),
 ('7', 'Entrée principale et marquise — accès maintenu, trois configurations', 'Zone H ; détail 2 de la feuille 002 — [lecture] marquise au sud', 'AR-PLN-008, 019 ; CI-TAB-014', (420, 550), (450, 613)),
 ('8', 'Nouvelle issue du laboratoire (niveau 100) — jalon ; escalier no 7', 'Zone B ; « basilaire nord-ouest » — [à confirmer] escalier no 7 = issue (Z-12)', 'AR-DEV-058, 198 ; AR-PLN-064 ; ST-039', (470, 320), (590, 235)),
 ('9', 'Chambres 216 (nord) et 307 (sud) ; soins intensifs 315', 'Façade nord ; façade sud ; ligne D5 N-F-V-009', 'ME-056 à 058', (560, 356), (650, 235)),
 ('10', 'Hotte de médecine nucléaire — conduit modifié sur toute la hauteur', '« Tour est »', 'ME-117 à 119', (662, 445), (735, 300)),
 ('11', 'Prises d\'air et registres du service alimentaire, sous-sol — classe IV « S »', 'Niveau SS, « zone A » — [à confirmer] sous-sol non zoné', 'CI-TAB-005 ; ME-025, 029', (520, 480), (600, 480)),
 ('12', 'Local R-22 — renforts des colonnes A4, A5, A6 (classe IV, J/S)', '« Secteur IRM / local R-22 (RC) » ; zone C au tableau CISSS — [à confirmer]', 'ME-108, 111 ; CI-TAB-010 ; C-40', (690, 525), (790, 613)),
 ('13', 'Salle des serveurs RC ; bi-bloc LG 18 MBH', '« Façade est »', 'ME-086, 088', (930, 440), (985, 470)),
 ('14', 'Persienne UT-2 (chirurgie d\'un jour) — coupure rapide', '« Façade sud »', 'ME-055', (380, 548), (320, 613)),
 ('15', 'Stationnement de l\'IRM mobile — sorties d\'arrosage', '« Coin nord-est » (D4) ; lignes D5 sud et nord — [à confirmer]', 'ME-116 ; CI-TAB-017', (928, 372), (985, 345)),
 ('16', 'Évents de la chaufferie (porte-à-faux) — 24/7 ; soffite du coin nord-ouest', '« Porte-à-faux », « coin nord-ouest » — [à confirmer] face (C-28)', 'ME-080, 096, 120 à 123', (262, 340), (205, 300)),
]
# matrice phase x système (03 §2.8 corrigé) : C coupure, P provisoire, I intervention classée, M maintenu, ? localisation non écrite
SYSTEMES = [  # matrice phase x système (03 §2.8 corrigé) — codes courts : C coupure, P provisoire, I intervention classée, M maintenu, ? localisation non écrite
 ('Gicleurs du quai des ambulances (ME-006 à 008)', {'3.S': 'C 2×2 h'}),
 ('Gicleurs des zones de plafond (ME-009 à 012)', {'1': 'I R-34', '3.S': 'P'}),
 ('Alarme incendie (ME-091 à 095, 097)', {'1': 'M', '3.N': 'M+issue', '3.S': 'P détect.', '4': 'cert.'}),
 ('PAF bloc opératoire, glycol (ME-042 à 048, 084)', {'2.O': 'P? C nuit', '3.O': 'P?', '4': 'mise en serv.'}),
 ('Évents d\'autoclaves, câbles chauffants (ME-075 à 083)', {'2.O': 'P?', '3.O': 'C→P→M'}),
 ('Air médical (ME-064 à 074)', {'2.N': 'M?', '2.O': 'M?', '3.N': 'P+cert.', '3.O': 'P→M', '4': 'cert.'}),
 ('Hémodialyse / labo niv. 200 (ME-049 à 054)', {'2.N': 'P ; C dim.', '2.O': 'P ; C dim.'}),
 ('Chambres 216 et 307 (ME-057, 056)', {'2.N': 'P (216)', '2.S': 'C→P (307)'}),
 ('Tour, face non écrite : bi-bloc 203 (ME-087), chambre 315 (ME-058), service alimentaire SS (CI-TAB-005)', {'2.N': 'C? I?', '2.E': 'C? I?', '2.S': 'C? I?', '2.O': 'C? I?'}),
 ('Hotte de médecine nucléaire (ME-117 à 119)', {'2.E': 'C→P'}),
 ('UT-2 et bi-bloc GREE de l\'urgence (ME-055, 085, 090)', {'3.S': 'C→P'}),
 ('Évacuations du laboratoire, V-53 (ME-059 à 061)', {'3.N': 'P'}),
 ('Bi-blocs est : serveurs RC, LG (ME-086, 088)', {'1': 'C ; C→P', '2.E': 'M?'}),
 ('Caméra, détecteur, contrôle d\'accès, enseigne (ME-099, 145 à 147)', {'3.N': 'M+KT-1', '3.S': 'P ; C'}),
 ('Lecteurs, luminaires, persiennes non touchées (ME-063, 104 à 106)', {k: 'P→M' for k in ['1', '2.N', '2.E', '2.S', '2.O', '3.N', '3.O', '3.S']}),
]
SYSTEMES_B = [  # 03 §3.6
 ('Gicleurs du quai des ambulances (ME-006 à 008)', {'B-A': 'C 2×2 h (A.1)'}),
 ('Alarme incendie (ME-091 à 095, 097)', {'B-A': 'M', 'B-B': 'M+issue ; P détect.', '4': 'cert.'}),
 ('PAF bloc opératoire, glycol (ME-042 à 048, 084)', {'B-A': 'P?', 'B-B': 'P?', 'B-C': 'P (« tour »)', '4': 'mise en serv.'}),
 ('Évents d\'autoclaves, câbles chauffants (ME-075 à 083)', {'B-A': 'P?', 'B-B': 'P ; C nuit ; hors hiver'}),
 ('Air médical (ME-064 à 074)', {'B-B': 'P+cert. (tour ?)', 'B-C': 'M?', '4': 'cert.'}),
 ('Hémodialyse / labo niv. 200 (ME-049 à 054)', {'B-C': 'P ; C dim. (C.2)'}),
 ('Chambres 216 et 307 (ME-057, 056)', {'B-C': 'P (C.2) ; C→P (C.4)'}),
 ('Tour : bi-bloc 203 (ME-087), chambre 315 (ME-058)', {'B-C': 'C semaine (C.2) ; I (C.4)'}),
 ('Hotte de médecine nucléaire (ME-117 à 119)', {'B-C': 'C→P'}),
 ('UT-2 chirurgie d\'un jour (ME-055)', {'B-B': 'C→P'}),
 ('Évacuations du laboratoire, V-53 (ME-059 à 061)', {'B-B': 'P'}),
 ('Sous-sol : service alimentaire (CI-TAB-005 ; ME-025, 029), atelier S17 (ME-062)', {'B-B': 'I (B.1.2) ; C durée du secteur'}),
 ('Bi-blocs est : serveurs RC, LG (ME-086, 088)', {'B-A': 'C ; C→P'}),
 ('Bi-bloc GREE de l\'urgence (ME-085, 090)', {'B-A': 'C→P→M'}),
 ('Caméra, détecteur, contrôle d\'accès, enseigne (ME-099, 145 à 147)', {'B-A': 'P ; C (A.1)', 'B-B': 'M+KT-1'}),
 ('Volets coupe-feu (AR-PLN-056, 057) ; lecteurs, luminaires, persiennes non touchées (ME-063, 104 à 106)', {'B-A': 'I (A.6) ; P→M', 'B-B': 'I ; P→M', 'B-C': 'I ; P→M'}),
]
SAISONS = [  # fenêtre, contrainte, ID, sous-phases (A), sous-phases (B)
 ('Novembre à avril', 'Bâti isolé au lieu du plexiglas pendant les travaux par l\'extérieur', 'AR-PLN-042', 'toutes les étapes de fenêtres', 'A.2 à A.6, B.1.x, B.2.x, C.x'),
 ('Hors période estivale', 'Coupures de l\'unité hémodialyse / labo : dimanche seulement', 'ME-051', '2.N, 2.O', 'C.2'),
 ('Hors période estivale', 'Bi-bloc traitement d\'eau 203 : arrêt court, semaine', 'ME-087', '2 (face ?)', 'C.2'),
 ('Hors période estivale', 'Bi-bloc salle des serveurs RC : arrêt court, semaine', 'ME-088', '1', 'B-A'),
 ('Hors période hivernale', 'Réinstallation des câbles chauffants des évents', 'ME-082', '3.O (2.O ?)', 'B-B'),
 ('Béton ≥ 10 °C ; mortiers ≥ 10 °C ; maçonnerie 5 à 50 °C', 'Réparations de béton, maçonnerie par temps froid (préchauffage, enceintes)', 'ST-034, 035 ; AR-DEV-304, 309', 'chaque façade', 'toutes'),
 ('Couverture ≥ 18 °C (bitume) ou 10 °C (soudé) ; solins > 2 °C', 'Bandes de toiture périmétriques', 'AR-DEV-320, 329', 'chaque toiture', 'toutes'),
 ('Pare-air > −10 °C ; membrane d\'hiver 5 à 40 °C', 'Pose du pare-air', 'AR-DEV-316, 317', 'chaque façade', 'toutes'),
 ('10 °C dans les zones de travaux ; vitrage : minimum prescrit 24 h', 'Chauffage temporaire surveillé hors heures', 'AR-DEV-144, 343, 112', 'toutes', 'toutes'),
]
VALIDATION = [  # point, moment, IDs
 ('Calendrier d\'exécution et calendrier d\'arrêt des installations approuvés ; tout changement d\'horaire', 'Phase 0, puis à chaque mise à jour', 'AR-DEV-026, 032, 286 ; CI-CTR-003, 004'),
 ('Préavis 48 h et approbation avant toute coupure ; calendrier hebdomadaire du jeudi', 'Avant chaque coupure', 'AR-DEV-024, 031, 032, 062'),
 ('Plan de sécurité incendie approuvé (CISSSGA, Établissement, service incendie) ; mise hors service de gicleurs couverte', 'Avant le démarrage ; quai des ambulances', 'AR-DEV-197 ; ME-006, 007 ; Z-08'),
 ('Méthodologie PCI, cloisons par phase, classification et fiche synthèse (classes III-IV), équipe pluridisciplinaire', 'Phase 0 ; avant chaque enceinte', 'AR-DEV-124, 148, 203 ; CI-PCI-001 à 003, 005'),
 ('Approbation de la préparation des lieux avant de débuter ; du nettoyage avant démantèlement ; réouverture', 'Début et fin de chaque zone', 'AR-DEV-204, 245 ; CI-PCI-023, 024'),
 ('Travaux bruyants et vibrations : coordination par secteur ; seuils à établir', 'Avant les travaux des secteurs listés', 'CI-TAB-011, 012, 022, 025, 028 ; Z-04'),
 ('Horaires « J », « S », « J/S » des activités classées ; délai de 2 jours ouvrables', 'Chaque activité du tableau CISSS', 'CI-TAB-001, 005 à 010, 019 à 021, 024, 027, 029'),
 ('Configurations des accès : entrée principale, ambulances, cliniques externes, marchandises, roulotte IRM ; préavis 3 semaines par voie déplacée', 'Avant chaque changement de configuration', 'AR-PLN-008, 018, 019 ; CI-TAB-013 à 018 ; AR-DEV-139'),
 ('Fenêtres des unités critiques (hémodialyse, UT-2, autoclaves, médecine nucléaire, PAF BO, bi-blocs, chambre 315) ; inoccupation des chambres 307 et 216 ; gaz médicaux : attestation, présence, deux certifications', 'Avant chaque coupure ; avant les faces nord et sud de la tour', 'ME-048, 050, 051, 055, 056, 058, 068, 069, 072, 073, 077, 087, 088, 119'),
]

def option_fill_layer(opt):
    out = []
    if opt == 'B':
        for k, (p, *_ ) in ZONES.items():
            if ZONES[k][3] != 'non touché': out.append(poly(p, 'url(#hatchb)', 0.55, '#1565c0', 1.4))
            else: out.append(poly(p, 'url(#hatch)', 0.9, '#666', 1))
        for k in ('B', 'H', 'D'): out.append(poly(ZONES[k][0], '#ffb300', 0.6, '#7a3300', 1.4))
        out.append(poly(ZONES['A'][0], '#66bb6a', 0.65, '#1b5e20', 1.6))
        return ''.join(out)
    for k, (p, short, fn, ph) in ZONES.items():
        if ph == '1': out.append(poly(p, FILL['1'], 0.6, '#0d3b75', 1.5))
        elif ph == 'non touché': out.append(poly(p, 'url(#hatch)', 0.9, '#666', 1))
    out.append(poly(ZONES['A'][0], FILL['2'], 0.35, '#1b5e20', 1.5))
    for f, p in FACES_TOUR.items(): out.append(poly(p, FACE_FILL[f], 0.85, '#fff', 0.8))
    for k in ('J', 'B', 'K'): out.append(poly(ZONES[k][0], P3_FILL['3.N'], 0.7, '#7a3300', 1.2))
    out.append(poly(ZONES['O'][0], P3_FILL['3.O'], 0.7, '#7a3300', 1.2))
    for k in ('I', 'H', 'G', 'P'): out.append(poly(ZONES[k][0], P3_FILL['3.S'], 0.7, '#7a3300', 1.2))
    return ''.join(out)
def order_badges(opt):
    out = []
    if opt == 'B':
        for n, (x, y, lab) in enumerate([(430, 590, 'RC'), (790, 395, 'niv. 1'), (459, 470, 'tour')], 1):
            x, y = x - OFF[0], y - OFF[1]; out.append(badge(x, y, str(n), '#111', 14, 14) + txt(x + 18, y + 5, lab, 13, 'start', 'bold'))
        return ''.join(out)
    for n, sp in enumerate(OPTIONS[opt]['ordre'], 1):
        x, y = BADGE_POS[sp]; out.append(badge(x - OFF[0], y - OFF[1], str(n), '#111', 14, 14))
    return ''.join(out)
def amb_diverg(): x, y = 532 - OFF[0], 556 - OFF[1]; return diverg(x + 28, y - 8)
def chips(opt):
    cls = ['s0', 's1', 's2', 's3', 's4']
    return '<div class="seq">' + ' → '.join(f'<span class="{cls[i]}">{html.escape(c)}</span>' for i, c in enumerate(OPTIONS[opt]['chips'])) + '</div>'

# ------------------------------------------------------------------ planches
def planche0(num, total):
    inner = [outlines(), zone_labels()]
    for l, (anc, d, name) in ELEV.items(): inner.append(view_arrow(l, anc, d))
    for no, lib, loc, ids, (px, py), (lx, ly) in POINTS_FIXES:
        x, y = px - OFF[0], py - OFF[1]; bx, by = lx - OFF[0], ly - OFF[1]
        inner += [leader(bx, by, x, y, '#8e24aa', '2,2'), dot(x, y, '#8e24aa'), badge(bx, by, no, '#8e24aa', 13, 13)]
    inner.append(amb_diverg())
    plan = plan_figure(40, 96, ''.join(inner))
    cap = '<div class="cap" style="left:40px;top:606px;width:940px">Fond : feuille 010 (D2), plan clé « Zones des travaux », couleurs des architectes (bleu phase 1, vert phase 2, orange phase 3, hachures « secteur non touché ») ; nord en haut à droite. Contours des zones, lettre O du basilaire ouest, repères d\'élévation A à I (feuille 011) et points fixes 1 à 16 : superposés [lecture] ; le numéro pointe l\'emplacement écrit ou lu, le tableau de droite donne la ligne du registre.</div>'
    rows = [['Zone', 'Fonction (légende 010, via 01 §8.5)', 'Phase du plan clé [lecture]']]
    for k in 'ABCDEFGHIJKL':
        p, short, fn, ph = ZONES[k]; rows.append([f'<b>{k}</b>', FN_COURT[k], {'1': 'Phase 1', '2': 'Phase 2', '3': 'Phase 3', 'non touché': 'Secteur non touché'}[ph]])
    rows.append(['<b>O</b>', 'Basilaire ouest, 1 étage — lettre attribuée ici [lecture]', 'Phase 3 [lecture]'])
    rows.append(['—', 'Saillie sud, portes de garage ▲▼ : quai des ambulances [lecture]', 'Phase 3 [lecture]'])
    zones_tab = box(40, 656, 560, BOT - 656, table(rows, ['44px', '372px', '124px']), 'Zones A à L et parties de bâtiment', 'p0-zones')
    faces = {'A': 'sud (basilaire sud et tour)', 'B': 'ouest (basilaire ouest et tour)', 'C': 'ouest, partielle — jonction est / saillie : <b>?</b>', 'D': 'est, partielle — saillie sud (G) : <b>?</b>', 'E': 'ouest, partielle — angle sud-ouest (I)', 'F': 'nord (basilaire nord, tour, archives)', 'G': 'est (basilaire est et tour)', 'H': 'nord, partielle — près des archives / K', 'I': 'ouest, partielle — près des archives / K'}
    rows = [['Élév.', 'Titre (feuille 011)', 'Face vue [lecture]']]
    for l, (anc, d, name) in ELEV.items(): rows.append([f'<b>{l}</b>', name, faces[l]])
    elev_tab = box(608, 656, 372, BOT - 656, table(rows, ['38px', '142px', '172px']) + '<div class="note">« ? » : à trancher par les architectes (planche 13).</div>', 'Repères d\'élévation A à I (plan clé de la 011)', 'p0-elev')
    impl = (f'<div class="box" id="p0-impl" style="left:1000px;top:96px;width:592px;height:240px"><div class="bt">Implantation existante (feuille 001) : issues et accès repérés par les architectes</div>'
            f'<img src="implantation.png" style="position:absolute;left:8px;top:24px;width:576px;max-height:144px;object-fit:contain">'
            f'<div class="note" style="position:absolute;left:8px;top:170px;width:576px">Légende 001/002 : ▲ issue ou accès au bâtiment protégé durant le chantier (AR-PLN-016) ; △ porte de garage ; borne-fontaine accessible en tout temps (AR-PLN-001) ; issues et chemins d\'évacuation maintenus à 1650 mm (AR-PLN-006) ; portes hors service repérées (AR-PLN-007) ; plan d\'action avant tout travail près d\'une issue (AR-PLN-011).</div></div>')
    rows = [['No', 'Point fixe ou accès à maintenir', 'Localisation écrite et marque', 'Registre']]
    for no, lib, loc, ids, _, _ in POINTS_FIXES: rows.append([f'<b>{no}</b>', lib, loc, ids])
    pf = box(1000, 342, 592, BOT - 342, table(rows, ['28px', '218px', '210px', '116px']), 'Points fixes 24/7, unités critiques et accès (registre 02)', 'p0-pf')
    return ('<section class="planche">' + header(num, 'Lecture du site', 'Zones A à L et O, repères d\'élévation A à I, points fixes 24/7 et accès à maintenir — planche commune à toutes les options')
            + plan + cap + zones_tab + elev_tab + impl + pf + footer(num, total, 'D2 feuilles 001, 002, 010, 011 (rendus 200 ppp) ; analyse/01-inventaire.md §8.5 ; analyse/02-contraintes.md ; analyse/03-phasage.md §2.1, §6.') + '</section>')

def planche_ordre(opt, num, total):
    o = OPTIONS[opt]
    inner = [option_fill_layer(opt), zone_labels()]
    for l, (anc, d, name) in ELEV.items(): inner.append(view_arrow(l, anc, d, '#555'))
    inner.append(order_badges(opt)); inner.append(amb_diverg())
    plan = plan_figure(40, 96, ''.join(inner), dim=0.5)
    if opt == 'B':
        legend = 'Hachures bleues = rez-de-chaussée (B-A, toutes les parties) ; ambre = parties à deux étages où le niveau 1 est touché (B, H, D ; sous-sol non zoné) ; vert = tour (B-C). Numéros = ordre des niveaux du tableau CISSS [lecture]. Gris hachuré = secteur non touché.'
    else:
        legend = 'Bleu = phase 1 ; vert clair = tour, ses faces 2.N, 2.E, 2.S, 2.O en bandes vertes ; oranges = 3.N, 3.O, 3.S ; gris hachuré = secteur non touché. Numéros noirs = ordre des phases et sous-phases de cette option.'
    cap = f'<div class="cap" style="left:40px;top:606px;width:940px">{legend} Pictogramme orange : localisation divergente (zone d\'ambulance « sud » selon D4/D5, « nord » selon D2).</div>'
    seqbox = box(40, 660, 940, 124, chips(opt) + f'<div class="seqn"><b>Fondement :</b> {html.escape(o["fondement"])} Correction des anomalies après chaque phase, avant la suivante (AR-DEV-275). Repères des architectes sur la feuille 010 : phase 1 « ±5 mois », phase 2 « ±8 mois », phase 3 « ±4 mois » (C-34) — aucun calendrier n\'en est déduit.</div>', None, f'{opt}-seq')
    # implications propres à l'option
    impl = {
     'R': ['Prototype de la première fenêtre et du premier mur-rideau en phase 1, en présence de l\'architecte (AR-PLN-050).', 'Nord avant ouest : la prise d\'air médical temporaire est « sur la façade ouest pour permettre les travaux de la façade nord » (ME-065) et réinstallée « après le revêtement nord » (ME-067) — ordre déduit [lecture], simultanéité non exclue (Z-02).', 'Faces de la tour : conduits temporaires hémodialyse avant démolition nord/ouest (ME-049) ; conduit de médecine nucléaire modifié pour permettre la façade est (ME-118) ; sinon [choix].', 'Repère des architectes : le plan clé numérote 1, 2, 3 dans cet ordre (C-34).'],
     'A2': ['Les deux basilaires (phases 1 et 3) sont achevés avant la tour : bandes de toiture périmétriques refaites (AR-PLN-063) avant que l\'échafaudage de la tour s\'y appuie [lecture] ; voies protégées (AR-PLN-036), entreposage restreint (AR-DEV-102 ; ST-024).', 'Prototype en phase 1 (AR-PLN-050).', 'Les installations temporaires de la façade ouest (air médical, autoclaves) précèdent le bloc opératoire si celui-ci est sur la tour (ME-045 « façade ouest (tour) ») : quatre systèmes 24/7 sur la même face, à échelonner (K2).', 'Aucun texte ne lie la tour aux basilaires : ordre [choix].'],
     'A3': ['Prototype dans la tour (AR-PLN-050 : « première fenêtre et premier mur-rideau »).', 'Échafaudage de la tour sur des toitures non refaites [lecture] : garde-corps maintenus (AR-DEV-100), voies protégées (AR-PLN-036), capacités et attestation (ST-023 à 026).', 'Coupures de l\'hémodialyse dès le début du projet, un dimanche hors période estivale (ME-051) : voir la couche saisons de la planche de séquence.', 'Aucun texte n\'impose la tour en premier : ordre [choix].'],
     'B': [],
    }[opt]
    if opt == 'B':
        k1 = ('<div class="txt"><b>Ce que K1 implique concrètement.</b> Le tableau CISSS met « installation plexiglass, tous les locaux RC » en une seule sous-phase A.2 sur les zones E <b>et</b> H (CI-TAB-006), puis thermos et cadrage par secteurs de locaux répartis sur E, H, F et L (CI-TAB-007, 008). Les fenêtres existantes restent en place « jusqu\'à ce que les travaux par l\'extérieur soient complétés » (AR-PLN-040). Deux façons de rendre B exécutable :<br>'
              '<b>V-K1b</b> — achever l\'extérieur des deux basilaires (est et sud, zones E et H) avant toute étape de fenêtres du RC ; l\'échafaudage reste par façade (CI-TAB-004) et le RC entier se fait ensuite d\'une traite. Compatible avec la lecture large d\'AR-PLN-040 ; cohabitation prolongée des fenêtres existantes avec l\'enveloppe neuve.<br>'
              '<b>V-K1a</b> — faire scinder par le CISSS chaque sous-phase par secteur du plan clé (A.2-est, A.2-sud ; B.1.2-nord, B.1.2-sud…) en conservant classes PCI et horaires : demande une réémission du tableau (R-31).<br>'
              '<b>V-K1d</b> — faire préciser par les architectes la portée de « travaux par l\'extérieur » (C-36, Z-07) : la lecture étroite (étape extérieure de chaque fenêtre, AR-PLN-046 à 048) réduit le conflit à l\'échafaudage.<br>'
              'Sous-phases écrites reprises telles quelles : A.1 accès extérieurs ; A.2 plexiglas RC ; A.3/A.4 thermos ; A.5/A.6 cadrage et toile, volets coupe-feu, structure R22, bruits et vibrations ; A.7 terrasse ; B.1.2 toile d\'échafaudage, prises d\'air SS, nouvelle issue, thermos 101/104/109 ; B.1.3 thermos 105 à 124 ; B.2.1, B.2.2 cadrage ; C.2, C.4, C.5 cadrage et toile des niveaux 2, 3, 4. Absentes : C.1, C.3, B.1.1 ; lignes sans sous-phase : échelles et issue no 3 vers les toitures (CI-TAB-023, 026).</div>')
        right_top = box(1000, 96, 592, 330, k1, 'Option B — découpage par niveaux et conflit K1', 'B-k1')
    else:
        right_top = box(1000, 96, 592, 330, '<ul class="txt">' + ''.join(f'<li>{p}</li>' for p in impl) + '</ul>', 'Ce que l\'ordre implique', f'{opt}-impl')
    sp_amb = 'A.1 (RC, extérieur)' if opt == 'B' else '3.S'
    det = (f'<div class="box" id="{opt}-acces" style="left:1000px;top:432px;width:592px;height:352px"><div class="bt">Configurations des accès portées par {sp_amb} (feuille 002) : ambulances, deux configurations (AR-PLN-018) ; entrée principale, trois (AR-PLN-019) ; « phase 1/2/3 » = numéros propres à la 002 (C-34)</div>'
           f'<img src="../img/A002_det1.png" style="position:absolute;left:8px;top:60px;height:278px"><img src="../img/A002_det2.png" style="position:absolute;left:250px;top:74px;width:334px">'
           f'<div class="txt" style="position:absolute;left:250px;top:190px;width:334px">Orientation du détail 1 non écrite : « entrée ambulance sud » selon D4/D5 (ME-006, ME-147), « zone ambulance (nord) » selon AR-PLN-004 — les deux lectures sont conservées (planche 13). Un panneau temporaire par configuration (AR-PLN-014) ; préavis de 3 semaines avant tout déplacement de voie (AR-DEV-139) ; durée devant les portes de garage limitée (R-20).</div></div>')
    issues = box(40, 790, 1552, BOT - 790, '<div class="txt cols2">'
        '<p><b>Nouvelle issue permanente</b> au laboratoire (zone B, niveau 100) : jalon du calendrier (AR-DEV-058), classe IV horaire « J » (CI-TAB-019), percements hors des heures d\'occupation (ME-020). Escalier no 7 des plans de structure présumé être cette issue [à confirmer] (Z-12 ; ST-039 : « basilaire nord-ouest »). Ordre nouvelle issue / condamnation d\'une issue existante : non écrit (Z-12, K4) ; variantes sur la planche de séquence.</p>'
        '<p><b>Issues touchées.</b> Deux issues minimum et capacité d\'évacuation maintenue dans les secteurs occupés (AR-DEV-198). Aucune issue condamnée n\'est écrite : à chaque issue touchée par une sous-phase, plan d\'action préalable (AR-PLN-011), chemin d\'évacuation maintenu à 1650 mm (AR-PLN-006) ou escalier d\'issue temporaire modulaire incombustible (AR-DEV-311, 195), portes hors service repérées (AR-PLN-007), renvoi à la feuille 002 pour le maintien des issues (AR-PLN-039). Sous-phases qui touchent des issues repérées sur 001/002 [lecture] : porte d\'issue de l\'urgence et escalier no 1 (ME-146) en 3.S ; portes du laboratoire, du bloc opératoire, de la salle du personnel, escaliers 3, 4, 6 et quai des ambulances (lecteurs de carte déposés, ME-104) selon la face ; issue no 3 vers la toiture 2 (CI-TAB-026).</p></div>', 'Issues : nouvelle issue, issues touchées et compensation', f'{opt}-issues')
    return ('<section class="planche">' + header(num, f'{o["nom"]} — ordre des phases', 'Plan clé recoloré par phase et sous-phase, numéros d\'ordre, configurations des accès, issues')
            + plan + cap + seqbox + right_top + det + issues + footer(num, total, 'D2 feuilles 002, 010, 011 ; analyse/03-phasage.md §2 (découpage A) ou §3 (découpage B), §2.7 (variantes), §4 (conflits).') + '</section>')

def planche_installations(opt, num, total):
    o = OPTIONS[opt]; is_b = opt == 'B'
    set_scale(780)
    inner = [option_fill_layer(opt), zone_labels()]
    inner.append(poly([(268,352),(272,352),(272,508),(268,508)], '#8e24aa', 0.9, 'none', 0))
    inner.append(poly([(243,335),(272,335),(272,352),(243,352)], 'url(#hatchm)', 1, '#8e24aa', 1.2))
    inner.append(poly([(243,352),(250,352),(250,548),(243,548)], 'url(#hatchm)', 1, '#8e24aa', 1))
    for code, spA, spB, quoi, ids, (px, py), (lx, ly), face in CALLOUTS:
        x, y = px - OFF[0], py - OFF[1]; bx, by = lx - OFF[0], ly - OFF[1]
        inner += [leader(bx, by, x, y, '#8e24aa', '2,2'), dot(x, y, '#8e24aa'), tag(bx, by, code)]
    inner.append(amb_diverg()); inner.append(diverg(272 - OFF[0] - 22, 440 - OFF[1] - 30, 13))
    plan = plan_figure(40, 96, ''.join(inner), width=780, dim=0.6); set_scale(940)
    cap = '<div class="cap" style="left:832px;top:96px;width:148px">Étiquettes T1 à T16 (magenta) : installations et mesures temporaires ; le point marque la face écrite au registre ; identifiants au tableau de droite. Hachures magenta : façade ouest, où le registre place l\'air médical temporaire (ME-065), les conduits du bloc opératoire (ME-047) et les évents d\'autoclaves (ME-075). Pictogramme près de T9 : tour ou basilaire non écrit.</div>'
    # matrice
    cols = ['0'] + o['ordre'] + ['4']
    systems = SYSTEMES_B if is_b else SYSTEMES
    rows = [['Système (registre)'] + cols]
    for name, cells in systems:
        rows.append([name] + [cells.get(c, 'M') for c in cols])
    widths = ['300px'] + [f'{(940 - 300 - 16) // len(cols)}px'] * len(cols)
    mat = box(40, 526, 940, BOT - 526, table(rows, widths, cls='mat') + '<div class="note">C coupure (fenêtre : tableau de droite) · P provisoire · I intervention classée · M maintenu · ? localisation non écrite · → états successifs · cert. certification. Source : 03 §2.8 (A) ou §3.6 (B).</div>', f'Matrice phase × système électromécanique — colonnes dans l\'ordre de l\'option', f'{opt}-mat')
    rows = [['Code', 'Sous-phase', 'Installation ou mesure temporaire', 'Registre']]
    for code, spA, spB, quoi, ids, _, _, face in CALLOUTS:
        rows.append([f'<b>{code}</b>', spB if is_b else spA, quoi, ids])
    tt = box(1000, 96, 592, BOT - 96, table(rows, ['40px', '58px', '310px', '160px']) + '<div class="note">Les sous-phases du découpage B sont celles de l\'affectation de 03 (annexe A) ; « B » et « C » sans numéro : niveau écrit, sous-phase non écrite.</div>', 'Installations temporaires électromécaniques et mesures propres aux sous-phases (fiches de 03 §2.2 à §2.4 ou §3.2 à §3.4)', f'{opt}-T')
    return ('<section class="planche">' + header(num, f'{o["nom"]} — installations et coupures', 'Où et quand les systèmes 24/7 sont maintenus, provisoires ou coupés ; étiquettes T sur la face écrite au registre')
            + plan + cap + mat + tt + footer(num, total, 'D4/D5 via le registre (ME-…) ; analyse/03-phasage.md §2.8 ou §3.6 ; analyse/04-verification.md §3.') + '</section>')

# libellés courts des nœuds du graphe (le sens complet est dans SP_LABEL et sur les planches d'ordre) ; préalables écrits, deux lignes au plus
GRAPH_LABEL = {'1': 'Phase 1 — basilaire est (D, E, F)', '3.O': '3.O — basilaire ouest (O ; J, I)', 'B-A': 'B-A — RC (A.1 à A.7)', 'B-B': 'B-B — niveau 1 et SS (B.1.2 à B.2.2)', 'B-C': 'B-C — tour, niv. 2 à 4 (C.2, C.4, C.5)'}
GRAPH_PRE = {'1': ['ME-108 : conduits EMT du R-22 relocalisés'], '2.N': ['ME-049 : conduits temp. hémodialyse'], '2.O': ['ME-043 : conduits temp. PAF bloc op.', 'ME-049 : conduits temp. hémodialyse'], '2.E': ['ME-118 : conduit méd. nucléaire modifié'],
             '3.N': ['ME-065/066 : air méd. temp., façade O'], '3.O': ['ME-075 : évents d\'autoclaves déplacés', 'ME-067 : réinstallé après nord [lecture]'], '3.S': ['ME-006/007 : gicleurs du quai, AR-DEV-032'],
             'B-A': ['AR-PLN-040 : ext. RC achevé [lecture]', 'ME-108 : conduits EMT du R-22'], 'B-B': ['CI-TAB-004 : toile d\'échafaudage', 'ME-065 : prise d\'air médical temp.'], 'B-C': ['ME-049 : conduits temp. hémodialyse', 'ME-118 : conduit méd. nucléaire'],
             '0': ['AR-DEV-058 : travaux préparatoires', 'AR-DEV-030 : piquages sur les réseaux'], '4': ['AR-DEV-170 : sécurité temp. maintenue']}
def graph(opt):
    """Chemin de dépendances : nœuds de phase en ligne, préalables électromécaniques au-dessus, clôture à droite."""
    o = OPTIONS[opt]; W = 1530; H = 266
    seq = ['0'] + o['ordre'] + ['4']; n = len(seq); step = (W - 40) / n; bw = min(step - 12, 150); y0 = 168
    pos = {sp: (30 + step * i + step / 2, y0) for i, sp in enumerate(seq)}
    col = {'0': '#607d8b', '4': '#455a64', '1': '#3b7dd8', 'B-A': '#1565c0', 'B-B': '#ffb300', 'B-C': '#2e7d32'}
    def c(sp): return col.get(sp) or FACE_FILL.get(sp) or P3_FILL.get(sp)
    out = [DEFS]
    for sp in seq:
        x, y = pos[sp]; lab = SP_LABEL[sp]
        lab = GRAPH_LABEL.get(sp, lab); parts = lab.split(' — ', 1); t1 = parts[0]; t2 = parts[1] if len(parts) > 1 else ''
        nchar = int((bw - 8) / 6.4)
        out.append(f'<rect x="{x - bw/2}" y="{y - 30}" width="{bw}" height="60" rx="6" fill="{c(sp)}" fill-opacity="0.9" stroke="#333"/>')
        out.append(txt(x, y - 8, t1, 14, 'middle', 'bold', '#fff'))
        for k, line in enumerate(wrap(t2, nchar)[:2]): out.append(txt(x, y + 9 + 15 * k, line, 12, 'middle', 'normal', '#fff'))
        rep = {'1': '±5 mois', '2.N': '±8 mois', '3.N': '±4 mois'}.get(sp)
        if rep and opt != 'B': out.append(txt(x, y + 46, f'Repère 010 : {rep}', 12, 'middle', 'normal', '#555'))
    for a, b in zip(seq, seq[1:]):
        xa, ya = pos[a]; xb, yb = pos[b]
        dashed = not (a == '0' or b == '4')
        dash_attr = 'stroke-dasharray="6,4"' if dashed else ''
        out.append(f'<line x1="{xa + bw/2}" y1="{ya}" x2="{xb - bw/2 - 6}" y2="{yb}" stroke="#17324d" stroke-width="2" {dash_attr} marker-end="url(#arb)"/>')
    # préalables écrits (magenta) au-dessus des nœuds concernés
    pre = GRAPH_PRE
    pchar = int((bw - 2) / 6.3)
    for sp in seq:
        x, y = pos[sp]
        for k, t in enumerate(pre.get(sp, [])[:2]):
            yy = 28 + k * 46
            out.append(f'<rect x="{x - bw/2 - 1}" y="{yy}" width="{bw + 2}" height="38" rx="4" fill="#fff" stroke="#8e24aa" stroke-width="1.4"/>')
            lines = wrap(t, pchar); assert len(lines) <= 2, (sp, t, lines)
            for j, line in enumerate(lines): out.append(txt(x, yy + 15 + 14 * j, line, 12, 'middle', 'normal', '#5e1a75'))
            if k == len(pre.get(sp, [])[:2]) - 1: out.append(f'<line x1="{x}" y1="{yy + 38}" x2="{x}" y2="{y - 32}" stroke="#8e24aa" stroke-width="1.6" marker-end="url(#arm)"/>')
    out.append(txt(20, H - 26, 'Flèches pleines : dépendance écrite (AR-DEV-058 au départ, AR-DEV-275 vers la clôture) ; pointillées : ordre de l\'option [lecture] ou [choix]. Cadres magenta : préalable électromécanique écrit, exécuté avant la démolition de la face (AR-DEV-058).', 12, 'start', 'normal', '#333'))
    out.append(txt(20, H - 10, 'AR-DEV-275 : anomalies corrigées après chaque phase, avant la suivante. Repères « ±5 / ±8 / ±4 mois » : indications des architectes sur la feuille 010 (C-34), sans calendrier déduit.', 12, 'start', 'normal', '#333'))
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">' + ''.join(out) + '</svg>'
def wrap(t, n):
    words = t.split(); lines = []; cur = ''
    for w in words:
        if len(cur) + len(w) + 1 > n and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    if cur: lines.append(cur)
    return lines

def planche_sequence(opt, num, total):
    o = OPTIONS[opt]; is_b = opt == 'B'
    g = f'<div class="box" id="{opt}-graph" style="left:40px;top:96px;width:1552px;height:300px"><div class="bt">Chemin de dépendances entre phases et sous-phases — {html.escape(o["nom"])}</div>{graph(opt)}</div>'
    rows = [['Fenêtre', 'Contrainte', 'Registre', 'Sous-phases concernées']]
    for f, c_, i, spA, spB in SAISONS: rows.append([f, c_, i, spB if is_b else spA])
    sais = box(40, 404, 940, 330, table(rows, ['200px', '360px', '120px', '236px']) + '<div class="note">Contrat : 31 août 2026 – 31 décembre 2027 (CI-CTR-001 ; dates jugées inapplicables en l\'état, C-14), soit deux périodes novembre–avril. « Période estivale » non définie (Z-10). K3 : coupures des unités critiques interdites l\'été, enveloppe contrainte l\'hiver ; sans durée, la répartition n\'est pas tranchée.</div>', 'Couche K3 — fenêtres saisonnières applicables', f'{opt}-sais')
    k4 = box(1000, 404, 592, 330, '<div class="txt"><b>Nouvelle issue en amont (K4).</b> Le jalon « construction d\'une nouvelle issue et protection des issues » (AR-DEV-058) ne dit pas si la nouvelle issue précède la mise hors service d\'une issue existante (Z-12). Deux issues minimum et capacité maintenue (AR-DEV-198).<br>'
        '<b>V-K4a</b> — nouvelle issue et escalier no 7 exécutés dès la phase 0, avant toute façade : classe IV « J » (CI-TAB-019), câblage souterrain protégé (AR-PLN-013), percements hors heures d\'occupation (ME-020).<br>'
        f'<b>V-K4b</b> — nouvelle issue en séquence dans {"B.1.2" if is_b else "3.N"} ; admissible si aucune issue existante n\'est condamnée avant.<br>'
        '<b>V-K4c</b> — escalier d\'issue temporaire modulaire (AR-DEV-311, 195) à chaque issue condamnée, indépendamment du nouvel escalier.<br>'
        '<b>Risque non sourcé :</b> AR-DEV-170 interdit de passer des installations temporaires de sécurité aux permanentes avant l\'achèvement substantiel ; le registre ne dit pas si un escalier d\'issue temporaire en est une — à confirmer par les professionnels.</div>', 'Couche K4 — nouvelle issue et issues condamnées', f'{opt}-k4')
    rows = [['Point de validation du CISSS', 'Moment', 'Registre']]
    for p_, m, i in VALIDATION: rows.append([p_, m, i])
    val = box(40, 740, 1552, BOT - 740, table(rows, ['760px', '340px', '424px']), 'Points de validation CISSS (registre consolidé de 03 §5)', f'{opt}-val')
    return ('<section class="planche">' + header(num, f'{o["nom"]} — séquence', 'Dépendances entre phases, fenêtres saisonnières (K3), nouvelle issue (K4), points de validation CISSS')
            + g + sais + k4 + val + footer(num, total, 'analyse/03-phasage.md §0.4 (séquences écrites), §2.6 ou §3.5 (diagrammes), §4 K3 et K4, §5 ; registre 02.') + '</section>')

def planche_comparaison(num, total):
    rows = [['Option', 'Ordre', 'Conflits levés', 'Conflits résiduels', 'Décisions à obtenir — de qui']]
    rows.append(['<b>R</b> — référence', '0 → 1 → 2 (N, E, S, O) → 3 (N → O ; S) → 4', 'K2 : la prise d\'air médical temporaire est sur la façade ouest pendant la façade nord (ME-065) et réinstallée après le revêtement nord (ME-067). K4 traitable par V-K4b ou V-K4c. Numérotation du plan clé respectée (C-34).', 'K1 (tableau CISSS par niveaux) ; K3 (saisons) ; K5 (régime PCI) ; K6 (zones C et L) ; ordre des faces de la tour [choix].', 'WSP : tour ou basilaire pour l\'air médical, le bloc opératoire, les autoclaves ; simultanéité nord/ouest. Architectes : portée d\'AR-PLN-040. CISSS : K1, K5, horaires J/S.'])
    rows.append(['<b>A2</b> — basilaires avant la tour', '0 → 1 → 3 (N → O ; S) → 2 → 4', 'K2 comme R. Toitures périmétriques des basilaires refaites avant l\'échafaudage de la tour [lecture].', 'Comme R ; ajoute la lecture de l\'appui de l\'échafaudage de la tour sur les toitures du basilaire (ST-023 à 026 ne le disent pas ; Z-27) ; quatre systèmes 24/7 sur la façade ouest à échelonner si le BO est sur la tour.', 'Comme R ; plus structure : appui et capacités des toitures pour l\'échafaudage de la tour.'])
    rows.append(['<b>A3</b> — tour d\'abord', '0 → 2 (N, E, S, O) → 1 → 3 → 4', 'K2 comme R ; prototype dans la tour (AR-PLN-050).', 'Comme R ; échafaudage de la tour sur des toitures non refaites [lecture] (AR-DEV-100, AR-PLN-036) ; coupures de l\'hémodialyse (dimanche hors été, ME-051) dès le début.', 'Comme R ; plus CISSS : fenêtres de coupure de l\'hémodialyse et des chambres 216/307 dès la première phase.'])
    rows.append(['<b>B</b> — par niveaux (tableau CISSS)', '0 → B-A (RC) → B-B (niveau 1, SS) → B-C (tour) → 4', 'Applique le tableau du CISSS tel qu\'écrit (classes PCI, horaires, secteurs de locaux) ; K1 n\'existe plus si V-K1b (façades des deux basilaires avant les fenêtres du RC) ou V-K1a (tableau scindé par secteur).', 'K1 tant que V-K1a/b/d n\'est pas décidé ; l\'extérieur reste à ordonner par façade (échafaudage, démolition, structure : ST-030, ST-011, CI-TAB-004) ; K2, K3, K5, K6 comme R.', 'CISSS : scinder le tableau par secteur (R-31) ou accepter V-K1b. Architectes : portée de « travaux par l\'extérieur » (C-36, Z-07). WSP : comme R.'])
    comp = box(40, 96, 1552, 300, table(rows, ['150px', '240px', '390px', '390px', '360px']), 'Comparaison des options', 'cmp')
    reco = box(40, 404, 760, 210, '<div class="txt big"><b>Option R recommandée.</b> Elle suit la numérotation du plan clé des architectes, respecte l\'emplacement écrit de la prise d\'air médical temporaire (ME-065/067) et ne repose sur aucune lecture supplémentaire par rapport à A2 et A3. A2 et A3 restent admissibles, mais chacune ajoute une hypothèse non écrite sur l\'échafaudage de la tour (toitures refaites ou non) et, pour A3, place les coupures de l\'hémodialyse en tout début de projet. B ne devient exécutable qu\'après une décision du CISSS sur K1 (tableau scindé par secteur ou façades des deux basilaires avant les fenêtres du RC) ; elle est à conserver comme lecture de contrôle des classes PCI et des horaires, pas comme ordre d\'exécution.</div>', 'Recommandation motivée', 'reco')
    dec = [['Décision', 'Portée', 'De qui', 'Renvoi'],
           ['Élévations C (ouest partielle) et D (est partielle) : faces et sous-phases concernées', 'Planche 0 et planches d\'ordre : « ? »', 'Architectes', 'Z-24 ; 03 §2.1'],
           ['Zone d\'ambulance : « sud » (D4, D5 : ME-006, ME-147) contre « nord » (D2 : AR-PLN-004) ; orientation du détail 1 de la 002', 'Sous-phase des configurations d\'accès ; T14', 'Architectes et WSP', '03 §6, §2.4.3 ; 04 §6'],
           ['Tour ou basilaire : centrale d\'air médical (ME-064), prise d\'air du bloc opératoire (ME-045 « (tour) »), évents d\'autoclaves (ME-075)', 'Faces 2.O/3.O, 3.N/2.N ; ordre nord/ouest', 'WSP', '03 §6, K2'],
           ['Portée de « travaux par l\'extérieur » dans la note de la 505 (AR-PLN-040)', 'Articulation façades / fenêtres ; K1', 'Architectes', 'C-36, Z-07 ; 03 K1'],
           ['Escalier no 7 = nouvelle issue ; ordre nouvelle issue / condamnation', 'K4 ; T11', 'Architectes, structure', 'Z-12 ; 03 K4'],
           ['Régime PCI applicable (procédure du CISSS de la Gaspésie absente), classes attribuées, sens de « J », « S », « J/S », « période estivale »', 'Toutes les activités classées ; K3, K5', 'CISSS', 'C-01, C-02, Z-01, Z-05, Z-10'],
           ['Secteurs « non touchés » C (local R-22) et L (fenêtres) présents dans les activités du tableau', 'Phase 1 ; A.6', 'Architectes et CISSS', 'C-40 ; 03 K6'],
           ['Caméra d\'urgence : « aucun arrêt » (D5) contre dépose temporaire (D4, ME-145)', 'T14 ; 3.S ou A.1', 'WSP', 'Z-06 ; 03 §2.8'],
           ['Sous-phases absentes du tableau CISSS (C.1, C.3, B.1.1) et lignes sans sous-phase (échelles, issue no 3)', 'Option B', 'CISSS', 'CI-TAB-023, 026 ; C-30']]
    decb = box(808, 404, 784, BOT - 404, table(dec, ['350px', '170px', '120px', '120px']), 'Décisions à obtenir, communes à toutes les options', 'dec')
    conv = box(40, 622, 760, BOT - 622, '<div class="txt"><b>Ce que le cahier ne fait pas.</b> Aucune durée ni calendrier : les repères « ±5 / ±8 / ±4 mois » de la feuille 010 sont des indications des architectes (C-34). Aucune contrainte ajoutée au registre : chaque élément dessiné cite sa ligne. Les contours des zones, les repères d\'élévation et les points fixes sont des superpositions [lecture] sur les rendus des feuilles 010, 011, 001 et 002 ; toute localisation que les documents ne fixent pas est marquée [à confirmer].<br><br><b>Lecture des planches.</b> Planche 0 : site, commune à toutes les options. Pour chaque option : ordre des phases (plan recoloré), installations temporaires et coupures (étiquettes T, matrice), séquence (dépendances, saisons, nouvelle issue, validations CISSS). Registre complet : analyse/02-contraintes.md ; plan de phasage : analyse/03-phasage.md ; vérification : analyse/04-verification.md.</div>', 'Portée et conventions du cahier', 'conv')
    return ('<section class="planche">' + header(num, 'Comparaison des options et recommandation', 'Conflits levés, conflits résiduels, décisions à obtenir et de qui ; option recommandée')
            + comp + reco + decb + conv + footer(num, total, 'analyse/03-phasage.md §2.7, §4 (K1 à K7), §6 ; analyse/04-verification.md §7, §8.') + '</section>')

CSS = """
@page { size: 17in 11in; margin: 0; }
body { margin: 0; font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif; color: #1a1a1a; font-size: 12px; }
.planche { position: relative; width: 1632px; height: 1056px; overflow: hidden; page-break-after: always; background: #fff; }
.planche:last-child { page-break-after: auto; }
.hdr { position: absolute; left: 40px; top: 22px; right: 40px; height: 66px; border-bottom: 2px solid #17324d; }
.h1 { font-size: 22px; font-weight: bold; color: #17324d; width: 980px; }
.h2 { font-size: 13px; color: #24486b; margin-top: 4px; }
.proj { position: absolute; right: 0; top: 4px; font-size: 12px; color: #444; text-align: right; width: 520px; line-height: 1.3; }
.ftr { position: absolute; left: 40px; right: 40px; top: 1008px; height: 36px; font-size: 12px; color: #444; border-top: 1px solid #b8c4d0; padding-top: 4px; line-height: 1.25; box-sizing: border-box; overflow: hidden; }
.ftr div { padding-right: 72px; white-space: nowrap; overflow: hidden; }
.ftr .pg { position: absolute; right: 0; top: 4px; font-weight: bold; color: #17324d; white-space: nowrap; font-size: 13px; }
.picto { display: inline-block; width: 15px; height: 15px; line-height: 15px; text-align: center; background: #f57c00; color: #fff; font-weight: bold; border-radius: 2px; font-size: 12px; }
.plan { position: absolute; overflow: hidden; border: 1px solid #b8c4d0; background: #fff; }
.box { position: absolute; border: 1px solid #b8c4d0; background: #fff; box-sizing: border-box; overflow: hidden; padding: 5px 7px; }
.bt { font-size: 13px; font-weight: bold; color: #17324d; margin-bottom: 4px; line-height: 1.25; }
.cap { position: absolute; font-size: 12px; color: #333; line-height: 1.28; }
.note { font-size: 12px; color: #444; margin-top: 4px; line-height: 1.25; }
.txt { font-size: 12px; line-height: 1.32; margin: 0; } .txt p { margin: 0 0 6px; } .txt.big { font-size: 13.5px; line-height: 1.4; }
.txt.cols2 { column-count: 2; column-gap: 18px; }
ul.txt { padding-left: 16px; } ul.txt li { margin-bottom: 5px; }
table.t { border-collapse: collapse; width: 100%; table-layout: fixed; font-size: 12px; }
table.t th, table.t td { border: 1px solid #c9d1da; padding: 2px 4px; vertical-align: top; text-align: left; line-height: 1.22; overflow-wrap: break-word; }
table.t th { background: #e8edf2; }
table.mat td { font-size: 12px; padding: 1.5px 3px; }
.seq { font-size: 14px; font-weight: bold; color: #17324d; line-height: 1.6; }
.seq span { padding: 2px 7px; border-radius: 3px; color: #fff; white-space: nowrap; }
.s0 { background: #607d8b; } .s1 { background: #3b7dd8; } .s2 { background: #2e7d32; } .s3 { background: #ef6c00; } .s4 { background: #455a64; }
.seqn { font-size: 12px; font-weight: normal; color: #333; margin-top: 6px; line-height: 1.3; }
"""

def main():
    args = sys.argv[1:]
    out = pathlib.Path(args[args.index('--out') + 1]) if '--out' in args else ROOT / 'plan-phasage-graphique.pdf'
    prep_images()
    pages = [lambda n, t: planche0(n, t)]
    for opt in ['R', 'A2', 'A3', 'B']:
        pages += [lambda n, t, o=opt: planche_ordre(o, n, t), lambda n, t, o=opt: planche_installations(o, n, t), lambda n, t, o=opt: planche_sequence(o, n, t)]
    pages.append(lambda n, t: planche_comparaison(n, t))
    total = len(pages)
    body = ''.join(f(i + 1, total) for i, f in enumerate(pages))
    doc = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Cahier de phasage graphique — Hôpital de Chandler R-657-24</title><style>{CSS}</style></head><body>{body}</body></html>'
    htmlp = BUILD / 'planches.html'; htmlp.write_text(doc, encoding='utf-8')
    r = subprocess.run(['node', str(ROOT / 'src' / 'topdf.cjs'), str(htmlp), str(out), str(BUILD / 'debordements.json')], capture_output=True, text=True)
    print(r.stdout, r.stderr[-1500:])

if __name__ == '__main__':
    main()
