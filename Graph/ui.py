import PySimpleGUI as sg

import os.path

import sys
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
from PaperData import *

from PyPDF2 import PdfFileReader

from graphCreate import *

papers = []

report_names = []
'''
enter everything into the report names`
'''
outgoing_links = {}

currId = 0

def findCitations(papers):

    global outgoing_links

    bkpPapersList = []
    for paper in papers:
        bkpPapersList.append(paper)

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
            for paperToFind in bkpPapersList:
                #print("searching for", paperToFind.title, "in page", page_number, "of", paper.title)
                authorToFind = paperToFind.author.split(',')[0]
                authorToFind = authorToFind.split(' ')[1]
                if ("".join(paperToFind.title.split())) in raw and authorToFind in raw and paperToFind.title != paper.title:
                    #print("found sumn")
                    paper.addCitation(paperToFind.id)
                #print("\n", paper.title, paper.year, "aka", paper.fileName[-20:], "has citation to: \n", paperToFind.title, paperToFind.year, "otherwise known as", paperToFind.fileName[-20:], "and id", paperToFind.id)
                print("\n")

    for paper in papers:
        print(paper.title + "(" + str(paper.id) + ")" + " cites " + str(paper.citations))

    return papers



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

selectedFileList = []

newPaper24 = PaperData("M V Berry", "Transitionless quantum driving", "2009", "/home/aztar/Dropbox/SyncHacc/Peroni19/Papers/Berry2009.pdf", 24, [], "", 0)
papers.append(newPaper24)
selectedFileList.append({"title": "Transitionless quantum driving", "authors": "M V Berry", "fileName": "/home/aztar/Dropbox/SyncHacc/Peroni19/Papers/Berry2009.pdf"})

newPaper25 = PaperData("E. Torrontegui", "Shortcuts to adiabaticity", "2015", "/home/aztar/Dropbox/SyncHacc/Peroni19/Papers/muga2015.pdf", 25, [], "", 0)
papers.append(newPaper25)
selectedFileList.append({"title": "Shortcuts to adiabaticity", "authors": "E. Torrontegui", "fileName": "/home/aztar/Dropbox/SyncHacc/Peroni19/Papers/muga2015.pdf"})


newPaper26 = PaperData("Shuo-Yen Tseng", "Counterdiabatic mode-evolution based coupled-waveguide devices", "2013", "/home/aztar/Dropbox/SyncHacc/Peroni19/Papers/oe-21-18-21224.pdf", 26, [], "", 0)
papers.append(newPaper26)

newPaper27 = PaperData("Shuo-Yen Tseng", "Short and robust directional couplers designed by shortcuts to adiabaticity", "2014", "/home/aztar/Dropbox/SyncHacc/Peroni19/Papers/oe-22-16-18849.pdf", 27, [], "", 0)
papers.append(newPaper27)

newPaper28 = PaperData("Tzu-Hsuan Pan", "Short and robust silicon mode (de)multiplexers using shortcuts to adiabaticity", "2015", "/home/aztar/Dropbox/SyncHacc/Peroni19/Papers/oe-23-8-10405.pdf", 28, [], "", 0)
papers.append(newPaper28)

newPaper29 = PaperData("M. Bukov", "Geometric Speed Limit of Accessible Many-Body State Preparation", "2019", "/home/aztar/Dropbox/SyncHacc/Peroni19/PapersWithTwoCol/PhysRevX.9.011034.pdf", 29, [], "", 0)
papers.append(newPaper29)

newPaper30 = PaperData("Xiao-Jing Lu", "Fast and robust population transfer in two-level quantum systems with dephasing noise and/or systematic frequency errors", "2013", "/home/aztar/Dropbox/SyncHacc/Peroni19/PapersWithTwoCol/PhysRevA.88.033406.pdf", 30, [], "", 0)
papers.append(newPaper30)

layout = [

    [

        sg.Column(file_list_column),

        sg.VSeperator(),

        sg.Column(pdfSelectedViewer(10)),

    ]

]

window = sg.Window("Select PDFs to Map", layout)



def pdfSelectedListboxManager():

    global selectedFileList
    global currId
    global window
    global papers
    global report_names

    for entry in selectedFileList:
        print("help me")
        tempArray.append(str(entry["fileName"]) + "\t -> \t" + str(entry["title"]))
    
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

        title = " ".join(title.split('\n'))
        authors = " ".join(authors.split('\n'))

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

    elif event == 'Generate Map':
        print(folder)
        '''tempFileName = []
        for selected in selectedFileList:
            tempFileName.append(folder+"/"+str(selected["fileName"]))'''
        links = findCitations(papers)

        print('execute')
        makeGraph(papers, values["output"])
        
        print(values["output"])
        break



window.close()





