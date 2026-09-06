# -*- coding: utf-8 -*-
"""Générateur du site « Bye Bye Belgium ». Python 3, sans dépendance."""

import json, os, re, shutil, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from data import SITE, SOURCES, LEXIQUE, CHRONO, CHIFFRES  # noqa: E402
from render import Inline, typo  # noqa: E402
import dossiers_a, dossiers_b, dossiers_c, dossiers_d, dossiers_e  # noqa: E402

DOSSIERS = (dossiers_a.DOSSIERS + dossiers_b.DOSSIERS + dossiers_c.DOSSIERS
            + dossiers_d.DOSSIERS + dossiers_e.DOSSIERS)

SECTIONS = [
    ("annonce", "I", "L'annonce",
     "Ce qui a été dit de la fin de la Belgique, par qui, et ce que ces annonces révèlent du "
     "fonctionnement réel du pays."),
    ("droit", "II", "Le droit de partir",
     "Ce que le droit belge, le droit international et le droit de l'Union autorisent, interdisent "
     "ou laissent indéterminé."),
    ("bruxelles", "III", "Le nœud bruxellois",
     "Une capitale enclavée, majoritairement francophone, siège de l'Union : la variable qui rend "
     "tous les scénarios insolubles."),
    ("facture", "IV", "La facture",
     "Dette, transferts, sécurité sociale, loi de financement, marchés : les montants que personne "
     "n'a répartis."),
    ("issues", "V", "Les issues",
     "Confédéralisme, indépendance, refédéralisation : les trois sorties possibles, instruites et "
     "comparées."),
]
SEC = {s[0]: s for s in SECTIONS}

STATUTS = {
    "instruit": ("Instruit", "s-oui",
                 "Le dossier est documenté par des sources publiques concordantes."),
    "partiellement instruit": ("Partiellement instruit", "s-part",
                               "Une partie des éléments décisifs n'a pas été publiée."),
    "non instruit": ("Non instruit", "s-non",
                     "Aucun texte public ne règle la question posée par ce dossier."),
    "archive": ("Archive", "s-arch", "Dossier historique."),
    "synthèse": ("Synthèse", "s-synth", "Conclusion de l'enquête."),
}

SRC = {s[0]: s for s in SOURCES}
LEX = {t[0]: t for t in LEXIQUE}
DOS = {d["slug"]: d for d in DOSSIERS}
BASE = SITE["base"]

NAV = [("sommaire.html", "Sommaire"), ("chronologie.html", "Chronologie"),
       ("chiffres.html", "Chiffres"), ("lexique.html", "Lexique"),
       ("sources.html", "Sources"), ("methode.html", "Méthode")]

ERRORS = []
PAGES = []  # (path, changefreq, priority)

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" fill="#16161a"/>'
           '<rect x="0" y="46" width="64" height="18" fill="#b3151f"/>'
           '<text x="32" y="38" font-family="Arial Narrow,Arial,sans-serif" font-weight="bold" '
           'font-size="34" fill="#f6f3ec" text-anchor="middle">BB</text></svg>')


def esc(t):
    """Échappement HTML, avec typographie française pour les textes lisibles."""
    if t.startswith(("http://", "https://", "mailto:")):
        return H.escape(t, quote=True)
    return typo(H.escape(t, quote=True))


# ---------------------------------------------------------------------------
# Gabarit
# ---------------------------------------------------------------------------

def head(title, desc, keywords, canonical, depth, jsonld, seo_title=None):
    p = "../" * depth
    t = seo_title or title
    full = t if t.startswith(SITE["titre"]) else t + " — " + SITE["titre"]
    og = BASE + "og.png"
    out = ['<!DOCTYPE html>', '<html lang="fr">', '<head>', '<meta charset="utf-8">',
           '<meta name="viewport" content="width=device-width, initial-scale=1">',
           '<title>%s</title>' % esc(full),
           '<meta name="description" content="%s">' % esc(desc),
           '<meta name="keywords" content="%s">' % esc(keywords),
           '<meta name="author" content="%s">' % esc(SITE["auteur"]),
           '<link rel="canonical" href="%s">' % esc(canonical),
           '<meta property="og:type" content="article">',
           '<meta property="og:site_name" content="%s">' % esc(SITE["titre"]),
           '<meta property="og:title" content="%s">' % esc(full),
           '<meta property="og:description" content="%s">' % esc(desc),
           '<meta property="og:url" content="%s">' % esc(canonical),
           '<meta property="og:image" content="%s">' % esc(og),
           '<meta property="og:image:width" content="1200">',
           '<meta property="og:image:height" content="630">',
           '<meta property="og:image:alt" content="Bye Bye Belgium — instruire la fin d\'un pays">',
           '<meta property="og:locale" content="fr_BE">',
           '<meta name="twitter:card" content="summary_large_image">',
           '<meta name="twitter:title" content="%s">' % esc(full),
           '<meta name="twitter:description" content="%s">' % esc(desc),
           '<meta name="twitter:image" content="%s">' % esc(og),
           '<link rel="stylesheet" href="%sassets/site.css">' % p,
           '<link rel="icon" href="%sfavicon.svg" type="image/svg+xml">' % p,
           '<link rel="alternate" type="application/rss+xml" title="%s" href="%srss.xml">'
           % (esc(SITE["titre"]), p),
           '<script type="application/ld+json">%s</script>'
           % json.dumps(jsonld, ensure_ascii=False, separators=(",", ":")),
           '</head>']
    return "\n".join(out)


def masthead(depth, current):
    p = "../" * depth
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append('<li><a href="%s%s"%s>%s</a></li>' % (p, href, cur, label))
    return (
        '<body>\n'
        '<a class="skip" href="#contenu">Aller au contenu</a>\n'
        '<header class="masthead"><div class="masthead-in">'
        '<a class="wordmark" href="%sindex.html"><span class="bye">Bye Bye</span> Belgium</a>'
        '<span class="tagline">Instruire la fin d\'un pays</span>'
        '<nav class="top" aria-label="Navigation principale"><ul>%s</ul></nav>'
        '</div></header>\n' % (p, "".join(items)))


