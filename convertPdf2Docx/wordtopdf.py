# Convert Pdf to Docx

# Install Module : ' pip install pdf2docx '

from pdf2docx import Converter

old_pdf = "dummy.pdf"
nec_doc = "new.docx"

obj = Converter(old_pdf)
obj.convert(nec_doc)
obj.close()