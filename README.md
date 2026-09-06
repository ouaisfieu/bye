# Bye Bye Belgium

Enquête documentée sur les scénarios de fin de l'État belge, publiée à
**<https://ouaisfieu.github.io/bye/>**.

Auteur des textes : **Vigie** (nom de plume). Éditeur : anonyme.
Corpus arrêté au 6 septembre 2026.

## Ce que contient le site

- **21 dossiers** en cinq parties : l'annonce, le droit de partir, le nœud bruxellois,
  la facture, les issues.
- Chaque dossier porte un **statut d'instruction** — instruit, partiellement instruit,
  non instruit — qui mesure l'état du débat public sur la question traitée, pas la qualité
  du dossier.
- **105 sources** classées par nature, **23 termes** de lexique ancrés, **25 repères**
  chronologiques, **14 indicateurs** reliés chacun à sa source.
- Accueil, sommaire, chronologie, chiffres, lexique, sources, méthode, 404,
  `sitemap.xml`, `robots.txt`, `rss.xml`, `llms.txt`.

Aucun JavaScript, aucun cookie, aucun traqueur, aucune ressource externe : la consultation
d'une page ne déclenche aucune requête vers un tiers. Thème clair et sombre selon le réglage
du système, feuille d'impression, typographie française (espaces insécables).

## Thèse

La fin de la Belgique est annoncée depuis plus d'un siècle et n'a jamais été écrite. Aucun
parti n'a publié de clé de partage de la dette, de statut juridique opposable pour Bruxelles
ni de régime transitoire pour les droits sociaux acquis. Ce qui se produit n'est pas une
rupture mais une dissociation continue : le pays ne se casse pas, il se vide, et sa capacité
d'arbitrage migre vers des instances non élues — Commission européenne, agences de notation,
juridictions.

## Structure du dépôt

```
index.html, sommaire.html, ...   sortie publiée (générée — ne pas éditer à la main)
dossiers/                        les 21 dossiers
assets/site.css                  feuille de style unique
bye/                             corpus d'origine, conservé en place
tools/
  data.py                        sources, lexique, chronologie, indicateurs
  dossiers_a.py … dossiers_e.py  contenu des cinq parties
  render.py                      balisage en ligne et typographie française
  build.py                       générateur
  check.py                       contrôle qualité
  assets/site.css                source de la feuille de style
```

## Reconstruire

Python 3, aucune dépendance à installer.

```sh
python3 tools/build.py
python3 tools/check.py
```

`check.py` valide : doctype et `lang`, un seul `h1` par page, hiérarchie des titres sans saut,
unicité des identifiants, résolution de **tous** les liens internes et de toutes les ancres,
métadonnées SEO (title, description, canonical, six propriétés Open Graph, carte Twitter),
parsing de chaque bloc JSON-LD et présence des types attendus, absence de script exécutable
et de ressource externe, absence de balisage résiduel, cohérence du `sitemap.xml` et du flux
RSS, longueur moyenne des phrases.

État actuel : **29 pages, 0 erreur, 0 avertissement**. La construction est reproductible
(aucune date dynamique) et un workflow GitHub Actions échoue si la sortie publiée ne
correspond pas aux sources.

## Balisage du contenu

Dans les textes des dossiers :

| Écriture | Rendu |
| --- | --- |
| `{{slug\|libellé}}` | lien vers le terme du lexique |
| `[[dossier\|libellé]]` | lien vers un autre dossier |
| `((identifiant-source))` | renvoi numéroté vers la source, listée en pied de dossier |
| `**gras**`, `*italique*` | emphase |

Blocs disponibles : `p`, `h`, `sh`, `ul`, `ol`, `q` (citation), `chiffres` (bandeau),
`table`, `contre` (objection la plus sérieuse), `doute` (incertitude assumée).

## Corriger

Toute erreur factuelle signalée avec sa source sera corrigée, et la correction mentionnée
sur la page méthode.

## Licence

Textes : CC BY 4.0. Le code du générateur est libre de réutilisation.

## Image de partage

`og.svg` est généré par `tools/build.py`. `og.png`, référencée par les métadonnées Open Graph
(la plupart des plateformes ne rendent pas le SVG), en est un rendu 1200 × 630 à régénérer
lorsque le nombre de sources change :

```sh
python3 - <<'PY'
import asyncio
from playwright.async_api import async_playwright
async def m():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1200, "height": 630})
        await pg.goto("file://" + __import__("os").getcwd() + "/og.svg")
        await pg.screenshot(path="og.png")
        await b.close()
asyncio.run(m())
PY
```
