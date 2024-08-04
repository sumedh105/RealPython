from PyPDF2 import PdfReader
from pathlib import Path

pdf_path = (Path.cwd() / "Pride_and_Prejudice.pdf")

pdf = PdfReader(str(pdf_path))

print(f"pdf.getNumPages() = {len(pdf.pages)}")

print(f"pdf.documentInfo = {pdf.metadata}")

print(f"pdf.metadata.title = {pdf.metadata.title}")
print(f"pdf.metadata.author = {pdf.metadata.author}")
print(f"pdf.metadata.creator = {pdf.metadata.creator}")
print(f"pdf.metadata.producer = {pdf.metadata.producer}")

first_page = pdf.pages[0]
print(f"first_page = {first_page}")

print(f"first_page.extractText() = {first_page.extract_text()}")

for page in pdf.pages:
    print(page.extract_text())
