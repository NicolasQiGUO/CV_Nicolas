"""Version ciblée Randstad Professional (Orléans) — Chef de Projets Informatique, focus Finance / ERP.

Part du CV général (build_cv.CV). SQL en simples notions : pas de détail (vues, procédures) qui laisserait croire à une pratique actuelle.
"""
import copy

import build_cv

cv = copy.deepcopy(build_cv.CV)

cv["title"] = "CHEF DE PROJET INFORMATIQUE | SI FINANCE & APPLICATIONS MÉTIERS"

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste). "
    "Pilotage de projets SI Finance de bout en bout, du recueil des besoins à la recette et au "
    "déploiement, coordination Métiers–IT et pilotage de prestataires. Double compétence fonctionnelle "
    "et technique, avec une expérience en développement low-code (Power Platform) et des bases en "
    "programmation et bases de données acquises en formation."
)

# Master 2 : enseignements utiles pour un poste ERP / SQL
m2 = cv["formation"][1]
cv["formation"][1] = (*m2[:4],
    "Enseignements : ERP (SAP), bases de données relationnelles (PostgreSQL, Oracle)")

# BNP : moins central pour ce poste, version resserrée
bnp = cv["experiences"][0]
label, text, subs = bnp["bullets"][0]
bnp["bullets"][0] = (label,
    "conception et mise en place d'un dispositif de collecte, qualification et priorisation "
    "des use cases ; 20+\u00a0use\u00a0cases identifiés, 3 lancés en projet", subs)
bnp["bullets"][2] = ("Conduite du changement ",
    "dans le cadre d'un programme IA transverse (5\u00a0000+\u00a0collaborateurs) : "
    "animation d'un réseau de 70+ ambassadeurs IA, sessions d'acculturation", [])

la_poste = cv["experiences"][1]
subs = la_poste["bullets"][0][2]
i = subs.index("Pilotage du développement, de la recette et de la mise en production")
subs[i] = "Pilotage du développement (interne et prestataires), de la recette et de la mise en production"
la_poste["bullets"].insert(1, (
    "Projet e-Note de crédit ",
    "(création et comptabilisation dans SAP des notes de crédit) : développement de la partie "
    "Power Platform ; délai de plusieurs semaines à quasi instantané, > 700 k€ de notes de crédit traitées", []))

cv["competences"] = [
    build_cv.CV["competences"][0],   # Gestion de projet
    ("Environnement SI : ", "SI Finance, SAP, interfaces applicatives, gouvernance des SI"),
    build_cv.CV["competences"][2],   # Outils digitaux
    ("Langages (notions) : ",
     "SQL, PHP, Java, C#, C, Python, HTML/CSS"),
]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.SECTION_GAP = (6, 5)
    for path in build_cv.build("CV_NicolasQiGUO_Randstad"):
        print(path)
