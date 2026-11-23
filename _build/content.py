# -*- coding: utf-8 -*-
"""Firma Plus — site content. Edit here, then run: python3 _build/build.py"""

SITE = {
    "name": "Firma Plus",
    "domain": "firmaplus.ca",
    "email": "cpa@firmaplus.ca",
    "email_rn": "inforn@firmaplus.ca",
    "facebook": "https://www.facebook.com/Firmacompta",
    "linkedin": "https://www.linkedin.com/company/firmagestion/",
}

OFFICES = [
    {
        "slug": "montreal-saguenay", "img": "montreal-soir",
        "name": "Montréal / Saguenay",
        "entity": "Cabinet Firma Plus CPA Inc.",
        "phones": [("Montréal", "438-817-0057", "+14388170057"), ("Saguenay (Jonquière)", "581-705-4344", "+15817054344")],
        "email": "cpa@firmaplus.ca",
        "address": None,  # TODO: adresses Montréal et Jonquière à confirmer
        "blurb": "Notre équipe d’origine, qui dessert les PME de la grande région de Montréal et du Saguenay–Lac-Saint-Jean, en personne ou à distance.",
    },
    {
        "slug": "saint-eustache", "img": "equipe-bureau",
        "name": "Saint-Eustache (Rive-Nord)",
        "entity": "Cabinet Firma Plus Rive-Nord S.E.N.C.R.L.",
        "phones": [("Saint-Eustache", "450-472-2828", "+14504722828")],
        "email": "inforn@firmaplus.ca",
        "address": "450, rue du Parc, bureau 113<br>Saint-Eustache (Québec) J7R 7G6",
        "blurb": "Notre bureau de la Rive-Nord, avec une équipe complète en comptabilité, en certification et en fiscalité pour les entreprises des Laurentides et de Laval.",
    },
]

