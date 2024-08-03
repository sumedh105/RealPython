from pathlib import Path

new_dir = Path.cwd() / "practice_files" / "images"
new_dir.mkdir(parents=True, exist_ok=True)

print(f"new_dir = {new_dir}")

doc_dir = Path.cwd() / "practice_files" / "documents"
doc_dir.mkdir(parents=True, exist_ok=True)

print(f"doc_dir = {doc_dir}")

for path in doc_dir.glob("*.*"):
    #print(path)
    #print(path.suffix)
    print(path.suffix.lower())
    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
        path.replace(new_dir / path.name)

