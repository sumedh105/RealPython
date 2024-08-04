from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"

input_pdf = PdfReader(str(pdf_path))

num_pages = len(input_pdf.pages)

print(f"num_pages = {num_pages}")

last_page = input_pdf.pages[num_pages - 1]

pdf_writer = PdfWriter()
pdf_writer.add_page(last_page)

with Path("last_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