# ---------------------------------------------------------------- SERVICES
SERVICES = [
    {
        "slug": "tenue-de-livres", "img": "calculatrice",
        "icon": "book",
        "title": "Tenue de livres",
        "short": "Payables, recevables, remises gouvernementales et états financiers internes, à la fréquence qui vous convient.",
        "intro": "Nous vous offrons un service complet de tenue de livres, incluant le rattrapage comptable, pour vous permettre de vous concentrer sur ce qui compte vraiment.",
        "bullets": [
            "Registres financiers précis et à jour.",
            "Gestion efficace de vos comptes fournisseurs et clients.",
            "Rapports financiers clairs pour une prise de décision éclairée.",
            "Conformité avec les exigences gouvernementales (TPS, TVQ, retenues à la source, etc.).",
        ],
        "close": "Laissez-nous nous occuper de vos finances et assurez-vous d’une gestion optimale, tout en vous concentrant sur la croissance de votre entreprise.",
        "for": ["Les PME sans service comptable interne", "Les entreprises qui ont pris du retard dans leurs livres", "Les dirigeants qui veulent des chiffres fiables chaque mois"],
        "faq": [
            ("À quelle fréquence ferez-vous mes livres ?", "Selon vos besoins : chaque semaine, chaque mois ou chaque trimestre. La fréquence est fixée avec vous au départ et peut être ajustée en tout temps."),
            ("J’ai plusieurs mois de retard. Pouvez-vous rattraper ?", "Oui. Le rattrapage comptable fait partie du service : nous reconstituons les périodes manquantes, puis nous passons au rythme régulier."),
            ("Dois-je changer de logiciel comptable ?", "Pas nécessairement. Nous travaillons avec les principales solutions infonuagiques et vous conseillons si un changement apporte un gain réel."),
        ],
    },
    {
        "slug": "service-de-paie", "img": "paie",
        "icon": "users",
        "title": "Service de paie",
        "short": "L’administration complète de la paie de vos employés, sans erreur et dans les délais.",
        "intro": "La gestion de la paie est essentielle pour garantir la satisfaction et la fidélité de vos employés. Nous prenons en charge cette tâche complexe afin que vous soyez sûr que tout est fait dans les règles.",
        "bullets": [
            "Le calcul et le versement des salaires, sans erreur.",
            "La gestion des déductions à la source et des remises gouvernementales.",
            "La production des relevés fiscaux (T4, Relevé 1, etc.).",
            "L’automatisation et l’optimisation du processus de paie.",
        ],
        "close": "En nous confiant votre paie, vous vous libérez de cette charge administrative tout en garantissant le respect des délais et des obligations légales.",
        "for": ["Les entreprises de 1 à 100 employés", "Les employeurs qui veulent éviter les pénalités de remise", "Les entreprises en croissance qui embauchent"],
        "faq": [
            ("Gérez-vous les feuillets de fin d’année ?", "Oui. Nous produisons et transmettons les T4 et les Relevés 1, ainsi que les sommaires, avant les échéances."),
            ("Que se passe-t-il lors d’une embauche ou d’un départ ?", "Nous traitons l’inscription, les dernières paies et le relevé d’emploi. Vous nous transmettez l’information, nous nous occupons du reste."),
        ],
    },
    {
        "slug": "budget-et-previsions", "img": "graphiques",
        "icon": "chart",
        "title": "Budget et prévisions financières",
        "short": "Des budgets réalistes et des prévisions fiables pour décider en connaissance de cause.",
        "intro": "La planification financière est un pilier de votre réussite à long terme. Nous vous aidons à élaborer des budgets réalistes et des prévisions financières précises.",
        "bullets": [
            "Créer un budget aligné avec vos objectifs d’affaires.",
            "Anticiper les défis et saisir les occasions grâce à des prévisions fiables.",
            "Optimiser la gestion de votre trésorerie et améliorer votre rentabilité.",
            "Prendre des décisions éclairées pour guider la croissance de votre entreprise.",
        ],
        "close": "Avec notre soutien, vous gérez votre entreprise de manière stratégique et sécurisez son avenir.",
        "for": ["Les entreprises qui préparent une demande de financement", "Les dirigeants qui veulent suivre l’écart budget-réel", "Les projets d’expansion ou d’investissement"],
        "faq": [
            ("Suivez-vous le budget en cours d’année ?", "Oui. Nous comparons le réel au budget à la fréquence convenue et commentons les écarts significatifs."),
            ("Pouvez-vous préparer des prévisions pour la banque ?", "Oui. Nous préparons des prévisions de trésorerie et de résultats présentées selon ce que les prêteurs s’attendent à voir."),
        ],
    },
    {
        "slug": "directeur-financier-fractionne", "img": "conseil-table",
        "icon": "compass",
        "title": "Directeur financier fractionné",
        "short": "Un CFO à la demande : l’expertise d’un directeur financier, sans l’embauche à temps plein.",
        "intro": "Vous n’avez pas besoin d’un directeur financier à temps plein ? Vous aimeriez discuter de votre plan avant une décision importante ? Notre service de CFO à la demande vous donne accès à une expertise financière de haut niveau.",
        "bullets": [
            "Optimiser la structure financière de votre entreprise.",
            "Élaborer des plans de croissance et de rentabilité.",
            "Gérer les risques financiers et mettre en place des contrôles internes.",
            "Vous accompagner dans vos décisions stratégiques.",
        ],
        "close": "Manque de visibilité sur la rentabilité, trésorerie complexe : bénéficiez d’une expertise sur mesure, sans embaucher un CFO à temps plein.",
        "for": ["Les PME en croissance rapide", "Les entreprises qui préparent une acquisition, une vente ou un financement", "Les dirigeants qui veulent un interlocuteur financier de confiance"],
        "faq": [
            ("Combien de temps par mois ?", "Le mandat est calibré selon vos besoins : quelques heures par mois, une présence ponctuelle lors d’un projet, ou une rencontre mensuelle de direction."),
            ("Participez-vous aux rencontres avec la banque ?", "Oui, lorsque c’est utile. Nous préparons le dossier et vous accompagnons dans les échanges avec vos partenaires financiers."),
        ],
    },
    {
        "slug": "accompagnement-debourses-bancaires", "img": "signature",
        "icon": "bank",
        "title": "Accompagnement lors de déboursés bancaires",
        "short": "Des dossiers de financement et de déboursés complets, prêts pour votre banque et votre consultant en coûts.",
        "intro": "Les démarches bancaires peuvent s’avérer complexes, surtout lorsqu’il s’agit de solliciter des financements. Nous vous accompagnons à chaque étape pour assurer une présentation claire et complète de votre dossier.",
        "bullets": [
            "Préparation et révision des documents financiers.",
            "Conseils stratégiques pour renforcer votre dossier.",
            "Assistance pour faciliter la communication avec votre banque.",
            "Préparation de votre dossier de déboursés pour le consultant en coûts dans le cadre de vos projets de construction.",
        ],
        "close": "Nous facilitons vos démarches pour vous permettre d’obtenir rapidement les financements nécessaires à vos projets.",
        "for": ["Les promoteurs et entrepreneurs en construction", "Les entreprises qui financent un projet par tranches", "Les dirigeants qui veulent accélérer les déboursés"],
        "faq": [
            ("Qu’est-ce qu’un dossier de déboursés ?", "C’est l’ensemble des pièces (factures, preuves de paiement, avancement des travaux, quittances) qui permettent au consultant en coûts de recommander un déboursé à la banque."),
            ("Pouvez-vous intervenir en cours de projet ?", "Oui. Nous mettons de l’ordre dans les pièces déjà accumulées, puis nous préparons chaque demande suivante."),
        ],
    },
    {
        "slug": "impots-et-autres-services", "img": "analyse",
        "icon": "doc",
        "title": "Impôts et autres services",
        "short": "Impôts, rattrapage comptable, états financiers et services-conseils, adaptés à vos besoins.",
        "intro": "Chaque entreprise a des besoins uniques. Nous proposons une gamme d’autres services adaptés à vos exigences.",
        "bullets": [
            "Impôts des sociétés et des particuliers en affaires.",
            "Rattrapage comptable.",
            "Préparation d’états financiers.",
            "Service-conseil.",
        ],
        "close": "Nous répondons à vos besoins comptables avec des solutions personnalisées pour soutenir la réussite de votre entreprise.",
        "for": ["Les entreprises qui veulent un seul interlocuteur pour la comptabilité et l’impôt", "Les sociétés de gestion et de portefeuille", "Les entreprises qui ont besoin d’états financiers pour un tiers"],
        "faq": [
            ("Préparez-vous les états financiers annuels ?", "Oui. Notre bureau de Saint-Eustache compte une équipe dédiée à la certification et aux états financiers."),
        ],
    },
]

