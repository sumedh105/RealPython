from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader

pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"

input_pdf = PdfReader(str(pdf_path))

first_page = input_pdf.pages[0]

pdf_writer = PdfWriter()
pdf_writer.add_page(first_page)

with Path("first_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
