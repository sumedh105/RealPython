from pathlib import Path

new_dir = Path.cwd() / "my_folder_one"
new_dir.mkdir(parents=True, exist_ok=True)

print(f"new_dir = {new_dir}")

file_path = new_dir / "file1.txt"
print(f"file_path.exists()? {file_path.exists()}")

file_path.touch()
print(f"file_path.exists()? {file_path.exists()}")

file_path = new_dir / "file2.txt"
print(f"file_path.exists()? {file_path.exists()}")

file_path.touch()
print(f"file_path.exists()? {file_path.exists()}")

file_path = new_dir / "image1.png"
print(f"file_path.exists()? {file_path.exists()}")

file_path.touch()
print(f"file_path.exists()? {file_path.exists()}")

new_dir_one = new_dir / "images"
new_dir_one.mkdir(parents=True, exist_ok=True)

print(f"new_dir = {new_dir}")
print(f"new_dir_one = {new_dir_one}")

source = new_dir / "image1.png" 
destination = new_dir / "images" / "image1.png"

file_path = new_dir / "images" / "image2.gif"
print(f"file_path.exists()? {file_path.exists()}")

file_path.touch()
print(f"file_path.exists()? {file_path.exists()}")

file_path = new_dir / "images" / "image3.png"
print(f"file_path.exists()? {file_path.exists()}")

file_path.touch()
print(f"file_path.exists()? {file_path.exists()}")

file_path = new_dir / "images" / "image4.jpg"
print(f"file_path.exists()? {file_path.exists()}")

file_path.touch()
print(f"file_path.exists()? {file_path.exists()}")

source.replace(destination)

del_file_path = new_dir / "file1.txt"
del_file_path.unlink(missing_ok=True)
