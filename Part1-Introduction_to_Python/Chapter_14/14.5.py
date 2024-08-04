from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.cwd() / "split_and_rotate.pdf"

pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

for page in pdf_reader.pages:
    rotated_page = page.rotate(270)
    pdf_writer.add_page(rotated_page)

with Path("rotated.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
