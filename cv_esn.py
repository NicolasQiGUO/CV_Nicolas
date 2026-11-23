"""CV « type dossier de compétences » sur 2 pages, pour les ESN et cabinets (Randstad Professional).

Structure conseillée par la recruteuse : savoir-faire en tête (classés du plus au moins maîtrisé,
avec où ils ont été mis en pratique), puis expériences détaillées (contexte, réalisations par axe,
résultats, méthodologie et outils), formation et langues en fin de document.
Seule source de faits : experiences.md.
"""
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.shared import Cm

import build_cv as b

b.SECTION_GAP = (6, 5)

NB = " "

CV = {
    "nom": b.CV["nom"],
    "title": b.CV["title"],
    "contact": ["Orléans | Disponibilité immédiate", "+33 6 30 23 24 41 | qi.guo@essec.edu"],
    "profil": "Chef de projet SI avec 3 ans d'expérience en transformation digitale au sein de grands groupes "
              "(BNP Paribas, La Poste). Pilotage de projets de bout en bout, coordination transverse Métiers–IT, "
              "gouvernance et conduite du changement.",
}

# Savoir-faire, du plus au moins maîtrisé : (domaine, ce que je sais faire, où je l'ai pratiqué)
SAVOIR_FAIRE = [
    ("Pilotage de projets SI",
     "cadrage, chiffrage, planning, risques, COPIL / COSUI, recette, mise en production",
     "2 projets de bout en bout chez La Poste"),
    ("Analyse des besoins",
     "ateliers métiers, cartographie des processus, cahiers des charges, spécifications fonctionnelles et techniques",
     "La Poste, BNP Paribas"),
    ("Coordination Métiers–IT",
     "interface entre métiers, équipes IT et prestataires",
     "La Poste, BNP Paribas"),
    ("Conduite du changement",
     "acculturation, supports pédagogiques, animation de communauté, formation des utilisateurs",
     f"programme AI4ALL, 70+{NB}ambassadeurs"),
    ("Cas d'usage IA & RPA",
     "collecte, qualification (valeur, ROI, faisabilité, conformité) et priorisation jusqu'au comité d'arbitrage",
     "20+ cas d'usage chez BNP Paribas"),
    ("Développement low-code",
     "Power Apps, Power Automate, SharePoint",
     "référent Power Platform"),
    ("RUN & amélioration continue",
     "monitoring, incidents, montées de version, KPI",
     "une dizaine de robots"),
]

ENVIRONNEMENT = [
    ("Méthodologies : ", "Cycle en V, hybride, Agile (notions)"),
    ("IA & automatisation : ", "GenAI, RAG, M365 Copilot, RPA (UiPath), Power Apps, Power Automate"),
    ("Outils : ", "Pack Office, Teams, SharePoint, Planner, Visio (BPMN), Power BI"),
    ("ERP & SI métiers : ", "SAP (ECC, Saphir, Equinox), eProc, Re4One, iRegate, Plume"),
    ("Langages (notions) : ", "SQL, Python, Java, PHP, C, C#, HTML/CSS"),
    ("À développer : ", "pratique de l'Agile, remise à niveau en programmation"),
]