def footer(depth):
    p = "../" * depth
    links = "".join('<li><a href="%s%s">%s</a></li>' % (p, h, l) for h, l in NAV)
    return (
        '<footer class="site"><div class="in">'
        '<ul>%s</ul>'
        '<p>%s — enquête indépendante sur les scénarios de fin de l\'État belge. '
        'Auteur des textes : %s (nom de plume). Éditeur : anonyme. '
        'Corpus arrêté au %s. Chaque affirmation chiffrée renvoie à sa source ; '
        'la <a href="%smethode.html">page méthode</a> expose les règles de vérification, '
        'les corrections apportées et les limites de l\'enquête.</p>'
        '<p>Site statique, sans JavaScript, sans cookie, sans traqueur, sans ressource externe. '
        'Corpus d\'origine : <a href="%sbye/">analyse de la démocratie belge</a> et '
        '<a href="%sbye/belgium/">analyse de la citoyenneté</a>.</p>'
        '</div></footer>\n</body>\n</html>\n'
        % (links, esc(SITE["titre"]), esc(SITE["auteur"]), SITE["arret"], p, p, p))


def finalize(content):
    """Applique la typographie française à la page, hors blocs de script."""
    out = []
    for part in re.split(r"(<script\b[^>]*>.*?</script>)", content, flags=re.S):
        out.append(part if part.startswith("<script") else typo(part))
    return "".join(out)


def write(relpath, content, changefreq="monthly", priority="0.6", indexable=True):
    content = finalize(content)
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    if indexable:
        PAGES.append((relpath, changefreq, priority))


# ---------------------------------------------------------------------------
# JSON-LD partagé
# ---------------------------------------------------------------------------

def person():
    return {"@type": "Person", "@id": BASE + "#auteur", "name": SITE["auteur"],
            "description": "Nom de plume. L'éditeur du site reste anonyme.",
            "url": BASE + "methode.html"}


def website():
    return {"@type": "WebSite", "@id": BASE + "#site", "url": BASE,
            "name": SITE["titre"], "alternateName": "Bye Bye Belgique",
            "description": SITE["description"], "inLanguage": "fr-BE",
            "author": {"@id": BASE + "#auteur"},
            "publisher": {"@id": BASE + "#auteur"},
            "about": [{"@id": BASE + "#belgique"}],
            "keywords": "fin de la Belgique, scission, confédéralisme, sécession, Bruxelles, "
                        "dette publique, fédéralisme belge"}


def place():
    return {"@type": "Country", "@id": BASE + "#belgique", "name": "Belgique",
            "sameAs": "https://www.wikidata.org/wiki/Q31"}


def breadcrumb(items):
    return {"@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                 "item": u} for i, (n, u) in enumerate(items)]}


def faq_ld(faq):
    return {"@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in faq]}


# ---------------------------------------------------------------------------
# Rendu des blocs
# ---------------------------------------------------------------------------

def excerpt(text, n):
    t = re.sub(r"\s+", " ", text).strip()
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(" ", 1)[0].rstrip(" ,;:—-")
    return cut + "…"


def slugify(text):
    t = text.lower()
    for a, b in (("à", "a"), ("â", "a"), ("ä", "a"), ("é", "e"), ("è", "e"), ("ê", "e"),
                 ("ë", "e"), ("î", "i"), ("ï", "i"), ("ô", "o"), ("ö", "o"), ("ù", "u"),
                 ("û", "u"), ("ü", "u"), ("ç", "c"), ("œ", "oe"), ("’", ""), ("'", "")):
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "section"


def render_blocks(blocks, il):
    out, toc, used = [], [], set()
    for b in blocks:
        kind = b[0]
        if kind == "p":
            out.append("<p>%s</p>" % il(b[1]))
        elif kind == "h":
            sid = slugify(b[1])
            n, base = 1, sid
            while sid in used:
                n += 1
                sid = "%s-%d" % (base, n)
            used.add(sid)
            toc.append((sid, b[1]))
            out.append('<h2 id="%s">%s</h2>' % (sid, il(b[1])))
        elif kind == "sh":
            sid = slugify(b[1])
            n, base = 1, sid
            while sid in used:
                n += 1
                sid = "%s-%d" % (base, n)
            used.add(sid)
            out.append('<h3 id="%s">%s</h3>' % (sid, il(b[1])))
        elif kind in ("ul", "ol"):
            items = "".join("<li>%s</li>" % il(x) for x in b[1])
            out.append("<%s>%s</%s>" % (kind, items, kind))
        elif kind == "q":
            out.append('<blockquote><p>%s</p><cite>%s</cite></blockquote>'
                       % (il(b[1]), il(b[2])))
        elif kind == "chiffres":
            lis = "".join(
                '<li><span class="v">%s</span><span class="l">%s</span>'
                '<span class="n">%s</span></li>' % (il(v), il(l), il(n))
                for v, l, n in b[1])
            out.append('<aside class="figures" aria-label="Chiffres clés"><ul>%s</ul></aside>' % lis)
        elif kind == "table":
            headers, rows, caption = b[1], b[2], b[3]
            th = "".join("<th scope=\"col\">%s</th>" % il(h) for h in headers)
            tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % il(c) for c in r) for r in rows)
            out.append('<figure><div class="tablewrap"><table><thead><tr>%s</tr></thead>'
                       '<tbody>%s</tbody></table></div><figcaption>%s</figcaption></figure>'
                       % (th, tr, il(caption)))
        elif kind in ("contre", "doute"):
            ps = "".join("<p>%s</p>" % il(x) for x in b[2])
            out.append('<aside class="box %s"><p class="t">%s</p>%s</aside>'
                       % (kind, il(b[1]), ps))
        else:
            ERRORS.append("bloc inconnu : %s" % kind)
    return "\n".join(out), toc


