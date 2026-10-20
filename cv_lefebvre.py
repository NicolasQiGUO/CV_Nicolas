"""Version ciblée Lefebvre Dalloz — Responsable IA & Digitalisation (Direction du Care).

Title du CV général conservé. Met en avant : cas d'usage IA / automatisation à fort ROI (BNP,
version Orano), développement low-code et résultat e-Note de crédit (La Poste, version Experteam),
adoption et culture IA, KPI / ROI, sens du service client (Louis Vuitton).
"""
import copy

import build_cv
import cv_experteam
import cv_orano

cv = copy.deepcopy(build_cv.CV)

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste). Identification et "
    "priorisation de cas d'usage IA et d'automatisation à fort ROI, développement low-code (référent "
    "Power Platform), conduite du changement et adoption à grande échelle. Sens du service client "
    "acquis en relation client VIP."
)

# BNP : formulation Orano (critères de qualification, comité, experts IA, Microsoft 365 Copilot)
bnp = cv["experiences"][0]
bnp["bullets"] = copy.deepcopy(cv_orano.cv["experiences"][0]["bullets"])

# La Poste : contenu général + projet e-Note de crédit (rédaction Experteam)
la_poste = cv["experiences"][1]
enote = next(b for b in cv_experteam.cv["experiences"][1]["bullets"] if b[0].startswith("Projet e-Note"))
la_poste["bullets"].insert(1, copy.deepcopy(enote))

cv["competences"] = [
    ("Gestion de projet : ",
     "Cadrage, recueil des besoins, POC, recette, déploiement, KPI / ROI\n"
     "Gouvernance (COPIL / COSUI), risques – Cycle en V, hybride, Agile (notions)"),
    ("IA & automatisation : ", "GenAI, RAG, Microsoft 365 Copilot, RPA, low-code (Power Platform)"),
    ("Outils digitaux : ", "Pack Office, Teams, SharePoint, Power BI"),
    build_cv.CV["competences"][3],   # Langages (notions)
]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.SECTION_GAP = (6, 5)
    for path in build_cv.build("CV_NicolasQiGUO_LefebvreDalloz"):
        print(path)
