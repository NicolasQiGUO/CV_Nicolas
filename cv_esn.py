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

# Savoir-faire, du plus au moins maîtrisé : (domaine, description). Les preuves sont dans les expériences.
SAVOIR_FAIRE = [
    ("Pilotage de projets SI",
     "conduite de projets du cadrage à la mise en production : chiffrage des charges, planification, "
     "suivi des risques, animation des COPIL / COSUI, organisation de la recette et accompagnement du déploiement"),
    ("Analyse des besoins (AMOA)",
     "animation d'ateliers métiers, cartographie des processus existants et cibles, rédaction des cahiers "
     "des charges et des spécifications fonctionnelles et techniques, stratégies et cahiers de recette"),
    ("Coordination Métiers–IT",
     "interface entre métiers, équipes de développement, experts IA et prestataires : traduction des besoins "
     "en solutions, suivi des développements et des corrections avec la TMA"),
    ("Conduite du changement",
     "conception d'actions d'acculturation et de supports pédagogiques, animation d'une communauté "
     "d'utilisateurs, formation et accompagnement des utilisateurs, rédaction de procédures et de guides"),
    ("IA & automatisation",
     "collecte, qualification (impact business, ROI, faisabilité, conformité) et priorisation de cas d'usage "
     "IA & RPA ; accompagnement du déploiement de solutions GenAI (RAG, Microsoft 365 Copilot)"),
    ("Développement low-code",
     "conception et développement d'applications Power Apps et de flux Power Automate connectés à SharePoint"),
    ("RUN & amélioration continue",
     "supervision de robots en production, gestion des incidents et des montées de version, suivi des KPI "
     "(ROI, fiabilité, adoption)"),
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
        "dates": "2024 – 2025", "duree": "1 an et 4 mois", "contrat": "Alternance",
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
        "dates": "2022 – 2024", "duree": "2 ans", "contrat": "Alternance + CDD",
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


def block_line(doc, label, text="", bullet=None, bold_text=False, before=0, after=0, size=None):
    """Ligne dont le libellé de bloc (CONTEXTE, RÉALISATIONS…) est centré dans la colonne des dates."""
    left = b.COL if bullet is None else b.BUL
    tabs = [(b.DATE_CENTER, WD_TAB_ALIGNMENT.CENTER)]
    if bullet is not None:
        tabs.append((b.BUL - 0.4, WD_TAB_ALIGNMENT.LEFT))
    tabs.append((left, WD_TAB_ALIGNMENT.LEFT))
    p = b.para(doc, before=before, after=after, left=left, first=-left, tabs=tabs, line=1.05)
    b.run(p, "\t")
    if label:
        b.run(p, label, size=8, bold=True, color=b.GREY)
    b.run(p, "\t")
    if bullet is not None:
        b.run(p, bullet + "\t", size=None if bullet == "•" else 7.5)
    if text:
        b.run(p, text, bold=bold_text, size=size)
    return p


def build(out_stem="CV_NicolasQiGUO_ESN"):
    doc = b.new_document()
    b.write_header(doc, CV)
    b.rule(doc, before=9, after=6)

    # --- Savoir-faire (en tête, du plus au moins maîtrisé)
    b.section(doc, "COMPÉTENCES CLÉS", first=True)
    for domaine, quoi in SAVOIR_FAIRE:
        p = b.para(doc, after=2, left=b.BUL, first=-0.4, tabs=((b.BUL, WD_TAB_ALIGNMENT.LEFT),), line=1.05)
        b.run(p, "•\t")
        b.run(p, domaine + " : ", bold=True)
        b.run(p, quoi)

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

        block_line(doc, "CONTEXTE", exp["contexte"], before=4, after=1)
        for k, (axe, items) in enumerate(exp["axes"]):
            block_line(doc, "RÉALISATIONS" if k == 0 else "", axe + " :", bullet="•", bold_text=True,
                       before=4 if k == 0 else 1)
            for item in items:
                b.bullet(doc, "", item, level=1, after=0)
        for k, res in enumerate(exp["resultats"]):
            block_line(doc, "RÉSULTATS" if k == 0 else "", res, bullet="•", before=5 if k == 0 else 0)
        block_line(doc, "OUTILS", exp["methodo_outils"], before=5, size=9)

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