def sources_block(page_sources):
    if not page_sources:
        return ""
    lis = []
    for i, sid in enumerate(page_sources, 1):
        s = SRC[sid]
        lis.append('<li id="s-%d"><a href="%s" rel="noopener nofollow" target="_blank">%s</a>'
                   '<span class="pub"> — %s, %s.</span></li>'
                   % (i, esc(s[5]), esc(s[1]), esc(s[2]), esc(s[3])))
    return ('<section class="sources"><h2 id="sources">Sources</h2><ol>%s</ol></section>'
            % "".join(lis))


def faq_block(faq, il):
    if not faq:
        return ""
    dl = "".join("<dt>%s</dt><dd>%s</dd>" % (il(q), il(a)) for q, a in faq)
    return ('<section class="faq"><h2 id="questions">Questions fréquentes</h2><dl>%s</dl></section>'
            % dl)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def ordered():
    out = []
    for key, _, _, _ in SECTIONS:
        out += [d for d in DOSSIERS if d["section"] == key]
    return out


ORDER = ordered()
INDEXOF = {d["slug"]: i for i, d in enumerate(ORDER)}


def build_dossier(d):
    i = INDEXOF[d["slug"]]
    sec = SEC[d["section"]]
    canon = BASE + "dossiers/" + d["slug"] + ".html"
    ps = []
    il = Inline(set(LEX), set(DOS), set(SRC), "../", ps)
    body, toc = render_blocks(d["blocks"], il)
    faq = faq_block(d.get("faq", []), il)
    ERRORS.extend("%s : %s" % (d["slug"], e) for e in il.errors)

    label, cls, expl = STATUTS[d["statut"]]
    article = {
        "@type": "Article", "@id": canon + "#article",
        "headline": d.get("seo_title", d["titre"])[:110],
        "name": d["titre"], "description": d["description"],
        "inLanguage": "fr-BE", "isPartOf": {"@id": BASE + "#site"},
        "author": {"@id": BASE + "#auteur"}, "publisher": {"@id": BASE + "#auteur"},
        "about": {"@id": BASE + "#belgique"},
        "articleSection": sec[2], "url": canon,
        "datePublished": SITE["date_iso"], "dateModified": SITE["date_iso"],
        "keywords": d["keywords"],
        "citation": [{"@type": "CreativeWork", "name": SRC[s][1],
                      "url": SRC[s][5],
                      "publisher": {"@type": "Organization", "name": SRC[s][2]}} for s in ps],
    }
    graph = [person(), website(), place(), article,
             {"@type": "WebPage", "@id": canon, "url": canon, "name": d["titre"],
              "description": d["description"], "inLanguage": "fr-BE",
              "isPartOf": {"@id": BASE + "#site"},
              "primaryImageOfPage": None} if False else
             {"@type": "WebPage", "@id": canon, "url": canon, "name": d["titre"],
              "description": d["description"], "inLanguage": "fr-BE",
              "isPartOf": {"@id": BASE + "#site"}},
             breadcrumb([("Accueil", BASE), ("Sommaire", BASE + "sommaire.html"),
                         (sec[2], BASE + "sommaire.html#" + sec[0]), (d["titre"], canon)])]
    if d.get("faq"):
        graph.append(faq_ld(d["faq"]))
    ld = {"@context": "https://schema.org", "@graph": graph}

    parts = [head(d["titre"], d["description"], d["keywords"], canon, 1, ld,
                  d.get("seo_title")),
             masthead(1, None), '<main id="contenu">',
             '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>'
             '<li><a href="../index.html">Accueil</a></li>'
             '<li><a href="../sommaire.html">Sommaire</a></li>'
             '<li><a href="../sommaire.html#%s">%s. %s</a></li>'
             '<li>%s</li></ol></nav>' % (sec[0], sec[1], esc(sec[2]), esc(d["titre"])),
             '<article class="wrap">',
             '<p class="kicker">%s. %s</p>' % (sec[1], esc(sec[2])),
             '<h1>%s</h1>' % esc(d["titre"]),
             '<p class="meta"><span class="statut %s" title="%s">%s</span>'
             '<span>Dossier %d sur %d</span><span>Corpus arrêté au %s</span></p>'
             % (cls, esc(expl), esc(label), i + 1, len(ORDER), SITE["arret"]),
             '<p class="chapo">%s</p>' % il(d["chapo"])]

    if len(toc) > 2:
        items = "".join('<li><a href="#%s">%s</a></li>' % (sid, esc(t)) for sid, t in toc)
        parts.append('<nav class="toc" aria-label="Sommaire du dossier">'
                     '<p class="t">Dans ce dossier</p><ol>%s</ol></nav>' % items)

    parts.append(body)
    parts.append(faq)
    parts.append(sources_block(ps))

    # dossiers liés : même section
    rel = [x for x in ORDER if x["section"] == d["section"] and x["slug"] != d["slug"]]
    if rel:
        lis = "".join('<li><a href="%s.html">%s</a></li>' % (x["slug"], esc(x["titre"]))
                      for x in rel)
        parts.append('<nav class="related" aria-label="Dossiers de la même partie">'
                     '<p class="t">Dans la même partie</p><ul>%s</ul></nav>' % lis)

    prev = ORDER[i - 1] if i > 0 else None
    nxt = ORDER[i + 1] if i < len(ORDER) - 1 else None
    pg = ['<nav class="pager" aria-label="Pagination">']
    if prev:
        pg.append('<a class="prev" href="%s.html"><span class="l">Précédent</span>'
                  '<span class="n">%s</span></a>' % (prev["slug"], esc(prev["titre"])))
    if nxt:
        pg.append('<a class="next" href="%s.html"><span class="l">Suivant</span>'
                  '<span class="n">%s</span></a>' % (nxt["slug"], esc(nxt["titre"])))
    pg.append("</nav>")
    parts.append("".join(pg))
    parts.append("</article></main>")
    parts.append(footer(1))
    write("dossiers/%s.html" % d["slug"], "\n".join(x for x in parts if x),
          "monthly", "0.8")
    return ps


