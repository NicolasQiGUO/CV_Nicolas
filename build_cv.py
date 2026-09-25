"""Génère le CV (DOCX + PDF) à partir du contenu défini dans CV ci-dessous.

Usage : python3 build_cv.py [nom_de_sortie]
Pour une version ciblée : dupliquer ce fichier (ou le dict CV) et n'ajuster que
TITLE, PROFIL, les bullets BNP / La Poste et COMPETENCES.
"""
import copy
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).parent
FONT = "Times New Roman"
BLACK = RGBColor(0x00, 0x00, 0x00)
GREY = RGBColor(0x40, 0x40, 0x40)
RULE = "A6A6A6"

# Géométrie (cm) : colonne gauche (dates / rubriques) + colonne de contenu
DATE_CENTER = 1.45
COL = 3.2
BUL = COL + 0.45
SUB = BUL + 0.55
SIZE = 9.5
LABEL = 3.3  # largeur des libellés Compétences / Langues

CV = {
    "nom": "NICOLAS QI GUO",
    "title": "CHEF DE PROJET SI | TRANSFORMATION IA & AUTOMATISATION",
    "contact": [
        "Orléans, France | Mobilité Île-de-France",
        "+33 6 30 23 24 41 | qi.guo@essec.edu",
    ],
    "profil": (
        "Chef de projet SI, 3 ans d'expérience en transformation digitale (BNP\u00a0Paribas, La\u00a0Poste), "
        "spécialisé dans le pilotage de bout en bout de projets IA et d'automatisation."
    ),
    "formation": [
        ("2024 – 2025",
         "Mastère spécialisé en Management des Systèmes d'Information en Réseaux",
         " – Major de promotion", "ESSEC Business School & Télécom Paris"),
        ("2022 – 2023",
         "Master 2 en Projets Informatiques et Stratégie d'entreprise",
         " – Major de promotion", "Université Paris Cité"),
        ("Avant 2016",
         "Master en Littératures Françaises",
         " – Université Paris-Sorbonne", None),
        ("",
         "Licence en Langue Française",
         " – Xi'an JiaoTong University, Chine", None),
    ],
    "experiences": [
        {
            "dates": "2024 – 2025",
            "poste": "Digital Transformation Project Manager – AIR TECH",
            "entreprise": "BNP PARIBAS",
            "contrat": "Alternance",
            "perimetre": "Périmètre : Compliance & Risk (AML, sanctions, contrôle et monitoring, sécurité financière)",
            "bullets": [
                ("Structuration et coordination des initiatives IA & RPA : ",
                 "co-construction d'un dispositif de qualification et de priorisation des use cases "
                 "(valeur business, ROI, faisabilité technique) ; 20+ use cases identifiés, "
                 "dont 3 retenus pour un lancement en projet", []),
                ("Pilotage et gouvernance des projets IA : ",
                 "recueil et formalisation des besoins, coordination transverse métiers / IT, "
                 "conduite de POC, coordination et suivi de l'industrialisation de 3 solutions IA "
                 "(GenAI, RAG, Copilot), reporting auprès des instances de gouvernance", []),
                ("Conduite du changement ",
                 "dans le cadre du déploiement d'un programme IA à grande échelle (5\u00a0000+\u00a0collaborateurs) : "
                 "animation d'un réseau de 70+ ambassadeurs IA, sessions d'onboarding et d'acculturation, "
                 "événements communautaires", []),
            ],
        },
        {
            "dates": "2022 – 2024",
            "poste": "Chef de Projet SI – Data Intelligence & Innovation DTSFG",
            "entreprise": "LA POSTE GROUPE",
            "contrat": "Alternance + CDD",
            "perimetre": "Périmètre : Direction de la Transformation des Solutions Finance (SI Finance, SIRH, SAP)",
            "bullets": [
                ("Pilotage de projets d'automatisation (RPA & Power Platform), dont 2 de bout en bout :", "", [
                    "Recueil et analyse des besoins métiers, rédaction des cahiers des charges et spécifications fonctionnelles",
                    "Coordination métiers / IT pour la coconception des solutions",
                    "Pilotage du développement, de la recette et de la mise en production",
                    "Gestion des risques et animation des instances projets (COSUI, COPIL)",
                    "Accompagnement du déploiement auprès des fonctions Finance et RH",
                ]),
                ("Phase RUN :", "", [
                    "Monitoring quotidien d'une dizaine de robots en production et gestion des incidents",
                    "Suivi de la performance des solutions déployées (ROI, fiabilité, adoption)",
                    "Identification et mise en œuvre d'axes d'amélioration continue",
                ]),
            ],
        },
        {
            "dates": "2018 – 2022",
            "poste": "Retail & VIP Guest Relations",
            "entreprise": "LOUIS VUITTON",
            "contrat": "",
            "perimetre": None,
            "bullets": [
                ("", "Gestion d'une clientèle VIP internationale : sens du service et adaptation en contexte multiculturel", []),
            ],
        },
    ],
    "competences": [
        ("Gestion de projet : ",
         "Cadrage, recueil des besoins, spécifications, recette, mise en production\n"
         "Gouvernance (COPIL / COSUI), gestion des risques – Cycle en V, Agile, hybride"),
        ("Environnement SI : ",
         "SI Finance, SAP, intégration applicative, sécurité, conformité et gouvernance des SI"),
        ("Outils digitaux : ", "Power Apps, Power Automate, Power BI, SharePoint"),
        ("Langages (notions) : ", "Python, SQL, Java, PHP, HTML/CSS, C, C#"),
    ],
    "langues": [
        ("Anglais", "Professionnel (TOEIC 955/990)"),
        ("Français", "Bilingue"),
        ("Chinois", "Langue maternelle"),
    ],
    "interets": "Crossfit, natation, voyages (18 pays), engagement associatif (protection animale)",
}


