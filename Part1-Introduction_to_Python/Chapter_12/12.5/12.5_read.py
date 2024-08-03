from pathlib import Path

path = Path.cwd() / "hello.txt"

with path.open(mode="r", encoding="utf-8") as file: 
    text = file.read()

print(f"text = {text}")

with path.open(mode="r", encoding="utf-8") as file: 
    for line in file.readlines():
        print(line)
