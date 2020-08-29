
import PySimpleGUI as sg

import os.path

import sys
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

from PyPDF2 import PdfFileReader


report_names = []
'''
enter everything into the report names`
'''
outgoing_links = {}



def pdfReader(file_names):

    global report_names
    global outgoing_links


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
                    
				    pdf_info[searchable_title] = file_name
				    pdf_info[broken_title] = pdf.documentInfo.title
				    pdf_info[author] = pdf.documentInfo.author
				    pdf_info[creationdate] = pdf.documentInfo.creationdate
				    outgoing_links[report].append(pdf_info)




file_list_column = [

    [

        sg.Text("PDF Folder"),

        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),

        sg.FolderBrowse(),

    ],

    [

        sg.Listbox(

            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"

        )

    ],

]



def pdfSelectedViewer(numRows):

    pdfSelected = []
    pdfSelected.append([sg.Text("choose PDF's from list on left: ")])

    pdfSelected.append([sg.Listbox(values=[], enable_events=True, size=(40, 20), key="selectedList")])
    pdfSelected.append([sg.Text("Enter Desired Output FileName: ")])
    pdfSelected.append([sg.InputText(do_not_clear = True, key = "output")])
    pdfSelected.append([sg.Button('execute')])
    return pdfSelected



# ----- Full layout -----

layout = [

    [

        sg.Column(file_list_column),

        sg.VSeperator(),

        sg.Column(pdfSelectedViewer(10)),

    ]

]

window = sg.Window("PDF Interface", layout)
selectedFileList = []



def pdfSelectedListboxManager():

    global selectedFileList
    global window


    try:
        filePath = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
        )  
        fileName = os.path.basename(filePath)     
    except:
        pass
    if(fileName in selectedFileList):
        selectedFileList[:] = [d for d in selectedFileList if d.get('fileName') != fileName]
    elif(fileName not in selectedFileList):
        temp = {}
        temp["fileName"] = fileName
        text = sg.popup_get_text('Title',"" ,'Title: Author(s)(comma seperated): ')
        title = text.split(" Author(s)(comma seperated):")[0].strip('Title: ')
        authors = text.split(" Author(s)(comma seperated):")[1]
        temp["title"] = title
        temp["authors"] = authors
        

        selectedFileList.append(temp)

    tempArray = []

    for entry in selectedFileList:
        tempArray.append(str(entry["fileName"]) + "\t" + str(entry["title"]))


    window["selectedList"].update(tempArray)



   

def displayPDFs():
    global folder
    global selectedFileList
    global window

    folder = values["-FOLDER-"]

    try:

	    # Get list of files in folde     
        print((os.listdir(folder)))
        file_list = os.listdir(folder)
        selectedFileList = []

    except:

        file_list = []


    fnames = [

        f

        for f in file_list

        if os.path.isfile(os.path.join(folder, f))

        and f.lower().endswith((".pdf"))

    ]
    
    window["-FILE LIST-"].update(fnames)



folder = 0

while True:

    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:

        break

# Folder name was filled in, make a list of files in the folder

    if event == "-FOLDER-":
        displayPDFs()
        

    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        pdfSelectedListboxManager()

    elif event == 'execute':
        print(folder)
        tempFileName = []
        for selected in selectedFileList:
            tempFileName.append(folder+"/"+str(selected["fileName"]))
        pdfReader(tempFileName)

        print('execute')
        
        print(values["output"])



window.close()





