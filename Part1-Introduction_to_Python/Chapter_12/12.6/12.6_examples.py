from pathlib import Path

temperature_readings = [68, 65, 68, 70, 74, 72]

path = Path.cwd() / "temperatures.csv"
path.touch()

print(f"path = {path}")

with path.open(mode="a", encoding="utf-8") as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f", {temp}")

with path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    print(text)
