import csv
from pathlib import Path

file_path = Path.cwd() / "numbers.csv"
file_path.touch()

file = file_path.open(mode="r", encoding="utf-8", newline="")

reader = csv.reader(file)

every_row = []

for row in reader:
    int_row = [int(value) for value in row]
    every_row.append(int_row)

print(every_row)

file.close()


