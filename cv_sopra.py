"""Version ciblée Sopra HR Software — poste ouvert à la reconversion vers le SIRH.

Part du CV général (build_cv.CV) avec des retouches légères : on garde l'identité
« Chef de projet SI » et les responsabilités de pilotage (compétences transférables),
on ajoute le lien réel avec le SI RH (NOEMIE) et l'orientation SIRH dans le profil.
"""
import copy

import build_cv

cv = copy.deepcopy(build_cv.CV)

cv["title"] = "CHEF DE PROJET SI | APPLICATIONS MÉTIERS & SI RH"

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste) en pilotage de projets "
    "SI de bout en bout, de l'analyse des besoins à la recette et au déploiement, avec une pratique du "
    "low-code et des flux de données SI RH. Souhaite mettre cette double compétence "
    "au service de projets SIRH."
)

m2 = cv["formation"][1]
cv["formation"][1] = (*m2[:4], "Enseignements : ERP (SAP), bases de données, programmation, gestion de projet IT")

# La Poste : contenu du CV général + projet NOEMIE (application alimentée par le SI RH)
la_poste = cv["experiences"][1]
la_poste["bullets"].insert(1, (
    "Projet NOEMIE ",
    "(cartes de paiement des managers) : solution Power Platform alimentée par le SI RH "
    "(SharePoint, circuits d'approbation, notifications) ; cadrage, recette, mise en production", []))

bnp = cv["experiences"][0]
label, text, subs = bnp["bullets"][0]
bnp["bullets"][0] = (label,
    "conception et mise en place d'un dispositif de collecte, qualification et priorisation "
    "des use cases ; 20+\u00a0use\u00a0cases identifiés, 3 lancés en projet", subs)

gestion = build_cv.CV["competences"][0]
cv["competences"] = [
    (gestion[0], gestion[1].replace("gestion des risques – Cycle en V, Agile, hybride",
                                    "risques – Cycle en V, hybride, Agile (notions)")),
    ("Environnement SI : ", "SI Finance, interfaces SI RH, SAP, intégration applicative, gouvernance des SI"),
    build_cv.CV["competences"][2],   # Outils digitaux
    build_cv.CV["competences"][3],   # Langages (notions)
]
assert "Agile (notions)" in cv["competences"][0][1]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.TITLE_SIZE = 11.5
    build_cv.SECTION_GAP = (6, 5)
    for path in build_cv.build("CV_NicolasQiGUO_SopraHR"):
        print(path)
