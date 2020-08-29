
import PySimpleGUI as sg

import os.path

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
        tempArray.append(entry["fileName"])


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
        print('execute')
        print(folder)



window.close()





