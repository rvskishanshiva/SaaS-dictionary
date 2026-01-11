from openpyxl import load_workbook

f = "data/inputs.xlsx"

def log_input(email, user_input):
    wb = load_workbook(f)
    ws = wb.active
    ws.append([email, user_input])
    wb.save(f)