# ---------------------------------------------------------------- SECTORS
# NOTE: secteurs proposés à partir des services actuels — à valider avec Firma Plus.
SECTORS = [
    {
        "slug": "construction", "img": "construction",
        "icon": "crane",
        "title": "Construction et entrepreneurs",
        "short": "Comptabilité par projet, dossiers de déboursés et suivi des retenues contractuelles.",
        "issues": ["Suivi des coûts et de la rentabilité par chantier", "Dossiers de déboursés pour la banque et le consultant en coûts", "Retenues contractuelles et quittances", "Trésorerie tendue entre deux paiements"],
        "services": ["accompagnement-debourses-bancaires", "tenue-de-livres", "budget-et-previsions"],
    },
    {
        "slug": "immobilier", "img": "immobilier",
        "icon": "building",
        "title": "Immobilier",
        "short": "Immeubles locatifs, promotion et sociétés de portefeuille : des livres clairs, entité par entité.",
        "issues": ["Plusieurs sociétés et immeubles à suivre séparément", "Financement et refinancement hypothécaire", "Revenus de loyers, dépenses et améliorations à distinguer", "États financiers exigés par les prêteurs"],
        "services": ["tenue-de-livres", "accompagnement-debourses-bancaires", "impots-et-autres-services"],
    },
    {
        "slug": "commerce-et-distribution", "img": "commerce",
        "icon": "cart",
        "title": "Commerce de détail et distribution",
        "short": "Inventaire, marges et taxes de vente : la rentabilité, ligne par ligne.",
        "issues": ["Valeur des stocks et coût des marchandises vendues", "Volume élevé de transactions et de rapprochements", "TPS et TVQ sur un grand nombre de ventes", "Saisonnalité de la trésorerie"],
        "services": ["tenue-de-livres", "budget-et-previsions", "service-de-paie"],
    },
    {
        "slug": "services-professionnels", "img": "services-pro",
        "icon": "brief",
        "title": "Services professionnels",
        "short": "Cabinets, agences et consultants : recevables, temps facturable et rémunération des associés.",
        "issues": ["Comptes clients et délais de recouvrement", "Rentabilité par mandat ou par client", "Rémunération des associés : salaire ou dividendes", "Croissance de l’équipe et paie"],
        "services": ["tenue-de-livres", "directeur-financier-fractionne", "service-de-paie"],
    },
    {
        "slug": "manufacturier", "img": "manufacturier",
        "icon": "gear",
        "title": "Manufacturier et industriel",
        "short": "Prix de revient, investissements en équipement et financement de la croissance.",
        "issues": ["Calcul du prix de revient et des marges", "Financement d’équipement et de fonds de roulement", "Contrôles internes sur les achats et les stocks", "Prévisions pour les projets d’expansion"],
        "services": ["budget-et-previsions", "directeur-financier-fractionne", "accompagnement-debourses-bancaires"],
    },
    {
        "slug": "entreprises-en-croissance", "img": "demarrage",
        "icon": "rocket",
        "title": "Démarrage et entreprises en croissance",
        "short": "Mettre en place les bonnes bases tôt, puis suivre le rythme de la croissance.",
        "issues": ["Structure comptable et fiscale de départ", "Premières embauches et inscription aux remises", "Prévisions pour investisseurs et prêteurs", "Passage du fondateur-comptable à un vrai système"],
        "services": ["directeur-financier-fractionne", "budget-et-previsions", "tenue-de-livres"],
    },
]

