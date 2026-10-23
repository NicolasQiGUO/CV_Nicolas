"""Version ciblée BNP Paribas TOP SERVICES / BPG — Chef de projet Portail BPG.

Part de la version Hôpital Américain (title sans IA, Agile en notions, Pack Office / Teams).
Met en avant : gouvernance projet, cadrage fonctionnel, chiffrage, portail SharePoint « point
d'entrée unique » (AI4ALL) et production de contenus / documentation utilisateurs.
"""
import copy

import build_cv
import cv_hopital

cv = copy.deepcopy(cv_hopital.cv)

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste). Pilotage de projets "
    "de bout en bout, du cadrage fonctionnel à la mise en production : planning, risques, gouvernance "
    "et reporting, coordination Métiers–IT et accompagnement des utilisateurs."
)

bnp = cv["experiences"][0]
bnp["bullets"][2] = (
    "Conduite du changement ",
    "dans le cadre d'un programme IA transverse (5 000+ collaborateurs) : pilotage d'un site "
    "SharePoint, point d'entrée unique des ressources IA, production de contenus et supports "
    "pédagogiques, animation de 70+ ambassadeurs IA", [])

subs = cv["experiences"][1]["bullets"][0][2]
for old, new in (
    ("Coordination Métiers–IT pour la coconception des solutions",
     "Coordination Métiers–IT, chiffrage et coconception des solutions"),
    ("Accompagnement du déploiement auprès des fonctions Finance et RH",
     "Accompagnement du déploiement, documentation et procédures utilisateurs (Finance, RH)"),
):
    subs[subs.index(old)] = new

cv["competences"][0] = (
    "Gestion de projet : ",
    "Cadrage fonctionnel, chiffrage, planning, jalons, dépendances, risques, livrables\n"
    "Gouvernance (COPIL / COSUI), reporting – Cycle en V, hybride, Agile (notions)")

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.TITLE_SIZE = 11.5  # même en-tête que la version Hôpital
    for path in build_cv.build("CV_NicolasQiGUO_BNP_BPG"):
        print(path)
