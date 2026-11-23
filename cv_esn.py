"""CV détaillé « orienté compétences » sur 2 pages, pour Randstad et ses partenaires ESN.

Contenu validé dans cv_esn_contenu.md (seule source de faits : experiences.md).
Structure : Savoir-faire → Environnement technique & méthodologique → expériences détaillées
(Contexte / Réalisations par thème / Résultats & livrables / Méthodologies & outils) → formation, langues.
"""
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

import build_cv as b

b.SECTION_GAP = (7, 5)

NB = " "

CV = {
    "nom": b.CV["nom"],
    "title": b.CV["title"],
    "contact": ["Orléans | Disponibilité immédiate", "+33 6 30 23 24 41 | qi.guo@essec.edu"],
    "profil": "Chef de projet SI avec 3 ans d'expérience en transformation digitale au sein de grands groupes "
              "(BNP Paribas, La Poste). Pilotage de projets de bout en bout, coordination transverse Métiers–IT, "
              "gouvernance et conduite du changement.",
}

SAVOIR_FAIRE = [
    ("Pilotage de projets SI",
     "cadrage, estimation des charges et planification, suivi de l'avancement et des risques ; animation des "
     "comités de suivi (COSUI), préparation des supports et contribution aux comités de pilotage (COPIL) ; "
     "coordination de la recette et accompagnement de la mise en production"),
    ("Analyse des besoins (AMOA)",
     "animation d'ateliers avec les métiers, analyse des processus existants et modélisation des processus "
     "cibles ; rédaction des cahiers des charges, des spécifications fonctionnelles et techniques, des "
     "stratégies et cahiers de recette"),
    ("Coordination Métiers–IT",
     "interface entre les métiers, les équipes de développement et les prestataires ; suivi des "
     "développements, des tests utilisateurs et des anomalies, puis des corrections avec la TMA"),
    ("Conduite du changement",
     "conception de supports pédagogiques et de contenus de communication, animation d'un réseau "
     "d'ambassadeurs, formation et accompagnement des utilisateurs, rédaction de guides"),
    ("IA & automatisation",
     "collecte, qualification et priorisation de cas d'usage IA et RPA selon des critères communs (impact "
     "business, ROI, faisabilité, conformité) ; organisation de POC ; accompagnement du déploiement de "
     "solutions d'IA générative"),
    ("Développement low-code",
     "conception et développement d'applications et de flux automatisés sur Power Platform, intégrés à SharePoint"),
    ("RUN & amélioration continue",
     "supervision de robots en production, gestion des incidents et des montées de version, suivi des "
     "indicateurs (ROI, fiabilité, adoption) et actions d'amélioration"),
]

ENVIRONNEMENT = [
    ("Méthodologies", "Cycle en V, approche hybride, Agile (notions)"),
    ("IA & automatisation", "IA générative, RAG, Microsoft 365 Copilot, RPA (UiPath)"),
    ("Low-code", "Power Apps, Power Automate"),
    ("Outils", "Pack Office, Teams, SharePoint, Planner, Visio (BPMN), Power BI"),
    ("ERP & SI métiers", "SAP (ECC, Saphir, Equinox), eProc, Re4One, iRegate, Plume"),
    ("Langages (notions)", "SQL, Python, Java, PHP, C, C#, HTML/CSS"),
]

