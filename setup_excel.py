from openpyxl import Workbook
import os

os.makedirs("data", exist_ok=True)

files = {
    "users.xlsx": ["Name", "Email"],
    "words.xlsx": ["Word", "Meaning"],
    "history.xlsx": ["Email", "Word"],
    "errors.xlsx": ["Email", "Wrong_Input"],
    "inputs.xlsx": ["Email", "Input"]
}

for file, headers in files.items():
    wb = Workbook()
    ws = wb.active
    ws.append(headers)
    wb.save(f"data/{file}")

print("Excel files created successfully.")
