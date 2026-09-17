"""Cahier de phasage par élévation — Hôpital de Chandler R-657-24.

Quatre planches tabloïd paysage : méthode et correspondance élévation ↔ façade,
façade nord (appareils sur l'élévation), façade nord (verrous appareils /
architecture), zones de chantier et clôtures.

Usage : python3 src/build_elevations.py [--out phasage/plan-phasage-elevations.pdf]
Règles : aucun texte sous 9 pt (12 px à 96 px/po) ; tout ce qui est lu sur un
plan porte [lecture], tout ce qui est proposé porte [choix].
"""
import sys, pathlib, subprocess, html, json

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import elev_data as E

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'; BUILD.mkdir(exist_ok=True)
BOT = 1002          # bas commun des boîtes ; le pied de page occupe 1008-1044
D5 = json.loads((ROOT / 'data' / 'd5_equipements.json').read_text(encoding='utf-8'))
D5I = {r['code']: r for r in D5}

def esc(t): return html.escape(str(t))
def rich(t):
    """Gras **…**, code `…` et échappement."""
    t = esc(t)
    while '**' in t: t = t.replace('**', '<b>', 1).replace('**', '</b>', 1)
    while t.count('`') >= 2: t = t.replace('`', '<span class="mk">', 1).replace('`', '</span>', 1)
    return t

# ------------------------------------------------------------------ HTML
def box(left, top, width, height, inner, title=None, id=''):
    t = f'<div class="bt">{rich(title)}</div>' if title else ''
    return f'<div class="box" id="{id}" style="left:{left}px;top:{top}px;width:{width}px;height:{height}px">{t}{inner}</div>'

def table(rows, widths, cls=''):
    out = [f'<table class="t {cls}"><colgroup>' + ''.join(f'<col style="width:{w}">' for w in widths) + '</colgroup>']
    for i, r in enumerate(rows):
        tag = 'th' if i == 0 else 'td'
        out.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in r) + '</tr>')
    return ''.join(out) + '</table>'

def header(num, total, titre, sous):
    return (f'<div class="hdr"><div class="h1">Planche {num} / {total} — {esc(titre)}</div><div class="h2">{rich(sous)}</div>'
            f'<div class="proj">Hôpital de Chandler — Réfection de l\'enveloppe · CISSS de la Gaspésie · AOC-077221 · Dossier GLCRM R-657-24<br>'
            f'Cahier de phasage par élévation — document de travail, non contractuel, sans durée</div></div>')

def footer(num, total, sources):
    return (f'<div class="ftr"><div><b>Sources :</b> {rich(sources)}</div>'
            f'<div><b>Conventions :</b> [lecture] = lu sur un plan, non écrit ; [choix] = proposition du présent cahier ; [à confirmer] = non fixé par les documents ; '
            f'N-F-V-005 = ligne du tableau de coordination des équipements électromécaniques (façade, élévation, discipline, numéro) ; '
            f'AR-DEV-, AR-PLN-, ME-, ST-, CI- = lignes du registre analyse/02-contraintes.md ; C-, Z-, K- = contradictions, zones d\'ombre, conflits.</div>'
            f'<span class="pg">page {num} / {total}</span></div>')