# ---------------------------------------------------------------- TEAM
# office: "mtl" (Montréal / Saguenay), "rn" (Saint-Eustache) — a person may belong to both
PARTNERS = [
    {"name": "Nicolas Lessard", "cred": "M.Sc. Fin., CPA", "role": "Associé principal", "office": "mtl rn",
     "bio": "Fort de plus de vingt ans d’expérience en financement d’entreprises, Nicolas reconnaît l’importance d’un accès rapide aux informations financières. Firma Plus propose ainsi des services comptables de qualité, permettant des décisions éclairées et rapides."},
    {"name": "Jérome Thibeault", "cred": "B.A.A.", "role": "Associé", "office": "mtl rn",
     "bio": "« Ayant connu une croissance soutenue dans l’immobilier, j’ai compris l’importance cruciale d’une comptabilité professionnelle. En confiant cette tâche à des experts, j’ai pu me concentrer sur la croissance de l’entreprise. »"},
    {"name": "Yannick P-Michel", "cred": "B.Ing.", "role": "Associé", "office": "mtl", "bio": ""},
    {"name": "Christophe Gingras", "cred": "", "role": "Associé principal — Rive-Nord", "office": "rn", "bio": ""},
    {"name": "Jessica Gingras", "cred": "", "role": "Associée principale — Rive-Nord", "office": "rn", "bio": ""},
]

