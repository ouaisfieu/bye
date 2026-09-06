# -*- coding: utf-8 -*-
"""Rendu du balisage en ligne et typographie française."""
import re, html

NBSP = " "
NNBSP = " "

def typo(text):
    """Espaces insécables françaises, appliquées hors des balises."""
    out = []
    for part in re.split(r"(<[^>]*>)", text):
        if part.startswith("<"):
            out.append(part)
            continue
        part = re.sub(r"\s+([;!?])", NNBSP + r"\1", part)
        part = re.sub(r"\s+(:)", NBSP + r"\1", part)
        part = re.sub(r"«\s+", "«" + NBSP, part)
        part = re.sub(r"\s+»", NBSP + "»", part)
        part = re.sub(r"(\d)\s+(\d{3})\b", r"\1" + NNBSP + r"\2", part)
        part = re.sub(r"(\d)\s+(%|‰|€|Md€|M€|km|ha|pts?)\b", r"\1" + NNBSP + r"\2", part)
        part = re.sub(r"(\d)\s+(%|€)", r"\1" + NNBSP + r"\2", part)
        part = re.sub(r"([≈±−])\s+", r"\1" + NNBSP, part)
        part = re.sub(r"(\d)\s+(Md€|M€)", r"\1" + NNBSP + r"\2", part)
        part = part.replace("' ", "' ") if False else part
        out.append(part)
    return "".join(out)


class Inline:
    """Résout {{terme|libellé}}, [[dossier|libellé]], ((source)), **gras**, *italique*."""

    def __init__(self, lexique_ids, dossier_ids, source_ids, prefix, page_sources):
        self.lex = lexique_ids
        self.dos = dossier_ids
        self.src = source_ids
        self.prefix = prefix
        self.page_sources = page_sources  # liste ordonnée, mutée
        self.errors = []

    def _srcnum(self, sid):
        if sid not in self.page_sources:
            self.page_sources.append(sid)
        return self.page_sources.index(sid) + 1

    def __call__(self, text):
        t = html.escape(text, quote=False)

        def term(m):
            slug, label = m.group(1), m.group(2)
            if slug not in self.lex:
                self.errors.append("terme inconnu : " + slug)
                return label
            return ('<a class="lex" href="%slexique.html#t-%s">%s</a>' % (self.prefix, slug, label))

        def dossier(m):
            slug, label = m.group(1), m.group(2)
            if slug not in self.dos:
                self.errors.append("dossier inconnu : " + slug)
                return label
            return '<a href="%sdossiers/%s.html">%s</a>' % (self.prefix, slug, label)

        def source(m):
            sid = m.group(1)
            if sid not in self.src:
                self.errors.append("source inconnue : " + sid)
                return ""
            n = self._srcnum(sid)
            return ('<a class="ref" href="#s-%d" title="Source %d"><sup>%d</sup></a>'
                    % (n, n, n))

        t = re.sub(r"\{\{([a-z0-9\-]+)\|([^}]+)\}\}", term, t)
        t = re.sub(r"\[\[([a-z0-9\-]+)\|([^\]]+)\]\]", dossier, t)
        t = re.sub(r"\(\(([a-z0-9\-]+)\)\)", source, t)
        t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
        return typo(t)
