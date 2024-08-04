from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path.cwd() / "Pride_and_Prejudice.pdf"

input_pdf = PdfReader(str(pdf_path)) 

num_pages = len(input_pdf.pages)

part1_writer = PdfWriter()
part2_writer =  PdfWriter()

part1_pages = input_pdf.pages[:150]
part2_pages = input_pdf.pages[150:]

for page in part1_pages:
    part1_writer.add_page(page)

for page in part2_pages:
    part2_writer.add_page(page)

part1_output_path = Path.cwd() / "part_1.pdf"
with part1_output_path.open(mode="wb") as part1_output_file:
    part1_writer.write(part1_output_file)

part2_output_path = Path.cwd() / "part_2.pdf"
with part2_output_path.open(mode="wb") as part2_output_file:
    part2_writer.write(part2_output_file)
