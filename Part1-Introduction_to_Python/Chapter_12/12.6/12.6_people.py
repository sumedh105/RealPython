import csv
from pathlib import Path

people = [
        {"name": "Veronica", "age": 29},
        {"name": "Audrey", "age":32},
        {"name": "Sam", "age": 24},
    ]

file_path = Path.cwd() / "people.csv"
file_path.touch()

print(f"file_path = {file_path}")

file = file_path.open(mode="w", encoding="utf-8", newline="")

writer = csv.DictWriter(file, fieldnames=["name", "age"])

writer.writeheader()

writer.writerows(people)

file.close()
