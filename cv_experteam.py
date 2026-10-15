"""Version ciblée Experteam — Consultant technico-fonctionnel Microsoft 365 / Power Platform.

Part du CV général (build_cv.CV) et ne modifie que title, profil, bullets BNP / La Poste
et compétences. Faits confirmés : listes SharePoint comme source de données et flux
Power Automate connectés à SharePoint (La Poste), Microsoft 365 Copilot (BNP), ateliers,
documentation et formation utilisateurs. Power BI : utilisation seulement (non mis en avant).
"""
import copy

import build_cv

cv = copy.deepcopy(build_cv.CV)

cv["title"] = "CHEF DE PROJET SI TECHNICO-FONCTIONNEL | POWER PLATFORM & M365"

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP\u00a0Paribas, La\u00a0Poste). "
    "Référent Power Platform : conception et déploiement de solutions Power Apps, Power Automate "
    "et SharePoint, des ateliers de cadrage à la formation des utilisateurs. Conduite du changement "
    "et adoption de l'IA (dont Microsoft\u00a0365\u00a0Copilot) à grande échelle."
)

bnp = cv["experiences"][0]
label, text, subs = bnp["bullets"][1]
assert "(GenAI, RAG, Copilot)" in text
bnp["bullets"][1] = (label, text.replace("(GenAI, RAG, Copilot)", "(GenAI, RAG, Microsoft 365 Copilot)"), subs)
bnp["bullets"][2] = (
    "Conduite du changement ",
    "dans le cadre d'un programme IA transverse (5\u00a0000+\u00a0collaborateurs) : pilotage d'un site "
    "SharePoint de ressources, canaux Teams et animation d'un réseau de 70+ ambassadeurs IA, "
    "sessions d'acculturation", [])

la_poste = cv["experiences"][1]
la_poste["bullets"].insert(1, (
    "Projet e-Note de crédit ",
    "(digitalisation des notes de crédit, RPA + Power Platform) : développement de toute la partie "
    "Power Platform – interface Power Apps et flux Power Automate reliant les briques (RPA, SharePoint) ; "
    "délai de plusieurs semaines à quasi instantané, > 700\u00a0k€ de notes de crédit traitées", []))

label, text, subs = bnp["bullets"][0]
bnp["bullets"][0] = (label,
    "conception et mise en place d'un dispositif de collecte, qualification et priorisation "
    "des use cases ; 20+\u00a0use\u00a0cases identifiés, 3 lancés en projet", subs)

cv["competences"] = [
    ("Microsoft 365 : ", "Power Apps, Power Automate, SharePoint (listes, sites), Teams, Copilot"),
    ("Gestion de projet : ",
     "Cadrage, ateliers métiers, spécifications, recette, mise en production\n"
     "Documentation et formation utilisateurs, COPIL / COSUI – Agile, cycle en V"),
    build_cv.CV["competences"][1],   # Environnement SI
    build_cv.CV["competences"][3],   # Langages (notions)
]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.SECTION_GAP = (6, 5)
    for path in build_cv.build("CV_NicolasQiGUO_Experteam"):
        print(path)