# ------------------------------------------------------------------ SVG
def txt(x, y, s, size=13, anchor='start', weight='normal', fill='#111'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="font-size:{size}px;font-weight:{weight};fill:{fill}">{esc(s)}</text>'

def elevation(fac, left=40, top=96, width=1540):
    """Élévation rendue depuis sa feuille d'architecture + calque des appareils.

    Les appareils dont le repère commence par « non repéré » ne sont jamais
    positionnés : le dessin ne les montre pas."""
    g = E.GEOMS[fac]
    h = round(width * g.hauteur / g.largeur)
    k = width / g.largeur                      # unité svg -> px de la planche
    s = [f'<svg viewBox="0 0 {g.largeur} {g.hauteur}" width="{width}" height="{h}" style="position:absolute;left:0;top:0" xmlns="http://www.w3.org/2000/svg">']
    for nom, mm in E.NIVEAUX:
        y = g.niv(mm)
        if 12 < y < g.hauteur - 4:
            s.append(f'<line x1="0" y1="{y:.1f}" x2="{g.largeur}" y2="{y:.1f}" stroke="#1565c0" stroke-width="{0.8/k:.2f}" stroke-dasharray="7,5" opacity="0.5"/>')
            s.append(txt(4, y - 3, nom, 12 / k, 'start', 'normal', '#1565c0'))
    for code, etat, lib, rep, a, mm, (dx, dy), v in E.APPAREILS.get(fac, []):
        if rep.startswith('non repéré'): continue
        x, y = g.ax(a), g.niv(mm)
        col = E.ETATS[etat][0]
        lab = code if code != '—' else 'hors ME'
        w = (7.0 * len(lab) + 8) / k
        hh = 18 / k
        lx = min(max(x + dx / k, w / 2 + 2), g.largeur - w / 2 - 2)
        ly = y + dy / k
        s.append(f'<line x1="{lx:.1f}" y1="{ly:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="{1.1/k:.2f}" stroke-dasharray="2,2"/>')
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4/k:.1f}" fill="{col}" stroke="#fff" stroke-width="{1.2/k:.2f}"/>')
        s.append(f'<rect x="{lx - w/2:.1f}" y="{ly - hh/2:.1f}" width="{w:.1f}" height="{hh:.1f}" rx="{3/k:.1f}" fill="{col}" stroke="#fff" stroke-width="{1/k:.2f}"/>')
        s.append(txt(lx, ly + 5 / k, lab, 12 / k, 'middle', 'bold', '#fff'))
    s.append('</svg>')
    return (f'<div class="plan" style="left:{left}px;top:{top}px;width:{width}px;height:{h}px">'
            f'<img src="../img/{g.img}" style="position:absolute;left:0;top:0;width:{width}px;height:{h}px">'
            + ''.join(s) + '</div>'), h

