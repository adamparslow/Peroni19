import sys
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

from PyPDF2 import PdfFileReader

#file_name = "./papers/muga2015.pdf"
report_names = []
'''
enter everything into the report names`
'''
outgoing_links = {}
file_names = []

#file_name = "./PapersWithTwoCol/4 - RevModPhys.91.045001.pdf"


for file_name in file_names:
	pdf = PdfFileReader(file_name)
	pdf_length = pdf.getNumPages()
	#print(pdf.documentInfo)

	for page_number in range(pdf_length):
		page = pdf.getPage(page_number)
		raw = page.extractText()
		raw = raw.replace('\n', '')
		#print(bytes(raw, 'ASCII'))

		#with open("hole.txt", "w+") as f:
		#	f.write(raw)

		for report in report_names:
			if report in raw:
				if len(outgoing_links[report]) == 0:
					outgoing_links[report] = []
				info = {}
				pdf_info[title] = pdf.documentInfo.title
				pdf_info[author] = pdf.documentInfo.author
				pdf_info[creationdate] = pdf.documentInfo.creationdate
				outgoing_links[report].append(pdf_info)

