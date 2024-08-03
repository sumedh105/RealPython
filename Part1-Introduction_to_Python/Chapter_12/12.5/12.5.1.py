from pathlib import Path

path = Path.cwd() / "starships.txt"
path.touch()

print(f"path={path}")

lines = [
        "Discovery\n",
        "Enterprise\n",
        "Defiant\n",
        "Voyager\n",
    ]

with path.open(mode="w", encoding="utf-8") as file:
    file.writelines(lines)