# ------------------------------------------------------------------ planches
def planche_methode(num, total):
    rows = [['Repère', 'Titre du dessin (feuilles 201 à 204)', 'Démo.', 'Constr.', 'Façade au tableau ME', 'Lignes', 'Cahier en plan (2026-09-15)']]
    for l, t, fd, fc, fa, n, anc in E.REPERES:
        corr = ' class="corr"' if 'tranché' in anc or 'corrigé' in anc else ''
        rows.append([f'<b>{l}</b>', esc(t), fd, fc, f'<b>{fa}</b>', str(n) if n else '—', f'<span{corr}>{esc(anc)}</span>'])
    tab = box(40, 96, 900, 390, table(rows, ['54px', '250px', '56px', '62px', '120px', '58px', '250px'])
              + '<div class="note">Les onze repères A à K sont les titres des dessins eux-mêmes : « Élévation nord », « Élévation est partielle »… La façade est donc <b>écrite</b>, elle n\'est plus lue sur le plan clé. Les repères J et K ne portent aucune ligne au tableau ME.</div>',
              'Correspondance repère d\'élévation ↔ façade — établie sur les titres des dessins et le codage du tableau ME', 'p0-rep')
    cite = ('<div class="txt"><b>Légende du tableau de coordination des équipements électromécaniques</b> (D5, révision du 11 mai 2026), notes générales 1 et 2 :<br>'
            '<span class="cit">« 1. Orientation façade : Nord, Sud, Est, Ouest »<br>'
            '« 2. Numérotation élévation : Se référer aux bulles d\'élévations en architecture et ingénierie (A à I) »</span><br><br>'
            'Chaque ligne du tableau porte donc déjà sa façade et son élévation. Les 93 lignes se répartissent ainsi :</div>')
    rep = [['Façade', 'Lignes', 'Élévations'], ['Sud', '30', 'A'], ['Ouest', '25', 'B (14), C (5), E (4), I (2)'],
           ['Nord', '23', 'F'], ['Est', '15', 'G (10), H (4), D (1)']]
    disc = [['Discipline', 'Lignes'], ['Électricité', '56'], ['Ventilation', '30'], ['Plomberie', '5'],
            ['Gaz médicaux', '1'], ['Protection incendie', '1']]
    d5 = box(956, 96, 636, 390, cite + table(rep, ['90px', '66px', '380px']) + '<div style="height:6px"></div>' + table(disc, ['380px', '222px'])
             + '<div class="note">Le codage couleur ajoute trois états : gris « non touché » (11 lignes), orange « à démanteler, non utilisé » (2), jaune « à valider avec le propriétaire » (3).</div>',
             'Le tableau ME est déjà indexé par élévation — c\'est le pivot de ce cahier', 'p0-d5')
    ce = box(40, 502, 900, BOT - 502,
             '<div class="txt"><b>Pourquoi repartir des élévations.</b> Le cahier de phasage en plan (14 planches, feuille 010) montre où sont les zones et dans quel ordre elles sont traitées. '
             'Il ne montre pas ce que l\'entrepreneur doit décrocher d\'un mur avant de le démolir. Or les documents électromécaniques sont organisés par façade et par élévation, pas par zone : '
             'le tableau de coordination de WSP et les élévations ME001 à ME003 se lisent en regard des élévations d\'architecture 201 à 204, axe par axe.<br><br>'
             '<b>Trois corrections que la lecture en élévation apporte au cahier en plan.</b><br>'
             '1. Les repères C et D portaient un « ? » (correspondance non tranchée, reportée en décision à obtenir des architectes). Les titres des dessins les tranchent : <b>C = élévation ouest partielle</b>, <b>D = élévation est partielle</b>. La décision tombe.<br>'
             '2. Le repère H était lu « nord partielle » sur le plan clé de la feuille 011. Le dessin s\'intitule <b>« Élévation est partielle »</b> et le tableau ME code ses quatre lignes en « E » (est) — dont la hotte de médecine nucléaire, déjà rattachée à la face est. La lecture du plan clé était fausse.<br>'
             '3. Deux repères, <b>J</b> (élévation sud partielle) et <b>K</b> (élévation ouest partielle), n\'apparaissaient pas du tout dans le cahier en plan.<br><br>'
             '<b>Ce que le présent cahier ajoute.</b> Pour chaque façade : l\'inventaire des appareils avec leur état et leur fenêtre d\'interruption, la séquence d\'architecture, et le <b>verrou</b> entre les deux — quel appareil bloque quelle étape. Plus une planche sur les zones de chantier et les clôtures, qui bougent au fil des phases.</div>',
             'Ce que change la lecture en élévation', 'p0-ce')
    meth = box(956, 502, 636, BOT - 502,
               '<div class="txt"><b>Méthode et calage géométrique.</b> Les élévations sont rendues depuis les feuilles d\'architecture à 200 points par pouce ; le calque des appareils est superposé en coordonnées de la feuille.<br><br>'
               'La position horizontale de chaque appareil est donnée par la <b>chaîne d\'axes</b> de la feuille 202 (entraxes écrits : ±7247, ±7113, ±7010… entre les axes 16 et 1, total ±105 927 mm), '
               'la position verticale par la <b>chaîne de niveaux</b> (R00 à 10 000, niveau 100 à 13 952, 200 à 17 901, 300 à 21 559, 400 à 25 202, 500 à 28 882, dessus de parapet à 29 820). '
               'Les deux chaînes donnent la même échelle, 1:200, ce qui vérifie le calage.<br><br>'
               'L\'axe 1 est à l\'ouest et l\'axe 16 à l\'est : l\'élévation nord se lit donc de l\'est (à gauche) vers l\'ouest (à droite). '
               'Vérification : la sortie d\'arrosage écrite « coin nord-est » tombe vers l\'axe 14, et les appareils du quai des ambulances écrits « porte nord du quai » tombent vers l\'axe 1, du côté où le plan clé place la sortie d\'ambulance.<br><br>'
               '<b>Ce qui reste une lecture.</b> La position de chaque appareil le long de l\'élévation est relevée sur les repères de la feuille ME001(D) : elle est marquée `[lecture]`. '
               'Les appareils que le tableau ME place sur une façade sans qu\'aucun repère ne les montre sur l\'élévation sont signalés comme tels plutôt que positionnés.</div>',
               'Méthode', 'p0-meth')
    return ('<section class="planche">' + header(num, total, 'Méthode et correspondance élévation ↔ façade',
            'Les onze repères A à K, la façade de chacun, et ce que la lecture en élévation corrige au cahier en plan')
            + tab + d5 + ce + meth
            + footer(num, total, 'D2 feuilles 201, 201-A, 202, 203, 204 (titres des dessins) ; D5 tableau de coordination des équipements électromécaniques, notes générales 1 et 2 et 93 lignes ; analyse/02-contraintes.md.') + '</section>')

