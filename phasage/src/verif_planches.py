"""Contrôles du cahier de phasage graphique (à lancer après build_planches.py).
1. Aucun débordement ni chevauchement de boîte (rapport de topdf.cjs).
2. Aucun texte sous 9 pt dans le PDF (spans PyMuPDF).
3. Chaque code de phase ou de sous-phase présent dans le HTML des planches existe dans analyse/03-phasage.md.
4. Chaque étiquette T est dessinée sur la face écrite au registre (champ « face » des CALLOUTS contre les bandes du plan clé).
5. Rasterisation de chaque page (60 ppp) dans build/pgNN.png pour la revue visuelle.
Usage : python3 src/verif_planches.py [chemin du PDF]"""
import sys, re, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pymupdf
from zones import ZONES, FACES_TOUR
import build_planches as bp

ROOT = pathlib.Path(__file__).resolve().parents[1]
pdf = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'plan-phasage-graphique.pdf'
ok = True
def fail(msg):
    global ok; ok = False; print('ÉCHEC :', msg)

# 1. débordements et chevauchements
rep = json.loads((ROOT / 'build' / 'debordements.json').read_text())
if rep:
    for e in rep: fail(f"planche {e['planche']} : {e}")
print(f'1. débordements et chevauchements : {len(rep)}')

# 2. tailles de police
doc = pymupdf.open(pdf); small = []
for pi, page in enumerate(doc):
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for sp in l['spans']:
                if sp['text'].strip() and sp['size'] < 8.9: small.append((pi + 1, round(sp['size'], 2), sp['text'][:40]))
for x in small: fail(f'texte sous 9 pt : {x}')
print(f'2. pages : {len(doc)} ; spans sous 9 pt : {len(small)}')

# 3. codes de sous-phases contre 03
html_txt = (ROOT / 'build' / 'planches.html').read_text()
p03 = (ROOT.parent / 'analyse' / '03-phasage.md').read_text()
pat = re.compile(r'(?<![\w.])(?:[23]\.[NESO]|[ABC]\.\d(?:\.\d)?|B-[ABC])(?![\w.])')
codes_html = sorted(set(pat.findall(html_txt))); codes_03 = set(pat.findall(p03))
missing = [c for c in codes_html if c not in codes_03]
for c in missing: fail(f'code de sous-phase absent de 03 : {c}')
print(f'3. codes dessinés ou cités : {len(codes_html)} ; absents de 03 : {len(missing)} — {" ".join(codes_html)}')

# 4. étiquettes T sur la face écrite
def bbox(polys):
    xs = [x for p in polys for x, _ in p]; ys = [y for p in polys for _, y in p]; return min(xs), min(ys), max(xs), max(ys)
tour = ZONES['A'][0]
bandes = {  # x0, y0, x1, y1 en px image ; déduites des polygones de zones.py
 'ouest': (bbox([ZONES['O'][0]])[0], bbox([ZONES['J'][0]])[1], bbox([FACES_TOUR['2.O']])[2] + 4, bbox([ZONES['I'][0]])[3]),   # basilaire ouest, face ouest de J, bande 2.O, angle I
 'nord': (bbox([ZONES['J'][0]])[0], bbox([ZONES['J'][0]])[1], bbox([ZONES['K'][0]])[2] + 4, bbox([FACES_TOUR['2.N']])[3]),       # basilaire nord J, B, K et bande 2.N
 'est': (bbox([FACES_TOUR['2.E']])[0], bbox([ZONES['D'][0]])[1], bbox([ZONES['L'][0]])[2], bbox([ZONES['E'][0]])[3]),         # bande 2.E et basilaire est D, F, E, L
 'sud': (bbox([ZONES['I'][0]])[0] - 6, bbox([FACES_TOUR['2.S']])[1], bbox([ZONES['G'][0]])[2], bbox([ZONES['P'][0]])[3]),      # bande 2.S, basilaires sud I, H, G, saillie P
}
print('4. bandes (px image) :', bandes)
for code, spA, spB, quoi, ids, (px, py), _, face in bp.CALLOUTS:
    x0, y0, x1, y1 = bandes[face]
    inside = x0 <= px <= x1 and y0 <= py <= y1
    print(f'   {code:4} face écrite {face:5} point ({px},{py}) -> {"ok" if inside else "HORS BANDE"}')
    if not inside: fail(f'{code} hors de la bande {face}')

# 5. rasterisation
for pi, page in enumerate(doc):
    page.get_pixmap(dpi=60).save(ROOT / 'build' / f'pg{pi + 1:02d}.png')
print(f'5. pages rasterisées : {len(doc)} (build/pgNN.png)')
print('RÉSULTAT :', 'conforme' if ok else 'non conforme')
sys.exit(0 if ok else 1)
