from pathlib import Path

path = Path.cwd() / "starships.txt"

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        if line[0] == "D":
            print(line, end="")