FACADES = {
 'nord':  ("Façade nord",  "Élévation F, feuille 202 — l'est est à gauche, l'ouest à droite",
           "D2 feuille 202 (élévation F) ; D4 ME001(D) ; D5 lignes N-F-…"),
 'est':   ("Façade est",   "Élévation G, feuille 202, et élévations partielles D et H — le sud est à gauche, le nord à droite",
           "D2 feuilles 202 et 201-A (élévations G, D, H) ; D4 ME002(D), ME003(D) ; D5 lignes E-G-…, E-H-…, E-D-…"),
 'sud':   ("Façade sud",   "Élévation A, feuille 201 — l'ouest est à gauche, l'est à droite",
           "D2 feuille 201 (élévation A) ; D4 ME002(D) ; D5 lignes S-A-…"),
 'ouest': ("Façade ouest", "Élévation B, feuille 201, et élévations partielles C, E, I — le nord est à gauche, le sud à droite",
           "D2 feuilles 201 et 201-A (élévations B, C, E, I) ; D4 ME001(D), ME003(D) ; D5 lignes O-B-…, O-C-…, O-E-…, O-I-…"),
}

def planche_appareils(fac, num, total):
    titre, sous, src = FACADES[fac]
    g = E.GEOMS[fac]
    app = E.APPAREILS.get(fac, [])
    plan, h = elevation(fac)
    y = 96 + h + 6
    nonpos = [a[0] for a in app if a[3].startswith('non repéré')]
    leg = [f'<div class="cap" style="left:40px;top:{y}px;width:1540px"><b>États :</b> ']
    for k in ('retire', 'deplace', 'coupe', 'maintenu', 'intact'):
        c, lib = E.ETATS[k]
        leg.append(f'<span class="pill" style="background:{c}">{lib}</span> ')
    leg.append("&nbsp;&nbsp;Chaque pastille porte le code de la ligne du tableau ME. Position le long de l'élévation relevée sur les repères des feuilles ME — [lecture]. "
               f"Traits bleus : niveaux de la feuille. Le {g.gauche} est à gauche, le {g.droite} à droite.")
    if nonpos:
        leg.append(f" <b>Lignes du tableau que le dessin ne montre nulle part</b>, donc non positionnées ici : {', '.join(nonpos)}.")
    leg.append('</div>')
    moitie = (len(app) + 1) // 2
    tab = []
    for col, (x0, part) in enumerate([(40, app[:moitie]), (816, app[moitie:])]):
        rows = [['Ligne ME', '&nbsp;', 'Appareil', 'Repère de la feuille ME', 'Fenêtre écrite']]
        for code, etat, lib, rep, a, mm, dxy, v in part:
            r = D5I.get(code)
            per = ' '.join((r['periode'] if r else '').split())[:46] or '—'
            if r and r['arret'].strip().lower().startswith('n/a'): per = 'non touché'
            rows.append([f'<b>{esc(code)}</b>', f'<span class="dot" style="background:{E.ETATS[etat][0]}"></span>',
                         esc(lib), esc(rep), esc(per)])
        tab.append(box(x0, y + 52, 776, BOT - (y + 52), table(rows, ['84px', '22px', '252px', '158px', '238px']), None, f'{fac}-app{col}'))
    return ('<section class="planche">' + header(num, total, f'{titre} — les appareils sur l\'élévation',
            f'{sous} ; {len(app)} appareils relevés')
            + plan + ''.join(leg) + ''.join(tab)
            + footer(num, total, src + ' ; analyse/02-contraintes.md.') + '</section>')

