import csv
from pathlib import Path

file_path = Path.cwd() / "employees.csv"
file_path.touch()

print(f"file_path= {file_path}")

file = file_path.open(mode="r", encoding="utf-8", newline="")
reader = csv.DictReader(file)

print(f"reader.fieldnames = {reader.fieldnames}")

def process_row(row):
    row["salary"] = float(row["salary"])
    return row

for row in reader:
    print(f"row = {process_row(row)}")

file.close()