def para(doc, before=0, after=0, line=1.0, left=None, first=None, tabs=(), keep=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    if left is not None:
        pf.left_indent = Cm(left)
    if first is not None:
        pf.first_line_indent = Cm(first)
    for pos, align in tabs:
        pf.tab_stops.add_tab_stop(Cm(pos), align)
    pf.keep_with_next = keep
    return p


def run(p, text, size=None, bold=False, italic=False, color=BLACK, underline=False):
    r = p.add_run(text)
    r.font.name = FONT
    r._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), FONT)
    r.font.size = Pt(size or SIZE)
    r.bold = bold
    r.italic = italic
    r.underline = underline
    r.font.color.rgb = color
    return r


def rule(doc, length_cm=None, before=6, after=6):
    """Filet gris fin ; court (length_cm) ou pleine largeur."""
    p = para(doc, before=before, after=after, line=0.1)
    if length_cm is not None:
        p.paragraph_format.right_indent = Cm(CONTENT_WIDTH - length_cm)
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    for k, v in (("w:val", "single"), ("w:sz", "4"), ("w:space", "1"), ("w:color", RULE)):
        b.set(qn(k), v)
    bdr.append(b)
    pPr.append(bdr)
    run(p, "", size=2)


def section(doc, title, first=False):
    if not first:
        rule(doc, length_cm=3.2, before=10, after=8)
    p = para(doc, after=5, keep=True)
    run(p, title)


def dated_line(doc, dates, before=0, after=0):
    """Ligne avec date centrée dans la colonne gauche et contenu en colonne droite."""
    from docx.enum.text import WD_TAB_ALIGNMENT
    p = para(doc, before=before, after=after, left=COL, first=-COL,
             tabs=((DATE_CENTER, WD_TAB_ALIGNMENT.CENTER), (COL, WD_TAB_ALIGNMENT.LEFT)), keep=True)
    run(p, "\t" + dates + "\t")
    return p


def bullet(doc, label, text, level=0, after=1):
    from docx.enum.text import WD_TAB_ALIGNMENT
    left = BUL if level == 0 else SUB
    p = para(doc, after=after, left=left, first=-0.4, tabs=((left, WD_TAB_ALIGNMENT.LEFT),))
    run(p, ("•" if level == 0 else "▪") + "\t", size=None if level == 0 else 7.5)
    if label:
        run(p, label, bold=True)
    if text:
        run(p, text)


def float_picture(paragraph, path, width_cm, top_offset_cm=0):
    """Ajoute une image flottante (ancrée à droite) sans casser le flux texte."""
    r = paragraph.add_run()
    inline = r.add_picture(str(path), width=Cm(width_cm))._inline
    cx, cy = inline.extent.cx, inline.extent.cy
    anchor = OxmlElement("wp:anchor")
    for k, v in (("distT", "0"), ("distB", "0"), ("distL", "114300"), ("distR", "0"),
                 ("simplePos", "0"), ("relativeHeight", "251658240"), ("behindDoc", "0"),
                 ("locked", "0"), ("layoutInCell", "1"), ("allowOverlap", "1")):
        anchor.set(k, v)
    sp = OxmlElement("wp:simplePos"); sp.set("x", "0"); sp.set("y", "0"); anchor.append(sp)
    ph = OxmlElement("wp:positionH"); ph.set("relativeFrom", "margin")
    al = OxmlElement("wp:align"); al.text = "right"; ph.append(al); anchor.append(ph)
    pv = OxmlElement("wp:positionV"); pv.set("relativeFrom", "paragraph")
    po = OxmlElement("wp:posOffset"); po.text = str(int(Cm(top_offset_cm))); pv.append(po); anchor.append(pv)
    ext = OxmlElement("wp:extent"); ext.set("cx", str(cx)); ext.set("cy", str(cy)); anchor.append(ext)
    ee = OxmlElement("wp:effectExtent")
    for k in ("l", "t", "r", "b"):
        ee.set(k, "0")
    anchor.append(ee)
    wrap = OxmlElement("wp:wrapSquare"); wrap.set("wrapText", "bothSides"); anchor.append(wrap)
    for child in ("wp:docPr", "wp:cNvGraphicFramePr", "a:graphic"):
        el = inline.find(qn(child))
        if el is not None:
            anchor.append(copy.deepcopy(el))
    inline.getparent().replace(inline, anchor)


