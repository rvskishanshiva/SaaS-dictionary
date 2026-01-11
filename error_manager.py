from openpyxl import load_workbook

f = "data/errors.xlsx"

def log_error(email, error):
    wb = load_workbook(f)
    ws = wb.active
    ws.append([email, error])
    wb.save(f)
