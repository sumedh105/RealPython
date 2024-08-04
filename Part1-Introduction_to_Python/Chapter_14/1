from pathlib import Path
from PyPDF2 import PdfReader

pdf_path = Path.cwd() / "zen.pdf"

pdf_reader =  PdfReader(str(pdf_path))

title = pdf_reader.metadata.title
num_pages = len(pdf_reader.pages)

print(f"title = {title}")
print(f"num_pages = {num_pages}")

for page in pdf_reader.pages:
    text = page.extract_text()
    print(f"text = {text}")
