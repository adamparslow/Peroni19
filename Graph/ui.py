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

def findCitations(papers):

    global outgoing_links

    for paper in papers:
        pdf = PdfFileReader(paper.fileName)
        pdf_length = pdf.getNumPages()
        paper.numPages = pdf_length


        #Read through each page in the file and extract the text from it
        for page_number in range(pdf_length):
            page = pdf.getPage(page_number)
            raw = page.extractText()
            raw = raw.replace('\n', '')
        
            #Check if the page that we are currently on contains the name of any of the other reports that we are looking for links too
            for paper2 in papers:
                if ("".join(paper2.title.split())) in raw:
                    if len(outgoing_links[report]) == 0:
                        outgoing_links[report] = []
                    outgoing_links[file_name].append(report)
                print(outgoing_links[file_name])

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

window = sg.Window("Select PDFs to Map", layout)
selectedFileList = []



def pdfSelectedListboxManager():

    global selectedFileList
    global currId
    global window
    global papers
    global report_names


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

        newPaper = PaperData(authors, title, year, fileName, currId, [], "", 0)
        currId += 1
        papers.append(newPaper)

        report_names.append("".join(title.split()))

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
        '''tempFileName = []
        for selected in selectedFileList:
            tempFileName.append(folder+"/"+str(selected["fileName"]))'''
        links = findCitations(papers)

        print('execute')
        
        print(values["output"])



window.close()





