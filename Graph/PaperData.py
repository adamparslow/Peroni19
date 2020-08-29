class PaperData: 
    def __init__(self, author, title, year, id, citations):
        self.author = author
        self.title = title
        self.year = year
        self.id = id
        self.citations = citations




dummyData = []

dummyData[0] = PaperData("Berry","Transitionless quantum driving","2009",1,[2,3,4,6])
dummyData[1] = PaperData("Tseng","Counterdiabatic mode-evolution based coupled-waveguide devices","2013",2,[])
dummyData[2] = PaperData("Muga","Shortcuts to adiabaticity","2015",3,[6])
dummyData[3] = PaperData("Tseng","Engineering of fast mode conversion in multimode waveguides","2012",4,[3])
dummyData[4] = PaperData("Guo","Silicon mode (de)multiplexers with parameters optimized using shortcuts to adiabaticity","2017",5,[6])
dummyData[5] = PaperData("Guery-Odelin","Shortcuts to adiabaticity: Concepts, methods, and applications","2019",6,[])


