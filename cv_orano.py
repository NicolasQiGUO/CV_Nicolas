"""Version ciblée Orano — Chargé(e) de Projet IA (cellule IA, programme Aval du Futur).

Part du CV général (build_cv.CV). Met en avant BNP (cas d'usage IA, gouvernance, adoption) ;
Agile écrit en « notions » (pratique réelle : cycle en V / hybride).
"""
import copy

import build_cv

cv = copy.deepcopy(build_cv.CV)

cv["title"] = "CHARGÉ DE PROJETS IA | TRANSFORMATION DIGITALE"

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste). Identification, "
    "qualification et priorisation de cas d'usage IA, coordination métiers, IT et experts IA, accompagnement "
    "du déploiement et conduite du changement à grande échelle. Formation en informatique et management des SI."
)

bnp = cv["experiences"][0]
bnp["bullets"] = [
    ("Structuration et coordination des initiatives IA & RPA : ",
     "conception et mise en place d'un dispositif de collecte, de qualification (valeur, ROI, faisabilité) "
     "et de priorisation des use cases jusqu'au comité d'arbitrage ; 20+ use cases identifiés, "
     "3 lancés en projet", []),
    ("Pilotage et gouvernance des projets IA : ",
     "cadrage des besoins avec les métiers, coordination métiers, IT et experts IA, conduite de POC, "
     "accompagnement du déploiement de 3 solutions IA (GenAI, RAG, Microsoft 365 Copilot) et reporting "
     "auprès des instances de gouvernance", []),
    ("Conduite du changement ",
     "dans le cadre d'un programme IA transverse (5 000+ collaborateurs) : acculturation, "
     "supports pédagogiques, site SharePoint dédié, animation de 70+ ambassadeurs IA", []),
]

cv["competences"] = [
    ("Gestion de projet : ",
     "Cadrage, recueil des besoins, spécifications, recette, mise en production\n"
     "Gouvernance (COPIL / COSUI), risques, KPI – Cycle en V, hybride, Agile (notions)"),
    ("IA & outils : ", "GenAI, RAG, Microsoft 365 Copilot, RPA, Power Platform, SharePoint"),
    build_cv.CV["competences"][1],   # Environnement SI
    build_cv.CV["competences"][3],   # Langages (notions)
]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.TITLE_SIZE = 11.5  # title court : un peu plus grand, profil plus large
    for path in build_cv.build("CV_NicolasQiGUO_Orano"):
        print(path)
