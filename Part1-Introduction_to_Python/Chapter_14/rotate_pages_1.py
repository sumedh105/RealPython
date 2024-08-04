from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.cwd() / "ugly.pdf"

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

for n in range(len(pdf_reader.pages)):
    page = pdf_reader._get_page(n)
    if n%2 == 0:
        page.rotate(90)
    pdf_writer.add_page(page)

with Path("ugly_rotated.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
