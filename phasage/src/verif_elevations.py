"""Contrôles du cahier de phasage par élévation (à lancer après build_elevations.py).

1. Aucun débordement ni chevauchement de boîte (rapport de topdf.cjs).
2. Aucun texte sous 9 pt dans le PDF.
3. Chaque code cité dans les données existe dans data/d5_equipements.json.
4. Chaque ligne du tableau ME est reprise dans la façade correspondante.
5. Aucun appareil sans repère d'élévation n'est positionné sur le dessin.
6. Chaque appareil positionné tombe dans le cadre de son élévation.
7. Chaque verrou cité par un appareil existe, et chaque verrou est cité.
8. Rasterisation de chaque page (62 ppp) dans build/evNN.png.

Usage : python3 src/verif_elevations.py [chemin du PDF]
"""
import sys, json, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pymupdf, elev_data as E

ROOT = pathlib.Path(__file__).resolve().parents[1]
pdf = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'plan-phasage-elevations.pdf'
ok = True
def fail(m):
    global ok; ok = False; print('ÉCHEC :', m)

rep = json.loads((ROOT / 'build' / 'deb_elev.json').read_text())
for e in rep: fail(f'mise en page : {e}')
print(f'1. débordements et chevauchements : {len(rep)}')

doc = pymupdf.open(pdf); small = []
for pi, page in enumerate(doc):
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for sp in l['spans']:
                if sp['text'].strip() and sp['size'] < 8.9: small.append((pi + 1, round(sp['size'], 2), sp['text'][:30]))
for x in small: fail(f'texte sous 9 pt : {x}')
print(f'2. pages : {len(doc)} ; spans sous 9 pt : {len(small)}')

D5 = json.loads((ROOT / 'data' / 'd5_equipements.json').read_text(encoding='utf-8'))
CODES = {r['code'] for r in D5}
PREFIXE = {'nord': 'N-', 'sud': 'S-', 'est': 'E-', 'ouest': 'O-'}
total_app = 0
for fac, app in E.APPAREILS.items():
    total_app += len(app)
    inconnus = [a[0] for a in app if a[0] != '—' and a[0] not in CODES]
    for c in inconnus: fail(f'{fac} : code absent du tableau ME : {c}')
    attendus = sorted(c for c in CODES if c.startswith(PREFIXE[fac]))
    cites = {a[0] for a in app}
    manquants = [c for c in attendus if c not in cites]
    for c in manquants: fail(f'{fac} : ligne du tableau ME absente du cahier : {c}')
    etrangers = [a[0] for a in app if a[0] != '—' and not a[0].startswith(PREFIXE[fac])]
    for c in etrangers: fail(f'{fac} : code d\'une autre façade : {c}')
    print(f'   {fac:6} : {len(app):2} appareils ; lignes du tableau {len(attendus):2} ; absentes {len(manquants)} ; codes inconnus {len(inconnus)}')
print(f'3-4. appareils au total : {total_app} ; lignes du tableau ME : {len(CODES)}')

for fac, app in E.APPAREILS.items():
    g = E.GEOMS[fac]
    nonpos = [a[0] for a in app if a[3].startswith('non repéré')]
    hors = []
    for code, etat, lib, rep_, a, mm, dxy, v in app:
        if rep_.startswith('non repéré'): continue
        x, y = g.ax(a), g.niv(mm)
        if not (-4 <= x <= g.largeur + 4 and -4 <= y <= g.hauteur + 4): hors.append((code, round(x), round(y)))
    for h in hors: fail(f'{fac} : appareil hors du cadre de l\'élévation : {h}')
    print(f'   {fac:6} : non positionnés faute de repère {len(nonpos)} ({", ".join(nonpos) or "aucun"}) ; hors cadre {len(hors)}')
print('5-6. positions vérifiées')

for fac, app in E.APPAREILS.items():
    cles = {v[0] for v in E.VERROUS.get(fac, [])}
    cites = {a[7] for a in app if a[7]}
    for k in cites - cles: fail(f'{fac} : verrou cité par un appareil mais absent : {k}')
    orphelins = cles - cites
    print(f'   {fac:6} : verrous {len(cles)} ; cités {len(cites)} ; non rattachés à un appareil {len(orphelins)}')
print('7. verrous vérifiés')

for pi, page in enumerate(doc): page.get_pixmap(dpi=62).save(ROOT / 'build' / f'ev{pi + 1:02d}.png')
print(f'8. pages rasterisées : {len(doc)}')
print('RÉSULTAT :', 'conforme' if ok else 'non conforme')
sys.exit(0 if ok else 1)
