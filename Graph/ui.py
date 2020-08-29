import PySimpleGUI as sg

import os.path

import sys
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
from PaperData import *

from PyPDF2 import PdfFileReader

papers = []

report_names = []
'''
enter everything into the report names`
'''
outgoing_links = {}

currId = 0

def findCitations(file_names):

    global report_names
    global outgoing_links


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
    pdfSelected.append([sg.Text("Choose PDFs from list on left: ")])

    pdfSelected.append([sg.Listbox(values=[], enable_events=True, size=(40, 20), key="selectedList")])
    pdfSelected.append([sg.Text("Enter Desired Output File: ")])
    pdfSelected.append([sg.InputText(do_not_clear = True, key = "output")])
    pdfSelected.append([sg.Button('Generate Map')])
    return pdfSelected



# ----- Full layout -----

layout = [

    [

        sg.Column(file_list_column),

        sg.VSeperator(),

        sg.Column(pdfSelectedViewer(10)),

    ]

]

window = sg.Window("Select PDFs to Map", layout)
selectedFileList = []



def pdfSelectedListboxManager():

    global selectedFileList
    global currId
    global window
    global papers


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
        text = sg.popup_get_text('Please enter title and authors:',"" ,'Title:  Author(s)(comma seperated):')
        text1 = sg.popup_get_text('Please enter year of publication:',"" ,'')
        title = text.split(" Author(s)(comma seperated):")[0].strip('Title: ')
        authors = text.split(" Author(s)(comma seperated):")[1]
        temp["title"] = title
        temp["authors"] = authors
        year = text1

        newPaper = PaperData(authors, title, year, currId, [], "", 0)
        currId += 1
        papers.append(newPaper)

        selectedFileList.append(temp)

    tempArray = []

    for entry in selectedFileList:
        tempArray.append(str(entry["fileName"]) + "\t -> \t" + str(entry["title"]))


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
        links = findCitations(tempFileName)

        print('execute')
        
        print(values["output"])



window.close()





