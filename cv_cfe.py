"""Version ciblée CFE (Caisse des Français de l'Étranger) — Chef de Projets MOA.

Part du CV général (build_cv.CV) et ne modifie que title, profil, bullets La Poste et compétences.
Faits MOA confirmés dans experiences.md (recette, chiffrage, procédures, support, TMA).
"""
import copy

import build_cv

cv = copy.deepcopy(build_cv.CV)

cv["title"] = "CHEF DE PROJETS MOA | SI & TRANSFORMATION DIGITALE"

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste). "
    "Pilotage de projets de bout en bout, de l'expression des besoins à la recette et au déploiement, "
    "coordination Métiers–IT et conduite du changement."
)

la_poste = cv["experiences"][1]
la_poste["bullets"] = [
    ("Pilotage de projets d'automatisation (RPA & Power Platform), dont 2 de bout en bout :", "", [
        "Ateliers métiers, cartographie des processus, cahiers des charges et spécifications fonctionnelles",
        "Coordination Métiers–IT, chiffrage, planning, risques, instances projets (COSUI, COPIL)",
        "Stratégie et cahiers de recette, pilotage de la recette fonctionnelle et suivi des anomalies",
        "Mises en production, accompagnement du déploiement et procédures utilisateurs (Finance, RH)",
    ]),
    ("Pilotage du RUN et support :", "", [
        "Monitoring d'une dizaine de robots en production, gestion des incidents, support fonctionnel",
        "Suivi des corrections avec les équipes de développement et la TMA / les prestataires",
        "Suivi de la performance (ROI, fiabilité, adoption) et amélioration continue",
    ]),
]

cv["competences"] = [
    ("Gestion de projet : ",
     "Expression des besoins, cahier des charges, cartographie des processus, cycle en V\n"
     "Stratégie et cahiers de recette, chiffrage, planning, COPIL / COSUI"),
    *build_cv.CV["competences"][1:],
]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.TITLE_SIZE = 11  # title court : un peu plus grand, profil plus large
    for path in build_cv.build("CV_NicolasQiGUO_CFE"):
        print(path)
