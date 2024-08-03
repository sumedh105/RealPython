import csv

from pathlib import Path

file_path_read = Path.cwd() / "scores.csv"
file_read = file_path_read.open(mode="r", encoding="utf-8", newline="")


reader = csv.DictReader(file_read)
scores = [row for row in reader]
print(f"score = {scores}")

high_scores = {}

for item in scores:
    name = item["name"]
    score = int(item["score"])

    if name not in high_scores:
        high_scores[name] = score
    else:
        if high_scores[name] < score:
            high_scores[name] = score
        

print(f"high_scores = {high_scores}")

file_path_write = Path.cwd() / "high_scores.csv"
file_path_write.touch()

file_write = file_path_write.open(mode="w", encoding="utf-8", newline="")

writer = csv.DictWriter(file_write, fieldnames = ["name", "high_score"])
writer.writeheader()

for name in high_scores:
    row_dict = {"name": name, "high_score": high_scores[name]}

file_read.close()

file_write.close()
