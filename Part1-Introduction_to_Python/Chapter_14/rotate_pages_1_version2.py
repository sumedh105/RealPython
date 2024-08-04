from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.cwd() / "ugly.pdf"

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

for page in pdf_reader.pages:
    if page["/Rotate"] == -90:
        page.rotate(90)
    pdf_writer.add_page(page)

with Path("ugly_rotated2.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
