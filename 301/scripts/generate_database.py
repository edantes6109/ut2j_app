#!/usr/bin/env python3
"""
Generate UE301_questions_database.xlsx
Matches the structure, styling and column order of UE304_questions_database.xlsx.
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Output path
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "UE301_questions_database.xlsx")

def create_database():
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

    # =========================================================================
    # SHEET 1: QCM
    # =========================================================================
    ws_qcm = wb.create_sheet(title="QCM")
    qcm_headers = [
        "Document", "Source file(s)", "Q n°", "Theme / chapter", "Question",
        "Answer A", "Answer B", "Answer C", "Answer D", "Answer E", "Answer F", "Answer G", "Answer"
    ]
    ws_qcm.append(qcm_headers)
    ws_qcm.row_dimensions[1].height = 28
    for col_idx in range(1, len(qcm_headers) + 1):
        cell = ws_qcm.cell(1, col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align

    # Column widths
    qcm_col_widths = {
        "A": 24, "B": 35, "C": 8, "D": 42, "E": 60,
        "F": 38, "G": 38, "H": 38, "I": 38, "J": 38, "K": 38, "L": 38, "M": 14
    }
    for col_letter, width in qcm_col_widths.items():
        ws_qcm.column_dimensions[col_letter].width = width

    # =========================================================================
    # SHEET 2: Open questions
    # =========================================================================
    ws_open = wb.create_sheet(title="Open questions")
    open_headers = [
        "Document", "Source file", "Q n°", "Theme / chapter", "Question",
        "Points", "Max lines", "Answer Guidelines", "Model Answer (Corrigé type rédigé)"
    ]
    ws_open.append(open_headers)
    ws_open.row_dimensions[1].height = 28
    for col_idx in range(1, len(open_headers) + 1):
        cell = ws_open.cell(1, col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align

    open_col_widths = {
        "A": 24, "B": 30, "C": 12, "D": 42, "E": 65,
        "F": 10, "G": 10, "H": 55, "I": 85
    }
    for col_letter, width in open_col_widths.items():
        ws_open.column_dimensions[col_letter].width = width

    # =========================================================================
    # SHEET 3: Notes
    # =========================================================================
    ws_notes = wb.create_sheet(title="Notes")
    notes_headers = ["Topic", "Note"]
    ws_notes.append(notes_headers)
    ws_notes.row_dimensions[1].height = 28
    for col_idx in range(1, len(notes_headers) + 1):
        cell = ws_notes.cell(1, col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align

    ws_notes.column_dimensions["A"].width = 20
    ws_notes.column_dimensions["B"].width = 110

    return wb, ws_qcm, ws_open, ws_notes

print("Base setup module ready.")

