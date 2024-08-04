from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"

input_pdf = PdfReader(pdf_path)

pdf_writer = PdfWriter()

num_pages = len(input_pdf.pages)

for n in range(0, num_pages, 2):
    page = input_pdf.pages[n]
    pdf_writer.add_page(page)

with Path("every_other_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
