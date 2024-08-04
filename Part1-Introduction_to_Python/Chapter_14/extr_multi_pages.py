from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"

input_pdf = PdfReader(str(pdf_path))

pdf_writer = PdfWriter()
for n in range(1, 4):
    page = input_pdf.pages[n]
    pdf_writer.add_page(page)

print(f"num_pages = {len(pdf_writer.pages)}")

with Path("chapter1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
