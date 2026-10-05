"""Assemble les cinq rapports lisibles en un seul PDF lettre portrait.

Usage : python3 analyse/lisible/outils/construire_pdf.py [dossier de travail]
Le HTML intermédiaire va dans le dossier de travail (par défaut /tmp) ; seul le
PDF est écrit dans analyse/lisible/.
"""
import sys, re, html, pathlib, subprocess
import markdown

ICI = pathlib.Path(__file__).resolve().parent
LISIBLE = ICI.parent
TRAVAIL = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('/tmp')
SORTIE = LISIBLE / 'R-657-24_Chandler_rapports_lisibles.pdf'
RAPPORTS = ['01-inventaire', '02-contraintes', '03-phasage', '04-verification', '05-phasage-elevations']

CSS = """
@page { size: Letter; }
body { font-family: "Liberation Sans", Arial, sans-serif; font-size: 10.5pt; line-height: 1.48; color: #1a1a1a; margin: 0; }
.couverture { page-break-after: always; padding-top: 40mm; }
.couverture .projet { font-size: 11pt; color: #444; letter-spacing: .02em; }
.couverture h1 { font-size: 26pt; line-height: 1.15; color: #17324d; margin: 10mm 0 6mm; border: 0; }
.couverture .sous { font-size: 13pt; color: #24486b; margin-bottom: 18mm; }
.couverture .mention { font-size: 10pt; color: #444; border-top: 1px solid #b8c4d0; padding-top: 4mm; margin-top: 14mm; }
.sommaire { page-break-after: always; }
.sommaire h2 { margin-top: 0; }
.sommaire .item { margin: 0 0 5mm; }
.sommaire .item b { color: #17324d; font-size: 11.5pt; }
.sommaire .item div { color: #333; margin-top: 1mm; }
.rapport { page-break-before: always; }
h1 { font-size: 18pt; color: #17324d; line-height: 1.2; margin: 0 0 3mm; padding-bottom: 2mm; border-bottom: 2px solid #17324d; }
h2 { font-size: 13pt; color: #17324d; margin: 7mm 0 2mm; page-break-after: avoid; }
h3 { font-size: 11pt; color: #24486b; margin: 5mm 0 1.5mm; page-break-after: avoid; }
p { margin: 0 0 3mm; text-align: left; orphans: 3; widows: 3; }
.entete { font-size: 9.5pt; color: #555; margin-bottom: 4mm; }
hr { border: 0; border-top: 1px solid #b8c4d0; margin: 3mm 0 5mm; }
ul, ol { margin: 0 0 3mm 5mm; padding-left: 4mm; }
li { margin-bottom: 1.5mm; }
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; line-height: 1.3; margin: 2mm 0 4mm; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #c9d1da; padding: 1.3mm 2mm; vertical-align: top; text-align: left; }
th { background: #e8edf2; }
code { font-family: "Liberation Mono", monospace; font-size: 9.5pt; color: #5e1a75; background: none; }
strong { color: #111; }
"""

def corps(nom):
    src = (LISIBLE / f'{nom}.md').read_text(encoding='utf-8')
    lignes = src.split('\n')
    titre = lignes[0].lstrip('# ').strip()
    # les deux premières lignes non vides après le titre (projet, version) sont mises en petit
    idx = [i for i, l in enumerate(lignes[1:], 1) if l.strip()][:2]
    entete = '<div class="entete">' + '<br>'.join(html.escape(lignes[i]) for i in idx) + '</div>'
    reste = '\n'.join(lignes[idx[-1] + 1:])
    h = markdown.markdown(reste, extensions=['tables', 'sane_lists'])
    # premier paragraphe après le filet = la phrase qui mène le rapport
    chapeau = re.sub(r'<[^>]+>', '', h.split('<hr />', 1)[1].split('</p>', 1)[0]).strip()
    return titre, f'<section class="rapport"><h1>{html.escape(titre)}</h1>{entete}{h}</section>', chapeau

def main():
    parts = [corps(n) for n in RAPPORTS]
    couverture = ('<div class="couverture"><div class="projet">Santé Québec – CISSS de la Gaspésie · Appel d\'offres AOC-077221 · Dossier GLCRM R-657-24</div>'
                  '<h1>Hôpital de Chandler<br>Réfection de l\'enveloppe</h1>'
                  '<div class="sous">Rapports d\'analyse du dossier d\'appel d\'offres et du phasage — version lisible</div>'
                  '<div class="mention">Version du 5 octobre 2026. Document de travail, non contractuel. '
                  'Chaque rapport reprend en prose la version de référence du même numéro, qui reste la source pour toute citation, '
                  'tout tableau complet et toute annexe. Les marqueurs [lecture], [choix] et [à confirmer] distinguent ce qui est lu sur un plan, '
                  'ce que GLCRM propose et ce que les documents ne fixent pas.</div></div>')
    sommaire = ('<div class="sommaire"><h2>Les cinq rapports</h2>'
                + ''.join(f'<div class="item"><b>{html.escape(t)}</b><div>{html.escape(c)}</div></div>' for t, _, c in parts)
                + '</div>')
    doc = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Hôpital de Chandler — rapports lisibles</title>'
           f'<style>{CSS}</style></head><body>{couverture}{sommaire}' + ''.join(b for _, b, _ in parts) + '</body></html>')
    htmlp = TRAVAIL / 'rapports_lisibles.html'
    htmlp.write_text(doc, encoding='utf-8')
    r = subprocess.run(['node', str(ICI / 'imprimer.cjs'), str(htmlp), str(SORTIE)], capture_output=True, text=True)
    print(r.stdout.strip(), r.stderr[-800:])

if __name__ == '__main__':
    main()
