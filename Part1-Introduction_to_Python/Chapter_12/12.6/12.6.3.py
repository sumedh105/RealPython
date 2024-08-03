import csv
from pathlib import Path

favorite_colors = [
        {"name": "Joe", "favorite_color": "blue"},
        {"name": "Anne", "favorite_color": "green"},
        {"name": "Bailey", "favorite_color": "red"}
    ]

file_path = Path.cwd() / "favorite_colors.csv"
file_path.touch()

file = file_path.open(mode="w", encoding="utf-8", newline="")

writer = csv.DictWriter(file, fieldnames=["name", "favorite_color"])

writer.writeheader()

writer.writerows(favorite_colors)

file.close()
