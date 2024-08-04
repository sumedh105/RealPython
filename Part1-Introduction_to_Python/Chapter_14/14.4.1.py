from pathlib import Path
from PyPDF2 import PdfMerger

pdf_merger = PdfMerger()
reports_dir = Path.cwd()

for path in reports_dir.glob("m*.pdf"):
    print(path.name)

expense_reports = list(reports_dir.glob("m*.pdf"))
expense_reports.sort()

for path in expense_reports:
    print(path.name)
    if path.name != "merge2.pdf":
        pdf_merger.append(str(path))

with Path("concatenated.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
