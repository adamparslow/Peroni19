import pygraphviz as pgv
from PaperData import *
import matplotlib.pyplot as plt
import matplotlib 
import drawSvg as draw
from drawSvg.widgets import DrawingWidget
import svgutils.transform as sg
import sys 

A = pgv.AGraph(directed=True, overlap=True, splines="ortho")

def createEdge(graph, src, dest): 
	graph.add_edge(src, dest)
	
def createNode(graph, node, x, y, label, url, color, height=2, width=3):
	graph.add_node(node, pos=str(x) + ", " + str(y) + "!", 
		label=label, height=height, width=width, 
		shape="polygon", sides=4, fontsize=29, fillcolor=color, href=url)

def getYear(paper):
	return int(paper.year)

def getTimescale(papers, widthPerYear=4, edgeWidth=10, height=3):
	years = list(map(getYear, papers))
	
	timeBounds = [min(years),max(years)]

	imageWidth = widthPerYear*(timeBounds[1]-timeBounds[0])
	# want a function that maps year to pixel location
	prevYear = ""
	yearCount = 0
	alternative = 1
	for paper in papers:
		timescale = widthPerYear*(getYear(paper) - timeBounds[0]) + edgeWidth
		paper.x = timescale
		
		if (prevYear == paper.year):
			yearCount += 1
			paper.y = height * alternative + height * yearCount
		else: 
			yearCount = 0
			prevYear = paper.year

			if alternative == 0: 
				alternative = 1 
			else:
				alternative = 0
			paper.y = height * alternative


def writeBoxContents(paper):
	stringToWrite = paper.author + " (" + paper.year + ")\n" "\"" + paper.title + "\"" 
	# make it a link somehow...

	return stringToWrite

def getNumWords(paper):
	return paper.numWords

def drawTimeline(minYear, maxYear, width=3279, margin=200):
	boxStart = margin
	boxEnd = width - margin
	numTicks = maxYear - minYear + 1
	tickHeight = 15
	thickness = 5
	height = 80
	correctionFactor = 27
	d = draw.Drawing(width, height)

	d.append(draw.Rectangle(0, 0, width, height, fill='white'))
	d.append(draw.Rectangle(boxStart, height/2, boxEnd - boxStart, thickness, fill='black'))
	tickSeparation = (boxEnd - boxStart - thickness) / (numTicks-1)

	for tick in range(numTicks):
		x = boxStart + tick * tickSeparation
		y = height/2 - tickHeight
		d.append(draw.Rectangle(x, y, thickness, tickHeight, fill='black'))
		d.append(draw.Text(str(minYear + tick), 29, x-correctionFactor, y - 20))

	d.saveSvg('timeline.svg')

dummyData = []

dummyData.append(PaperData("Berry","Transitionless quantum driving","2009",1,[2,3,4,6], "http://www.google.com", 100))
dummyData.append(PaperData("Berry","Transitionless quantum driving again","2009",7,[2,3,4,6], "http://www.google.com", 200))
dummyData.append(PaperData("Berry","Transitionless quantum driving again again","2009",8,[2,3,4,6], "http://www.google.com", 300))
dummyData.append(PaperData("Tseng","Counterdiabatic mode-evolution based coupled-waveguide devices","2013",2,[], "/home/aztar/Downloads/Paper.pdf", 400))
dummyData.append(PaperData("Muga","Shortcuts to adiabaticity","2015",3,[6], "", 600))
dummyData.append(PaperData("Tseng","Engineering of fast mode conversion in multimode waveguides","2012",4,[3], "", 700))
dummyData.append(PaperData("Tseng","Engineering of fast mode conversion in multimode waveguides again","2012",10,[3], "", 800))
dummyData.append(PaperData("Guo","Silicon mode (de)multiplexers with parameters optimized using shortcuts to adiabaticity","2017",5,[6], "", 900))
dummyData.append(PaperData("Guery-Odelin","Shortcuts to adiabaticity: Concepts, methods, and applications","2019",6,[], "", 1000))

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

	createNode(A, paper.id, paper.x, paper.y, writeBoxContents(paper), paper.url, hex)
	
	for cit in paper.citations:
		createEdge(A, paper.id, cit)

A.node_attr['style']='filled'

A.layout(prog='neato')
A.draw('map.svg', format='svg')

years = list(map(getYear, dummySorted))
minYear = min(years)
maxYear = max(years)

drawTimeline(minYear, maxYear)

fig = sg.SVGFigure("3279pt", "688pt")

fig1 = sg.fromfile('map.svg')
fig2 = sg.fromfile('timeline.svg')

plot1 = fig1.getroot()
plot2 = fig2.getroot()
plot2.moveto(0, 688)

fig.append([plot1, plot2])

fig.save("combined.svg")