def planche_verrous(fac, num, total):
    titre, sous, src = FACADES[fac]
    ver = E.VERROUS.get(fac, [])
    rows = [['#', 'Appareil et position', 'À faire avant', 'Étape d\'architecture bloquée', 'Sources']]
    for k, app, av, et, s in ver:
        rows.append([f'<b>{k}</b>', rich(app), rich(av), rich(et), esc(s)])
    tv = box(40, 96, 1552, 568, table(rows, ['32px', '386px', '356px', '416px', '330px']),
             f'Verrous entre les appareils et les travaux d\'architecture — {titre.lower()}', f'{fac}-ver')
    seq = ['<div class="seq">']
    for code, nom, cont in E.ETAPES:
        seq.append(f'<span class="st">{code} {esc(nom)}</span> <span class="ar">→</span> ')
    seq.append('</div><div class="seqn">' + ' · '.join(f'<b>{c}</b> {rich(t)}' for c, n, t in E.ETAPES) + '</div>')
    et = box(40, 680, 940, BOT - 680, ''.join(seq),
             'Séquence type d\'une façade (analyse/03-phasage.md §1.2 et §1.3) — le verrou se joue presque toujours entre E1 et E2', f'{fac}-seq')
    cf = box(996, 680, 596, BOT - 680, E.COMMENTAIRES.get(fac, '<div class="txt">—</div>'),
             f'Ce que les verrous de la {titre.lower()} révèlent', f'{fac}-conf')
    return ('<section class="planche">' + header(num, total, f'{titre} — verrous entre appareils et architecture',
            'Ce qui doit être déplacé, coupé ou maintenu avant chaque étape de la façade, et ce qui reste bloqué tant qu\'il est en place')
            + tv + et + cf
            + footer(num, total, src + ' ; analyse/03-phasage.md §1.3 ; analyse/02-contraintes.md.') + '</section>')

def planche_synthese(num, total):
    ch = box(40, 96, 940, 218, table(E.SYNTHESE_CHIFFRES, ['176px', '58px', '148px', '246px', '96px', '110px', '82px']),
             'Les 93 lignes du tableau de coordination, réparties par façade', 'sy-ch')
    sa = box(40, 326, 940, 232, table(E.SAISON, ['90px', '70px', '450px', '300px'])
             + '<div class="note">Trois lignes exigent l\'été, deux l\'excluent, une se contredit. « Période estivale » n\'est définie nulle part (Z-10) et le contrat n\'ouvre que deux périodes de novembre à avril (C-14).</div>',
             'Les six lignes qui nomment la période estivale — sur les quatre façades', 'sy-sa')
    tx = box(40, 570, 940, BOT - 570, E.SYNTHESE_TXT, 'Ce que l\'exercice apporte au phasage', 'sy-tx')
    dec = [['Décision à obtenir', 'De qui', 'Ce qu\'elle débloque'],
           ['Définition de « période estivale »', 'CISSS', 'La planification saisonnière des quatre façades : six lignes du tableau en dépendent, dont trois qui exigent l\'été et deux qui l\'excluent'],
           ['Sens de la ligne S-A-V-001, « en dehors de la période estivale (quelques jours en été) »', 'CISSS et WSP', 'La façade sud : la ligne se contredit elle-même'],
           ['Correspondance entre les trois numérotations « phase 1/2/3 » (feuille 010, feuille 002, tableau du CISSS)', 'Architectes et CISSS', 'La planche des zones de chantier par phase, et le rattachement des configurations d\'accès au phasage du bâtiment (C-34)'],
           ['Tracé et forme des conduits temporaires de l\'unité d\'hémodialyse, séquence de basculement, fenêtres d\'interruption', 'WSP', 'La façade nord entre les axes 8 et 6 — préalable écrit à la démolition (Z-29)'],
           ['Position de la prise d\'air de la centrale d\'air médical, placée sur l\'élévation F sans repère sur le dessin', 'WSP', 'L\'ordre nord / ouest, qui dépend de l\'emplacement de la prise temporaire (ME-065, ME-067)'],
           ['Doublon de code N-F-E-006 (deux lignes consécutives portent le même numéro, page 6)', 'WSP', 'La traçabilité du tableau'],
           ['Longueur des tronçons traités d\'un coup sur chaque façade', 'Entrepreneur, avec le CISSS', 'La durée d\'indisponibilité de chaque appareil marqué « toute la durée des travaux » : 47 lignes sur 93'],
           ['Plan de situation de la zone clôturée par phase, barrières verrouillables, cloisons anti-poussière', 'Entrepreneur', 'Les zones de chantier, que les plans ne montrent que dans une seule configuration (AR-DEV-171, 190, 148)'],
           ]
    dc = box(996, 96, 596, BOT - 96, table(dec, ['300px', '110px', '166px']),
             'Décisions à obtenir, par destinataire', 'sy-dec')
    return ('<section class="planche">' + header(num, total, 'Synthèse des quatre façades',
            'Ce que le regroupement des appareils par façade fait apparaître, et les décisions qui commandent la suite')
            + ch + sa + tx + dc
            + footer(num, total, 'D5 tableau de coordination (93 lignes, notes générales 1, 2 et 8) ; analyse/02-contraintes.md ; analyse/03-phasage.md §0.4, §4 K2 et K3 ; Z-10, Z-29, C-14, C-34.') + '</section>')

