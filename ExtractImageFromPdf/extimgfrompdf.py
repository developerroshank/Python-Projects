# Extracting Image From Pdf

# Install Module : ' pip install pikepdf '

from pikepdf import Pdf, Name, PdfImage

old_pdf = Pdf.open("test.pdf")

page_1 = old_pdf.pages[0]

print(list(page_1.images.keys()))
