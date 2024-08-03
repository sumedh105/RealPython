from pathlib import Path

new_dir = Path.cwd() / "new_directory"
new_dir.mkdir(exist_ok=True)

new_dir_one = Path.cwd() / "new_directory_one"
new_dir_one.mkdir(exist_ok=True)

nested_dir = new_dir / "folder_a" / "folder_b"
nested_dir.mkdir(parents=True, exist_ok=True)

nested_dir = new_dir / "folder_c" / "folder_b"
nested_dir.mkdir(parents=True, exist_ok=True)

file_path = new_dir / "file1.txt"
print(f"file_path.exists() = {file_path.exists()}")

file_path.touch()
print(f"file_path.exists() = {file_path.exists()}")

file_path.is_file()
print(f"file_path.is_file() = {file_path.is_file()}")

for path in new_dir.iterdir():
    print(f"path = {path}")

for path in new_dir.glob("*.txt"):
    print(f"path = {path}")


paths = [
        new_dir / "program1.py",
        new_dir / "program2.py",
        new_dir / "folder_a" / "program3.py",
        new_dir / "folder_a" / "folder_b" / "image1.jpg",
        new_dir / "folder_a" / "folder_b" / "image2.png",
    ]

for path in paths:
    path.touch()
