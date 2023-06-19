from pathlib import Path
from pypdf import PdfReader
from pypdf import PdfWriter

# Get path to pdfs directory
pdf_path = (Path(__file__).parent/"calc_exercises"/"calc_textbook.pdf")

# reader and writer perform operations
reader = PdfReader(pdf_path)
writer = PdfWriter()

for page in reader.pages:
    # Extract text from page
    text = page.extract_text().lower()
    
    # Find all occurances of key word
    if text.find('exercises') > -1:
        writer.add_page(page)

# Write all pages to new pdf, saves in working dir
writer.write('exercises_calc.pdf')