def build_index():
    canon = BASE
    ps = []
    il = Inline(set(LEX), set(DOS), set(SRC), "", ps)
    ld = {"@context": "https://schema.org", "@graph": [
        person(), website(), place(),
        {"@type": "WebPage", "@id": canon, "url": canon,
         "name": SITE["titre"] + " — " + SITE["sous_titre"],
         "description": SITE["description"], "inLanguage": "fr-BE",
         "isPartOf": {"@id": BASE + "#site"}},
        {"@type": "ItemList", "name": "Dossiers",
         "numberOfItems": len(ORDER),
         "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": d["titre"],
              "url": BASE + "dossiers/" + d["slug"] + ".html"}
             for i, d in enumerate(ORDER)]},
    ]}
    stats = "".join(
        '<li><span class="v">%s</span><span class="l">%s</span><span class="n">%s</span></li>'
        % (il(v), il(l), il(n)) for v, l, n, _ in CHIFFRES[:4])

    secs = []
    for key, num, name, desc in SECTIONS:
        ds = [d for d in ORDER if d["section"] == key]
        cards = "".join(
            '<li><a href="dossiers/%s.html"><span class="num">%02d</span>'
            '<span class="ti">%s</span><span class="de">%s</span>'
            '<span class="statut %s">%s</span></a></li>'
            % (d["slug"], INDEXOF[d["slug"]] + 1, esc(d["titre"]),
               il(excerpt(d["chapo"], 145)),
               STATUTS[d["statut"]][1], esc(STATUTS[d["statut"]][0]))
            for d in ds)
        secs.append('<section class="sectionhead" id="%s"><p class="r">%s</p>'
                    '<h2>%s</h2><p>%s</p></section><ul class="grid">%s</ul>'
                    % (key, num, esc(name), il(desc), cards))

    parts = [head(SITE["titre"] + " — " + SITE["sous_titre"], SITE["description"],
                  "fin de la Belgique, scission, confédéralisme, indépendance flamande, Bruxelles, "
                  "dette publique, sécession, fédéralisme belge, Bye Bye Belgium",
                  canon, 0, ld,
                  "Bye Bye Belgium — instruire la fin d'un pays"),
             masthead(0, None), '<main id="contenu">',
             '<section class="hero">',
             '<p class="kicker">Enquête · corpus arrêté au %s</p>' % SITE["arret"],
             '<h1>La fin de la Belgique n\'a jamais été écrite</h1>',
             '<p class="sub">Le 13 décembre 2006, la RTBF annonçait la fin du pays et découvrait '
             'que personne ne savait ce qui se passerait ensuite. Vingt ans plus tard, la réponse '
             'n\'existe toujours pas. Ce site instruit les scénarios : ce qu\'ils exigent, ce '
             'qu\'ils coûtent, et où ils cassent.</p>',
             '</section>',
             '<ul class="stats">%s</ul>' % stats,
             '<div class="wrap intro">',
             '<p class="lead">Vingt-et-un dossiers, %d sources, %d termes de lexique, '
             '%d repères chronologiques. Chaque scénario de sortie porte un '
             '<strong>statut d\'instruction</strong> : instruit, partiellement instruit, non '
             'instruit. Le résultat de l\'enquête tient dans ce classement — la grande majorité '
             'des questions décisives n\'a fait l\'objet d\'aucun texte public, dans aucun camp.</p>'
             % (len(SOURCES), len(LEXIQUE), len(CHRONO)),
             '<p>La thèse défendue ici est que le pays ne se casse pas : il se vide. Les capacités '
             'd\'administrer et de gouverner tiennent ; la capacité d\'arbitrer a migré vers des '
             'instances non élues. Voir le <a href="dossiers/verdict.html">verdict</a>, ou la '
             '<a href="methode.html">méthode</a>.</p>',
             '</div>'] + secs + ['</main>', footer(0)]
    write("index.html", "\n".join(parts), "weekly", "1.0")


def build_sommaire():
    canon = BASE + "sommaire.html"
    ps = []
    il = Inline(set(LEX), set(DOS), set(SRC), "", ps)
    ld = {"@context": "https://schema.org", "@graph": [
        person(), website(), place(),
        {"@type": "CollectionPage", "@id": canon, "url": canon, "name": "Sommaire",
         "description": "Les vingt-et-un dossiers de l'enquête, classés en cinq parties.",
         "inLanguage": "fr-BE", "isPartOf": {"@id": BASE + "#site"}},
        {"@type": "ItemList", "numberOfItems": len(ORDER), "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": d["titre"],
             "description": d["description"],
             "url": BASE + "dossiers/" + d["slug"] + ".html"} for i, d in enumerate(ORDER)]},
        breadcrumb([("Accueil", BASE), ("Sommaire", canon)]),
    ]}
    rows = []
    for key, num, name, desc in SECTIONS:
        ds = [d for d in ORDER if d["section"] == key]
        tr = "".join(
            '<tr><td><a href="dossiers/%s.html">%s</a></td><td>%s</td>'
            '<td><span class="statut %s">%s</span></td></tr>'
            % (d["slug"], esc(d["titre"]), il(d["description"]),
               STATUTS[d["statut"]][1], esc(STATUTS[d["statut"]][0]))
            for d in ds)
        rows.append('<section class="sectionhead" id="%s"><p class="r">%s</p><h2>%s</h2>'
                    '<p>%s</p></section>'
                    '<div class="tablewrap"><table><thead><tr><th scope="col">Dossier</th>'
                    '<th scope="col">Objet</th><th scope="col">Statut</th></tr></thead>'
                    '<tbody>%s</tbody></table></div>' % (key, num, esc(name), il(desc), tr))
    parts = [head("Sommaire", "Les vingt-et-un dossiers de l'enquête sur la fin de la Belgique, "
                  "classés en cinq parties, avec leur statut d'instruction.",
                  "sommaire, dossiers, scission Belgique, confédéralisme, sécession",
                  canon, 0, ld),
             masthead(0, "sommaire.html"), '<main id="contenu">',
             '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>'
             '<li><a href="index.html">Accueil</a></li><li>Sommaire</li></ol></nav>',
             '<h1>Sommaire</h1>',
             '<div class="wrap intro"><p class="chapo">Vingt-et-un dossiers en cinq parties. La colonne '
             'de droite indique le statut d\'instruction : elle est le résultat principal de '
             'l\'enquête.</p></div>'] + rows + ['</main>', footer(0)]
    write("sommaire.html", "\n".join(parts), "weekly", "0.9")


