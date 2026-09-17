"""Cahier de phasage par élévation — Hôpital de Chandler R-657-24.

Quatre planches tabloïd paysage : méthode et correspondance élévation ↔ façade,
façade nord (appareils sur l'élévation), façade nord (verrous appareils /
architecture), zones de chantier et clôtures.

Usage : python3 src/build_elevations.py [--out phasage/plan-phasage-elevations.pdf]
Règles : aucun texte sous 9 pt (12 px à 96 px/po) ; tout ce qui est lu sur un
plan porte [lecture], tout ce qui est proposé porte [choix].
"""
import sys, re, pathlib, subprocess, html, json

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import elev_data as E

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'; BUILD.mkdir(exist_ok=True)
BOT = 1002          # bas commun des boîtes ; le pied de page occupe 1008-1044
MES = {}            # hauteurs réelles mesurées au 1er passage {id: px}
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

def _brut(c):
    """Texte d'une cellule, balises retirées — pour estimer sa hauteur."""
    return re.sub(r'<[^>]+>', '', str(c)).replace('&nbsp;', ' ')

def _hligne(cells, widths):
    """Hauteur estimée d'une ligne : 12 px, interligne 1.24, 4 px de marge."""
    n = 1
    for c, w in zip(cells, widths):
        px = int(str(w).rstrip('px'))
        cpl = max(1, int((px - 10) / 6.05))
        n = max(n, -(-len(_brut(c)) // cpl))
    return n * 15 + 7

def hauteur_table(rows, widths):
    return int(sum(_hligne(r, widths) for r in rows) * 1.06) + 6

def hauteur_txt(h, largeur, taille=12, lh=1.34):
    """Hauteur estimée d'un bloc de texte courant dans une boîte donnée."""
    brut = re.sub(r'<br\s*/?>', '\n', str(h))
    brut = re.sub(r'</(div|p)>', '\n', brut)
    brut = re.sub(r'<[^>]+>', '', brut).replace('&nbsp;', ' ')
    cpl = max(12, int(largeur / (taille * 0.505)))
    n = sum(max(1, -(-len(l) // cpl)) for l in brut.split('\n'))
    return int(n * taille * lh) + 8

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
    positionnés : le dessin ne les montre pas. Les étiquettes sont d'abord
    posées à la position demandée par les données, puis écartées verticalement
    tant que deux d'entre elles se recouvrent ; le trait de rappel garde le
    lien avec le point exact."""
    g = E.GEOMS[fac]
    h = round(width * g.hauteur / g.largeur)
    k = width / g.largeur                      # unité svg -> px de la planche
    s = [f'<svg viewBox="0 0 {g.largeur} {g.hauteur}" width="{width}" height="{h}" style="position:absolute;left:0;top:0" xmlns="http://www.w3.org/2000/svg">']
    for nom, mm in E.NIVEAUX:
        y = g.niv(mm)
        if 12 < y < g.hauteur - 4:
            s.append(f'<line x1="0" y1="{y:.1f}" x2="{g.largeur}" y2="{y:.1f}" stroke="#1565c0" stroke-width="{0.8/k:.2f}" stroke-dasharray="7,5" opacity="0.5"/>')
            s.append(txt(4, y - 3, nom, 12 / k, 'start', 'normal', '#1565c0'))
    et = []
    for code, etat, lib, rep, a, mm, (dx, dy), v in E.APPAREILS.get(fac, []):
        if rep.startswith('non repéré'): continue
        x, y = g.ax(a), g.niv(mm)
        lab = code if code != '—' else 'ME ' + rep.split('—')[0].strip()
        et.append({'x': x, 'y': y, 'w': (7.0 * len(lab) + 8) / k, 'h': 18 / k,
                   'c': E.ETATS[etat][0], 't': lab, 'lx': x + dx / k, 'ly': y + dy / k})
    marge = 2 / k
    for e in et:
        e['lx'] = min(max(e['lx'], e['w'] / 2 + 2), g.largeur - e['w'] / 2 - 2)
    for _ in range(150):
        bouge = False
        for i in range(len(et)):
            for j in range(i + 1, len(et)):
                A, B = et[i], et[j]
                if abs(A['lx'] - B['lx']) >= (A['w'] + B['w']) / 2 + marge: continue
                d = (A['h'] + B['h']) / 2 + marge - abs(A['ly'] - B['ly'])
                if d <= 0: continue
                if A['ly'] <= B['ly']: A['ly'] -= d / 2; B['ly'] += d / 2
                else: A['ly'] += d / 2; B['ly'] -= d / 2
                bouge = True
        for e in et:
            e['ly'] = min(max(e['ly'], e['h'] / 2 + 2), g.hauteur - e['h'] / 2 - 2)
        if not bouge: break
    for e in et:
        x, y, lx, ly, w, hh, col = e['x'], e['y'], e['lx'], e['ly'], e['w'], e['h'], e['c']
        s.append(f'<line x1="{lx:.1f}" y1="{ly:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="{1.1/k:.2f}" stroke-dasharray="2,2"/>')
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4/k:.1f}" fill="{col}" stroke="#fff" stroke-width="{1.2/k:.2f}"/>')
        s.append(f'<rect x="{lx - w/2:.1f}" y="{ly - hh/2:.1f}" width="{w:.1f}" height="{hh:.1f}" rx="{3/k:.1f}" fill="{col}" stroke="#fff" stroke-width="{1/k:.2f}"/>')
        s.append(txt(lx, ly + 5 / k, e['t'], 12 / k, 'middle', 'bold', '#fff'))
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

NOTE_ELEV = {
 'est': "Les appareils des élévations partielles D et H sont reportés sur l'élévation G le long de la même chaîne d'axes : "
        "la cote d'axe est `[lecture]`, le report sur ce dessin est `[choix]` de présentation.",
 'ouest': "Les appareils des élévations partielles C, E et I sont reportés sur l'élévation B le long de la même chaîne d'axes : "
          "la cote d'axe est `[lecture]`, le report sur ce dessin est `[choix]` de présentation.",
}

def planche_appareils(fac, num, total):
    """Deux mises en page selon la proportion de l'élévation : élévation large
    (nord, sud) au-dessus de deux colonnes de tableau ; élévation ramassée
    (est, ouest) à gauche, tableau à droite et, s'il déborde, suite en bandeau
    sous l'élévation. Les hauteurs sont calculées à partir du contenu."""
    titre, sous, src = FACADES[fac]
    g = E.GEOMS[fac]
    app = E.APPAREILS.get(fac, [])
    def lignes(part):
        out = [['Ligne ME', '&nbsp;', 'Appareil', 'Bulle ME et élévation', 'Fenêtre écrite']]
        for code, etat, lib, rep, a, mm, dxy, v in part:
            r = D5I.get(code)
            per = ' '.join((r['periode'] if r else '').split())[:46] or '—'
            if r and r['arret'].strip().lower().startswith('n/a'): per = 'non touché'
            out.append([f'<b>{esc(code)}</b>', f'<span class="dot" style="background:{E.ETATS[etat][0]}"></span>',
                        esc(lib), esc(rep), esc(per)])
        return out
    nonpos = [a[0] for a in app if a[3].startswith('non repéré')]
    leg = ["<b>États :</b> "]
    for c in ('retire', 'deplace', 'coupe', 'maintenu', 'intact'):
        col, lib = E.ETATS[c]
        leg.append(f'<span class="pill" style="background:{col}">{lib}</span> ')
    leg.append("&nbsp;&nbsp;Chaque pastille porte le code de la ligne du tableau ME. Position relevée sur les repères des feuilles ME — [lecture] ; "
               "les étiquettes sont écartées verticalement pour rester lisibles, le trait de rappel pointe le point exact. "
               f"Traits bleus : niveaux de la feuille. Le {g.gauche} est à gauche, le {g.droite} à droite.")
    if NOTE_ELEV.get(fac): leg.append(' ' + NOTE_ELEV[fac])
    if nonpos:
        leg.append(f" <b>Lignes que le dessin ne montre nulle part</b>, donc non positionnées : {', '.join(nonpos)}.")
    if g.largeur / g.hauteur > 2.5:
        W = ['82px', '20px', '256px', '180px', '216px']
        m = (len(app) + 1) // 2
        parts = [app[:m], app[m:]]
        besoin = max(MES.get(f'{fac}-app{c}') or hauteur_table(lignes(pp), W) for c, pp in enumerate(parts)) + 16
        w = min(1540, max(820, round((BOT - 156 - besoin) * g.largeur / g.hauteur)))
        plan, h = elevation(fac, width=w)
        y = 96 + h + 6
        cap = f'<div class="cap" style="left:40px;top:{y}px;width:1540px">' + ''.join(leg) + '</div>'
        tabs = ''.join(box(x0, y + 54, 776, BOT - (y + 54), table(lignes(pp), W), None, f'{fac}-app{c}')
                       for c, (x0, pp) in enumerate([(40, parts[0]), (816, parts[1])]))
    else:
        w = min(946, round(560 * g.largeur / g.hauteur))
        plan, h = elevation(fac, width=w)
        WD = ['76px', '20px', '186px', '148px', '144px']
        WB = ['84px', '22px', '250px', '200px', '330px']
        n = len(app)
        while n > 1 and hauteur_table(lignes(app[:n]), WD) > BOT - 96 - 16: n -= 1
        tabs = box(56 + w, 96, 1536 - w, BOT - 96, table(lignes(app[:n]), WD), None, f'{fac}-app0')
        ycap = 96 + h + 6
        if n < len(app):
            ybas = ycap + 92
            tabs += box(40, ybas, w, BOT - ybas, table(lignes(app[n:]), WB), None, f'{fac}-app1')
        cap = f'<div class="cap" style="left:40px;top:{ycap}px;width:{w}px">' + ''.join(leg) + '</div>'
    return ('<section class="planche">' + header(num, total, f'{titre} — les appareils sur l\'élévation',
            f'{sous} ; {len(app)} appareils relevés')
            + plan + cap + tabs
            + footer(num, total, src + ' ; analyse/02-contraintes.md.') + '</section>')

SEQ_NOTE = ("Détail des six étapes : analyse/03-phasage.md §1.3. Le seul préalable écrit tient en une phrase du devis : "
            "les contournements électromécaniques doivent être en place avant la démolition de l'enveloppe (AR-DEV-058) — "
            "c'est pourquoi presque tous les verrous ci-dessus se jouent entre E1 et E2.")
VER_ENT = ['#', 'Appareil et position', 'À faire avant', "Étape d'architecture bloquée", 'Sources']
VER_W = ['32px', '386px', '356px', '416px', '330px']

def _ligne_verrou(v):
    k, app, av, et_, s = v
    return [f'<b>{k}</b>', rich(app), rich(av), rich(et_), esc(s)]

def planches_verrous(fac):
    """Une planche de verrous, ou deux quand le tableau ne tient pas : la
    dernière porte en plus le rappel de la séquence type et le commentaire de
    façade. La répartition est calculée d'après le contenu."""
    titre, sous, src = FACADES[fac]
    ver = E.VERROUS.get(fac, [])
    hseq = 58 + hauteur_txt(SEQ_NOTE, 1520)
    com = E.COMMENTAIRES.get(fac, '<div class="txt">—</div>')
    hcom = 30 + hauteur_txt(com, 1520)
    fin_dispo = BOT - 96 - 32 - hseq - hcom
    plein = BOT - 96
    def ht(part): return 34 + hauteur_table([VER_ENT] + [_ligne_verrou(v) for v in part], VER_W)
    reste, blocs = list(ver), []
    while reste:
        if ht(reste) <= fin_dispo:
            blocs.append((reste, True)); reste = []
        else:
            n = len(reste)
            while n > 1 and ht(reste[:n]) > plein: n -= 1
            blocs.append((reste[:n], False)); reste = reste[n:]
    def planche(num, total, part, fin, i, nb):
        rows = [VER_ENT] + [_ligne_verrou(v) for v in part]
        th = min(ht(part), fin_dispo if fin else plein)
        suite = f' ({i + 1} de {nb})' if nb > 1 else ''
        corps = box(40, 96, 1552, th, table(rows, VER_W),
                    f'Verrous entre les appareils et les travaux d\'architecture — {titre.lower()}{suite}', f'{fac}-ver{i}')
        if fin:
            seq = ['<div class="seq">']
            for code, nom, cont in E.ETAPES:
                seq.append(f'<span class="st">{code} {esc(nom)}</span> <span class="ar">→</span> ')
            seq.append('</div><div class="seqn">' + rich(SEQ_NOTE) + '</div>')
            y2 = 112 + th
            corps += box(40, y2, 1552, hseq, ''.join(seq),
                         'Séquence type d\'une façade (analyse/03-phasage.md §1.2 et §1.3) — le verrou se joue presque toujours entre E1 et E2', f'{fac}-seq')
            y3 = y2 + hseq + 16
            corps += box(40, y3, 1552, max(120, BOT - y3), com, f'Ce que les verrous de la {titre.lower()} révèlent', f'{fac}-conf')
        return ('<section class="planche">' + header(num, total, f'{titre} — verrous entre appareils et architecture{suite}',
                'Ce qui doit être déplacé, coupé ou maintenu avant chaque étape de la façade, et ce qui reste bloqué tant qu\'il est en place')
                + corps
                + footer(num, total, src + ' ; analyse/03-phasage.md §1.3 ; analyse/02-contraintes.md.') + '</section>')
    nb = len(blocs)
    return [(lambda n, t_, part=b[0], fin=b[1], i=i: planche(n, t_, part, fin, i, nb)) for i, b in enumerate(blocs)]

def empiler(x, w, blocs, top=96, gap=12):
    """Empile des boîtes dans une colonne, chacune à la hauteur de son contenu
    (mesurée au premier passage, estimée sinon)."""
    out, y = [], top
    for bid, titre, contenu, hest in blocs:
        h = MES.get(bid) or hest
        if y + h > BOT: h = BOT - y
        if h < 40: break
        out.append(box(x, y, w, h, contenu, titre, bid))
        y += h + gap
    return ''.join(out)

def planche_synthese(num, total):
    gauche = empiler(40, 940, [
     ('sy-ch', 'Les 93 lignes du tableau de coordination, réparties par façade',
      table(E.SYNTHESE_CHIFFRES, ['172px', '56px', '146px', '244px', '94px', '108px', '80px']), 218),
     ('sy-cal', 'Calendrier de travail et fenêtres saisonnières',
      table(E.CALENDRIER, ['326px', '218px', '374px']) + E.CALENDRIER_TXT, 300),
     ('sy-sa', 'Les huit lignes du tableau bornées par une saison — sur les quatre façades',
      table(E.SAISON, ['88px', '68px', '474px', '286px']), 230),
    ])
    droite = empiler(996, 596, [
     ('sy-tx', "Ce que l'exercice apporte au phasage", E.SYNTHESE_TXT, 500),
     ('sy-fac', 'Ce que chaque façade impose au calendrier',
      table(E.CAL_FACADES, ['70px', '236px', '272px']), 300),
    ])
    return ('<section class="planche">' + header(num, total, 'Synthèse — saisons et calendrier',
            'Ce que le regroupement des appareils par façade fait apparaître sur le calendrier')
            + gauche + droite
            + footer(num, total, 'D5 tableau de coordination (93 lignes, notes générales 1, 2 et 8) ; D8 annexe 0.01.13 ; analyse/02-contraintes.md ; analyse/03-phasage.md §0.4, §4 K2 et K3 ; Z-10, Z-29, C-14, C-34.') + '</section>')

DECISIONS = [
 ['Décision à obtenir', 'De qui', "Ce qu'elle débloque"],
 ['Confirmer la période estivale retenue — mi-juin à mi-août, environ du 24 juin au 15 août — et arbitrer le conflit interne de la façade nord', 'CISSS',
  "La planification saisonnière des quatre façades : sept lignes du tableau en dépendent, dont deux qui exigent l'été et quatre qui l'excluent (Z-10)"],
 ['Sens de la ligne S-A-V-001, « en dehors de la période estivale (quelques jours en été) »', 'CISSS et WSP',
  'La façade sud : la ligne se contredit elle-même'],
 ['Correspondance entre les trois numérotations « phase 1/2/3 » (feuille 010, feuille 002, tableau du CISSS)', 'Architectes et CISSS',
  "La planche des zones de chantier par phase, et le rattachement des configurations d'accès au phasage du bâtiment (C-34)"],
 ["Tracé et forme des conduits temporaires de l'unité d'hémodialyse, séquence de basculement, fenêtres d'interruption", 'WSP',
  'Les façades nord ET ouest, entre les axes 8 et 6 et entre A et B — préalable écrit à la démolition (Z-29)'],
 ["Rattachement de l'unité d'hémodialyse au tableau côté ouest : elle est repérée sur l'élévation B sans aucune ligne O-B", 'WSP',
  "La façade ouest : la plus grosse intervention temporaire de l'angle nord-ouest n'y a pas de fenêtre écrite"],
 ["Position de la prise d'air de la centrale d'air médical, placée sur l'élévation F sans repère sur le dessin", 'WSP',
  "L'ordre nord / ouest, qui dépend de l'emplacement de la prise temporaire (ME-065, ME-067)"],
 ["Trois travaux repérés sur l'élévation sud sans ligne au tableau : thermostat des câbles chauffants, évents de l'autoclave, évents de la chaufferie", 'WSP',
  'La façade sud : ce sont des travaux réels, sans fenêtre ni durée écrites'],
 ['Nature de la zone grise au-dessus de la marquise des ambulances (2e bulle D1 ventilation ; note 24 de la feuille 201)', 'WSP et architectes',
  'Le tronçon le plus chargé de la façade sud'],
 ['Appariement des deux couples luminaire / lecteur des portes du laboratoire et du bloc opératoire (O-B-E-002 à 005)', 'Architectes',
  'La façade ouest : les quatre lignes ne sont pas départageables sur les feuilles ME'],
 ["Longueur des tronçons traités d'un coup sur chaque façade", 'Entrepreneur, avec le CISSS',
  "La durée d'indisponibilité de chaque appareil marqué « toute la durée des travaux » : 47 lignes sur 93"],
 ['Plan de situation de la zone clôturée par phase, barrières verrouillables, cloisons anti-poussière', 'Entrepreneur',
  'Les zones de chantier, que les plans ne montrent que dans une seule configuration (AR-DEV-171, 190, 148)'],
]

DEFAUTS = [
 ['Défaut relevé en lisant les élévations', 'Où', 'Conséquence'],
 ['Deux lignes consécutives portent le même code <b>N-F-E-006</b>', 'Tableau ME, page 6',
  'La seconde a le même contenu que N-F-E-007 : doublon ou numérotation à corriger'],
 ["Unité de ventilation de l'hémodialyse et sa passerelle repérées sur l'élévation ouest, sans aucune ligne O-B", 'ME001D note D7 ventilation',
  "L'intervention la plus lourde de l'angle nord-ouest n'a pas de fenêtre écrite côté ouest"],
 ['Thermostat des câbles chauffants repéré au sud, sans ligne S-A-E', 'ME002D note D14 électricité',
  "Travail d'électricité réel, sans arrêt ni période écrits"],
 ['Évents de vapeur de la chaufferie : <b>trois annoncés</b> (150, 150 et 200 mm), <b>un seul dessiné</b>', 'ME002D note D3 plomberie',
  'Quantité non fixée, aucune ligne au tableau'],
 ["Évents de l'autoclave dessinés sur l'élévation sud, rattachés par écrit à la façade ouest", 'ME002D note D2 plomberie ; D5 O-B-P-001',
  'Verrou inter-façades invisible dans un découpage par zones'],
 ["Persienne de prise d'air frais du service alimentaire repérée à l'ouest, sans ligne", 'ME001D notes D10 et D17 ventilation',
  'Registre coupe-feu à ajouter, sans fenêtre écrite'],
 ['Sectionneur de thermopompe du repère D, sans ligne', 'ME003D repère D note D6 électricité', 'Aucune fenêtre écrite'],
 ["Enseigne « ambulance urgence » du repère E, sans ligne", 'ME003D repère E note D5 électricité', 'Aucune fenêtre écrite'],
 ["<b>E-G-E-006</b> : le tableau écrit « salle des serveurs », le dessin accole la bulle à l'unité LG du toit", 'D5 contre ME002D',
  "Localisation incertaine d'un arrêt en local critique"],
 ['<b>E-G-V-001 et 002</b> : le tableau écrit « persienne à relocaliser », la note dit « démanteler complètement, aucune remise en service »', 'D5 contre ME002D note D5 ventilation',
  "Nature de l'intervention non fixée"],
 ['<b>E-G-V-003</b> : le tableau écrit « supports muraux », la note dit « support au toit »', 'D5 contre ME002D note D7 ventilation', 'Nature du support non fixée'],
 ['<b>O-B-V-002</b> : le tableau écrit « persienne à relocaliser », la note dit « à remplacer par une persienne moins large »', 'D5 contre ME001D note D16 ventilation',
  "Nature de l'intervention non fixée"],
 ["Le repère D de la feuille ME003D ne porte aucune ligne d'axe", 'ME003D', "E-D-V-001 n'est pas positionnable sur une élévation"],
 ["Groupe D4 de l'élévation sud : sept cibles identiques pour six lignes grises", 'ME002D note D4 électricité',
  "Aucune des six lignes n'est identifiable individuellement"],
 ['Numéros de persiennes P-01 à P-18 portés aux dessins sans nomenclature retrouvée dans le jeu', 'ME001D, ME002D, ME003D',
  "L'appariement repose sur la concordance des dimensions mesurées `[lecture]`"],
]

def planche_decisions(num, total):
    corps = empiler(40, 1552, [
     ('de-dec', 'Décisions à obtenir, par destinataire', table(DECISIONS, ['620px', '190px', '716px']), 420),
     ('de-def', 'Défauts documentaires relevés en lisant les quatre élévations — à faire lever avant la mise en phase',
      table(DEFAUTS, ['620px', '320px', '586px']), 450),
    ])
    return ('<section class="planche">' + header(num, total, 'Décisions à obtenir et défauts documentaires',
            'Ce qui doit être tranché avant de figer un phasage, et ce que la lecture en élévation a fait apparaître dans les documents')
            + corps
            + footer(num, total, 'D5 tableau de coordination ; D4 ME001(D), ME002(D), ME003(D) ; D2 feuilles 201, 201-A, 202 ; analyse/02-contraintes.md ; Z-10, Z-27, Z-29, C-14, C-34.') + '</section>')

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
        pages.append(lambda n, t, f=fac: planche_appareils(f, n, t))
        pages += planches_verrous(fac)
    pages += [planche_chantier, planche_synthese, planche_decisions]
    total = len(pages)
    htmlp = BUILD / 'elevations.html'
    mesp = BUILD / 'mes_elev.json'
    # deux passages : le premier mesure la hauteur réelle des tableaux, le
    # second dimensionne les élévations avec ces hauteurs.
    for passage in (1, 2):
        body = ''.join(f(i + 1, total) for i, f in enumerate(pages))
        doc = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
               f'<title>Cahier de phasage par élévation — Hôpital de Chandler R-657-24</title><style>{CSS}</style></head><body>{body}</body></html>')
        htmlp.write_text(doc, encoding='utf-8')
        r = subprocess.run(['node', str(ROOT / 'src' / 'topdf.cjs'), str(htmlp), str(out),
                            str(BUILD / 'deb_elev.json'), str(mesp)], capture_output=True, text=True)
        if r.returncode: print(r.stdout, r.stderr[-1200:]); return
        if passage == 1: MES.update(json.loads(mesp.read_text()))
    print(r.stdout, r.stderr[-1200:])

if __name__ == '__main__':
    main()
