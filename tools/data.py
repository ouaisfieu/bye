# -*- coding: utf-8 -*-
"""Registres partagés : sources, lexique, chronologie, indicateurs."""

SITE = {
    "titre": "Bye Bye Belgium",
    "sous_titre": "Instruire la fin d'un pays",
    "base": "https://ouaisfieu.github.io/bye/",
    "auteur": "Vigie",
    "langue": "fr-BE",
    "description": (
        "Enquête documentée sur les scénarios de fin de la Belgique : droit de sécession, "
        "statut de Bruxelles, partage de la dette, confédéralisme, indépendance flamande, "
        "refédéralisation. Chaque scénario instruit, chaque chiffre sourcé."
    ),
    "arret": "6 septembre 2026",
    "date_iso": "2026-09-06",
}

# ---------------------------------------------------------------------------
# SOURCES
# nature : institution | juridiction | parlement | recherche | presse | parti | organisation
# ---------------------------------------------------------------------------

SOURCES = [
    # -- Le canular et sa postérité
    ("rtbf-bbb-electrochoc", "Bye Bye Belgium : en 2006, le docu-fiction de la RTBF créait un électrochoc",
     "RTBF", "2021", "presse",
     "https://www.rtbf.be/article/bye-bye-belgium-en-2006-le-docu-fiction-de-la-rtbf-creait-un-electrochoc-9479103"),
    ("rtbf-bbb-coulisses", "15 ans après Bye Bye Belgium : les coulisses d'une émission toujours controversée",
     "RTBF", "2021", "presse",
     "https://www.rtbf.be/article/15-ans-apres-bye-bye-belgium-les-coulisses-dune-emission-toujours-controversee-10894570"),
    ("wp-bbb", "Bye Bye Belgium — notice encyclopédique (audiences, réactions, suites déontologiques)",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://fr.wikipedia.org/wiki/Bye_Bye_Belgium"),
    ("slate-bbb", "Bye Bye Belgium : le jour où la télé belge a annoncé la fin du pays en direct",
     "Slate.fr", "2025", "presse",
     "https://www.slate.fr/story/221313/bye-bye-belgium-television-belge-annonce-fin-du-pays-direct-independance-canular-dutilleul"),
    ("moustique-bbb", "Comment Bye Bye Belgium a révolutionné le docu-fiction",
     "Moustique", "6 juillet 2026", "presse",
     "https://www.moustique.be/notre-epoque/les-histoires/2026/07/06/la-serie-de-lete-les-meilleures-histoires-de-la-television-belge-comment-bye-bye-belgium-a-revolutionne-le-docu-fiction-NE5AW44TQBEWJMCD5S6YNKC6DI/"),

    # -- Opinion publique
    ("dsen26-rapport", "De Stemming / L'Enquête nationale 2026 — rapport (partie 1)",
     "UAntwerpen & ULB, pour la VRT, De Standaard et la RTBF", "26 mai 2026", "recherche",
     "https://www.vrt.be/content/dam/vrtnieuws/bestanden/2026/20260526_DSEN26_report_part1.pdf"),
    ("dsen25-rapport", "De Stemming / L'Enquête nationale 2025 — rapport Wallonie et Bruxelles",
     "UAntwerpen & ULB, pour la VRT, De Standaard et la RTBF", "23 mai 2025", "recherche",
     "https://www.vrt.be/content/dam/vrtnieuws/bestanden/2025/20250523_DSEN2025_WAL_BXL_rapport_2025.pdf"),
    ("rtbf-dsen26-cliches", "L'Enquête nationale 2026 déconstruit les clichés des Belges",
     "RTBF", "2026", "presse",
     "https://www.rtbf.be/article/la-flandre-a-droite-la-wallonie-a-gauche-respect-de-l-etat-de-droit-et-reconnaissance-de-la-palestine-l-enquete-nationale-2026-deconstruit-les-cliches-des-belges-11728073"),
    ("vrt-dsen25-democratie", "Regain de confiance dans la démocratie en Flandre depuis l'arrivée du gouvernement De Wever",
     "VRT NWS", "22 mai 2025", "presse",
     "https://www.vrt.be/vrtnws/fr/2025/05/22/regain-de-confiance-dans-la-democratie-en-flandre-depuis-larrive/"),
    ("vrt-flamingant", "Le Flamand est-il flamingant ou veut-il au contraire un retour à plus de Belgique ?",
     "VRT NWS", "23 mai 2021", "presse",
     "https://www.vrt.be/vrtnws/fr/2021/05/23/le-flamand-est-il-un-flamingant-ou-veut-il-au-contraire-un-retou/"),
    ("wp-scission", "Scission de la Belgique — notice encyclopédique (scénarios, sondages, positions)",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://fr.wikipedia.org/wiki/Scission_de_la_Belgique"),
    ("wp-sondages-rattachement", "Liste de sondages portant sur le rattachement de la Wallonie à la France",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://fr.wikipedia.org/wiki/Liste_de_sondages_portant_sur_le_rattachement_de_la_Wallonie_%C3%A0_la_France"),

    # -- Droit constitutionnel belge
    ("senat-constitution", "La Constitution belge — texte coordonné",
     "Sénat de Belgique", "consulté en 2026", "institution",
     "https://www.senate.be/doc/const_fr.html"),
    ("wp-art195", "Article 195 de la Constitution belge — procédure de révision",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://fr.wikipedia.org/wiki/Article_195_de_la_Constitution_belge"),
    ("venise-art195", "Avis sur la révision de la Constitution belge (CDL-AD(2012)010)",
     "Commission de Venise, Conseil de l'Europe", "2012", "institution",
     "https://docs-venice.coe.int/api/Document?pdffile=CDL-AD%282012%29010-f"),
    ("mb-art195-2012", "29 mars 2012 — Révision de l'article 195 de la Constitution",
     "Moniteur belge", "2012", "institution",
     "https://refli.be/fr/lex/2012201995"),
    ("llb-senat-precedent", "« C'est un dangereux précédent » : les conséquences de l'entourloupe utilisée pour supprimer le Sénat",
     "La Libre Belgique", "9 avril 2026", "presse",
     "https://www.lalibre.be/belgique/politique-belge/2026/04/09/cest-un-dangereux-precedent-les-consequences-de-lentourloupe-utilisee-pour-supprimer-le-senat-EPS4QO53BVEBPKNSZG4I4OAY4U/"),
    ("bx1-senat-195", "La Chambre approuve la révision de l'article 195, première étape en vue de la suppression du Sénat",
     "BX1", "2026", "presse",
     "https://bx1.be/categories/news/la-chambre-approuve-la-revision-de-larticle-195-de-la-constitution-premiere-etape-en-vue-de-la-suppression-du-senat/"),
    ("llb-senat-vote", "Suppression du Sénat : un vote incertain jusqu'au bout et de vives tensions",
     "La Libre Belgique", "3 avril 2026", "presse",
     "https://www.lalibre.be/belgique/politique-belge/2026/04/03/suppression-du-senat-un-vote-incertain-jusquau-bout-et-de-vives-tensions-6MPBNVDRPNB4VNJUXOICX62TAQ/"),
    ("surligneurs-195", "Révision de la Constitution : l'article 195, au cœur des débats, c'est quoi ?",
     "Les Surligneurs Belgique", "consulté en 2026", "recherche",
     "https://be.lessurligneurs.eu/revision-de-la-constitution-larticle-195-au-coeur-des-debats-cest-quoi/"),
    ("uclouvain-195", "L'article 195 fixant la procédure de révision de la Constitution — mémoire",
     "UCLouvain (DIAL)", "consulté en 2026", "recherche",
     "https://thesis.dial.uclouvain.be/bitstreams/1a6cab4e-98d3-43b1-9945-b1e2f1b989ed/download"),
    ("ep-etat-de-droit-be", "L'État de droit, une perspective de droit comparé : Belgique (EPRS_STU(2023)745680)",
     "Parlement européen, EPRS", "2023", "institution",
     "https://www.europarl.europa.eu/RegData/etudes/STUD/2023/745680/EPRS_STU(2023)745680_FR.pdf"),
    ("uliege-droit-public", "Éléments de droit public — considérations générales et particularités belges (F. Bouhon)",
     "Université de Liège (ORBi)", "2019", "recherche",
     "https://orbi.uliege.be/bitstream/2268/232623/1/Introduction%20au%20droit%20-%20partim%20droit%20public%20(F.%20BOUHON)%20-%20syllabus%202019%20-%20chapitres%202-3-4-5&7.pdf"),

    # -- Droit international
    ("un-vienne-1983", "Convention de Vienne sur la succession d'États en matière de biens, archives et dettes d'État (8 avril 1983)",
     "Nations unies, Commission du droit international", "1983", "institution",
     "https://legal.un.org/ilc/texts/instruments/english/conventions/3_3_1983.pdf"),
    ("wp-vienne-1983", "Vienna Convention on Succession of States in Respect of State Property, Archives and Debts — état des ratifications",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://en.wikipedia.org/wiki/Vienna_Convention_on_Succession_of_States_in_Respect_of_State_Property,_Archives_and_Debts"),
    ("nus-vienne-1983", "1983 Vienna Convention on the Succession of States in respect of State Property, Archives and Debts",
     "Centre for International Law, National University of Singapore", "consulté en 2026", "recherche",
     "https://cil.nus.edu.sg/databasecil/1983-vienna-convention-on-the-succession-of-states-in-respect-of-state-property-archives-debt"),
    ("consilium-secession", "Separatism in Europe (3) — New states and EU membership",
     "Bibliothèque du Conseil de l'Union européenne", "consulté en 2026", "institution",
     "https://www.consilium.europa.eu/en/documents-publications/library/library-blog/posts/separatism-in-europe-3-new-states-and-eu-membership/"),
    ("eucl-secession", "Secession from a Member State and EU Membership: the View from the Union",
     "European Constitutional Law Review, Cambridge University Press", "2016", "recherche",
     "https://www.cambridge.org/core/journals/european-constitutional-law-review/article/secession-from-a-member-state-and-eu-membership/1587F05B173012C2268E6BFA908888BB"),
    ("tandf-voluntary", "Voluntary association, not state consent: why the EU's approach to secession is flawed",
     "Regional & Federal Studies (Taylor & Francis)", "2023", "recherche",
     "https://www.tandfonline.com/doi/pdf/10.1080/13597566.2023.2225435"),
    ("travers-tchecoslovaquie", "The Dissolution of Czechoslovakia — are there any lessons for Brexit?",
     "Travers Smith", "consulté en 2026", "recherche",
     "https://www.traverssmith.com/knowledge/knowledge-container/the-dissolution-of-czechoslovakia-are-there-any-lessons-for-brexit/"),
    ("wp-tchecoslovaquie", "Dissolution of Czechoslovakia — notice encyclopédique",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://en.wikipedia.org/wiki/Dissolution_of_Czechoslovakia"),
    ("radio-prague-divorce", "« It was falling apart by itself » — Czechoslovakia's Velvet Divorce",
     "Radio Prague International", "consulté en 2026", "presse",
     "https://english.radio.cz/it-was-falling-apart-itself-czechoslovakias-velvet-divorce-8771087"),

    # -- Bruxelles, frontière, territoire
    ("bx1-francophones", "91,8 % de francophones à Bruxelles ? Pourquoi ce chiffre doit être nuancé",
     "BX1", "consulté en 2026", "presse",
     "https://bx1.be/dossiers/dossiers-redaction/918-de-francophones-a-bruxelles-pourquoi-ce-chiffre-doit-etre-nuance/"),
    ("ibsa-population", "Population — statistiques de la Région de Bruxelles-Capitale",
     "IBSA (Institut bruxellois de statistique et d'analyse)", "consulté en 2026", "institution",
     "https://ibsa.brussels/themes/population"),
    ("brussels-studies-confed", "Le statut de Bruxelles dans l'hypothèse du confédéralisme",
     "Brussels Studies", "consulté en 2026", "recherche",
     "https://journals.openedition.org/brussels/469?lang=en"),
    ("cairn-bxl-impasses", "Bruxelles-Capitale : cinq impasses, une issue",
     "Outre-Terre (Cairn)", "2014", "recherche",
     "https://shs.cairn.info/revue-outre-terre2-2014-3-page-229?lang=fr"),
    ("cairn-brussels-dc", "Brussels, DC : le rêve américain ?",
     "Outre-Terre (Cairn)", "2014", "recherche",
     "https://www.cairn.info/revue-outre-terre2-2014-3-page-321.htm"),
    ("wp-facilites", "Facilités linguistiques en Belgique — communes, lois de 1962-1963, circulaire Peeters",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://fr.wikipedia.org/wiki/Facilit%C3%A9s_linguistiques_en_Belgique"),
    ("wallonie-facilites", "Le régime des facilités linguistiques (1963)",
     "Connaître la Wallonie, Service public de Wallonie", "consulté en 2026", "institution",
     "https://connaitrelawallonie.wallonie.be/histoire-et-symboles/histoire/atlas-historique/le-regime-des-facilites-linguistiques-1963"),
    ("axl-loi1962", "Belgique : loi du 8 novembre 1962 modifiant les limites des provinces, arrondissements et communes",
     "Université Laval, TLFQ", "consulté en 2026", "recherche",
     "https://www.axl.cefan.ulaval.ca/europe/belgiqueetat-loi1962.htm"),
    ("axl-demolinguistique", "Belgique : données démolinguistiques",
     "Université Laval, TLFQ", "consulté en 2026", "recherche",
     "https://www.axl.cefan.ulaval.ca/europe/belgiqueetat_demo.htm"),
    ("diplomatie-oi", "49 organisations internationales en Belgique",
     "SPF Affaires étrangères, Commerce extérieur et Coopération au développement", "avril 2022", "institution",
     "https://diplomatie.belgium.be/fr/politique/themes-politiques/sous-la-loupe/chiffre-davril-2022-49-organisations-internationales-en"),
    ("tle-sieges", "Bruxelles, Luxembourg, Strasbourg : où siègent les institutions européennes ?",
     "Toute l'Europe", "consulté en 2026", "recherche",
     "https://www.touteleurope.eu/fonctionnement-de-l-ue/bruxelles-luxembourg-strasbourg-ou-siegent-les-institutions-europeennes/"),
    ("nato-siege", "Siège de l'OTAN",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://fr.wikipedia.org/wiki/Si%C3%A8ge_de_l'OTAN"),

    # -- Argent
    ("rtbf-transferts", "Transferts financiers Nord-Sud, la décrue ?",
     "RTBF", "2017, mis à jour en 2025", "presse",
     "https://www.rtbf.be/article/transferts-financiers-nord-sud-la-decrue-9654790"),
    ("bplus-transferts", "Le mythe des transferts financiers démasqué",
     "B Plus", "consulté en 2026", "organisation",
     "https://bplus.be/fr/articles/mythes-separatistes/le-mythe-des-transferts-financiers-demasque"),
    ("vbb-transferts", "Transferts financiers de la Flandre vers la Wallonie et Bruxelles",
     "Vlaams Belang Bruxelles", "consulté en 2026", "parti",
     "https://vlaamsbelangbruxelles.be/transferts-financiers-de-la-flandre-vers-la-wallonie-et-bruxelles/"),
    ("bx1-transferts-bxl", "Les transferts bruxellois vers la Wallonie sont de 1,3 milliard",
     "BX1", "consulté en 2026", "presse",
     "https://bx1.be/news/les-transferts-bruxellois-vers-la-wallonie/"),
    ("crisp-financement", "Financement des Communautés et des Régions — mécanisme de transition",
     "CRISP, Vocabulaire politique", "consulté en 2026", "recherche",
     "https://www.vocabulairepolitique.be/financement-des-communautes-et-des-regions/"),
    ("bam-lsf", "La bombe à retardement sous les finances de Bruxelles et de la Wallonie : la loi spéciale de financement",
     "Business AM", "consulté en 2026", "presse",
     "https://fr.businessam.be/la-bombe-a-retardement-sous-les-finances-de-bruxelles-et-de-la-wallonie-la-loi-speciale-de-financement-menace-de-faire-eclater-les-entites-federees-et-constitue-un-levier-important-pour-les-disc/"),
    ("daardaar-lsf", "La loi spéciale de financement : un levier de négociation flamand qui déstabilise la Wallonie",
     "DaarDaar", "consulté en 2026", "presse",
     "https://daardaar.be/rubriques/politique/la-loi-speciale-de-financement-un-levier-de-negociation-flamand-qui-destabilise-la-wallonie/"),
    ("wallex-lsf", "Loi spéciale du 16 janvier 1989 relative au financement des Communautés et des Régions (texte coordonné)",
     "Wallex, Service public de Wallonie", "consulté en 2026", "institution",
     "https://wallex.wallonie.be/contents/acts/8/8367/1.html?doc=3123&rev=2457-38"),
    ("rtbf-moodys", "Moody's dégrade la note financière de la Belgique et la prive de son « double A »",
     "RTBF", "17 avril 2026", "presse",
     "https://www.rtbf.be/article/moody-s-degrade-la-note-financiere-de-la-belgique-et-la-prive-de-son-double-a-11711602"),
    ("llb-moodys", "La Belgique rétrogradée par Moody's, symptôme d'une dérive budgétaire persistante",
     "La Libre Belgique", "17 avril 2026", "presse",
     "https://www.lalibre.be/belgique/politique-belge/2026/04/17/la-belgique-retrogradee-par-moodys-symptome-dune-derive-budgetaire-persistante-WROVLE4MVBD37CHHCEFVHKGIMM/"),
    ("lpost-moodys", "Moody's dégrade la note de la Belgique pour cause de dérapage budgétaire",
     "L-Post", "18 avril 2026", "presse",
     "https://lpost.be/2026/04/18/moodys-degrade-la-note-de-la-belgique-pour-cause-de-derapage-budgetaire/"),
    ("tresor-fr-belgique", "Situation économique et financière de la Belgique",
     "Direction générale du Trésor, France", "consulté en 2026", "institution",
     "https://www.tresor.economie.gouv.fr/Pays/BE/situation-economique-et-financiere-de-la-belgique"),
    ("avenir-conclave", "10 milliards d'euros d'économie ou de nouvelles élections : le gouvernement fédéral face à un conclave décisif",
     "L'Avenir", "1er septembre 2026", "presse",
     "https://www.lavenir.net/actu/belgique/politique/2026/09/01/10-milliards-deuros-deconomie-ou-de-nouvelles-elections-le-gouvernement-federal-face-a-un-conclave-decisif-HEXFQ3SKNFD57G67JA57ZYMKVE/"),
    ("rtbf-boule-de-neige", "Budget fédéral : le gouvernement au pied du mur pour éviter la « catastrophe » de l'effet boule de neige",
     "RTBF", "2026", "presse",
     "https://www.rtbf.be/article/budget-federal-le-gouvernement-au-pied-du-mur-pour-eviter-la-catastrophe-de-l-effet-boule-de-neige-11778462"),
    ("llb-diete", "Pourquoi l'Arizona doit à nouveau mettre l'État à la diète",
     "La Libre Belgique", "1er septembre 2026", "presse",
     "https://www.lalibre.be/belgique/2026/09/01/pourquoi-larizona-doit-a-nouveau-mettre-letat-a-la-diete-3YWEDLPITJFANNVSRC7MZRYTAQ/"),
    ("feb-secu", "Le déficit de la sécurité sociale continue de se creuser, passant de 6,2 à 7,6 milliards d'euros",
     "Fédération des entreprises de Belgique (FEB)", "consulté en 2026", "organisation",
     "https://www.vbo-feb.be/fr/communiques-de-presse/le-deficit-de-la-securite-sociale-continue-de-se-creuser-de-maniere-insoutenable-passant-de-62-a-76-milliards-eur/"),
    ("bfp-vieillissement", "Perspectives financières de la sécurité sociale : vieillissement et viabilité du système légal de pensions",
     "Bureau fédéral du Plan", "consulté en 2026", "institution",
     "https://www.plan.be/en/publications/perspectives-financieres-de-la-securite-sociale-en"),
    ("spf-secu-apercu", "Aperçu de la sécurité sociale en Belgique",
     "SPF Sécurité sociale", "consulté en 2026", "institution",
     "https://socialsecurity.belgium.be/fr/publications/apercu-de-la-securite-sociale-en-belgique"),

    # -- Partis et projets institutionnels
    ("vrt-nva-confed", "La N-VA donne sa définition du confédéralisme",
     "VRT NWS", "30 octobre 2013", "presse",
     "https://www.vrt.be/vrtnws/fr/2013/10/30/la_n-va_donne_sadefinitionduconfederalisme-1-1766676/"),
    ("llb-confed-clarte", "« Le confédéralisme de la N-VA est d'une clarté totale »",
     "La Libre Belgique", "30 mai 2023", "presse",
     "https://www.lalibre.be/belgique/politique-belge/2023/05/30/le-confederalisme-de-la-n-va-est-dune-clarte-totale-je-felicite-bart-de-wever-TBR6XBDHJ5AMFAAV7C5Z5OIWVA/"),
    ("avenir-confed-tait", "Accord de gouvernement : Bart De Wever amorce un virage vers ce confédéralisme dont l'Arizona tait le nom",
     "L'Avenir", "3 février 2025", "presse",
     "https://www.lavenir.net/actu/belgique/politique/2025/02/03/vers-ce-confederalisme-dont-larizona-tait-le-nom-IV7HUXWRY5G57IZCXPM3OLH6PY/"),
    ("bx1-comite-concertation", "Réforme du Comité de concertation : « derrière ce projet de Bart De Wever, il y a un objectif confédéral »",
     "BX1", "consulté en 2026", "presse",
     "https://bx1.be/dossiers/bonsoir-bruxelles/reforme-du-comite-de-concertation-derriere-ce-projet-de-bart-de-wever-il-y-a-un-objectif-confederal/"),
    ("vrt-vb-feuille", "Le Vlaams Belang lance une feuille de route pour l'indépendance de la Flandre",
     "VRT NWS", "12 juin 2023", "presse",
     "https://www.vrt.be/vrtnws/fr/2023/06/12/le-vlaams-belang-lance-une-feuille-de-route-pour-lindependance-d/"),
    ("rtbf-vb-elan", "Pour le Vlaams Belang, l'élan pour l'indépendance de la Flandre sera lancé après le scrutin",
     "RTBF", "2024", "presse",
     "https://www.rtbf.be/article/elections-2024-pour-le-vlaams-belang-l-elan-pour-l-independance-de-la-flandre-sera-lance-apres-le-scrutin-11211661"),
    ("vb-programme", "Programme du Vlaams Belang",
     "Vlaams Belang", "consulté en 2026", "parti",
     "https://www.vlaamsbelang.org/programma"),
    ("crisp-resolutions", "Les résolutions du Parlement flamand pour une réforme de l'État",
     "CRISP, Courrier hebdomadaire", "2000", "recherche",
     "https://www.crisp.be/librairie/catalogue/1370-resolutions-Parlement-flamand-pour-une-reforme-letat.html"),
    ("llb-resolutions-2020", "La présidente du Parlement flamand veut redonner vie à cinq résolutions flamandes pour plus d'autonomie",
     "La Libre Belgique", "11 juillet 2020", "presse",
     "https://www.lalibre.be/belgique/politique-belge/2020/07/11/la-presidente-du-parlement-flamand-veut-redonner-vie-a-cinq-resolutions-flamandes-pour-plus-dautonomie-2MTF733F5ZERTD22ZGRXN3NTYY/"),
    ("rtbf-implosion", "« La Belgique peut disparaître par implosion »",
     "RTBF", "2019", "presse",
     "https://www.rtbf.be/article/la-belgique-peut-disparaitre-par-implosion-10240352"),
    ("chambre-kieskring", "Proposition de loi instaurant une circonscription électorale fédérale (DOC 53 3446/001)",
     "Chambre des représentants", "2014", "parlement",
     "https://www.dekamer.be/FLWB/PDF/53/3446/53K3446001.pdf"),
    ("cairn-circonscription", "Une idée qui fait son chemin : historique de la proposition de circonscription fédérale en Belgique",
     "Outre-Terre (Cairn)", "2014", "recherche",
     "https://www.cairn.info/revue-outre-terre2-2014-3-page-262.htm"),
    ("crisp-circonscription", "La circonscription électorale fédérale",
     "CRISP, Courrier hebdomadaire n° 2142", "consulté en 2026", "recherche",
     "https://shs.cairn.info/article/CRIS_2142_0005?lang=fr&ID_ARTICLE=CRIS_2142_0005"),
    ("dh-sinardet", "« Une circonscription fédérale profiterait d'abord à la démocratie » — Dave Sinardet (VUB)",
     "La DH", "18 avril 2023", "presse",
     "https://www.dhnet.be/actu/belgique/2023/04/18/une-circonscription-federale-profiterait-dabord-a-la-democratie-analyse-dave-sinardet-professeur-de-science-politique-vub-DYPSLQQTEFACVJKRMPWNULYA6U/"),
    ("crisp-identites", "Identités et préférences des parlementaires envers le fédéralisme belge à l'aube d'une septième réforme de l'État",
     "CRISP, Courrier hebdomadaire", "2022", "recherche",
     "https://shs.cairn.info/revue-courrier-hebdomadaire-du-crisp-2022-7-page-5?lang=fr"),
    ("cairn-tombe", "Le fédéralisme belge creuse-t-il sa propre tombe ?",
     "Outre-Terre (Cairn)", "2014", "recherche",
     "https://shs.cairn.info/revue-outre-terre2-2014-3-page-45?lang=fr"),
    ("cairn-consociatif", "Le fédéralisme consociatif belge : vecteur d'instabilité ?",
     "Pouvoirs (Cairn)", "2011", "recherche",
     "https://droit.cairn.info/revue-pouvoirs-2011-1-page-21?lang=fr"),
    ("cairn-croisee", "La Belgique à la croisée des chemins : entre fédéralisme et confédéralisme",
     "Outre-Terre (Cairn)", "2014", "recherche",
     "https://shs.cairn.info/revue-outre-terre2-2014-3-page-251?lang=fr"),
    ("destatte-confed", "Le confédéralisme, spectre institutionnel — une Flandre inachevée (1995-2020)",
     "Philippe Destatte, PhD2050", "15 décembre 2019", "recherche",
     "https://phd2050.org/2019/12/15/spectre-inst-4/"),
    ("crisp-5e-reforme", "Cinquième réforme de l'État",
     "CRISP, Vocabulaire politique", "consulté en 2026", "recherche",
     "https://www.vocabulairepolitique.be/cinquieme-reforme-de-letat/"),

    # -- Élections et gouvernement
    ("chambre-resultats-2024", "Résultats des élections fédérales du 9 juin 2024",
     "Chambre des représentants", "2024", "parlement",
     "https://www.lachambre.be/pdf_sections/pri/fiche/fr_09_02.pdf"),
    ("rtbf-resultats-2024", "Résultats des élections 2024 — Parlement fédéral",
     "RTBF", "2024", "presse",
     "https://www.rtbf.be/elections-2024/resultats/federal"),
    ("wp-dewever-gouv", "De Wever government — composition et calendrier de formation",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://en.wikipedia.org/wiki/De_Wever_government"),
    ("schuman-2024", "Les Belges ont fait mentir les sondages — analyse des élections de juin 2024",
     "Fondation Robert Schuman", "2024", "recherche",
     "https://www.robert-schuman.eu/observatoire/6210-les-belges-ont-fait-mentir-les-sondages-la-nouvelle-alliance-flamande-est-victorieuse-en-flandre-et-le-mouvement-reformateur-s-impose-en-wallonie-et-a-bruxelles"),
    ("llb-un-an-arizona", "Un an d'Arizona. Mais quel projet pour la Belgique ?",
     "La Libre Belgique", "9 février 2026", "presse",
     "https://www.lalibre.be/debats/opinions/2026/02/09/un-an-darizona-mais-quel-projet-pour-la-belgique-RELIJWO5FRBFPBSRWG3VQTH4EE/"),

    # -- Jurisprudence de la sécession
    ("cij-kosovo-resume", "Résumé de l'avis consultatif du 22 juillet 2010 sur la déclaration d'indépendance du Kosovo",
     "Cour internationale de justice", "22 juillet 2010", "juridiction",
     "https://www.icj-cij.org/node/103912"),
    ("cij-kosovo-affaire", "Conformité au droit international de la déclaration unilatérale d'indépendance relative au Kosovo — affaire n° 141",
     "Cour internationale de justice", "2010", "juridiction",
     "https://www.icj-cij.org/case/141"),
    ("csc-quebec", "Renvoi relatif à la sécession du Québec, [1998] 2 R.C.S. 217",
     "Cour suprême du Canada", "20 août 1998", "juridiction",
     "https://decisions.scc-csc.ca/scc-csc/scc-csc/fr/1643/1/document.do"),
    ("juricaf-quebec", "Renvoi relatif à la sécession du Québec — texte intégral",
     "Juricaf", "1998", "juridiction",
     "https://juricaf.org/arret/CANADA-COURSUPREME-19980820-19982RCS217"),
    ("wp-quebec-renvoi", "Renvoi relatif à la sécession du Québec — notice encyclopédique",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://fr.wikipedia.org/wiki/Renvoi_relatif_%C3%A0_la_s%C3%A9cession_du_Qu%C3%A9bec"),
    ("nilr-kosovo", "The ICJ's Advisory Opinion on Kosovo's Declaration of Independence: a missed opportunity?",
     "Netherlands International Law Review, Cambridge University Press", "2011", "recherche",
     "https://www.cambridge.org/core/journals/netherlands-international-law-review/article/abs/icjs-advisory-opinion-on-kosovos-declaration-of-independence-a-missed-opportunity-international-court-of-justice-accordance-with-international-law-of-the-unilateral-declaration-of-independence-in-respect-of-kosovo-advisory-opinion-of-22-july-2010/D96FADAE5EA808F4D1E5D6F6E032D3DA"),
    ("llb-bnb-flux", "Une étude inédite démontre que Bruxelles finance massivement les autres Régions",
     "La Libre Belgique, sur l'étude de la Banque nationale de Belgique", "23 octobre 2025", "presse",
     "https://www.lalibre.be/belgique/2025/10/23/bruxelles-finance-massivement-les-autres-regions-YS4M7IJASFDVPNAU7ITR4TY5SM/"),
    ("ibsa-cahier15", "La géographie de la création de richesse en Belgique — Cahier de l'IBSA n° 15",
     "IBSA, Région de Bruxelles-Capitale", "consulté en 2026", "institution",
     "https://ibsa.brussels/sites/default/files/publication/documents/Cahier_15_FR.pdf"),
    ("ibsa-economie", "Économie — statistiques de la Région de Bruxelles-Capitale",
     "IBSA, Région de Bruxelles-Capitale", "consulté en 2026", "institution",
     "https://ibsa.brussels/themes/economie"),
    ("rtbf-pib-bxl", "Bruxelles-Capitale dans le top quatre des régions européennes en matière de PIB par habitant",
     "RTBF", "consulté en 2026", "presse",
     "https://www.rtbf.be/article/bruxelles-capitale-dans-le-top-quatre-des-regions-europeennes-en-matiere-de-pib-par-habitant-10448518"),
    ("debtagency", "Plan de financement de l'État fédéral",
     "Agence fédérale de la dette", "consulté en 2026", "institution",
     "https://www.debtagency.be/fr/chiffre/etat-federal/datafederalstatefinancingplan"),
    ("bfp-perspectives", "Perspectives économiques 2026-2031 — communiqué de presse du 12 février 2026",
     "Bureau fédéral du Plan", "12 février 2026", "institution",
     "https://www.plan.be/sites/default/files/documents/PRESS_20260212_FR.pdf"),
    ("statbel-population", "Structure de la population",
     "Statbel, Office belge de statistique", "consulté en 2026", "institution",
     "https://statbel.fgov.be/fr/themes/population/structure-de-la-population"),
    ("rtbf-population-2026", "La Belgique comptait 11,8 millions d'habitants au 1er janvier 2026",
     "RTBF, d'après Statbel", "2026", "presse",
     "https://www.rtbf.be/article/la-belgique-comptait-11-8-millions-d-habitants-au-1er-janvier-2026-un-nombre-legerement-en-hausse-11738209"),
    ("wp-art54", "Article 54 de la Constitution belge — la sonnette d'alarme",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://fr.wikipedia.org/wiki/Article_54_de_la_Constitution_belge"),
    ("crisp-sonnette", "Sonnette d'alarme",
     "CRISP, Vocabulaire politique", "consulté en 2026", "recherche",
     "https://www.vocabulairepolitique.be/sonnette-d-alarme/"),
    ("wp-montenegro", "Référendum d'indépendance du Monténégro de 2006 — seuil de 55 % et résultat",
     "Wikipédia", "consulté en 2026", "recherche",
     "https://en.wikipedia.org/wiki/2006_Montenegrin_independence_referendum"),
    ("coe-montenegro", "Observation du référendum sur le statut d'État de la République du Monténégro, 21 mai 2006",
     "Assemblée parlementaire du Conseil de l'Europe", "2006", "institution",
     "https://assembly.coe.int/nw/xml/XRef/X2H-Xref-ViewHTML.asp?FileID=11276&lang=en"),
]


# ---------------------------------------------------------------------------
# LEXIQUE
# ---------------------------------------------------------------------------

LEXIQUE = [
    ("alarme", "Sonnette d'alarme",
     "Procédure de l'article 54 de la Constitution : une motion signée par les trois quarts d'un groupe "
     "linguistique de la Chambre ou du Sénat suspend l'examen d'un texte réputé porter atteinte gravement "
     "aux relations entre communautés, et renvoie l'affaire au Conseil des ministres, paritaire. Elle "
     "n'annule pas le texte : elle interrompt le temps parlementaire ((wp-art54)) ((crisp-sonnette)).",
     ["veto"]),
    ("bhv", "BHV (Bruxelles-Hal-Vilvorde)",
     "Ancienne circonscription électorale et arrondissement judiciaire à cheval sur la Région bruxelloise "
     "et sur trente-cinq communes flamandes du Brabant. Scindée en 2012 au terme de la crise de 541 jours. "
     "L'affaire résume la question territoriale belge : une frontière linguistique fixe traversée par des "
     "flux de population qui ne le sont pas.",
     ["frontiere", "facilites"]),
    ("condominium", "Condominium",
     "Régime par lequel deux ou plusieurs États exercent conjointement la souveraineté sur un même "
     "territoire. Formule régulièrement proposée pour Bruxelles en cas de séparation. Les précédents "
     "historiques (Nouvelles-Hébrides, Andorre avant 1993) sont peu nombreux et rarement heureux.",
     ["citeetat"]),
    ("confederalisme", "Confédéralisme",
     "Régime dans lequel les entités constituantes sont souveraines et délèguent, par traité, l'exercice "
     "de compétences limitées à un organe commun. En droit, un confédéralisme réel implique la disparition "
     "de l'État fédéral belge et sa reconstitution par accord entre entités. Le terme est employé en "
     "politique belge pour désigner des degrés très variables de dissociation.",
     ["dissociation", "federalisme"]),
    ("citeetat", "Cité-État",
     "Statut d'un territoire urbain constitué en État souverain ou en entité fédérée de plein exercice. "
     "Proposé pour Bruxelles, seul ou sous garantie internationale, comme troisième voie entre le "
     "rattachement à la Flandre et le rattachement à la Wallonie.",
     ["condominium"]),
    ("dissociation", "Fédéralisme de dissociation",
     "Fédéralisme obtenu en démembrant un État unitaire, par opposition au fédéralisme d'agrégation qui "
     "réunit des entités préexistantes. La logique de dissociation ne connaît pas de terme naturel : chaque "
     "réforme légitime la suivante, sans qu'aucun mécanisme ne prévoie un point d'arrêt.",
     ["confederalisme", "refederalisation"]),
    ("facilites", "Communes à facilités",
     "Communes où un régime linguistique dérogatoire permet aux habitants d'obtenir certains services dans "
     "une autre langue que celle de la région. Instituées par les lois de 1962 et 1963, elles concernent "
     "une trentaine de communes, dont les six de la périphérie bruxelloise. Leur portée fait l'objet d'un "
     "conflit d'interprétation permanent.",
     ["frontiere", "peripherie"]),
    ("federalisme", "Fédéralisme",
     "Régime où la souveraineté est partagée entre un État fédéral et des entités fédérées, chacun agissant "
     "directement sur les citoyens dans sa sphère. La Belgique est un État fédéral depuis 1993 (article 1er "
     "de la Constitution).",
     ["confederalisme"]),
    ("frontiere", "Frontière linguistique",
     "Ligne fixée par la loi du 8 novembre 1962 et complétée par celle du 2 août 1963. Elle a rendu "
     "immuables les limites des régions linguistiques et supprimé le volet linguistique du recensement. "
     "Ce gel est la condition de possibilité de tout le reste : sans frontière fixe, pas d'entités "
     "territoriales à séparer.",
     ["facilites", "bhv"]),
    ("lsf", "Loi spéciale de financement",
     "Loi spéciale du 16 janvier 1989, profondément révisée en 2014, qui organise le financement des "
     "Communautés et des Régions. Elle contient un mécanisme de transition destiné à amortir les pertes "
     "de la sixième réforme : constant de 2015 à 2024, réduit de 10 % par an depuis 2025, éteint en 2034.",
     ["transition", "transferts"]),
    ("peripherie", "Périphérie bruxelloise",
     "Ensemble de communes flamandes entourant la Région bruxelloise, dont six disposent de facilités pour "
     "les francophones : Kraainem, Drogenbos, Linkebeek, Rhode-Saint-Genèse, Wemmel et Wezembeek-Oppem. "
     "Zone où la question territoriale est la plus dense.",
     ["facilites", "bhv"]),
    ("refederalisation", "Refédéralisation",
     "Transfert de compétences des entités fédérées vers l'État fédéral. Mouvement inverse de celui des six "
     "réformes de l'État. Aucune n'a jamais été opérée à grande échelle ; la crise sanitaire de 2020 a "
     "relancé le débat sans le trancher.",
     ["dissociation"]),
    ("responsabilisation", "Responsabilisation",
     "Mécanismes prévus par la loi spéciale de financement pour faire supporter aux entités fédérées le "
     "coût de leurs performances en matière fiscale, climatique et de pensions. Aucun n'a été activé à ce "
     "jour, ce qui prive le système de son ressort correcteur.",
     ["lsf"]),
    ("succession", "Succession d'États",
     "Branche du droit international qui règle le sort des traités, des biens, des archives et des dettes "
     "lorsqu'un État se substitue à un autre sur un territoire. La Convention de Vienne de 1983, qui "
     "codifie la matière des biens et des dettes, n'est jamais entrée en vigueur.",
     ["vienne"]),
    ("transition", "Mécanisme de transition",
     "Dotation instituée par la sixième réforme de l'État pour neutraliser les gagnants et les perdants du "
     "nouveau modèle de financement. Pour la Région wallonne, 620,5 millions d'euros par an de 2015 à 2024, "
     "puis une réduction de 10 % par an jusqu'à extinction en 2034. Falaise budgétaire programmée et jamais "
     "renégociée.",
     ["lsf"]),
    ("transferts", "Transferts interrégionaux",
     "Écart entre ce qu'une région verse au budget fédéral et de sécurité sociale et ce qu'elle en reçoit. "
     "Les estimations académiques les situent entre 6 et 7 milliards d'euros par an du nord vers le sud, "
     "soit environ 2,5 % du PIB belge. La notion est un artefact comptable : elle mesure une solidarité "
     "interpersonnelle en la ventilant par territoire.",
     ["lsf"]),
    ("udi", "Déclaration unilatérale d'indépendance",
     "Acte par lequel une entité proclame sa souveraineté sans l'accord de l'État dont elle relève. Le droit "
     "international ne l'interdit ni ne la garantit : l'avis consultatif de la Cour internationale de justice "
     "du 22 juillet 2010 sur le Kosovo constate seulement qu'une telle déclaration ne viole pas, en soi, le "
     "droit international général.",
     ["succession", "secession"]),
    ("secession", "Sécession",
     "Séparation d'une partie du territoire d'un État pour former un nouvel État ou rejoindre un État tiers. "
     "Hors situation coloniale ou d'oppression extrême, le droit international ne reconnaît pas de droit à "
     "la sécession unilatérale — position retenue par la Cour suprême du Canada dans son renvoi de 1998 sur "
     "le Québec.",
     ["udi", "succession"]),
    ("veto", "Vétocratie",
     "Système dans lequel le nombre d'acteurs disposant d'un pouvoir de blocage rend l'action collective "
     "improbable. En Belgique : parité au Conseil des ministres, majorités spéciales, sonnette d'alarme, "
     "coalitions à cinq ou sept partis, neuf exécutifs.",
     ["alarme"]),
    ("vienne", "Convention de Vienne de 1983",
     "Convention sur la succession d'États en matière de biens, archives et dettes d'État, adoptée le "
     "8 avril 1983. Elle pose la règle de la « proportion équitable » pour la répartition de la dette. "
     "Elle n'est jamais entrée en vigueur, faute des quinze ratifications requises.",
     ["succession"]),
    ("art195", "Article 195",
     "Article de la Constitution qui organise sa révision : déclaration de révision par la Chambre, le Sénat "
     "et le Roi, dissolution automatique des chambres, puis vote à la majorité des deux tiers avec quorum "
     "des deux tiers. La Commission de Venise le range parmi les procédures les plus rigides au monde.",
     ["veto"]),
    ("arizona", "Arizona",
     "Nom donné à la coalition fédérale formée par la N-VA, le MR, Les Engagés, Vooruit et le CD&V, "
     "assermentée le 3 février 2025 sous la conduite de Bart De Wever, premier nationaliste flamand à "
     "diriger un gouvernement belge.",
     []),
    ("consociatif", "Démocratie consociative",
     "Modèle décrit par Arend Lijphart : dans une société profondément segmentée, la stabilité repose sur "
     "la coopération des élites au moyen de grandes coalitions, de la proportionnalité, de l'autonomie "
     "segmentaire et du veto mutuel. La Belgique en est le cas d'école — et le cas limite.",
     ["veto", "alarme"]),
]

# ---------------------------------------------------------------------------
# CHRONOLOGIE
# ---------------------------------------------------------------------------

CHRONO = [
    ("1830", "Indépendance de la Belgique",
     "Le Gouvernement provisoire proclame l'indépendance le 4 octobre. Le Congrès national adopte la "
     "Constitution le 7 février 1831. L'État est unitaire, la langue officielle est le français.",
     ["senat-constitution"]),
    ("1912", "La lettre au Roi de Jules Destrée",
     "« Sire, il n'y a pas de Belges. » Le socialiste wallon plaide pour une séparation administrative. "
     "La première formulation politique d'une division du pays vient du sud, non du nord.",
     ["wp-scission"]),
    ("1962-1963", "Fixation de la frontière linguistique",
     "Les lois du 8 novembre 1962 et du 2 août 1963 figent les limites des régions linguistiques, "
     "instituent les communes à facilités et suppriment le volet linguistique du recensement.",
     ["axl-loi1962", "wallonie-facilites"]),
    ("1970", "Première réforme de l'État",
     "Création des communautés culturelles et reconnaissance du principe des régions. Introduction de la "
     "parité au Conseil des ministres, des lois à majorité spéciale et de la sonnette d'alarme.",
     ["crisp-5e-reforme"]),
    ("1980 · 1988-1989 · 1993", "Deuxième, troisième et quatrième réformes",
     "Institution des régions, régionalisation de l'enseignement et transfert de compétences majeures. "
     "En 1993, l'article 1er dispose que « la Belgique est un État fédéral qui se compose des communautés "
     "et des régions ».",
     ["senat-constitution", "crisp-5e-reforme"]),
    ("3 mars 1999", "Les cinq résolutions du Parlement flamand",
     "Le Parlement flamand adopte cinq résolutions demandant une autonomie fiscale élargie, la scission "
     "des soins de santé et des allocations familiales, et une refonte du financement. Elles servent de "
     "programme de fond au flamingantisme institutionnel depuis lors.",
     ["crisp-resolutions", "rtbf-implosion"]),
    ("2001", "Cinquième réforme de l'État (Lambermont et Lombard)",
     "Régionalisation de l'agriculture, du commerce extérieur et des lois communale et provinciale. "
     "Refinancement des communautés et garanties pour les néerlandophones de Bruxelles.",
     ["crisp-5e-reforme"]),
    ("13 décembre 2006", "Bye Bye Belgium",
     "À 20 h 21, la RTBF interrompt sa grille pour annoncer la déclaration unilatérale d'indépendance de "
     "la Flandre. La fiction dure jusqu'à 22 h. Pic d'audience à 20 h 53 : 674 275 téléspectateurs, "
     "35,57 % de part de marché. 31 368 appels et 21 338 SMS.",
     ["wp-bbb", "rtbf-bbb-electrochoc"]),
    ("juillet 2007", "Avertissement du CSA",
     "Le Collège d'autorisation et de contrôle du Conseil supérieur de l'audiovisuel adresse un "
     "avertissement à la RTBF pour n'avoir pas pris les mesures nécessaires afin d'éviter la confusion "
     "des téléspectateurs. Trente-huit plaintes avaient été déposées.",
     ["wp-bbb", "rtbf-bbb-electrochoc"]),
    ("2007-2011", "Les crises de formation",
     "284 jours pour former le gouvernement Leterme I après le scrutin de 2007 ; 541 jours après celui de "
     "2010. La question communautaire s'impose comme facteur premier d'instabilité gouvernementale.",
     ["schuman-2024"]),
    ("22 juillet 2010", "Avis de la Cour internationale de justice sur le Kosovo",
     "La Cour constate que la déclaration unilatérale d'indépendance du 17 février 2008 n'a pas violé le "
     "droit international général. Elle ne se prononce pas sur l'existence d'un droit à la sécession.",
     ["consilium-secession"]),
    ("29 mars 2012", "Révision de l'article 195",
     "Une disposition transitoire est insérée dans l'article 195 pour ouvrir à la révision des articles "
     "non déclarés. La Commission de Venise rend un avis critique. Le procédé permet la sixième réforme "
     "de l'État — et fait précédent.",
     ["mb-art195-2012", "venise-art195"]),
    ("2012-2014", "Sixième réforme de l'État",
     "Scission de BHV, transfert des allocations familiales et de pans de la santé et de l'emploi, "
     "nouvelle loi spéciale de financement avec un mécanisme de transition constant jusqu'en 2024.",
     ["crisp-financement", "wallex-lsf"]),
    ("2015-2024", "Le mécanisme de transition, phase constante",
     "620,5 millions d'euros par an pour la seule Région wallonne, sans indexation. La dotation compense "
     "les effets de la nouvelle loi de financement.",
     ["crisp-financement"]),
    ("9 juin 2024", "Élections fédérales",
     "La N-VA arrive en tête avec 16,71 % et 24 sièges ; le Vlaams Belang obtient 13,77 % et 20 sièges. "
     "Les deux formations nationalistes flamandes totalisent 44 des 150 sièges de la Chambre.",
     ["chambre-resultats-2024"]),
    ("13 octobre 2024", "Communales sans vote obligatoire en Flandre",
     "Première application de l'abolition du vote obligatoire au niveau local en Flandre. La participation "
     "tombe à 63,5 %, contre 92,6 % en 2018.",
     ["rtbf-resultats-2024"]),
    ("3 février 2025", "Le gouvernement De Wever",
     "Bart De Wever devient le premier nationaliste flamand à diriger un gouvernement belge, à la tête "
     "d'une coalition N-VA, MR, Les Engagés, Vooruit et CD&V. L'accord ne comporte pas de réforme de "
     "l'État, mais une révision du Comité de concertation.",
     ["wp-dewever-gouv", "avenir-confed-tait"]),
    ("juin 2025", "Fitch retire le double A",
     "L'agence dégrade la note souveraine de la Belgique, ouvrant la séquence de révision des notations.",
     ["rtbf-moodys"]),
    ("14 février 2026", "Fin de la crise bruxelloise",
     "Le gouvernement Dilliès prête serment après vingt mois de négociations ; le Parlement bruxellois lui "
     "accorde sa confiance le 27 février.",
     ["llb-un-an-arizona"]),
    ("mars-avril 2026", "L'Enquête nationale 2026",
     "5 354 répondants dans les trois régions, du 9 mars au 5 avril. La réforme de l'État ne figure dans "
     "aucun des cinq premiers problèmes cités, dans aucune région.",
     ["dsen26-rapport", "rtbf-dsen26-cliches"]),
    ("3 avril 2026", "Le Sénat vote sa propre suppression",
     "Le Sénat adopte à la majorité des deux tiers la révision de l'article 195, première des douze étapes "
     "nécessaires. Le procédé de 2012, alors dénoncé par la N-VA, est réemployé.",
     ["llb-senat-vote", "llb-senat-precedent"]),
    ("9 avril 2026", "Constat de précédent constitutionnel",
     "Les constitutionnalistes Marc Verdussen (UCLouvain) et Anne-Emmanuelle Bourgaux (UMons) qualifient "
     "publiquement la manœuvre de dangereux précédent : « cela malmène la Constitution tout en la "
     "respectant à la lettre ».",
     ["llb-senat-precedent"]),
    ("17 avril 2026", "Moody's dégrade la Belgique",
     "De Aa3 à A1, perspective stable. L'agence invoque sa conviction que le gouvernement ne pourra pas "
     "prendre des mesures suffisantes pour stabiliser la dette.",
     ["rtbf-moodys", "llb-moodys"]),
    ("fin septembre 2026", "Conclave budgétaire",
     "Dix milliards d'euros d'effort à trouver d'ici 2029. Échéance du 15 octobre pour la transmission à "
     "la Commission européenne. L'hypothèse d'élections anticipées à l'hiver est publiquement évoquée.",
     ["avenir-conclave", "rtbf-boule-de-neige"]),
    ("2025-2034", "Extinction du mécanisme de transition",
     "Réduction de 10 % par an de la dotation de transition, jusqu'à disparition complète en 2034. "
     "Aucune renégociation n'est engagée.",
     ["crisp-financement", "bam-lsf"]),
]

# ---------------------------------------------------------------------------
# INDICATEURS
# ---------------------------------------------------------------------------

CHIFFRES = [
    ("674 275", "téléspectateurs au pic de Bye Bye Belgium",
     "Pic à 20 h 53 le 13 décembre 2006, soit 35,57 % de part de marché. 31 368 appels et 21 338 SMS reçus.",
     "wp-bbb"),
    ("0", "scénario de sortie chiffré et publié",
     "Aucun parti défendant la fin de la Belgique n'a publié de clé de partage de la dette, de statut "
     "juridique pour Bruxelles ni de calendrier de négociation opposable.",
     "vrt-vb-feuille"),
    ("5 %", "des Belges citaient la réforme de l'État comme premier problème en 2025",
     "Enquête nationale 2025, question ouverte, 5 749 répondants. En 2026, le thème ne figure plus dans "
     "les cinq premiers problèmes cités, dans aucune région.",
     "dsen25-rapport"),
    ("44", "sièges nationalistes flamands sur 150",
     "N-VA 24 sièges (16,71 %) et Vlaams Belang 20 sièges (13,77 %) à la Chambre au scrutin du 9 juin 2024.",
     "chambre-resultats-2024"),
    ("6 à 7 Md€", "de transferts interrégionaux annuels",
     "Estimation académique (Decoster et Sas, KU Leuven) : 7,1 milliards en 2014, 6,6 milliards projetés "
     "en 2020, soit environ 2,5 % du PIB belge.",
     "rtbf-transferts"),
    ("91,8 %", "de déclarations fiscales en français à Bruxelles",
     "Données 2019, en recul par rapport à 92,8 % en 2016. Indicateur administratif qui ne mesure ni la "
     "langue parlée ni le multilinguisme réel de la population bruxelloise.",
     "bx1-francophones"),
    ("30", "communes à facilités",
     "Dont les six de la périphérie bruxelloise. Régime institué par les lois de 1962 et 1963, "
     "objet d'un conflit d'interprétation permanent depuis la circulaire Peeters.",
     "wp-facilites"),
    ("620,5 M€", "par an de mécanisme de transition pour la Wallonie",
     "Constant de 2015 à 2024, non indexé, puis réduit de 10 % par an depuis 2025 jusqu'à extinction "
     "en 2034.",
     "crisp-financement"),
    ("A1", "note souveraine de la Belgique chez Moody's",
     "Dégradation de Aa3 à A1 le 17 avril 2026, perspective stable, après le retrait du double A par "
     "Fitch en juin 2025.",
     "rtbf-moodys"),
    ("10 Md€", "d'effort budgétaire à trouver d'ici 2029",
     "Objectif du conclave de septembre 2026, avec une échéance de transmission à la Commission "
     "européenne fixée au 15 octobre.",
     "avenir-conclave"),
    ("7", "États parties à la Convention de Vienne de 1983",
     "Quinze ratifications sont requises pour l'entrée en vigueur. La convention qui codifie le partage "
     "des dettes en cas de succession d'États n'est donc pas en vigueur.",
     "wp-vienne-1983"),
    ("49", "organisations internationales établies en Belgique",
     "Dont l'Union européenne et l'OTAN. Chacune est liée à l'État belge par un accord de siège dont le "
     "sort en cas de succession d'États n'est réglé par aucun texte.",
     "diplomatie-oi"),
    ("6", "réformes de l'État depuis 1970",
     "1970, 1980, 1988-1989, 1993, 2001, 2012-2014. Toutes dans le même sens. Aucune refédéralisation "
     "d'ampleur n'a jamais été opérée.",
     "crisp-5e-reforme"),
    ("2:1", "clé de partage du divorce tchécoslovaque",
     "Rapport de population appliqué aux avoirs financiers et aux dettes ; principe de territorialité pour "
     "les immeubles. Séparation négociée et exécutée en moins d'un an.",
     "travers-tchecoslovaquie"),
]
