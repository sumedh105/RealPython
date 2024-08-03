from pathlib import Path

path = Path.cwd() / "hello.txt"

with path.open(mode="a", encoding="utf-8") as file:
    file.write("\nHi Sumedh W. Jambekar")


lines_of_text = [
        "\nHello from line1\n",
        "Hello from line2\n",
        "Hello from line3\n",
    ]

with path.open(mode="a", encoding="utf-8") as file:
    file.writelines(lines_of_text)