def build_chronologie():
    canon = BASE + "chronologie.html"
    ps = []
    il = Inline(set(LEX), set(DOS), set(SRC), "", ps)
    items = []
    for date, titre, texte, srcs in CHRONO:
        refs = "".join(il("((%s))" % s) for s in srcs)
        items.append('<li><span class="d">%s</span><span class="h">%s</span>'
                     '<p>%s %s</p></li>' % (esc(date), esc(titre), il(texte), refs))
    ld = {"@context": "https://schema.org", "@graph": [
        person(), website(), place(),
        {"@type": "WebPage", "@id": canon, "url": canon, "name": "Chronologie",
         "description": "De 1830 à 2034 : les dates qui décident du sort de l'État belge.",
         "inLanguage": "fr-BE", "isPartOf": {"@id": BASE + "#site"}},
        {"@type": "ItemList", "name": "Chronologie", "numberOfItems": len(CHRONO),
         "itemListElement": [{"@type": "ListItem", "position": i + 1,
                              "item": {"@type": "Event", "name": t,
                                       "description": x, "startDate": d}}
                             for i, (d, t, x, _) in enumerate(CHRONO)]},
        breadcrumb([("Accueil", BASE), ("Chronologie", canon)]),
    ]}
    parts = [head("Chronologie", "De 1830 à 2034 : les vingt-cinq dates qui décident du sort de "
                  "l'État belge, du gel de la frontière linguistique à l'extinction du mécanisme "
                  "de transition.",
                  "chronologie Belgique, réformes de l'État, frontière linguistique, 1962, 2034",
                  canon, 0, ld),
             masthead(0, "chronologie.html"), '<main id="contenu">',
             '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>'
             '<li><a href="index.html">Accueil</a></li><li>Chronologie</li></ol></nav>',
             '<div class="wrap"><h1>Chronologie</h1>',
             '<p class="chapo">Vingt-cinq repères, de la fondation de l\'État à l\'extinction '
             'programmée du mécanisme de transition en 2034. La dernière date est la seule qui '
             'soit à la fois future, chiffrée et automatique.</p>',
             '<ol class="chrono">%s</ol>' % "".join(items),
             sources_block(ps), '</div></main>', footer(0)]
    write("chronologie.html", "\n".join(parts), "monthly", "0.7")


def build_chiffres():
    canon = BASE + "chiffres.html"
    ps = []
    il = Inline(set(LEX), set(DOS), set(SRC), "", ps)
    lis = []
    for v, l, n, sid in CHIFFRES:
        refs = il("((%s))" % sid)
        lis.append('<li><span class="v">%s</span><span class="l">%s</span>'
                   '<span class="n">%s %s</span></li>' % (il(v), il(l), il(n), refs))
    ld = {"@context": "https://schema.org", "@graph": [
        person(), website(), place(),
        {"@type": "WebPage", "@id": canon, "url": canon, "name": "Chiffres",
         "description": "Les quatorze indicateurs de l'enquête, chacun relié à sa source.",
         "inLanguage": "fr-BE", "isPartOf": {"@id": BASE + "#site"}},
        {"@type": "Dataset", "@id": canon + "#dataset",
         "name": "Indicateurs — fin de la Belgique",
         "description": "Indicateurs chiffrés utilisés dans l'enquête, avec leur source.",
         "creator": {"@id": BASE + "#auteur"}, "inLanguage": "fr-BE",
         "license": "https://creativecommons.org/licenses/by/4.0/",
         "spatialCoverage": {"@id": BASE + "#belgique"},
         "variableMeasured": [{"@type": "PropertyValue", "name": l, "value": v,
                               "description": n} for v, l, n, _ in CHIFFRES]},
        breadcrumb([("Accueil", BASE), ("Chiffres", canon)]),
    ]}
    parts = [head("Chiffres", "Quatorze indicateurs sourcés : audience du canular de 2006, "
                  "sièges nationalistes, transferts, dette, mécanisme de transition, notation.",
                  "chiffres Belgique, indicateurs, dette publique, transferts, sièges, notation",
                  canon, 0, ld),
             masthead(0, "chiffres.html"), '<main id="contenu">',
             '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>'
             '<li><a href="index.html">Accueil</a></li><li>Chiffres</li></ol></nav>',
             '<div class="wrap"><h1>Chiffres</h1>',
             '<p class="chapo">Quatorze indicateurs. Chacun renvoie à sa source. Deux d\'entre eux '
             'valent zéro : c\'est le résultat central de l\'enquête.</p></div>',
             '<ul class="stats">%s</ul>' % "".join(lis),
             '<div class="wrap">%s</div>' % sources_block(ps),
             '</main>', footer(0)]
    write("chiffres.html", "\n".join(parts), "monthly", "0.7")


