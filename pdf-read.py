import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

from PyPDF2 import PdfFileReader

file_name = "./papers/muga2015.pdf"

fd = open(file_name, "rb")
'''
doc = PDFDocument(fd)

viewer = SimplePDFViewer(fd)
viewer.navigate(46)
viewer.render()
#print(viewer.canvas.text_content)
print(viewer.canvas.strings)
with open("tutorial-sample-content-stream-p2.txt", "w+") as f:
	f.write(viewer.canvas.text_content)

'''


pdf = PdfFileReader(file_name)
pdf.getNumPages()
first_page = pdf.getPage(45)

raw = first_page.extractText()
raw = raw.replace('\n', '')
print(bytes(raw, 'ASCII'))

with open("hole.txt", "w+") as f:
	f.write(raw)