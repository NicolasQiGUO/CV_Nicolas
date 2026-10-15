"""Version ciblée Sopra HR Software — Consultant(e) SIRH junior (reconversion).

Part du CV général (build_cv.CV). Positionnement « consultant SI qui se spécialise en SIRH » :
liens réels avec le SIRH (périmètre La Poste, NOEMIE alimenté par le SI RH, déploiement RH),
analyse / recette / évolutions-corrections, BNP resserré pour éviter l'effet surqualifié.
"""
import copy

import build_cv

cv = copy.deepcopy(build_cv.CV)

cv["title"] = "CONSULTANT SIRH | SI RH & TRANSFORMATION DIGITALE"

cv["profil"] = (
    "3 ans d'expérience en projets SI au sein de grands groupes (BNP Paribas, La Poste), "
    "dont des solutions s'appuyant sur le SI RH. Analyse des besoins, spécifications, recette, "
    "évolutions et corrections, en lien avec les métiers et les équipes techniques. "
    "Bases en low-code, programmation et bases de données."
)

m2 = cv["formation"][1]
cv["formation"][1] = (*m2[:4], "Enseignements : ERP (SAP), bases de données, programmation, gestion de projet IT")

bnp = cv["experiences"][0]
bnp["bullets"] = [
    ("Qualification et priorisation des use cases IA & RPA : ",
     "conception du dispositif de collecte et de qualification ; 20+ use cases identifiés, 3 lancés en projet", []),
    ("Coordination de projets IA : ",
     "recueil des besoins, coordination Métiers–IT, POC, organisation des recettes utilisateurs et "
     "accompagnement du déploiement (GenAI, RAG, Copilot)", []),
    ("Conduite du changement : ",
     "programme IA transverse (5 000+ collaborateurs), animation de 70+ ambassadeurs IA", []),
]

la_poste = cv["experiences"][1]
la_poste["bullets"] = [
    ("Pilotage de projets d'automatisation (RPA & Power Platform), dont 2 de bout en bout :", "", [
        "Analyse des besoins métiers (Finance, RH), cahiers des charges et spécifications fonctionnelles",
        "Développement low-code (Power Apps, Power Automate, SharePoint) et coordination Métiers–IT",
        "Stratégie et cahiers de recette, tests, suivi des anomalies et validation",
        "Mise en production, accompagnement du déploiement et documentation utilisateurs (Finance, RH)",
    ]),
    ("Projet NOEMIE ",
     "(cartes de paiement des managers) : solution Power Platform alimentée par le SI RH "
     "(SharePoint, circuits d'approbation, notifications) ; cadrage, recette, mise en production", []),
    ("Pilotage du RUN :", "", [
        "Monitoring d'une dizaine de robots en production, gestion des incidents et support fonctionnel",
        "Suivi des corrections et évolutions avec la TMA / les prestataires, amélioration continue",
    ]),
]

cv["competences"] = [
    ("Analyse & recette : ", "Recueil des besoins, spécifications, cahiers de recette, tests, gestion des anomalies"),
    ("Gestion de projet : ", "Planning, COPIL / COSUI, risques, documentation – Cycle en V, hybride"),
    ("Environnement SI : ", "SIRH (flux de données RH), SI Finance, SAP, Power Platform, SharePoint"),
    build_cv.CV["competences"][3],   # Langages (notions)
]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.TITLE_SIZE = 11.5
    for path in build_cv.build("CV_NicolasQiGUO_SopraHR"):
        print(path)
