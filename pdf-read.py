import sys
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

from PyPDF2 import PdfFileReader

#Set up. This will contain the links FROM a given report TO everything it points to.
outgoing_links = {}
#File names need to be entered manually
file_names = []
#Report names come from Cavell's UI
report_names = []


#Open each of the files that were specified. 
for file_name in file_names:
	pdf = PdfFileReader(file_name)
	pdf_length = pdf.getNumPages()

	#Read through each page in the file and extract the text from it
	for page_number in range(pdf_length):
		page = pdf.getPage(page_number)
		raw = page.extractText()
		raw = raw.replace('\n', '')
	
		#Check if the page that we are currently on contains the name of any of the other reports that we are looking for links too
		for report in report_names:
			if report in raw:
				if len(outgoing_links[report]) == 0:
					outgoing_links[report] = []
				outgoing_links[file_name].append(report)

return outgoing_links