def build_lexique():
    canon = BASE + "lexique.html"
    ps = []
    il = Inline(set(LEX), set(DOS), set(SRC), "", ps)
    terms = sorted(LEXIQUE, key=lambda t: t[1].lower())
    lis = []
    for slug, label, defi, xrefs in terms:
        xr = ""
        if xrefs:
            links = ", ".join('<a href="#t-%s">%s</a>' % (x, esc(LEX[x][1]))
                              for x in xrefs if x in LEX)
            if links:
                xr = '<p class="xr">Voir aussi : %s</p>' % links
        lis.append('<li id="t-%s"><h2>%s</h2><p>%s</p>%s</li>'
                   % (slug, esc(label), il(defi), xr))
    ld = {"@context": "https://schema.org", "@graph": [
        person(), website(), place(),
        {"@type": "WebPage", "@id": canon, "url": canon, "name": "Lexique",
         "description": "Vingt-trois termes du dossier institutionnel belge, définis.",
         "inLanguage": "fr-BE", "isPartOf": {"@id": BASE + "#site"}},
        {"@type": "DefinedTermSet", "@id": canon + "#lexique", "name": "Lexique",
         "inLanguage": "fr-BE",
         "hasDefinedTerm": [{"@type": "DefinedTerm", "@id": canon + "#t-" + s,
                             "name": l, "description": re.sub(r"\{\{[a-z0-9\-]+\|([^}]+)\}\}",
                                                              r"\1", d),
                             "inDefinedTermSet": {"@id": canon + "#lexique"}}
                            for s, l, d, _ in terms]},
        breadcrumb([("Accueil", BASE), ("Lexique", canon)]),
    ]}
    parts = [head("Lexique", "Vingt-trois termes du dossier institutionnel belge : sécession, "
                  "confédéralisme, facilités, mécanisme de transition, vétocratie, succession "
                  "d'États.",
                  "lexique, définitions, confédéralisme, sécession, facilités linguistiques, "
                  "vétocratie, loi spéciale de financement",
                  canon, 0, ld),
             masthead(0, "lexique.html"), '<main id="contenu">',
             '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>'
             '<li><a href="index.html">Accueil</a></li><li>Lexique</li></ol></nav>',
             '<div class="wrap"><h1>Lexique</h1>',
             '<p class="chapo">Vingt-trois termes, définis pour être utilisés — pas pour être '
             'récités. Les mots du dossier belge sont piégés : « confédéralisme » et « transferts » '
             'désignent des choses différentes selon qui les emploie.</p>',
             '<ul class="lexlist">%s</ul>' % "".join(lis),
             sources_block(ps), '</div></main>', footer(0)]
    write("lexique.html", "\n".join(parts), "monthly", "0.6")


def build_sources(usage):
    canon = BASE + "sources.html"
    natures = [("institution", "Institutions et administrations"),
               ("juridiction", "Juridictions"),
               ("parlement", "Parlements"),
               ("recherche", "Recherche et encyclopédies"),
               ("organisation", "Organisations et société civile"),
               ("parti", "Partis politiques"),
               ("presse", "Presse")]
    blocks = []
    for key, label in natures:
        items = [s for s in SOURCES if s[4] == key]
        if not items:
            continue
        lis = []
        for s in sorted(items, key=lambda x: x[2].lower()):
            used = usage.get(s[0], [])
            ul = ""
            if used:
                ul = ('<span class="used">Cité dans : %s</span>'
                      % ", ".join('<a href="dossiers/%s.html">%s</a>'
                                  % (sl, esc(DOS[sl]["titre"])) for sl in used))
            lis.append('<li><a class="ti" href="%s" rel="noopener nofollow" target="_blank">%s</a>'
                       '<span class="mt">%s — %s</span>%s</li>'
                       % (esc(s[5]), esc(s[1]), esc(s[2]), esc(s[3]), ul))
        blocks.append('<h2 id="%s">%s <span class="note">(%d)</span></h2>'
                      '<ul class="srclist">%s</ul>' % (key, esc(label), len(items), "".join(lis)))
    ld = {"@context": "https://schema.org", "@graph": [
        person(), website(), place(),
        {"@type": "WebPage", "@id": canon, "url": canon, "name": "Sources",
         "description": "Les sources de l'enquête, classées par nature.",
         "inLanguage": "fr-BE", "isPartOf": {"@id": BASE + "#site"}},
        {"@type": "ItemList", "numberOfItems": len(SOURCES), "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "item": {"@type": "CreativeWork", "name": s[1], "url": s[5],
                      "publisher": {"@type": "Organization", "name": s[2]}}}
            for i, s in enumerate(SOURCES)]},
        breadcrumb([("Accueil", BASE), ("Sources", canon)]),
    ]}
    parts = [head("Sources", "Les %d sources de l'enquête, classées par nature : institutions, "
                  "juridictions, parlements, recherche, presse." % len(SOURCES),
                  "sources, bibliographie, références, Belgique, institutions, presse",
                  canon, 0, ld),
             masthead(0, "sources.html"), '<main id="contenu">',
             '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>'
             '<li><a href="index.html">Accueil</a></li><li>Sources</li></ol></nav>',
             '<div class="wrap intro"><h1>Sources</h1>',
             '<p class="chapo">%d références, classées par nature. Les liens sortants ouvrent '
             'dans un nouvel onglet et ne transmettent pas de référent.</p></div>' % len(SOURCES),
             '<div class="wrap intro">%s</div>' % "".join(blocks),
             '</main>', footer(0)]
    write("sources.html", "\n".join(parts), "monthly", "0.6")


