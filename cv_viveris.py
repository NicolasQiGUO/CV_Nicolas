"""Version ciblée Viveris (ESN, projets applicatifs / web) : double compétence fonctionnelle et technique.

Part du CV général (build_cv.CV) et ne modifie que title, profil, bullets La Poste,
compétences et la ligne projets sous le Master 2.
"""
import copy

import build_cv

cv = copy.deepcopy(build_cv.CV)

cv["title"] = "CHEF DE PROJET SI | TRANSFORMATION DIGITALE | PROJETS APPLICATIFS"

cv["profil"] = (
    "3 ans d'expérience au sein de grands groupes (BNP Paribas, La Poste). "
    "Pilotage de projets de bout en bout, coordination transverse Métiers–IT, "
    "gouvernance et conduite du changement. Double compétence fonctionnelle et technique : "
    "développement applicatif (projets académiques en Java, C#, PHP, SQL) et low-code (Power Platform)."
)

# Master 2 Paris Cité : projets académiques, classés par pertinence pour des projets web
m2 = cv["formation"][1]
cv["formation"][1] = (*m2[:4],
    "Projets : e-commerce (PHP/HTML/CSS), BDD médicale (PostgreSQL/Oracle), "
    "jeux (Java/C#), calcul d'impôt (C)")

la_poste = cv["experiences"][1]
subs = la_poste["bullets"][0][2]
i = subs.index("Pilotage du développement, de la recette et de la mise en production")
subs[i] = "Développement low-code (Power Apps, Power Automate), recette et mise en production"

cv["competences"] = [
    build_cv.CV["competences"][0],
    ("Environnement SI : ",
     "SI Finance, SAP (S/4HANA, ECC), intégration applicative, gouvernance des SI"),
    ("Outils digitaux : ", "Power Apps, Power Automate, Power BI, SharePoint"),
    ("Développement : ", "Java, C#, C, PHP, HTML/CSS, SQL (PostgreSQL, Oracle) ; Python (notions)"),
]

if __name__ == "__main__":
    build_cv.CV = cv
    build_cv.SECTION_GAP = (6, 5)  # contenu plus long : rubriques un peu plus serrées
    for path in build_cv.build("CV_NicolasQiGUO_Viveris"):
        print(path)
