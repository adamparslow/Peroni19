import pygraphviz as pgv
from PaperData import *
import matplotlib.pyplot as plt
import matplotlib 

A = pgv.AGraph(directed=True, overlap=True, splines="ortho")

def createEdge(graph, src, dest): 
	graph.add_edge(src, dest)
	
def createNode(graph, node, x, y, label, color, height=2, width=3):
	graph.add_node(node, pos=str(x) + ", " + str(y) + "!", 
		label=label, height=height, width=width, 
		shape="polygon", sides=4, fontsize=29, fillcolor=color)

def getYear(paper):
	return int(paper.year)

def getTimescale(papers, widthPerYear=4, edgeWidth=10, height=3):
	years = list(map(getYear, papers))
	
	timeBounds = [min(years),max(years)]

	imageWidth = widthPerYear*(timeBounds[1]-timeBounds[0])
	# want a function that maps year to pixel location
	alternative = 0
	for paper in papers:
		timescale = widthPerYear*(getYear(paper) - timeBounds[0]) + edgeWidth
		paper.x = timescale
		paper.y = height * alternative
		if alternative == 0: 
			alternative = 1 
		else:
			alternative = 0

def writeBoxContents(paper):
	stringToWrite = paper.author + " (" + paper.year + ")\n" "\"" + paper.title + "\"" 
	# make it a link somehow...

	return stringToWrite

def getNumWords(paper):
	return paper.numWords

dummyData = []

dummyData.append(PaperData("Berry","Transitionless quantum driving","2009",1,[2,3,4,6], 100))
dummyData.append(PaperData("Tseng","Counterdiabatic mode-evolution based coupled-waveguide devices","2013",2,[], 1500))
dummyData.append(PaperData("Muga","Shortcuts to adiabaticity","2015",3,[6], 2))
dummyData.append(PaperData("Tseng","Engineering of fast mode conversion in multimode waveguides","2012",4,[3], 2000))
dummyData.append(PaperData("Guo","Silicon mode (de)multiplexers with parameters optimized using shortcuts to adiabaticity","2017",5,[6], 700))
dummyData.append(PaperData("Guery-Odelin","Shortcuts to adiabaticity: Concepts, methods, and applications","2019",6,[], 1800))

dummySorted = sorted(dummyData, key=lambda paper: paper.year)
words = list(map(getNumWords, dummySorted))
minWords = min(words)
maxWords = max(words)


getTimescale(dummySorted)

for paper in dummySorted:
	colorFn = plt.get_cmap("Wistia")

	# calculation would be something like
	rgb = colorFn((paper.numWords-minWords)/(maxWords-minWords))[:3]
	hex = matplotlib.colors.rgb2hex(rgb)

	createNode(A, paper.id, paper.x, paper.y, writeBoxContents(paper), hex)
	
	for cit in paper.citations:
		createEdge(A, paper.id, cit)

A.node_attr['style']='filled'

A.layout(prog='neato')
A.draw('map.svg', format='svg')