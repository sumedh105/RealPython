from pathlib import Path
from PyPDF2 import PdfMerger

pdf_merger = PdfMerger()

reports_dir = Path.cwd()

source_path = reports_dir / "concatenated.pdf"
dest_path = reports_dir / "merge3.pdf"

pdf_merger.append(str(source_path))

pdf_merger.merge(1, str(dest_path))

with Path("merged.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
