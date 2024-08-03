import csv
from pathlib import Path

file_path = Path.cwd() / "favorite_colors.csv"
file_path.touch()

file = file_path.open(mode="r", encoding="utf-8", newline="")

dict_list = []

reader = csv.DictReader(file)

for row in reader:
    dict_list.append(row)

print(dict_list)

file.close()
