from pathlib import Path
from PyPDF2 import PdfReader

pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"

pdf_reader = PdfReader(str(pdf_path))
output_file_path = Path.cwd() / "Pride_and_Prejudice.txt"

with output_file_path.open(mode="w") as output_file:
    title = pdf_reader.metadata.title
    num_pages = len(pdf_reader.pages)
    output_file.write(f"{title}\nNumber of pages: {num_pages}\n\n")

    for page in pdf_reader.pages:
        text = page.extract_text()
        output_file.write(text)