STAFF = [
    ("Cathy Thibeault", "", "Directrice du développement humain", "mtl rn"),
    ("Marie-Pierre Charron-Ligez", "CPA", "Directrice principale, comptabilité", "mtl"),
    ("Hadja Fatou Barry", "CPA", "Responsable de dossier", "mtl"),
    ("Marie-Claude Fontaine", "", "Technicienne comptable", "mtl"),
    ("Patrick Royer", "", "Technicien comptable", "mtl"),
    ("Roxanne Mongeau", "", "Technicienne comptable", "mtl"),
    ("Noémie Girard-Tremblay", "", "Technicienne comptable", "mtl"),
    ("Myriam Perreault", "", "Technicienne comptable", "mtl"),
    ("Jessica Brassard-Samson", "", "Technicienne comptable", "mtl"),
    ("Tessa Haudecoeur", "", "Commis comptable", "mtl"),
    ("Manon Perreault", "", "Directrice en certification", "rn"),
    ("Nancy Charbonneau", "", "Directrice en comptabilité", "rn"),
    ("Stéphanie Groulx", "", "Gestionnaire d’équipe", "rn"),
    ("Émilie Rose", "", "Coordonnatrice des opérations", "rn"),
    ("Nancy-Lee Chevanelle", "", "Adjointe administrative", "rn"),
    ("Arnold Nguessan", "", "Chargé de mission", "rn"),
    ("Fhami Aouani", "", "Chargé de mission", "rn"),
    ("Osama Habshy", "", "Technicien comptable senior", "rn"),
    ("Isabelle Gagnon", "", "Technicienne comptable", "rn"),
    ("Anik Champagne", "", "Technicienne comptable", "rn"),
    ("Wafa Ben Akacha", "", "Technicienne comptable", "rn"),
    ("Fabiola Beauchemin", "", "Technicienne comptable", "rn"),
    ("Khadija Ait Ben Ouissaden", "", "Technicienne comptable", "rn"),
    ("Chantal Longtin", "", "Consultante externe", "rn"),
    ("Liliana Aguiar", "", "Adjointe administrative", "rn"),
    ("Félix Nadeau", "", "Adjoint administratif", "rn"),
    ("Claude Nadeau", "", "Adjoint administratif", "rn"),
]