EXPERIENCES = [
    {
        "dates": "2024 – 2025", "duree": "Sept. 2024 – déc. 2025", "contrat": "Alternance",
        "poste": "Digital Transformation Project Manager – AIR TECH @ BNP PARIBAS",
        "contexte": "AIR Tech (AI, RPA & Technologies), entité dédiée à la transformation technologique des "
                    "fonctions Compliance & Risk (AML, sanctions, sécurité financière). Rôle transverse sur trois axes : "
                    "initiatives IA & RPA, pilotage de projets, conduite du changement.",
        "axes": [
            ("Structuration et priorisation des initiatives IA & RPA", [
                "Conception d'un processus end-to-end de gestion des cas d'usage, de l'idéation à la validation "
                "en comité d'arbitrage",
                "Définition de critères communs : impact business, ROI, faisabilité, conformité",
                "Sessions de cadrage avec les métiers et les experts IT, fiches cas d'usage pour les comités",
            ]),
            ("Pilotage et coordination de projets", [
                "POC blockchain (AML) : benchmark du marché, organisation des tests, analyse de performances "
                "et recommandation d'une solution",
                "Projet Whistleblowing (IA) : cadrage des besoins, organisation de la recette utilisateurs, "
                "accompagnement des métiers",
                "Déploiement GenAI (Microsoft 365 Copilot, solutions internes) : onboarding des utilisateurs, "
                "nouveaux cas d'usage, bonnes pratiques",
            ]),
            (f"Conduite du changement – programme AI4ALL (≈{NB}5{NB}000{NB}collaborateurs)", [
                "Contribution aux sessions d'acculturation et à la création de supports pédagogiques",
                "Pilotage de la mise en place du site SharePoint « AI4ALL@Compliance », point d'entrée unique "
                f"des ressources{NB}IA",
                f"Animation d'un réseau de 70+{NB}ambassadeurs{NB}IA (canaux Teams, événements)",
            ]),
        ],
        "resultats": [
            f"20+{NB}cas d'usage collectés et qualifiés en deux mois environ, dont 3 lancés en projet",
            "POC blockchain (AML) : solution recommandée retenue dans le cadre d'un contrat pluriannuel",
            "Un point d'entrée unique vers les ressources, formations et outils IA des équipes Compliance & Risk",
        ],
        "methodo_outils": "Cycle en V, hybride · GenAI, RAG, Microsoft 365 Copilot, SharePoint, Teams, "
                          "Visio (BPMN), Planner",
    },
    {
        "dates": "2022 – 2024", "duree": "Sept. 2022 – août 2024", "contrat": "Alternance + CDD",
        "poste": "Chef de Projet SI – Data Intelligence & Innovation DTSFG @ LA POSTE GROUPE",
        "contexte": "Équipe Data Intelligence & Innovation, rattachée à la Direction de la Transformation des "
                    "Solutions Finance du Groupe (SI Finance, SIRH, SAP). Rôle orienté pilotage opérationnel et "
                    "delivery de projets d'automatisation (RPA, low-code), du cadrage au RUN.",
        "axes": [
            ("BUILD – pilotage de projets d'automatisation, dont 2 de bout en bout", [
                "Ateliers de cadrage, analyse des processus existants et cibles, cahiers des charges et "
                "spécifications fonctionnelles et techniques",
                "Chiffrage, planification, gestion des risques, animation des COSUI / COPIL",
                "Coordination des développements internes et prestataires ; développement low-code "
                "(Power Apps, Power Automate)",
                "Stratégie et cahiers de recette, tests utilisateurs, suivi des anomalies, mise en production "
                "et accompagnement du déploiement (Finance, RH)",
            ]),
            ("RUN", [
                "Monitoring quotidien d'une dizaine de robots, gestion des incidents, montées de version, "
                "suivi des KPI (ROI, fiabilité, adoption), amélioration continue",
            ]),
            ("Projets phares", [
                "e-Note de crédit : digitalisation de la création et de la comptabilisation dans SAP des notes "
                "de crédit (RPA + Power Platform, développement de l'ensemble de la partie Power Platform)",
                "NOEMIE : gestion des cartes de paiement des directions, 100 % Power Platform et SharePoint "
                "(données SI RH, circuits d'approbation)",
                "DAVE : participation à la mise en place d'un outil de collecte et de qualification des besoins métiers",
            ]),
        ],
        "resultats": [
            "e-Note de crédit : de plusieurs semaines à un traitement quasi instantané, "
            "zéro erreur de saisie",
            f"Plusieurs milliers de notes traitées en quelques mois, pour plus de 700{NB}k€ de notes de crédit",
            "Référent Power Platform de l'équipe",
        ],
        "methodo_outils": "Cycle en V, hybride · UiPath, Power Apps, Power Automate, SharePoint, "
                          "Visio (BPMN), Planner, Teams, Office, SAP (ECC, Saphir, Equinox), eProc, Re4One, "
                          "iRegate, Plume",
    },
]

LOUIS_VUITTON = ("2018 – 2022", "Retail & VIP Guest Relations @ LOUIS VUITTON",
                 "Gestion d'une clientèle VIP internationale dans un environnement exigeant : sens du service "
                 "et adaptation en contexte multiculturel")


def sub_heading(doc, text, before=3):
    """Intertitre en italique dans la colonne de contenu (Contexte, Réalisations…)."""
    p = b.para(doc, before=before, after=1, left=b.COL, keep=True)
    b.run(p, text, size=9, italic=True, color=b.GREY)
    return p


def text_block(doc, text, after=1):
    p = b.para(doc, after=after, left=b.COL, line=1.05)
    b.run(p, text)
    return p