def planche_chantier(num, total):
    img = ('<div class="plan" style="left:40px;top:96px;width:470px;height:522px">'
           '<img src="../img/A001_site.png" style="position:absolute;left:0;top:0;width:470px;height:522px"></div>'
           '<div class="cap" style="left:40px;top:622px;width:470px">Feuille 001, plan d\'implantation. <b>Une seule configuration de clôture</b> pour tout le site, '
           'repérée dix fois par la note 23 « zone de chantier clôturer ». Aucune mention de phase sur cette feuille.</div>'
           '<div class="plan" style="left:526px;top:96px;width:236px;height:260px"><img src="../img/A002_amb.png" style="position:absolute;left:0;top:0;width:236px;height:260px"></div>'
           '<div class="plan" style="left:526px;top:362px;width:236px;height:256px"><img src="../img/A002_entree.png" style="position:absolute;left:0;top:0;width:236px;height:256px"></div>'
           '<div class="cap" style="left:526px;top:622px;width:236px">Feuille 002, détails 1 et 2 : les <b>seuls</b> endroits où la clôture est dessinée dans plus d\'une position — '
           'zone d\'ambulance (2 configurations), entrée principale (3).</div>')
    rows = [['Ce qui est écrit et dessiné', 'Où', 'Identifiant'],
            ['Clôture de chantier neuve, 1830 mm, palissade métallique avec glissières de béton et toile anti-poussière', 'Légende 001/002 ; devis 01 56 00', 'AR-PLN-005 ; AR-DEV-189'],
            ['Zone d\'ambulance : deux configurations, entrée et sortie au nord puis au sud', 'Feuille 002, détail 1', 'AR-PLN-018'],
            ['Entrée principale : trois configurations autour de la marquise, la troisième sans clôture sous la marquise', 'Feuille 002, détail 2', 'AR-PLN-019'],
            ['Un panneau indicateur d\'ambulance <b>par phase de travaux</b> du secteur', 'Note 35', 'AR-PLN-014'],
            ['Chemin en gravier temporaire vers l\'accès ambulance, terrain remis en état', 'Note 22 ; détail 1', 'AR-PLN-004'],
            ['Débarcadère et case de stationnement réservés à l\'entrepreneur', 'Notes 19 et 21', 'AR-PLN-002, 003'],
            ['Deux accès de chantier : accès général au sud-est, accès au sud-ouest', 'Notes 30 et 32', 'AR-PLN-012'],
            ['Issue extérieure et chemin d\'évacuation libres, 1650 mm jusqu\'à la voie publique', 'Note 24 ; détails 3, 4, 5', 'AR-PLN-006'],
            ['Zone IRM : aucun entreposage métallique quand l\'IRM est en service', 'Note 27 ; détail 5', 'AR-PLN-009'],
            ['Accès pompier à la borne-fontaine en tout temps', 'Note 1', 'AR-PLN-001'],
            ['Section de clôture plus haute près du nouvel escalier no 7', 'Note 15 de la 001 seulement', 'C-38'],
            ]
    t1 = box(778, 96, 814, 306, table(rows, ['470px', '190px', '138px']), 'Ce que les feuilles 001 et 002 fixent', 'ch-ecrit')
    rows = [['Ce que le devis exige par phase', 'Qui le produit', 'Identifiant'],
            ['« Barrières d\'accès verrouillables <b>selon l\'aménagement du site et selon les phasages</b> » pour les camions, plus au moins une porte piétonne', 'Entrepreneur', 'AR-DEV-190'],
            ['Plan de situation : emprise et dimensions de la zone à clôturer, nombre de roulottes, voies d\'accès, détails d\'installation de la clôture', 'Entrepreneur', 'AR-DEV-171'],
            ['« Emplacements des cloisons servant à lutter contre la poussière <b>durant chaque phase</b> des travaux »', 'Entrepreneur', 'AR-DEV-148'],
            ['Choix du type d\'échafaudage tenant compte « du phasage des travaux », conçu et scellé par un ingénieur', 'Entrepreneur', 'AR-DEV-172'],
            ['Déplacement des supports et structures temporaires « selon le phasage des travaux »', 'Entrepreneur', 'AR-DEV-155'],
            ['Préavis de <b>trois semaines</b> avant tout déplacement d\'une voie d\'accès ou de circulation, avec nouvelle signalisation', 'Entrepreneur → CISSS', 'AR-DEV-139'],
            ['Autorisation 48 h avant l\'installation d\'une grue ; levages planifiés avec le propriétaire et la municipalité', 'Entrepreneur → CISSS, ville', 'AR-DEV-161, 173'],
            ['Emplacement, pente, largeur et tracé des voies et pistes de chantier soumis à approbation', 'Entrepreneur → CISSS', 'AR-DEV-187'],
            ]
    t2 = box(778, 414, 814, 306, table(rows, ['536px', '162px', '92px']), 'Ce que le devis exige phase par phase — et que les plans ne montrent pas', 'ch-devis')
    manque = box(778, 732, 814, BOT - 732,
                 '<div class="txt"><b>L\'écart central.</b> Le devis exige des barrières et des cloisons anti-poussière « selon les phasages », et le choix de l\'échafaudage doit tenir compte du phasage. '
                 'Les plans, eux, ne montrent qu\'<b>une seule clôture</b>, hors phase, plus deux détails d\'accès locaux. Le plan de chantier par phase est donc un livrable de l\'entrepreneur, pas une donnée des documents (Z-27).<br><br>'
                 '<b>Ce qui n\'est dessiné nulle part</b>, vérifié sur les feuilles 001 et 002 : implantation de clôture par phase ; zone ou emprise d\'échafaudage ; position de grue et aire de levage ; '
                 'aire d\'entreposage ; roulotte et bureau de chantier ; conteneur à déchets, alors que le devis renvoie aux plans pour le trouver (AR-DEV-225) ; '
                 'symbole de portail, alors que le devis exige des signaleurs à chaque « barrière d\'accès au chantier <b>identifiée aux plans</b> » (AR-DEV-137). '
                 'Aucune cote de la clôture.<br><br>'
                 '<b>Une incohérence à lever.</b> Le devis situe le bureau de chantier « dans le stationnement étagé existant » (AR-DEV-180) ; la feuille 001 ne montre que des stationnements de surface.<br><br>'
                 '<b>Trois numérotations « phase 1/2/3 » coexistent</b> sans lien écrit : les phases du plan clé de la feuille 010, les configurations d\'accès de la feuille 002, '
                 'et les phases du tableau du CISSS (niveaux) : constat C-34. La planche de zones par phase se construit une fois cette correspondance tranchée.</div>',
                 'Ce qui manque pour dessiner les zones de chantier phase par phase', 'ch-manque')
    return ('<section class="planche">' + header(num, total, 'Zones de chantier et clôtures',
            'Ce que les documents fixent, ce que le devis exige phase par phase, et ce qui reste à produire')
            + img + t1 + t2 + manque
            + footer(num, total, 'D2 feuilles 001 et 002 (36 notes, légende, détails 1 à 5) ; D1 01 51 00, 01 52 00, 01 56 00 ; analyse/02-contraintes.md ; Z-27, C-34, C-38.') + '</section>')