def text_width_cm(text, size, bold=False):
    """Largeur d'un texte en Times (pour caler le bloc d'en-tête sur la ligne de title)."""
    try:
        import pymupdf
        return pymupdf.Font("tibo" if bold else "tiro").text_length(text, fontsize=size) / 72 * 2.54
    except ImportError:
        return len(text) * size * (0.26 if bold else 0.24) / 72 * 2.54


PAGE_W, MARGIN_LR = 21.0, 1.5
CONTENT_WIDTH = PAGE_W - 2 * MARGIN_LR
HEADER_INDENT = 0
PHOTO_W = 4.4
TITLE_SIZE = 10.5


def build(out_stem):
    from docx.enum.text import WD_TAB_ALIGNMENT
    doc = Document()
    s = doc.sections[0]
    s.page_height, s.page_width = Cm(29.7), Cm(PAGE_W)
    s.top_margin, s.bottom_margin = Cm(1.0), Cm(0.7)
    s.left_margin = s.right_margin = Cm(MARGIN_LR)
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(SIZE)

    # --- En-tête : title > nom > coordonnées > profil ; photo seule à droite.
    # Tout le texte s'arrête avant la photo (retrait droit) pour laisser la colonne photo nette.
    right = CONTENT_WIDTH - HEADER_INDENT - text_width_cm(CV["title"], TITLE_SIZE, bold=True) - 0.05

    def head(after=0, before=0):
        p = para(doc, before=before, after=after, left=HEADER_INDENT)
        p.paragraph_format.right_indent = Cm(right)
        return p

    p = head()
    photo = ROOT / "assets" / "photo.png"
    if photo.exists():
        float_picture(p, photo, width_cm=PHOTO_W, top_offset_cm=0.1)
    run(p, CV["title"], size=TITLE_SIZE, bold=True)

    p = head(before=6, after=1)
    run(p, CV["nom"], size=10, bold=True)
    for line in CV["contact"]:
        p = head()
        run(p, line, size=9)

    p = head(before=7)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run(p, "Profil : ", bold=True)
    run(p, CV["profil"])

    rule(doc, before=8, after=7)

    # --- Expériences
    section(doc, "EXPÉRIENCES PROFESSIONNELLES", first=True)
    for i, exp in enumerate(CV["experiences"]):
        p = dated_line(doc, exp["dates"], before=9 if i else 0)
        run(p, exp["poste"] + " @ " + exp["entreprise"], bold=True)
        if exp["perimetre"]:
            # le type de contrat se place sous la date, dans la colonne gauche
            p = dated_line(doc, "", after=2)
            p.runs[0].text = "\t"
            run(p, exp["contrat"], size=8.5, italic=True)
            run(p, "\t")
            run(p, exp["perimetre"], size=9, italic=True)
        else:
            p.paragraph_format.space_after = Pt(2)
        for label, text, subs in exp["bullets"]:
            bullet(doc, label, text, after=1 if subs else 2)
            for j, sub in enumerate(subs):
                bullet(doc, "", sub, level=1, after=2 if j == len(subs) - 1 else 0)

    # --- Formation
    section(doc, "FORMATION")
    prev = None
    for dates, diplome, suite, ecole in CV["formation"]:
        p = dated_line(doc, dates, before=4 if prev and dates else 0)
        run(p, diplome, bold=True)
        run(p, suite)
        if ecole:
            p = para(doc, left=COL)
            run(p, ecole)
        prev = dates

    # --- Compétences / Langues / Intérêts : rubrique en colonne gauche, sur la 1re ligne
    def label_rows(title, rows, after=1):
        rule(doc, length_cm=3.2, before=10, after=8)
        for k, (label, text) in enumerate(rows):
            p = para(doc, after=after, left=COL + LABEL, first=-(COL + LABEL),
                     tabs=((COL, WD_TAB_ALIGNMENT.LEFT), (COL + LABEL, WD_TAB_ALIGNMENT.LEFT)))
            run(p, title if k == 0 else "")
            run(p, "\t")
            run(p, label.rstrip(), bold=True)
            run(p, "\t" + text)

    label_rows("COMPÉTENCES", CV["competences"], after=2)
    label_rows("LANGUES", CV["langues"])

    rule(doc, length_cm=3.2, before=10, after=8)
    p = para(doc, left=COL + LABEL, first=-(COL + LABEL), tabs=((COL + LABEL, WD_TAB_ALIGNMENT.LEFT),))
    run(p, "CENTRES D'INTÉRÊT\t" + CV["interets"])

    out_dir = ROOT / "output"
    out_dir.mkdir(exist_ok=True)
    docx_path = out_dir / f"{out_stem}.docx"
    doc.save(docx_path)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(out_dir), str(docx_path)],
                   check=True, capture_output=True)
    return docx_path, out_dir / f"{out_stem}.pdf"


if __name__ == "__main__":
    stem = sys.argv[1] if len(sys.argv) > 1 else "CV_NicolasQiGUO_General"
    for path in build(stem):
        print(path)