def build(out_stem="CV_NicolasQiGUO_ESN"):
    doc = b.new_document()
    b.write_header(doc, CV)
    b.rule(doc, before=9, after=6)

    # --- Savoir-faire (en tête, du plus au moins maîtrisé)
    b.section(doc, "COMPÉTENCES CLÉS", first=True)
    for domaine, quoi, ou in SAVOIR_FAIRE:
        p = b.para(doc, after=1.5, left=b.BUL, first=-0.4, tabs=((b.BUL, WD_TAB_ALIGNMENT.LEFT),), line=1.05)
        b.run(p, "•\t")
        b.run(p, domaine + " : ", bold=True)
        b.run(p, quoi)
        b.run(p, " – " + ou, italic=True, color=b.GREY)

    # --- Environnement technique
    b.rule(doc, length_cm=3.2, before=b.SECTION_GAP[0], after=b.SECTION_GAP[1])
    label = 3.6
    for k, (lab, txt) in enumerate(ENVIRONNEMENT):
        p = b.para(doc, after=1, left=b.COL + label, first=-(b.COL + label),
                   tabs=((b.COL, WD_TAB_ALIGNMENT.LEFT), (b.COL + label, WD_TAB_ALIGNMENT.LEFT)))
        b.run(p, "ENVIRONNEMENT" if k == 0 else "")
        b.run(p, "\t")
        b.run(p, lab.rstrip(), bold=True)
        b.run(p, "\t" + txt)

    # --- Expériences détaillées
    b.rule(doc, length_cm=3.2, before=b.SECTION_GAP[0], after=b.SECTION_GAP[1])
    b.section(doc, "EXPÉRIENCES PROFESSIONNELLES", first=True)
    for i, exp in enumerate(EXPERIENCES):
        p = b.dated_line(doc, exp["dates"], before=8 if i else 0)
        b.run(p, exp["poste"], bold=True)
        p = b.dated_line(doc, "", after=1)
        p.runs[0].text = "\t"
        b.run(p, exp["contrat"], size=8.5, italic=True)
        b.run(p, "\t")
        b.run(p, exp["duree"], size=9, italic=True)

        sub_heading(doc, "Contexte")
        text_block(doc, exp["contexte"])
        sub_heading(doc, "Réalisations")
        for axe, items in exp["axes"]:
            b.bullet(doc, axe + " :", "", after=0)
            for j, item in enumerate(items):
                b.bullet(doc, "", item, level=1, after=1.5 if j == len(items) - 1 else 0)
        sub_heading(doc, "Résultats")
        for j, r in enumerate(exp["resultats"]):
            b.bullet(doc, "", r, after=0)
        p = b.para(doc, before=3, after=0, left=b.COL, line=1.05)
        b.run(p, "Méthodologie & outils : ", size=9, bold=True)
        b.run(p, exp["methodo_outils"], size=9)

    dates, poste, texte = LOUIS_VUITTON
    p = b.dated_line(doc, dates, before=8, after=1)
    b.run(p, poste, bold=True)
    b.bullet(doc, "", texte)

    # --- Formation, langues, centres d'intérêt (page 2 moins dense : on aère)
    b.SECTION_GAP = (14, 10)
    b.section(doc, "FORMATION")
    prev = None
    for dates, diplome, suite, ecole, *_ in b.CV["formation"]:
        p = b.dated_line(doc, dates, before=6 if prev and dates else 0)
        b.run(p, diplome, bold=True)
        b.run(p, suite)
        if ecole:
            p = b.para(doc, left=b.COL)
            b.run(p, ecole)
        prev = dates

    b.rule(doc, length_cm=3.2, before=b.SECTION_GAP[0], after=b.SECTION_GAP[1])
    for k, (langue, niveau) in enumerate(b.CV["langues"]):
        p = b.para(doc, after=1, left=b.COL + b.LABEL, first=-(b.COL + b.LABEL),
                   tabs=((b.COL, WD_TAB_ALIGNMENT.LEFT), (b.COL + b.LABEL, WD_TAB_ALIGNMENT.LEFT)))
        b.run(p, "LANGUES" if k == 0 else "")
        b.run(p, "\t")
        b.run(p, langue, bold=True)
        b.run(p, "\t" + niveau)
        p.paragraph_format.space_after = b.Pt(2)

    b.rule(doc, length_cm=3.2, before=b.SECTION_GAP[0], after=b.SECTION_GAP[1])
    p = b.para(doc, left=b.COL + b.LABEL, first=-(b.COL + b.LABEL),
               tabs=((b.COL + b.LABEL, WD_TAB_ALIGNMENT.LEFT),))
    b.run(p, "CENTRES D'INTÉRÊT\t" + b.CV["interets"])

    return b.save(doc, out_stem)


if __name__ == "__main__":
    for path in build():
        print(path)
