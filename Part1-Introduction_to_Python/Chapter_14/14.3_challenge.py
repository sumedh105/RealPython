from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

class PdfFileSplitter:

    def __init__(self, pdf_path):
        self.pdf_reader = PdfReader(pdf_path)
        self.writer1 = None
        self.writer2 = None

    def split(self, break_point):
        self.writer1 = PdfWriter()
        self.writer2 = PdfWriter()

        for page in self.pdf_reader.pages[:break_point]:
            self.writer1.add_page(page)

        for page in self.pdf_reader.pages[break_point:]:
            self.writer2.add_page(page)

    def write(self, filename):
        with Path(filename + "_1.pdf").open(mode="wb") as output_file:
            self.writer1.write(output_file)

        with Path(filename + "_2.pdf").open(mode="wb") as output_file:
            self.writer2.write(output_file)

pdf_splitter = PdfFileSplitter("/home/sumedh/Courses/Python/RealPython/Part1-Introduction_to_Python/Chapter_14/Pride_and_Prejudice.pdf")
pdf_splitter.split(150)
pdf_splitter.write("Pride_and_Prejudice")
