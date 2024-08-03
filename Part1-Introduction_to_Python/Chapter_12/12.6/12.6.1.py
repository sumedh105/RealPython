import csv
from pathlib import Path

numbers = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]

file_path = Path.cwd() / "numbers.csv"
file_path.touch()

file = file_path.open(mode="w", encoding="utf-8", newline="")

writer = csv.writer(file)

for num in numbers:
    writer.writerow(num)

file.close()

