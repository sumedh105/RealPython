from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.cwd() / "half_and_half.pdf"

pdf_reader = PdfReader(str(pdf_path))
first_page = pdf_reader._get_page(0)

print(f"first_page.mediabox = {first_page.mediabox}")
print(f"first_page.mediabox.lower_left = {first_page.mediabox.lower_left}")
print(f"first_page.mediabox.lower_right = {first_page.mediabox.lower_right}")
print(f"first_page.mediabox.upper_left = {first_page.mediabox.upper_left}")
print(f"first_page.mediabox.upper_right = {first_page.mediabox.upper_right}")

first_page.mediabox.upper_left = (0, 480)

print(f"first_page.mediabox.lower_left = {first_page.mediabox.lower_left}")
print(f"first_page.mediabox.lower_right = {first_page.mediabox.lower_right}")
print(f"first_page.mediabox.upper_left = {first_page.mediabox.upper_left}")
print(f"first_page.mediabox.upper_right = {first_page.mediabox.upper_right}")

pdf_writer = PdfWriter()   
pdf_writer.add_page(first_page)

with Path("cropped_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
