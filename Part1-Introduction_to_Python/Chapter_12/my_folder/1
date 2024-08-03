import pathlib

path = pathlib.Path("/home/sumedh/Courses/Python/RealPython/Part1-Introduction_to_Python/Chapter_12/my_folder/hello.txt")
print(path)

home = pathlib.Path.home()
print(home)

curr = pathlib.Path.cwd()
print(curr)

print(f"{path.is_absolute()}")

for directory in path.parents:
    print(directory)

print(f"path.anchor = {path.anchor}")

print(f"path.stem = {path.stem} and path.suffix = {path.suffix}")

print(f"path = {path}")
print(f"path.exists? {path.exists()}")
print(f"path.is_file? {path.is_file()}")
print(f"path.is_dir? {path.is_dir()}")

file_path = path
print(f"file_path = {file_path}")
print(f"file_path.name = {file_path.name}")
print(f"file_path.parent = {file_path.parent}")