EXPERIENCES = [
    {
        "dates": "2024 – 2025", "contrat": "Alternance",
        "poste": "Digital Transformation Project Manager",
        "entreprise": "BNP Paribas – AIR Tech · 1 an et 4 mois",
        "contexte": "Au sein d'AIR Tech (AI, RPA & Technologies), entité chargée de la transformation technologique "
                    "des fonctions Compliance & Risk (lutte anti-blanchiment, sanctions, sécurité financière). "
                    "Rôle transverse entre les métiers, les experts IA et les équipes IT.",
        "axes": [
            ("Structuration et priorisation des initiatives IA & RPA", [
                "Conception et mise en place d'un processus de gestion des cas d'usage, de la collecte au comité d'arbitrage",
                "Définition de critères d'évaluation communs : impact business, ROI, faisabilité technique, conformité",
                "Animation de sessions de cadrage et de qualification avec les métiers et les experts IT ; "
                "rédaction des fiches cas d'usage destinées au comité",
            ]),
            ("Pilotage et coordination de projets IA", [
                "POC blockchain (AML) : benchmark du marché, organisation des tests, analyse des performances "
                "et recommandation d'une solution",
                "Projet Whistleblowing : cadrage du besoin, coordination du déploiement d'une recherche "
                "sémantique et d'un assistant RAG, organisation de la recette utilisateurs",
                "Déploiement de l'IA générative (Microsoft 365 Copilot, solutions internes) : accompagnement des "
                "utilisateurs dans l'adoption, identification de nouveaux cas d'usage, diffusion des bonnes pratiques",
            ]),
            ("Conduite du changement – programme AI4ALL", [
                "Contribution aux sessions d'acculturation, aux supports pédagogiques et aux contenus de communication",
                "Pilotage de la mise en place du site SharePoint « AI4ALL@Compliance », point d'entrée unique "
                f"vers les ressources, formations et outils{NB}IA",
                f"Animation du réseau de 70+{NB}ambassadeurs{NB}IA : création des canaux Teams, contribution à "
                "l'organisation des événements, accompagnement individualisé",
            ]),
        ],
        "resultats": [
            f"20+{NB}cas d'usage collectés et qualifiés en deux mois environ, dont 3 retenus et lancés en projet",
            "POC blockchain : recommandation ayant abouti à la contractualisation pluriannuelle de la solution",
            f"Programme AI4ALL destiné à ≈{NB}5{NB}000{NB}collaborateurs ; site « AI4ALL@Compliance » mis en place",
        ],
        "outils": "Cycle en V, approche hybride · IA générative, RAG, Microsoft 365 Copilot · SharePoint, Teams, "
                  "Office, Visio (BPMN), Planner",
    },
    {
        "dates": "2022 – 2024", "contrat": "Alternance + CDD",
        "poste": "Chef de Projet SI",
        "entreprise": "La Poste Groupe – Data Intelligence & Innovation, DTSFG · 2 ans",
        "contexte": "Au sein de la Direction de la Transformation des Solutions Finance du Groupe : projets d'automatisation (RPA, Power Platform) pour les fonctions "
                    "support (Finance, Achats, RH), du cadrage au RUN.",
        "axes": [
            ("BUILD – projets d'automatisation, dont 2 pilotés de bout en bout", [
                "Animation des ateliers de cadrage, analyse des processus existants et conception des processus cibles",
                "Rédaction des cahiers des charges et des spécifications fonctionnelles et techniques",
                "Estimation des charges et du budget, planification et suivi des risques ; animation des comités "
                "de suivi (COSUI), préparation des supports et contribution aux comités de pilotage (COPIL)",
                "Coordination des développements internes et des prestataires",
                "Rédaction des stratégies et cahiers de recette, exécution et organisation des tests, suivi des anomalies",
                "Mise en production, procédures et guides utilisateurs, support fonctionnel, suivi des corrections (TMA)",
            ]),
            ("RUN", [
                "Supervision d'une dizaine de robots RPA en production, gestion des incidents et des montées de version",
                "Suivi des indicateurs (ROI, fiabilité, adoption) et amélioration continue",
            ]),
            ("Projets phares", [
                "e-Note de crédit : digitalisation de la gestion des notes de crédit, de leur création (jusque-là "
                "manuelle, par les achats) à leur contrôle et leur comptabilisation dans SAP ; développement de toute la partie Power Platform "
                "(Power Apps, Power Automate, SharePoint), partie RPA réalisée par l'équipe de développement",
                "NOEMIE : application Power Platform de gestion des cartes de paiement des directions, développée "
                "par un prestataire ; cadrage, recette, mise en production et gestion d'un incident de production "
                "sensible",
                "DAVE : participation à la mise en place d'un outil de collecte et de qualification des besoins métiers",
            ]),
        ],
        "resultats": [
            "e-Note de crédit : délai de traitement ramené de plusieurs semaines à un traitement instantané ; "
            f"plusieurs milliers de notes traitées en quelques mois, pour plus de 700{NB}k€ de notes de crédit",
            "Référent Power Platform de l'équipe",
        ],
        "outils": "Cycle en V, approche hybride · UiPath, Power Apps, Power Automate, SharePoint · Visio (BPMN), "
                  "Planner, Teams, Office · SAP (ECC, Saphir, Equinox), eProc, Re4One, iRegate, Plume",
    },
]

LOUIS_VUITTON = ("2018 – 2022", "Retail & VIP Guest Relations", "Louis Vuitton",
                 "Gestion d'une clientèle VIP internationale : sens du service et adaptation en contexte multiculturel")

LINE = 1.05


def bottom_border(p, color=b.RULE):
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    el = OxmlElement("w:bottom")
    for k, v in (("w:val", "single"), ("w:sz", "4"), ("w:space", "1"), ("w:color", color)):
        el.set(qn(k), v)
    bdr.append(el)
    pPr.append(bdr)


def rubrique(doc, text, before=6):
    """Rubrique d'expérience (CONTEXTE…) : majuscules grasses, filet fin limité à la colonne droite."""
    p = b.para(doc, before=before, after=3, left=b.COL, keep=True)
    b.run(p, text, size=8.5, bold=True)
    bottom_border(p)
    return p


def axe(doc, text, before=3):
    p = b.para(doc, before=before, after=1, left=b.COL, keep=True, line=LINE)
    b.run(p, text, bold=True, italic=True)
    return p


def puce(doc, text, after=1):
    p = b.para(doc, after=after, left=b.COL + 0.4, first=-0.4,
               tabs=((b.COL + 0.4, WD_TAB_ALIGNMENT.LEFT),), line=LINE)
    b.run(p, "•\t")
    b.run(p, text)
    return p


