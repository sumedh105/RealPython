from pathlib import Path

path = Path.cwd() / "temperatures.csv"
path.touch()

print(f"path = {path}")
