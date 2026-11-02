import os
import re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Create workbook
wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# Styles matching UE304_questions_database.xlsx
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

# -------------------------------------------------------------
# 1. QCM SHEET
# -------------------------------------------------------------
ws_qcm = wb.create_sheet(title="QCM")
qcm_headers = [
    "Document", "Source file(s)", "Q n°", "Theme / chapter", "Question",
    "Answer A", "Answer B", "Answer C", "Answer D", "Answer E", "Answer F", "Answer G", "Answer"
]
ws_qcm.append(qcm_headers)

# -------------------------------------------------------------
# 2. OPEN QUESTIONS SHEET
# -------------------------------------------------------------
ws_open = wb.create_sheet(title="Open questions")
open_headers = [
    "Document", "Source file", "Q n°", "Theme / chapter", "Question",
    "Points", "Max lines", "Answer Guidelines", "Model Answer (Corrigé type rédigé)"
]
ws_open.append(open_headers)

# -------------------------------------------------------------
# 3. NOTES SHEET
# -------------------------------------------------------------
ws_notes = wb.create_sheet(title="Notes")
notes_headers = ["Topic", "Note"]
ws_notes.append(notes_headers)

print("Workbook initialized with sheets.")

