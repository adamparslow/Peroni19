class PaperData: 
    def __init__(self, author, title, year, fileName, id, citations, url, numPages):
        self.author = author
        self.title = title
        self.year = year
        self.fileName = fileName
        self.id = id
        self.citations = citations
        self.x = 0
        self.y = 0
        self.url = url
        self.numPages = numPages
        
        self.addNewLines()
        
    def addNewLines(self):
        separator = 15
        charList = list(self.title)
        charIndex = separator
        while (charIndex < len(charList)):
            if (charList[charIndex] == ' '):
                charList[charIndex] = '\n'
                charIndex += separator
            else:
                charIndex += 1
        self.title = "".join(charList)

    def addCitation(self, citation):
        self.citations.append(citation)