def texte(doc, text, after=1):
    p = b.para(doc, after=after, left=b.COL, line=LINE)
    b.run(p, text)
    return p


def entete_poste(doc, dates, contrat, poste, entreprise, before):
    p = b.dated_line(doc, dates, before=before)
    b.run(p, poste, bold=True, size=10.5)
    p = b.dated_line(doc, "", after=0)
    p.runs[0].text = "\t"
    b.run(p, contrat, size=8.5, italic=True)
    b.run(p, "\t")
    b.run(p, entreprise, size=9, color=b.GREY)


def section_titre(doc, title, first=False):
    if not first:
        b.rule(doc, length_cm=3.2, before=b.SECTION_GAP[0], after=b.SECTION_GAP[1])
    p = b.para(doc, after=5, keep=True)
    b.run(p, title)


def build(out_stem="CV_NicolasQiGUO_ESN"):
    doc = b.new_document()
    b.write_header(doc, CV)
    b.rule(doc, before=9, after=6)

    # --- Savoir-faire
    section_titre(doc, "SAVOIR-FAIRE", first=True)
    for domaine, quoi in SAVOIR_FAIRE:
        p = b.para(doc, after=2.5, left=b.BUL, first=-0.4, tabs=((b.BUL, WD_TAB_ALIGNMENT.LEFT),), line=LINE)
        b.run(p, "•\t")
        b.run(p, domaine + " : ", bold=True)
        b.run(p, quoi)

    # --- Environnement technique & méthodologique
    section_titre(doc, "ENVIRONNEMENT TECHNIQUE & MÉTHODOLOGIQUE")
    label = 3.4
    for lab, txt in ENVIRONNEMENT:
        p = b.para(doc, after=1.5, left=b.COL + label, first=-label,
                   tabs=((b.COL + label, WD_TAB_ALIGNMENT.LEFT),))
        b.run(p, lab + " :", bold=True)
        b.run(p, "\t" + txt)

    # --- Expériences
    section_titre(doc, "EXPÉRIENCES PROFESSIONNELLES")
    for i, exp in enumerate(EXPERIENCES):
        entete_poste(doc, exp["dates"], exp["contrat"], exp["poste"], exp["entreprise"], before=10 if i else 0)
        rubrique(doc, "CONTEXTE", before=5)
        texte(doc, exp["contexte"])
        rubrique(doc, "RÉALISATIONS")
        for k, (titre, items) in enumerate(exp["axes"]):
            axe(doc, titre, before=1 if k == 0 else 4)
            for n, item in enumerate(items):
                puce(doc, item).paragraph_format.keep_with_next = n < len(items) - 1
        rubrique(doc, "RÉSULTATS & LIVRABLES")
        for r in exp["resultats"]:
            puce(doc, r)
        rubrique(doc, "MÉTHODOLOGIES & OUTILS")
        texte(doc, exp["outils"])

    dates, poste, entreprise, desc = LOUIS_VUITTON
    p = b.dated_line(doc, dates, before=10)
    b.run(p, poste, bold=True, size=10.5)
    p = b.para(doc, left=b.COL, line=LINE)
    b.run(p, entreprise, size=9, color=b.GREY)
    b.run(p, " – " + desc)

    # --- Formation, langues, centres d'intérêt
    section_titre(doc, "FORMATION")
    for k, (dates, diplome, suite, ecole, *_) in enumerate(b.CV["formation"][:2]):
        p = b.dated_line(doc, dates, before=5 if k else 0)
        b.run(p, diplome, bold=True)
        b.run(p, suite)
        p = b.para(doc, left=b.COL)
        b.run(p, ecole)
    # Diplômes littéraires antérieurs, regroupés sur une ligne
    p = b.dated_line(doc, "Avant 2016", before=5)
    b.run(p, "Master en Littératures Françaises", bold=True)
    b.run(p, " (Sorbonne) · ")
    b.run(p, "Licence en Langue Française", bold=True)
    b.run(p, " (Xi'an JiaoTong University)")

    b.rule(doc, length_cm=3.2, before=b.SECTION_GAP[0], after=b.SECTION_GAP[1])
    p = b.para(doc, left=b.COL, first=-b.COL, tabs=((b.COL, WD_TAB_ALIGNMENT.LEFT),))
    b.run(p, "LANGUES\t")
    for k, (langue, niveau) in enumerate(b.CV["langues"]):
        b.run(p, (" · " if k else "") + langue, bold=True)
        b.run(p, " " + niveau[0].lower() + niveau[1:])

    p = b.para(doc, before=4, left=b.COL, first=-b.COL, tabs=((b.COL, WD_TAB_ALIGNMENT.LEFT),))
    b.run(p, "INTÉRÊTS\t" + b.CV["interets"])

    return b.save(doc, out_stem)


if __name__ == "__main__":
    for path in build():
        print(path)