def build_methode(usage):
    canon = BASE + "methode.html"
    ps = []
    il = Inline(set(LEX), set(DOS), set(SRC), "", ps)
    n_non = sum(1 for d in ORDER if d["statut"] == "non instruit")
    n_part = sum(1 for d in ORDER if d["statut"] == "partiellement instruit")
    n_oui = sum(1 for d in ORDER if d["statut"] == "instruit")

    blocks = [
        ("p", "Ce site est une enquête documentaire. Il ne défend ni le maintien ni la fin de "
              "l'État belge : il vérifie si les scénarios de sortie ont été instruits, et publie "
              "le résultat de cette vérification."),
        ("h", "Le statut d'instruction"),
        ("p", "Chaque dossier porte un statut. Il ne mesure pas la qualité de ce site mais l'état "
              "du débat public sur la question traitée."),
        ("ul", [
            "**Instruit** : la question est documentée par des sources publiques concordantes, "
            "que l'on soit d'accord ou non avec leurs conclusions.",
            "**Partiellement instruit** : une partie des éléments décisifs a été publiée, une "
            "autre non.",
            "**Non instruit** : aucun texte public ne règle la question posée. C'est un constat "
            "d'absence, vérifiable par quiconque : il suffit de produire le texte pour l'infirmer.",
        ]),
        ("chiffres", [
            ("%d" % n_oui, "dossiers instruits", "questions documentées par des sources publiques"),
            ("%d" % n_part, "partiellement instruits", "éléments décisifs manquants"),
            ("%d" % n_non, "non instruits", "aucun texte public ne règle la question"),
            ("%d" % len(SOURCES), "sources", "classées par nature et reliées aux dossiers"),
        ]),
        ("h", "Règles de vérification"),
        ("ol", [
            "Tout chiffre cité renvoie à une source identifiée, datée et accessible en ligne.",
            "Lorsque deux sources divergent, la plus récente et la plus proche du producteur de la "
            "donnée est retenue, et l'écart est signalé dans le dossier.",
            "Les estimations issues de partis politiques sont signalées comme telles et ne sont "
            "jamais présentées comme des données.",
            "Les calculs propres à ce site — il n'y en a qu'un, la répartition illustrative de la "
            "dette dans [[partager-la-dette|Partager la dette]] — sont explicitement identifiés "
            "comme tels et accompagnés de leurs hypothèses.",
            "Chaque dossier expose l'objection la plus sérieuse à sa propre thèse et ce qu'elle "
            "vaut. Ce n'est pas une clause de style : plusieurs objections ne sont pas réfutées.",
        ]),
        ("h", "Corpus d'origine et vérifications"),
        ("p", "Le point de départ est constitué de deux analyses publiées sur ce dépôt : "
              "l'analyse de la démocratie belge et l'analyse de la citoyenneté. Elles restent en "
              "ligne et sont accessibles depuis le pied de page. Chaque donnée reprise a fait "
              "l'objet d'une recherche complémentaire ; quatre séries ont dû être corrigées ou "
              "actualisées."),
        ("ol", [
            "**Notation souveraine.** Le corpus est antérieur à la séquence de 2025-2026. Vérifié : "
            "Fitch retire le double A en juin 2025 ; Moody's dégrade la Belgique de Aa3 à A1 le "
            "17 avril 2026 ((rtbf-moodys)).",
            "**Résultats électoraux.** Les chiffres retenus sont ceux de la Chambre des "
            "représentants pour le scrutin du 9 juin 2024 ((chambre-resultats-2024)), et non des "
            "estimations de sondage.",
            "**Transferts interrégionaux.** Le corpus n'intègre pas l'étude de la Banque nationale "
            "publiée en octobre 2025, qui établit un flux inverse de Bruxelles vers les deux "
            "autres régions ((llb-bnb-flux)). Ce résultat a été intégré et modifie la lecture du "
            "dossier.",
            "**Opinion publique.** Le corpus s'appuie sur des données d'Eurobaromètre agrégées. "
            "L'Enquête nationale 2026, plus récente et plus proche du sujet, lui a été préférée "
            "((dsen26-rapport)).",
        ]),
        ("h", "Ce que ce site ne traite pas"),
        ("ul", [
            "L'histoire du mouvement flamand et du mouvement wallon pour elle-même.",
            "Les politiques sectorielles — enseignement, santé, mobilité, énergie — sauf lorsqu'elles "
            "sont directement engagées par un scénario de séparation.",
            "La question migratoire, l'extrême droite et le cordon sanitaire, traités dans le "
            "corpus d'origine.",
            "Le sort de la Communauté germanophone, qui mériterait un dossier propre et n'en a pas.",
        ]),
        ("h", "Auteur, langue, technique"),
        ("p", "Les textes sont signés **Vigie**, nom de plume. L'éditeur du site reste anonyme. La "
              "rédaction a été assistée par un modèle de langage ; la sélection des sources, les "
              "vérifications et les arbitrages éditoriaux relèvent de l'éditeur."),
        ("p", "Le site est un site statique généré par un script Python sans dépendance. Il ne "
              "contient aucun JavaScript, aucun cookie, aucun traqueur et aucune ressource "
              "externe : aucune requête n'est faite à un tiers lors de la consultation. Le thème "
              "clair ou sombre suit le réglage du système. Une feuille d'impression est fournie."),
        ("h", "Corrections"),
        ("p", "Toute erreur factuelle signalée avec sa source sera corrigée et la correction "
              "mentionnée sur cette page. Le corpus est arrêté au %s ; les dossiers "
              "[[la-loi-de-financement|La falaise de 2034]] et "
              "[[les-marches-et-les-notes|Les marchés et les notes]] devront être mis à jour après "
              "le conclave budgétaire et l'échéance européenne du 15 octobre 2026." % SITE["arret"]),
    ]
    body, _ = render_blocks(blocks, il)
    ERRORS.extend("methode : %s" % e for e in il.errors)
    ld = {"@context": "https://schema.org", "@graph": [
        person(), website(), place(),
        {"@type": "WebPage", "@id": canon, "url": canon, "name": "Méthode",
         "description": "Règles de vérification, statuts d'instruction, corrections et limites.",
         "inLanguage": "fr-BE", "isPartOf": {"@id": BASE + "#site"}},
        breadcrumb([("Accueil", BASE), ("Méthode", canon)]),
    ]}
    parts = [head("Méthode", "Règles de vérification, statut d'instruction des dossiers, "
                  "corrections apportées au corpus d'origine et limites assumées de l'enquête.",
                  "méthode, vérification, sources, corrections, transparence, statut d'instruction",
                  canon, 0, ld),
             masthead(0, "methode.html"), '<main id="contenu">',
             '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>'
             '<li><a href="index.html">Accueil</a></li><li>Méthode</li></ol></nav>',
             '<div class="wrap"><h1>Méthode</h1>',
             '<p class="chapo">Ce site publie un constat d\'absence. Un constat d\'absence se '
             'réfute par la production du texte manquant — c\'est la seule réfutation qui '
             'l\'intéresse.</p>',
             body, sources_block(ps), '</div></main>', footer(0)]
    write("methode.html", "\n".join(parts), "monthly", "0.6")


