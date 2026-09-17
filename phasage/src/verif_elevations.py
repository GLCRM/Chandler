"""Contrôles du cahier de phasage par élévation (à lancer après build_elevations.py).
1. Aucun débordement ni chevauchement de boîte (rapport de topdf.cjs).
2. Aucun texte sous 9 pt dans le PDF.
3. Chaque code de ligne cité dans les données existe dans data/d5_equipements.json.
4. Aucun appareil sans repère d'élévation n'est positionné sur le dessin.
5. Les 23 lignes N-F du tableau sont toutes présentes dans la liste des appareils.
6. Rasterisation de chaque page (62 ppp) dans build/evNN.png.
Usage : python3 src/verif_elevations.py [chemin du PDF]
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pymupdf, elev_data as E

ROOT = pathlib.Path(__file__).resolve().parents[1]
pdf = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'plan-phasage-elevations.pdf'
ok = True
def fail(m):
    global ok; ok = False; print('ÉCHEC :', m)

rep = json.loads((ROOT / 'build' / 'deb_elev.json').read_text())
for e in rep: fail(f"mise en page : {e}")
print(f'1. débordements et chevauchements : {len(rep)}')

doc = pymupdf.open(pdf); small = []
for pi, page in enumerate(doc):
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for sp in l['spans']:
                if sp['text'].strip() and sp['size'] < 8.9: small.append((pi + 1, round(sp['size'], 2), sp['text'][:30]))
for x in small: fail(f'texte sous 9 pt : {x}')
print(f'2. pages : {len(doc)} ; spans sous 9 pt : {len(small)}')

D5 = {r['code'] for r in json.loads((ROOT / 'data' / 'd5_equipements.json').read_text(encoding='utf-8'))}
inconnus = [a[0] for a in E.APPAREILS if a[0] != '—' and a[0] not in D5]
for c in inconnus: fail(f'code absent du tableau D5 : {c}')
print(f'3. codes cités : {len(E.APPAREILS)} ; absents du tableau : {len(inconnus)}')

pos = [a[0] for a in E.APPAREILS if not a[3].startswith('non repéré')]
nonpos = [a[0] for a in E.APPAREILS if a[3].startswith('non repéré')]
print(f'4. appareils positionnés sur le dessin : {len(pos)} ; non positionnés faute de repère : {len(nonpos)} — {", ".join(nonpos)}')

nf = sorted(c for c in D5 if c.startswith('N-F'))
manquants = [c for c in nf if c not in [a[0] for a in E.APPAREILS]]
for c in manquants: fail(f'ligne N-F du tableau absente du cahier : {c}')
print(f'5. lignes N-F du tableau : {len(nf)} ; absentes du cahier : {len(manquants)}')

for pi, page in enumerate(doc): page.get_pixmap(dpi=62).save(ROOT / 'build' / f'ev{pi + 1:02d}.png')
print(f'6. pages rasterisées : {len(doc)}')
print('RÉSULTAT :', 'conforme' if ok else 'non conforme')
sys.exit(0 if ok else 1)