# ---------------------------------------------------------------- INSIGHTS
ARTICLES = [
    {
        "slug": "t4-releve-1-preparer-fin-annee", "img": "paie",
        "date": "2026-11-18", "cat": "Paie", "read": 4,
        "title": "T4 et Relevé 1 : préparer la fin d’année de paie dès novembre",
        "excerpt": "Les feuillets doivent être remis aux employés et transmis aux gouvernements au plus tard le dernier jour de février. Le travail se gagne en novembre.",
        "body": """
<p>Chaque année, les employeurs doivent remettre à leurs employés un feuillet T4 (fédéral) et un Relevé 1 (Québec), et transmettre ces feuillets avec leurs sommaires à l’Agence du revenu du Canada et à Revenu Québec. L’échéance tombe le dernier jour de février. Quand on attend janvier pour s’y mettre, les erreurs de l’année deviennent des corrections urgentes.</p>
<h2>Ce qu’il faut vérifier avant le 31 décembre</h2>
<ul>
<li><strong>Les renseignements des employés.</strong> Nom, adresse et numéro d’assurance sociale à jour pour chaque personne payée dans l’année, y compris celles qui ont quitté.</li>
<li><strong>Les avantages imposables.</strong> Véhicule de l’entreprise, cellulaire personnel payé, cadeaux en argent : ils doivent être inclus dans la paie avant la fin de l’année, pas ajoutés après coup.</li>
<li><strong>Les remises de l’année.</strong> Le total remis aux deux paliers de gouvernement doit concorder avec les retenues calculées. Un écart découvert en février coûte plus cher qu’en novembre.</li>
<li><strong>Les primes et la dernière paie.</strong> Une prime versée le 2 janvier appartient à l’année suivante. Le calendrier de versement a un effet fiscal réel pour l’employé.</li>
</ul>
<h2>Les cotisations propres au Québec</h2>
<p>Le Relevé 1 et le sommaire des retenues et cotisations de l’employeur couvrent des éléments qui n’existent pas ailleurs au Canada : RRQ, RQAP, cotisation au Fonds des services de santé, et, selon la masse salariale, les cotisations au développement de la main-d’œuvre et aux normes du travail. Une erreur de taux sur l’un de ces éléments se propage sur toute l’année.</p>
<h2>Notre recommandation</h2>
<p>Faites une conciliation de la paie au 30 novembre : retenues calculées, remises effectuées et cumulatifs par employé. Ce qui reste à corriger en décembre se fait encore dans l’année courante, sans feuillets modifiés.</p>
<div class="note">Notre <a href="{root}services/service-de-paie/">service de paie</a> inclut la production et la transmission des T4 et des Relevés 1, ainsi que la conciliation de fin d’année.</div>
""",
    },
    {
        "slug": "tps-tvq-erreurs-frequentes", "img": "calculatrice",
        "date": "2026-11-04", "cat": "Fiscalité", "read": 5,
        "title": "TPS et TVQ : cinq erreurs fréquentes dans les déclarations des PME",
        "excerpt": "Taxes de 5 % et de 9,975 %, crédits de taxe sur les intrants, seuil du petit fournisseur : là où les PME se trompent le plus souvent.",
        "body": """
<p>Au Québec, la plupart des fournitures sont assujetties à la TPS (5 %) et à la TVQ (9,975 %). Les montants perçus n’appartiennent pas à l’entreprise : elle les détient en fiducie jusqu’à la remise. Voici les erreurs que nous corrigeons le plus souvent lors d’un rattrapage.</p>
<h2>1. S’inscrire trop tard</h2>
<p>Une entreprise reste un petit fournisseur tant que ses fournitures taxables ne dépassent pas 30 000 $ sur quatre trimestres civils consécutifs. Dès que le seuil est franchi, l’inscription devient obligatoire, et les taxes non perçues sur les ventes suivantes peuvent devenir payables par l’entreprise elle-même.</p>
<h2>2. Réclamer des crédits sans pièces justificatives conformes</h2>
<p>Les crédits et remboursements de taxe sur les intrants exigent des factures qui contiennent les renseignements requis, dont le numéro d’inscription du fournisseur au-delà de certains montants. Une facture incomplète peut faire refuser le crédit lors d’une vérification.</p>
<h2>3. Mélanger dépenses personnelles et dépenses d’entreprise</h2>
<p>Les taxes payées sur des dépenses personnelles ne sont pas récupérables. Une carte de crédit partagée complique les rapprochements et augmente le risque d’erreur.</p>
<h2>4. Oublier les restrictions sur certaines dépenses</h2>
<p>Les frais de repas et de divertissement, certains véhicules et d’autres catégories font l’objet de règles particulières, notamment pour la TVQ. Les traiter comme des dépenses ordinaires surestime les crédits réclamés.</p>
<h2>5. Déclarer sans rapprocher</h2>
<p>Une déclaration doit découler de livres rapprochés avec le relevé bancaire. Produire la déclaration à partir des factures de vente seulement est la source la plus courante d’écarts.</p>
<div class="note">Vous avez des périodes en retard ou un doute sur vos déclarations ? Notre <a href="{root}services/tenue-de-livres/">service de tenue de livres</a> inclut la préparation et la production des déclarations de taxes.</div>
""",
    },
    {
        "slug": "directeur-financier-fractionne-quand", "img": "conseil-table",
        "date": "2026-10-21", "cat": "Gestion", "read": 4,
        "title": "Directeur financier fractionné : cinq signes que votre PME en a besoin",
        "excerpt": "Entre le technicien comptable et le CFO à temps plein, il existe une étape. Voici comment savoir si vous y êtes.",
        "body": """
<p>Une PME en croissance atteint souvent un point où ses livres sont bien tenus, mais où personne n’a le temps ni le rôle d’en tirer des décisions. Un directeur financier fractionné comble cet écart, quelques heures par mois.</p>
<h2>Les signes</h2>
<ol>
<li><strong>Vous ne connaissez pas votre rentabilité par client, par produit ou par projet.</strong> Le résultat global est positif, mais vous ne savez pas ce qui le porte.</li>
<li><strong>La trésorerie vous surprend.</strong> Le compte est plus bas que prévu alors que les ventes augmentent.</li>
<li><strong>Une décision importante approche.</strong> Embauche clé, acquisition d’équipement, nouveau local, financement : vous voulez valider le plan avant de signer.</li>
<li><strong>Votre banquier pose des questions auxquelles vous répondez de mémoire.</strong> Ratios, clauses restrictives, prévisions : il faut des chiffres à jour et une personne pour les présenter.</li>
<li><strong>Vous êtes le seul à regarder les chiffres.</strong> Un regard externe et régulier réduit le risque d’angle mort.</li>
</ol>
<h2>À quoi ressemble un mandat</h2>
<p>Typiquement : un tableau de bord mensuel, une rencontre de direction pour commenter les écarts, un plan de trésorerie sur douze mois, et une présence ponctuelle lors des projets majeurs. Le mandat s’ajuste à la saison et aux besoins.</p>
<div class="note">Découvrez notre <a href="{root}services/directeur-financier-fractionne/">service de directeur financier fractionné</a>.</div>
""",
    },
    {
        "slug": "dossier-debourses-construction", "img": "architecte",
        "date": "2026-10-07", "cat": "Financement", "read": 5,
        "title": "Projets de construction : monter un dossier de déboursés qui passe du premier coup",
        "excerpt": "Le consultant en coûts recommande, la banque débourse. Entre les deux, la qualité de votre dossier fixe le délai.",
        "body": """
<p>Dans un financement de construction, la banque ne verse pas le prêt d’un seul coup. Elle débourse par tranches, sur recommandation d’un consultant en coûts qui vérifie l’avancement des travaux et les sommes réellement engagées. Chaque dossier incomplet retarde le déboursé suivant, et la trésorerie du projet en dépend.</p>
<h2>Ce que le consultant en coûts veut voir</h2>
<ul>
<li>Un sommaire des coûts par poste budgétaire, comparé au budget approuvé.</li>
<li>Les factures des fournisseurs et sous-traitants, classées par poste.</li>
<li>Les preuves de paiement correspondantes.</li>
<li>Le suivi des retenues contractuelles et, au besoin, les quittances des sous-traitants.</li>
<li>Les avenants et changements, avec leur effet sur le budget.</li>
</ul>
<h2>Les causes de retard les plus courantes</h2>
<p>Factures non classées, paiements sans facture, dépassements non expliqués et écarts entre la comptabilité et le sommaire présenté. Ce sont des problèmes de préparation, pas de fond.</p>
<h2>La méthode qui fonctionne</h2>
<p>Tenir la comptabilité du projet par poste budgétaire dès le premier jour, rapprocher chaque mois, et préparer chaque demande à partir des livres plutôt qu’en reconstituant les pièces à la dernière minute.</p>
<div class="note">Notre service d’<a href="{root}services/accompagnement-debourses-bancaires/">accompagnement lors de déboursés bancaires</a> prend en charge la préparation complète de vos dossiers.</div>
""",
    },
    {
        "slug": "rattrapage-comptable-par-ou-commencer", "img": "analyse",
        "date": "2026-09-23", "cat": "Comptabilité", "read": 4,
        "title": "Rattrapage comptable : par où commencer quand les livres ont pris du retard",
        "excerpt": "Six mois, un an, plus ? Le retard se rattrape. L’ordre dans lequel on s’y prend fait toute la différence.",
        "body": """
<p>Le retard comptable s’installe souvent en période de forte croissance : on vend, on livre, on embauche, et les livres attendent. Le rattrapage n’a rien de honteux, mais il doit suivre un ordre précis.</p>
<h2>1. Les échéances gouvernementales d’abord</h2>
<p>Remises de retenues à la source, déclarations de TPS et de TVQ, déclarations de revenus : ce sont elles qui génèrent des intérêts et des pénalités. On les identifie et on les priorise.</p>
<h2>2. Les relevés bancaires et de cartes</h2>
<p>Ils sont la colonne vertébrale du rattrapage. Toutes les transactions y figurent ; on part d’eux pour reconstruire les livres, mois par mois.</p>
<h2>3. Les pièces justificatives</h2>
<p>Factures de ventes et d’achats, contrats, relevés de paie. Ce qui manque se demande aux fournisseurs ou se retrouve dans les courriels. Ce qui demeure introuvable est documenté.</p>
<h2>4. Le rapprochement</h2>
<p>Chaque mois rattrapé est rapproché avec la banque avant de passer au suivant. Sans cette étape, les erreurs s’additionnent.</p>
<h2>5. Le passage au régime régulier</h2>
<p>Une fois à jour, on fixe une fréquence de tenue de livres réaliste et un processus simple de transmission des pièces, pour ne plus revenir en arrière.</p>
<div class="note">Le rattrapage fait partie de notre <a href="{root}services/tenue-de-livres/">service de tenue de livres</a>.</div>
""",
    },
    {
        "slug": "budget-annuel-pme-methode", "img": "graphiques",
        "date": "2026-09-09", "cat": "Gestion", "read": 4,
        "title": "Budget annuel : une méthode simple pour les PME",
        "excerpt": "Un budget utile tient sur une page, part des ventes et se compare au réel chaque mois.",
        "body": """
<p>Beaucoup de PME n’ont pas de budget parce qu’elles imaginent un exercice lourd. Un budget utile est pourtant simple : il traduit vos objectifs en chiffres et vous dit, chaque mois, si vous êtes sur la bonne trajectoire.</p>
<h2>Partir des ventes</h2>
<p>Estimez les ventes par mois, en tenant compte de la saisonnalité, à partir de l’historique et des contrats connus. Tout le reste en découle.</p>
<h2>Distinguer coûts variables et coûts fixes</h2>
<p>Les coûts variables suivent les ventes ; les coûts fixes (loyer, salaires de base, assurances, abonnements) ne bougent pas. Cette distinction permet de calculer votre seuil de rentabilité.</p>
<h2>Ajouter la trésorerie</h2>
<p>Un budget de résultats ne suffit pas. Les délais de paiement des clients, les remboursements de prêt, les achats d’équipement et les remises de taxes déplacent l’argent dans le temps. Un plan de trésorerie mensuel évite les surprises.</p>
<h2>Comparer au réel chaque mois</h2>
<p>Le budget prend sa valeur dans la comparaison. Un écart significatif mérite une explication et, au besoin, une décision.</p>
<div class="note">Notre service de <a href="{root}services/budget-et-previsions/">budget et prévisions financières</a> vous accompagne de la préparation au suivi.</div>
""",
    },
]

