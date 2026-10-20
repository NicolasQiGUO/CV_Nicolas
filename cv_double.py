"""Version « double compétence » fonctionnelle et technique (dérivée de la version Randstad).

Title général IA & automatisation, sans le bloc projet e-Note de crédit ; développement low-code
en sous-point La Poste ; projets de développement académiques sous le Master 2.
"""
import copy

import build_cv
import cv_randstad

cv = copy.deepcopy(cv_randstad.cv)

cv["title"] = "CHEF DE PROJET SI | TRANSFORMATION DIGITALE | IA & AUTOMATISATION"

la_poste = cv["experiences"][1]
la_poste["bullets"] = [b for b in la_poste["bullets"] if not b[0].startswith("Projet e-Note")]
subs = la_poste["bullets"][0][2]
i = subs.index("Pilotage du développement (interne et prestataires), de la recette et de la mise en production")
subs.insert(i + 1, "Développement low-code (Power Apps, Power Automate)")

m2 = cv["formation"][1]
cv["formation"][1] = (*m2[:4],
    "Projets de développement : site e-commerce (PHP), BDD médicale (SQL), jeux (Java/C#), calcul d'impôt (C)")

cv["profil"] = cv["profil"].replace("Pilotage de projets SI Finance de bout en bout", "Pilotage de projets SI de bout en bout")
assert "SI Finance de bout" not in cv["profil"]

comp = []
for label, text in cv["competences"]:
    if label.startswith("Gestion de projet"):
        assert "Agile (notions)" in text
    elif label.startswith("Outils digitaux"):
        text = "Pack Office, Teams, SharePoint, Power Apps, Power Automate, Power BI"
    comp.append((label, text))
cv["competences"] = comp

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.SECTION_GAP = (6, 5)
    for path in build_cv.build("CV_NicolasQiGUO_DoubleCompetence"):
        print(path)
