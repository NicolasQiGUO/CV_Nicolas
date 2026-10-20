"""Version ciblée Hôpital Américain de Paris — Chef de Projet (projets numériques, bout en bout).

Part du CV général sans retoucher les expériences : title sans IA, profil « du cadrage à la mise
en production », Agile en notions (l'offre cite Scrum / Jira), Teams et Pack Office dans les outils.
"""
import copy

import build_cv

cv = copy.deepcopy(build_cv.CV)

cv["title"] = "CHEF DE PROJET SI | TRANSFORMATION DIGITALE"

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste). "
    "Pilotage de projets de bout en bout, du cadrage des besoins à la mise en production, "
    "coordination transverse Métiers–IT, gouvernance et conduite du changement."
)

bnp = cv["experiences"][0]
label, text, subs = bnp["bullets"][0]
bnp["bullets"][0] = (label,
    "conception et mise en place d'un dispositif de collecte, qualification et priorisation "
    "des use cases ; 20+\u00a0use\u00a0cases identifiés, 3 lancés en projet", subs)

gestion = build_cv.CV["competences"][0]
cv["competences"] = [
    gestion,                         # Gestion de projet (CV général, Agile en notions)
    build_cv.CV["competences"][1],   # Environnement SI
    ("Outils digitaux : ", "Pack Office, Teams, SharePoint, Power Apps, Power Automate, Power BI"),
    build_cv.CV["competences"][3],   # Langages (notions)
]
assert "Agile (notions)" in cv["competences"][0][1]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.TITLE_SIZE = 11.5  # title court : un peu plus grand, profil plus large
    for path in build_cv.build("CV_NicolasQiGUO_HopitalAmericain"):
        print(path)
