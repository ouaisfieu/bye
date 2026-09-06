# -*- coding: utf-8 -*-
"""Contrôle qualité du site construit. Python 3, sans dépendance."""

import json, os, re, sys, glob
from html.parser import HTMLParser
from urllib.parse import urldefrag, unquote
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from data import SITE, SOURCES  # noqa: E402

BASE = SITE["base"]
ERR, WARN = [], []
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


def err(f, m):
    ERR.append("%s : %s" % (f, m))


def warn(f, m):
    WARN.append("%s : %s" % (f, m))


class Doc(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.dup = [], [], []
        self.headings, self.links, self.assets = [], [], []
        self.unbalanced = []
        self.text_parts, self._skip = [], 0
        self.h1 = 0
        self.imgs_no_alt = 0
        self.scripts = []
        self.cur_h = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if "id" in a:
            if a["id"] in self.ids:
                self.dup.append(a["id"])
            self.ids.append(a["id"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
        if tag == "link" and "href" in a:
            if a.get("rel") not in ("canonical", "alternate"):
                self.assets.append(a["href"])
        if tag in ("img", "script", "iframe", "source", "video", "audio", "embed") and "src" in a:
            self.assets.append(a["src"])
        if tag == "img" and not a.get("alt") and a.get("role") != "presentation":
            self.imgs_no_alt += 1
        if tag == "script":
            self.scripts.append(a.get("type", ""))
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
            self.cur_h = int(tag[1])
            if tag == "h1":
                self.h1 += 1
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.unbalanced.append(self.stack.pop())
            if self.stack:
                self.stack.pop()
        else:
            self.unbalanced.append("</%s> sans ouverture" % tag)
        if tag in ("script", "style"):
            self._skip = max(0, self._skip - 1)

    def handle_data(self, data):
        if not self._skip:
            self.text_parts.append(data)


def check_page(path, rel, all_ids):
    raw = open(path, encoding="utf-8").read()

    if not raw.startswith("<!DOCTYPE html>"):
        err(rel, "doctype manquant")
    if '<html lang="fr">' not in raw:
        err(rel, "attribut lang manquant")

    d = Doc()
    d.feed(raw)
    d.close()

    if d.h1 != 1:
        err(rel, "%d élément h1 (attendu : 1)" % d.h1)
    if d.stack:
        err(rel, "balises non fermées : %s" % ", ".join(d.stack[:5]))
    if d.unbalanced:
        err(rel, "balises mal imbriquées : %s" % ", ".join(map(str, d.unbalanced[:5])))
    if d.dup:
        err(rel, "identifiants dupliqués : %s" % ", ".join(sorted(set(d.dup))[:5]))
    if d.imgs_no_alt:
        err(rel, "%d image sans attribut alt" % d.imgs_no_alt)

    # hiérarchie des titres
    prev = 0
    for h in d.headings:
        if prev and h > prev + 1:
            err(rel, "saut de niveau de titre : h%d après h%d" % (h, prev))
            break
        prev = h

    # scripts : seul le JSON-LD est admis
    for t in d.scripts:
        if t != "application/ld+json":
            err(rel, "script exécutable détecté (type=%r)" % t)

    # ressources externes
    for a in d.assets:
        if a.startswith("http://") or a.startswith("https://") or a.startswith("//"):
            err(rel, "ressource externe : %s" % a)
        if a.startswith("data:"):
            warn(rel, "ressource en data-URI")

    # métadonnées
    def meta(name, attr="name"):
        m = re.search(r'<meta %s="%s" content="([^"]*)"' % (attr, re.escape(name)), raw)
        return m.group(1) if m else None

    title = re.search(r"<title>(.*?)</title>", raw, re.S)
    if not title:
        err(rel, "title manquant")
    else:
        n = len(title.group(1))
        if n > 95:
            warn(rel, "title long : %d caractères" % n)
        if n < 15:
            warn(rel, "title court : %d caractères" % n)
    desc = meta("description")
    if not desc:
        err(rel, "meta description manquante")
    elif not (50 <= len(desc) <= 320):
        warn(rel, "meta description de %d caractères" % len(desc))
    if not re.search(r'<link rel="canonical" href="([^"]+)"', raw):
        err(rel, "canonical manquant")
    for p in ("og:type", "og:title", "og:description", "og:url", "og:image", "og:site_name"):
        if not meta(p, "property"):
            err(rel, "propriété Open Graph manquante : %s" % p)
    if not meta("twitter:card"):
        err(rel, "twitter:card manquante")

    # JSON-LD
    types = set()
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', raw, re.S):
        try:
            data = json.loads(m.group(1))
        except Exception as e:
            err(rel, "JSON-LD illisible : %s" % e)
            continue
        for node in data.get("@graph", [data]):
            t = node.get("@type")
            if isinstance(t, list):
                types.update(t)
            elif t:
                types.add(t)
    if "CollectionPage" in types:
        types.add("WebPage")
    for req in ("WebSite", "Person", "WebPage", "BreadcrumbList"):
        if rel not in ("404.html",) and req not in types:
            if req == "BreadcrumbList" and rel == "index.html":
                continue
            err(rel, "type JSON-LD attendu absent : %s" % req)

    # balisage résiduel
    body = "".join(d.text_parts)
    for pat, label in ((r"\{\{[^}]*\}\}", "modèle de lexique"), (r"\(\([a-z0-9\-]+\)\)", "renvoi de source"),
                       (r"\[\[[^\]]*\]\]", "lien de dossier"), (r"\*\*", "gras Markdown")):
        if re.search(pat, body):
            err(rel, "balisage non résolu (%s)" % label)

    all_ids[rel] = set(d.ids)
    return d, raw


def main():
    pages = sorted(glob.glob(os.path.join(ROOT, "*.html"))
                   + glob.glob(os.path.join(ROOT, "dossiers", "*.html")))
    if not pages:
        print("Aucune page. Lancer d'abord tools/build.py.")
        sys.exit(1)

    all_ids, docs = {}, {}
    for p in pages:
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        docs[rel] = check_page(p, rel, all_ids)

    # liens internes et ancres
    for rel, (d, raw) in docs.items():
        base_dir = os.path.dirname(rel)
        for href in d.links:
            if href.startswith(("http://", "https://", "mailto:", "tel:", "//")):
                continue
            target, frag = urldefrag(href)
            frag = unquote(frag)
            if not target:
                if frag and frag not in all_ids[rel]:
                    err(rel, "ancre interne inexistante : #%s" % frag)
                continue
            resolved = os.path.normpath(os.path.join(base_dir, unquote(target)))
            resolved = resolved.replace(os.sep, "/")
            fs = os.path.join(ROOT, resolved)
            if resolved.endswith("/"):
                fs = os.path.join(fs, "index.html")
            if not os.path.exists(fs):
                if os.path.isdir(os.path.join(ROOT, resolved)):
                    if not os.path.exists(os.path.join(ROOT, resolved, "index.html")):
                        err(rel, "lien interne cassé : %s" % href)
                else:
                    err(rel, "lien interne cassé : %s" % href)
                continue
            if frag:
                key = resolved if resolved.endswith(".html") else resolved.rstrip("/") + "/index.html"
                if key in all_ids and frag not in all_ids[key]:
                    err(rel, "ancre inexistante : %s" % href)

    # fichiers annexes
    for f in ("sitemap.xml", "robots.txt", "rss.xml", "llms.txt", "favicon.svg",
              "og.svg", "og.png", "assets/site.css", "404.html", "README.md", ".nojekyll"):
        if not os.path.exists(os.path.join(ROOT, f)):
            err(f, "fichier manquant")

    # sitemap
    try:
        tree = ET.parse(os.path.join(ROOT, "sitemap.xml"))
        locs = [e.text for e in tree.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        for loc in locs:
            rel = loc[len(BASE):] or "index.html"
            if not os.path.exists(os.path.join(ROOT, rel)):
                err("sitemap.xml", "URL sans fichier : %s" % loc)
        listed = {(l[len(BASE):] or "index.html") for l in locs}
        for rel in docs:
            if rel != "404.html" and rel not in listed:
                err("sitemap.xml", "page absente du sitemap : %s" % rel)
    except Exception as e:
        err("sitemap.xml", "XML invalide : %s" % e)

    # RSS
    try:
        rss = ET.parse(os.path.join(ROOT, "rss.xml"))
        n = len(list(rss.iter("item")))
        if n < 20:
            warn("rss.xml", "%d entrées seulement" % n)
    except Exception as e:
        err("rss.xml", "XML invalide : %s" % e)

    # robots
    rob = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
    if "Sitemap:" not in rob:
        err("robots.txt", "directive Sitemap absente")

    # URLs des sources : unicité et forme
    seen = {}
    for s in SOURCES:
        if not s[5].startswith("https://"):
            err("sources", "URL non https : %s" % s[0])
        seen.setdefault(s[5], []).append(s[0])
    for url, ids in seen.items():
        if len(ids) > 1:
            warn("sources", "URL partagée par %s" % ", ".join(ids))

    # lisibilité
    for rel, (d, raw) in docs.items():
        if not rel.startswith("dossiers/"):
            continue
        text = re.sub(r"\s+", " ", "".join(d.text_parts))
        sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if len(s) > 20]
        if sentences:
            avg = sum(len(s.split()) for s in sentences) / len(sentences)
            if avg > 34:
                warn(rel, "phrases longues : %.1f mots en moyenne" % avg)

    print("Pages vérifiées : %d" % len(docs))
    if WARN:
        print("\nAvertissements (%d) :" % len(WARN))
        for w in WARN:
            print("  ·", w)
    if ERR:
        print("\nErreurs (%d) :" % len(ERR))
        for e in ERR:
            print("  ✗", e)
        sys.exit(1)
    print("0 erreur, %d avertissement." % len(WARN))


if __name__ == "__main__":
    main()
