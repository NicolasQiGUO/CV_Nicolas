"""Version ciblée Cocoon — Chargé d'Études MOA (recette, maintenance applicative, évolutions).

Reprend la version CFE (MOA, recette, RUN / TMA) ; change le profil (suivi des anomalies et des
évolutions applicatives) et ajoute le Pack Office demandé par l'offre.
"""
import copy

import build_cv
import cv_cfe

cv = copy.deepcopy(cv_cfe.cv)

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste). "
    "Pilotage de projets, de l'expression des besoins à la recette et à la mise en "
    "production, suivi des anomalies et des évolutions applicatives, coordination Métiers–IT."
)

cv["competences"] = [
    ("Outils digitaux : ", "Pack Office (Word, Excel, PowerPoint), Power Apps, Power Automate, SharePoint")
    if label.startswith("Outils digitaux") else (label, text)
    for label, text in cv["competences"]
]
assert any("Pack Office" in t for _, t in cv["competences"])

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.TITLE_SIZE = 11  # même mise en page que la version CFE
    for path in build_cv.build("CV_NicolasQiGUO_Cocoon"):
        print(path)