# ---------------------------------------------------------------- ICONS (inline SVG paths, 24x24, stroke)
ICONS = {
    "book": '<path d="M4 4h10a4 4 0 0 1 4 4v12H8a4 4 0 0 1-4-4z"/><path d="M8 8h6M8 12h6"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.5a5 5 0 0 1 5.5 5"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    "bank": '<path d="M3 10l9-6 9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
    "doc": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    "crane": '<path d="M4 21V5h14M4 5l4-2v2M8 9h10M14 5v6M14 11v3M12 14h4v3h-4zM2 21h8"/>',
    "building": '<path d="M4 21V4h10v17M14 9h6v12M2 21h20M7 8h1M10 8h1M7 12h1M10 12h1M7 16h1M10 16h1"/>',
    "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="17" cy="20" r="1.5"/><path d="M2 3h3l2.5 12h11l2-8H6"/>',
    "brief": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3M3 13h18"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
    "rocket": '<path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2M9 15l-3-3c2-6 7-9 13-9 0 6-3 11-9 13z"/><circle cx="14.5" cy="9.5" r="1.5"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "cloud": '<path d="M7 18a5 5 0 0 1-.5-10A6 6 0 0 1 18 9a4.5 4.5 0 0 1-.5 9z"/>',
    "handshake": '<path d="M2 12l4-4 4 2 3-2 5 1 4 3M6 8l-4 8M22 12l-3 5-4 2-6-5"/>',
    "pin": '<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
}
