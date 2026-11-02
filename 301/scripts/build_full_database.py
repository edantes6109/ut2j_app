#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the full UE301_questions_database.xlsx
Matches UE304_questions_database.xlsx in structure, styling, and column ordering.
"""

import os
import json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

from data_exams_part1 import EXAMS_PART1
from data_exams_part2 import EXAMS_PART2
from data_exams_part3 import EXAMS_PART3
from data_open_questions import OPEN_QUESTIONS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "..", "docs")
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
OUTPUT_XLSX = os.path.join(DOCS_DIR, "UE301_questions_database.xlsx")

def main():
    os.makedirs(DOCS_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

    all_exams = EXAMS_PART1 + EXAMS_PART2 + EXAMS_PART3
    total_qcm = sum(len(e["questions"]) for e in all_exams)
    print(f"Loaded {len(all_exams)} exams with a total of {total_qcm} QCM questions.")
    print(f"Loaded {len(OPEN_QUESTIONS)} open questions.")

    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # remove default sheet

    header_font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")
    header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

    cell_font = Font(name="Arial", size=9)
    cell_align_left = Alignment(horizontal="left", vertical="top", wrap_text=True)
    cell_align_center = Alignment(horizontal="center", vertical="top", wrap_text=True)

    thin_border = Border(
        left=Side(style="thin", color="D9D9D9"),
        right=Side(style="thin", color="D9D9D9"),
        top=Side(style="thin", color="D9D9D9"),
        bottom=Side(style="thin", color="D9D9D9")
    )

    # -------------------------------------------------------------------------
    # 1. SHEET: QCM
    # -------------------------------------------------------------------------
    ws_qcm = wb.create_sheet(title="QCM")
    ws_qcm.views.sheetView[0].showGridLines = True
    qcm_headers = [
        "Document", "Source file(s)", "Q n°", "Theme / chapter", "Question",
        "Answer A", "Answer B", "Answer C", "Answer D", "Answer E", "Answer F", "Answer G", "Answer",
        "Correction Source"
    ]
    ws_qcm.append(qcm_headers)
    ws_qcm.row_dimensions[1].height = 28

    for col_idx in range(1, len(qcm_headers) + 1):
        cell = ws_qcm.cell(1, col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align

    qcm_col_widths = {
        "A": 24, "B": 35, "C": 8, "D": 42, "E": 65,
        "F": 35, "G": 35, "H": 35, "I": 35, "J": 35, "K": 35, "L": 35, "M": 14, "N": 35
    }
    for col_letter, width in qcm_col_widths.items():
        ws_qcm.column_dimensions[col_letter].width = width

    OFFICIAL_CORRECTIONS_301 = {
        "Exemple de sujet d'examen (C. Sorsana)": (
            "official",
            "Corrigé officiel",
            "UE301_Corrige_Sujet_Examen.docx (Document officiel enseignant C. Sorsana)"
        ),
        "2025-2026 – CC2 et CT SED": (
            "official",
            "Corrigé officiel",
            "annale_301_2025_2026_session1.csv (Grille officielle UT2J SED)"
        ),
        "2024-2025 – Seconde chance SED": (
            "official",
            "Corrigé officiel",
            "correction 2nd chance dev 2025.docx.pdf (Grille officielle de notation)"
        ),
        "2023-2024 – Session 1": (
            "official",
            "Corrigé officiel",
            "Annale 301 - 2023_2024 - Session 1 CORRECTION.pdf (Document officiel)"
        ),
        "2018-2019 – Session 2": (
            "official",
            "Corrigé officiel",
            "Annale 301 - 2018-2019 Session 2.pdf (Page 3, encart CORRECTION)"
        ),
    }

    qcm_json_list = []
    global_q_id = 1

    for exam in all_exams:
        doc_name = exam["document"]
        src_file = exam["source"]
        if doc_name in OFFICIAL_CORRECTIONS_301:
            c_type, c_src, c_detail = OFFICIAL_CORRECTIONS_301[doc_name]
        else:
            c_type, c_src, c_detail = (
                "syllabus",
                "PDF du cours",
                "PY00301T_SI-26-27.pdf (Polycopié officiel de cours)"
            )

        for q in exam["questions"]:
            q_num = q["q_num"]
            theme = q["theme"]
            q_text = q["question"]
            opts = q.get("options", {})
            ans = q.get("answer", "")

            opt_a = opts.get("A", "")
            opt_b = opts.get("B", "")
            opt_c = opts.get("C", "")
            opt_d = opts.get("D", "")
            opt_e = opts.get("E", "")
            opt_f = opts.get("F", "")
            opt_g = opts.get("G", "")

            row_data = [
                doc_name, src_file, q_num, theme, q_text,
                opt_a, opt_b, opt_c, opt_d, opt_e, opt_f, opt_g, ans,
                f"{c_src} : {c_detail}"
            ]
            ws_qcm.append(row_data)
            curr_row = ws_qcm.max_row

            # Apply cell styling
            for c_idx in range(1, len(row_data) + 1):
                c = ws_qcm.cell(curr_row, c_idx)
                c.font = cell_font
                c.border = thin_border
                if c_idx in (3, 13):  # Q n°, Answer
                    c.alignment = cell_align_center
                else:
                    c.alignment = cell_align_left

            # Build JSON item
            options_json = []
            for letter in ["A", "B", "C", "D", "E", "F", "G"]:
                if letter in opts and opts[letter]:
                    options_json.append({"letter": letter, "text": opts[letter]})
            correct_letters = [l.strip() for l in ans.split(",") if l.strip()]

            qcm_json_list.append({
                "id": global_q_id,
                "document": doc_name,
                "source": src_file,
                "q_num": str(q_num),
                "theme": theme,
                "question": q_text,
                "options": options_json,
                "correct": correct_letters,
                "type": "qcm",
                "correction_source_type": c_type,
                "correction_source": c_src,
                "correction_source_detail": c_detail
            })
            global_q_id += 1

    # -------------------------------------------------------------------------
    # 2. SHEET: Open questions
    # -------------------------------------------------------------------------
    ws_open = wb.create_sheet(title="Open questions")
    ws_open.views.sheetView[0].showGridLines = True
    open_headers = [
        "Document", "Source file", "Q n°", "Theme / chapter", "Question",
        "Points", "Max lines", "Answer Guidelines", "Model Answer (Corrigé type rédigé)",
        "Correction Source"
    ]
    ws_open.append(open_headers)
    ws_open.row_dimensions[1].height = 28

    for col_idx in range(1, len(open_headers) + 1):
        cell = ws_open.cell(1, col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align

    open_col_widths = {
        "A": 24, "B": 32, "C": 10, "D": 42, "E": 65,
        "F": 10, "G": 10, "H": 55, "I": 85, "J": 35
    }
    for col_letter, width in open_col_widths.items():
        ws_open.column_dimensions[col_letter].width = width

    open_json_list = []
    for idx, oq in enumerate(OPEN_QUESTIONS, start=1):
        c_type = "syllabus"
        c_src = "PDF du cours"
        c_detail = "PY00301T_SI-26-27.pdf (Polycopié officiel de cours)"
        row_data = [
            oq["document"], oq["source"], oq["q_num"], oq["theme"], oq["question"],
            oq["points"], oq["max_lines"], oq["guidelines"], oq["model_answer"],
            f"{c_src} : {c_detail}"
        ]
        ws_open.append(row_data)
        curr_row = ws_open.max_row

        for c_idx in range(1, len(row_data) + 1):
            c = ws_open.cell(curr_row, c_idx)
            c.font = cell_font
            c.border = thin_border
            if c_idx in (3, 6, 7):  # Q n°, Points, Max lines
                c.alignment = cell_align_center
            else:
                c.alignment = cell_align_left

        guidelines_list = [g.strip() for g in oq["guidelines"].split("|") if g.strip()]
        open_json_list.append({
            "id": f"OPEN-{idx}",
            "type": "open",
            "document": oq["document"],
            "source": oq["source"],
            "q_num": oq["q_num"],
            "theme": oq["theme"],
            "question": oq["question"],
            "points": oq["points"],
            "max_lines": oq["max_lines"],
            "guidelines": guidelines_list,
            "model_answer": oq["model_answer"],
            "correction_source_type": c_type,
            "correction_source": c_src,
            "correction_source_detail": c_detail
        })

    # -------------------------------------------------------------------------
    # 3. SHEET: Notes
    # -------------------------------------------------------------------------
    ws_notes = wb.create_sheet(title="Notes")
    ws_notes.views.sheetView[0].showGridLines = True
    notes_headers = ["Topic", "Note"]
    ws_notes.append(notes_headers)
    ws_notes.row_dimensions[1].height = 28

    for col_idx in range(1, len(notes_headers) + 1):
        cell = ws_notes.cell(1, col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align

    ws_notes.column_dimensions["A"].width = 24
    ws_notes.column_dimensions["B"].width = 110

    notes_data = [
        ("Scope & Structure", "Base de données exhaustive des questions d'examen de l'UE PY00301T (Psychologie du développement : de la période fœtale aux prémices de l'adolescence, Université Toulouse Jean Jaurès). La structure reproduit rigoureusement celle de l'UE304 avec trois onglets : 'QCM', 'Open questions' et 'Notes'."),
        ("Correction Source", "Chaque question précise l'origine exacte de sa clé de correction selon 3 catégories : (1) 'Corrigé officiel' pour les annales disposant d'un document ou grille de correction officiel (2025-2026 CC2, 2024-2025 Seconde chance, 2023-2024 S1, 2018-2019 S2, Exemple Sorsana) ; (2) 'PDF du cours' pour les réponses établies et vérifiées d'après le polycopié officiel PY00301T_SI-26-27.pdf (2024-2025 CC2, 2023-2024 S2, 2021-2022 S1, 2020-2021, 2016-2017 S1 & S2, Open questions) ; (3) 'Généré par IA' pour les questions d'entraînement générées dynamiquement par les modèles de langage."),
        ("Exams covered", "11 sessions officielles complètes intégrées pour un total de 211 questions QCM : Exemple de sujet d'examen (C. Sorsana, 20 Q), 2016-2017 Session 1 (20 Q), 2016-2017 Session 2 (20 Q), 2018-2019 Session 2 (9 Q), 2020-2021 (22 Q), 2021-2022 Session 1 (20 Q), 2023-2024 Session 1 (20 Q), 2023-2024 Session 2 (20 Q), 2024-2025 CC2 et CT SED (20 Q), 2024-2025 Seconde chance SED (20 Q), 2025-2026 CC2 et CT SED (20 Q)."),
        ("Corrections officielles", "Toutes les grilles et documents officiels de correction disponibles dans le dossier ont été utilisés en priorité absolue : Annale 2023-2024 Session 1 CORRECTION.pdf, correction 2nd chance dev 2025.docx.pdf (pour Seconde chance SED), UE301_Corrige_Sujet_Examen.docx (pour le sujet exemple), Annale 301 - 2018-2019 Session 2.pdf (p.3 encart CORRECTION), annale_301_2025_2026_session1.csv (pour CC2 2025-2026)."),
        ("Validation par le syllabus", "Pour les sessions ne disposant pas d'une grille officielle jointe (2016-2017 S1 & S2, 2021-2022 S1, 2023-2024 S2, 2024-2025 CC2, 2020-2021), les réponses ont été vérifiées et établies directement à partir du polycopié de référence PY00301T_SI-26-27.pdf et de la littérature scientifique du domaine."),
        ("Spécificité format UE301", "Les épreuves officielles de l'UE301 sont constituées à 100% de QCM (Partie 1 à choix simple, Partie 2 à choix multiple). Contrairement à l'UE304, il n'existe pas d'épreuve de questions ouvertes aux examens terminaux écrits de l'UE301."),
        ("Questions ouvertes proposées", "Conformément à la consigne, l'onglet 'Open questions' propose 10 questions ouvertes types de niveau L2 couvrant l'ensemble des concepts théoriques cardinaux du cours (Vygotski, Wallon, Bowlby & Ainsworth, Théorie de l'esprit, Piaget moral et cognitif, Baillargeon, Luquet, Doise, conflit sociocognitif). Chaque question est pourvue de son barème en points, de ses critères d'évaluation (Answer Guidelines) et d'un corrigé type rédigé exhaustif (Model Answer)."),
        ("Thèmes et chapitres", "La colonne 'Theme / chapter' suit fidèlement le plan officiel du cours SED 2026-2027 (PY00301T_SI-26-27) articulé en 6 grands chapitres : Ch. 1 (Introduction, repères et méthodes), Ch. 2 (De l'embryon au nouveau-né), Ch. 3 (De la naissance à 3 ans), Ch. 4 (L'enfant de 3 à 6 ans), Ch. 5 (L'enfant de 6 à 12 ans) et Ch. 6 (Perspectives de l'adolescence au senior)."),
        ("Options Answer A à G", "L'onglet QCM inclut des colonnes Answer A jusqu'à Answer G afin d'accueillir fidèlement les questions comportant jusqu'à 7 propositions de réponses (ex. 2024-2025 Seconde chance Q11 et Q14)."),
        ("Fichiers sources & doublons", "Dans le dossier docs, 2025-26_301_session 1 (1).pdf et Annale 301 - 2025 -2026 - session 1.pdf sont la version scannée de Examen_CC2_CT_SED_PY00301T_2025-2026.docx. Annale 301 - 2025 -2026 - session 2.pdf est la version scannée de Examen_Seconde_Chance_PY00301T_2025-2026.docx. Question examen 301.xlsx constituait un brouillon partiel regroupant des items de différentes annales.")
    ]

    for topic, note in notes_data:
        ws_notes.append([topic, note])
        curr_row = ws_notes.max_row
        c_a = ws_notes.cell(curr_row, 1)
        c_b = ws_notes.cell(curr_row, 2)
        c_a.font = Font(name="Arial", size=9, bold=True)
        c_a.alignment = cell_align_left
        c_a.border = thin_border
        c_b.font = cell_font
        c_b.alignment = cell_align_left
        c_b.border = thin_border

    # Save Excel workbook
    wb.save(OUTPUT_XLSX)
    print(f"✅ Successfully written Excel file to: {OUTPUT_XLSX}")

    # Export CSV files with utf-8-sig for immediate and universal access
    import csv
    csv_qcm_path = os.path.join(DOCS_DIR, "UE301_questions.csv")
    with open(csv_qcm_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        for row in ws_qcm.iter_rows(values_only=True):
            writer.writerow(row)
    print(f"✅ Saved QCM CSV data to: {csv_qcm_path}")

    csv_quick_path = os.path.join(DOCS_DIR, "UE301_questions_quick_lookup.csv")
    with open(csv_quick_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Document", "Q n°", "Theme / chapter", "Question", "Options", "Answer", "Correction Source"])
        for r in range(2, ws_qcm.max_row + 1):
            doc = ws_qcm.cell(r, 1).value
            q_num = ws_qcm.cell(r, 3).value
            theme = ws_qcm.cell(r, 4).value
            q_text = ws_qcm.cell(r, 5).value
            opts = []
            for c_idx, letter in enumerate(["A", "B", "C", "D", "E", "F", "G"], start=6):
                val = ws_qcm.cell(r, c_idx).value
                if val:
                    opts.append(f"{letter}. {val}")
            opts_str = "\n".join(opts)
            ans = ws_qcm.cell(r, 13).value
            corr_src = ws_qcm.cell(r, 14).value
            writer.writerow([r - 1, doc, q_num, theme, q_text, opts_str, ans, corr_src])
    print(f"✅ Saved Quick Lookup CSV to: {csv_quick_path}")

    csv_open_path = os.path.join(DOCS_DIR, "UE301_open_questions.csv")
    with open(csv_open_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        for row in ws_open.iter_rows(values_only=True):
            writer.writerow(row)
    print(f"✅ Saved Open Questions CSV to: {csv_open_path}")

    # Also save JSON files in 301/data/ for the web app pipeline
    json_qcm_path = os.path.join(DATA_DIR, "questions_database.json")
    with open(json_qcm_path, "w", encoding="utf-8") as f:
        json.dump(qcm_json_list, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved QCM JSON data to: {json_qcm_path}")

    json_open_path = os.path.join(DATA_DIR, "open_questions.json")
    with open(json_open_path, "w", encoding="utf-8") as f:
        json.dump(open_json_list, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved Open Questions JSON data to: {json_open_path}")

if __name__ == "__main__":
    main()