def build_404():
    canon = BASE + "404.html"
    ld = {"@context": "https://schema.org", "@graph": [
        person(), website(),
        {"@type": "WebPage", "@id": canon, "url": canon, "name": "Page introuvable",
         "description": "Cette page n'existe pas.", "inLanguage": "fr-BE",
         "isPartOf": {"@id": BASE + "#site"}}]}
    parts = [head("Page introuvable",
                  "Cette adresse n'existe pas sur ce site. Reprendre par le sommaire, la "
                  "chronologie ou l'accueil de l'enquête sur la fin de la Belgique.",
                  "404, page introuvable", canon, 0, ld),
             masthead(0, None), '<main id="contenu"><div class="wrap">',
             '<h1>Ceci n\'existe pas</h1>',
             '<p class="chapo">La page demandée est introuvable. C\'est une situation que ce site '
             'traite abondamment par ailleurs.</p>',
             '<p>Reprendre par le <a href="sommaire.html">sommaire</a>, la '
             '<a href="chronologie.html">chronologie</a> ou l\'<a href="index.html">accueil</a>.</p>',
             '</div></main>', footer(0)]
    write("404.html", "\n".join(parts), indexable=False)


def build_static(usage):
    # favicon et image de partage
    with open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON)
    og = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" '
          'height="630" role="img" aria-label="Bye Bye Belgium">'
          '<rect width="1200" height="630" fill="#16161a"/>'
          '<rect x="0" y="520" width="1200" height="110" fill="#b3151f"/>'
          '<text x="70" y="250" font-family="Arial Narrow,Arial,sans-serif" font-weight="bold" '
          'font-size="150" fill="#b3151f">BYE BYE</text>'
          '<text x="70" y="390" font-family="Arial Narrow,Arial,sans-serif" font-weight="bold" '
          'font-size="150" fill="#f6f3ec">BELGIUM</text>'
          '<text x="70" y="452" font-family="Arial,sans-serif" font-size="30" fill="#a9a49a">'
          'Instruire la fin d\'un pays</text>'
          '<text x="70" y="588" font-family="Arial,sans-serif" font-weight="bold" font-size="34" '
          'fill="#ffffff">21 dossiers · %d sources · aucun scénario écrit</text>'
          '</svg>' % len(SOURCES))
    with open(os.path.join(ROOT, "og.svg"), "w", encoding="utf-8") as f:
        f.write(og)

    # feuille de style
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "assets", "site.css"),
                    os.path.join(ROOT, "assets", "site.css"))

    # robots.txt
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % BASE)

    # sitemap
    urls = []
    for path, freq, prio in PAGES:
        loc = BASE + ("" if path == "index.html" else path)
        urls.append("  <url><loc>%s</loc><changefreq>%s</changefreq>"
                    "<priority>%s</priority></url>" % (esc(loc), freq, prio))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "\n".join(urls) + "\n</urlset>\n")

    # flux RSS
    items = []
    for d in ORDER:
        link = BASE + "dossiers/" + d["slug"] + ".html"
        items.append("    <item><title>%s</title><link>%s</link><guid isPermaLink=\"true\">%s</guid>"
                     "<description>%s</description></item>"
                     % (esc(d["titre"]), esc(link), esc(link), esc(d["description"])))
    with open(os.path.join(ROOT, "rss.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0">\n  <channel>\n'
                '    <title>%s — %s</title>\n    <link>%s</link>\n'
                '    <description>%s</description>\n    <language>fr-be</language>\n%s\n'
                '  </channel>\n</rss>\n'
                % (esc(SITE["titre"]), esc(SITE["sous_titre"]), esc(BASE),
                   esc(SITE["description"]), "\n".join(items)))

    # llms.txt
    lines = ["# %s — %s" % (SITE["titre"], SITE["sous_titre"]), "",
             "> %s" % SITE["description"], "",
             "Auteur : %s (nom de plume). Éditeur anonyme. Corpus arrêté au %s."
             % (SITE["auteur"], SITE["arret"]),
             "Site statique, sans JavaScript ni ressource externe. %d sources listées."
             % len(SOURCES), "",
             "## Thèse", "",
             "La fin de la Belgique est annoncée depuis un siècle et n'a jamais été écrite. "
             "Aucun parti n'a publié de clé de partage de la dette, de statut juridique pour "
             "Bruxelles ni de régime transitoire pour les droits sociaux. Ce qui se produit n'est "
             "pas une rupture mais une dissociation continue : le pays ne se casse pas, il se vide, "
             "et sa capacité d'arbitrage migre vers des instances non élues.", "",
             "## Dossiers", ""]
    for key, num, name, desc in SECTIONS:
        lines.append("### %s. %s" % (num, name))
        lines.append("")
        for d in [x for x in ORDER if x["section"] == key]:
            lines.append("- [%s](%sdossiers/%s.html) — %s *(%s)*"
                         % (d["titre"], BASE, d["slug"], d["description"],
                            STATUTS[d["statut"]][0].lower()))
        lines.append("")
    lines += ["## Pages", ""]
    for href, label in NAV:
        lines.append("- [%s](%s%s)" % (label, BASE, href))
    lines.append("")
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    usage = {}
    for d in ORDER:
        ps = build_dossier(d)
        for sid in ps:
            usage.setdefault(sid, []).append(d["slug"])
    build_index()
    build_sommaire()
    build_chronologie()
    build_chiffres()
    build_lexique()
    build_sources(usage)
    build_methode(usage)
    build_404()
    build_static(usage)

    orphans = [s[0] for s in SOURCES if s[0] not in usage]
    print("Pages écrites : %d" % (len(PAGES) + 1))
    print("Dossiers : %d — sources : %d — termes : %d — repères : %d — indicateurs : %d"
          % (len(ORDER), len(SOURCES), len(LEXIQUE), len(CHRONO), len(CHIFFRES)))
    if orphans:
        print("Sources non citées dans un dossier : %d" % len(orphans))
    if ERRORS:
        print("\nERREURS DE CONSTRUCTION :")
        for e in ERRORS:
            print("  -", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
