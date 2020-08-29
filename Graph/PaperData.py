class PaperData: 
    def __init__(self, author, title, year, id, citations, url, numWords):
        self.author = author
        self.title = title
        self.year = year
        self.id = id
        self.citations = citations
        self.x = 0
        self.y = 0
        self.url = url
        self.numWords = numWords
        
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