CSS = """
@page { size: 17in 11in; margin: 0; }
body { margin: 0; font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif; color: #1a1a1a; font-size: 12px; }
.planche { position: relative; width: 1632px; height: 1056px; overflow: hidden; page-break-after: always; background: #fff; }
.planche:last-child { page-break-after: auto; }
.hdr { position: absolute; left: 40px; top: 22px; right: 40px; height: 66px; border-bottom: 2px solid #17324d; }
.h1 { font-size: 22px; font-weight: bold; color: #17324d; width: 1000px; }
.h2 { font-size: 13px; color: #24486b; margin-top: 4px; width: 1000px; }
.proj { position: absolute; right: 0; top: 4px; font-size: 12px; color: #444; text-align: right; width: 520px; line-height: 1.3; }
.ftr { position: absolute; left: 40px; right: 40px; top: 1008px; height: 36px; font-size: 12px; color: #444; border-top: 1px solid #b8c4d0; padding-top: 4px; line-height: 1.25; box-sizing: border-box; overflow: hidden; }
.ftr div { padding-right: 72px; white-space: nowrap; overflow: hidden; }
.ftr .pg { position: absolute; right: 0; top: 4px; font-weight: bold; color: #17324d; white-space: nowrap; font-size: 13px; }
.plan { position: absolute; overflow: hidden; border: 1px solid #b8c4d0; background: #fff; }
.box { position: absolute; border: 1px solid #b8c4d0; background: #fff; box-sizing: border-box; overflow: hidden; padding: 5px 7px; }
.bt { font-size: 13px; font-weight: bold; color: #17324d; margin-bottom: 4px; line-height: 1.25; }
.cap { position: absolute; font-size: 12px; color: #333; line-height: 1.3; }
.note { font-size: 12px; color: #444; margin-top: 4px; line-height: 1.25; }
.txt { font-size: 12px; line-height: 1.34; }
.cit { color: #5e1a75; font-style: italic; }
.mk { font-family: "Liberation Mono", monospace; font-size: 12px; color: #5e1a75; }
table.t { border-collapse: collapse; width: 100%; table-layout: fixed; font-size: 12px; }
table.t th, table.t td { border: 1px solid #c9d1da; padding: 2px 4px; vertical-align: top; text-align: left; line-height: 1.24; overflow-wrap: break-word; }
table.t th { background: #e8edf2; }
.corr { color: #b71c1c; font-weight: bold; }
.pill { display: inline-block; color: #fff; border-radius: 3px; padding: 1px 7px; margin-right: 3px; font-size: 12px; }
.dot { display: inline-block; width: 12px; height: 12px; border-radius: 50%; }
.seq { font-size: 13px; font-weight: bold; color: #17324d; line-height: 1.9; }
.seq .st { background: #17324d; color: #fff; padding: 2px 7px; border-radius: 3px; white-space: nowrap; }
.seq .ar { color: #17324d; }
.seqn { font-size: 12px; font-weight: normal; color: #333; margin-top: 6px; line-height: 1.32; }
"""

def main():
    args = sys.argv[1:]
    out = pathlib.Path(args[args.index('--out') + 1]) if '--out' in args else ROOT / 'plan-phasage-elevations.pdf'
    ordre = [f for f in ('nord', 'est', 'sud', 'ouest') if E.APPAREILS.get(f)]
    pages = [planche_methode]
    for fac in ordre:
        pages += [lambda n, t, f=fac: planche_appareils(f, n, t), lambda n, t, f=fac: planche_verrous(f, n, t)]
    pages += [planche_chantier, planche_synthese]
    total = len(pages)
    body = ''.join(f(i + 1, total) for i, f in enumerate(pages))
    doc = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
           f'<title>Cahier de phasage par élévation — Hôpital de Chandler R-657-24</title><style>{CSS}</style></head><body>{body}</body></html>')
    htmlp = BUILD / 'elevations.html'; htmlp.write_text(doc, encoding='utf-8')
    r = subprocess.run(['node', str(ROOT / 'src' / 'topdf.cjs'), str(htmlp), str(out), str(BUILD / 'deb_elev.json')],
                       capture_output=True, text=True)
    print(r.stdout, r.stderr[-1200:])

if __name__ == '__main__':
    main()
