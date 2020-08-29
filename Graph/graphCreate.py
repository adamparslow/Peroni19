import pygraphviz as pgv
from PaperData import *
import matplotlib.pyplot as plt
import matplotlib 
import drawSvg as draw
from drawSvg.widgets import DrawingWidget
import svgutils.transform as svg
import sys 
import os

def createEdge(graph, src, dest): 
	graph.add_edge(dest, src)
	
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
	return paper.numPages

def drawTimeline(minYear, maxYear, width=3279, margin=200):
	boxStart = margin
	boxEnd = width - margin
	numTicks = maxYear - minYear + 1
	tickHeight = 15
	thickness = 5
	height = 80
	correctionFactor = 35
	d = draw.Drawing(width, height)

	d.append(draw.Rectangle(0, 0, width, height, fill='white'))
	d.append(draw.Rectangle(boxStart, height/2, boxEnd - boxStart, thickness, fill='black'))
	tickSeparation = (boxEnd - boxStart - thickness) / (numTicks-1)

	for tick in range(numTicks):
		x = boxStart + tick * tickSeparation
		y = height/2 - tickHeight
		d.append(draw.Rectangle(x, y, thickness, tickHeight, fill='black'))
		d.append(draw.Text(str(minYear + tick), 29, x-correctionFactor, y - 24))

	d.saveSvg('timeline.svg')

def createKey(minWords, maxWords):
	d = draw.Drawing(450, 100)
	colorFn = plt.get_cmap("Wistia")
	x = 70
	y = 50
	length = 300
	width = 30
	g = draw.LinearGradient(x, y, x+length, y+width)
	min = matplotlib.colors.rgb2hex(colorFn(0)[:3])
	max = matplotlib.colors.rgb2hex(colorFn(1.0)[:3])
	g.addStop(0, min, 1)
	g.addStop(1, max, 1)
	d.append(draw.Text("Key", 29, 0, 55))
	d.append(draw.Text(str(minWords), 29, 50, 20))
	d.append(draw.Text("Pages", 29, 178, 20))
	d.append(draw.Text(str(maxWords), 29, 350, 20))
	d.append(draw.Rectangle(x, y, length, width, stroke='black', stroke_width=1, fill=g))

	d.saveSvg('key.svg')
	
def makeGraph(papers, output):
	A = pgv.AGraph(directed=True, overlap=True, splines="ortho")
	papersSorted = sorted(papers, key=lambda paper: paper.year)
	words = list(map(getNumWords, papersSorted))
	minWords = min(words)
	maxWords = max(words)

	getTimescale(papersSorted)

	for paper in papersSorted:
		colorFn = plt.get_cmap("Wistia")

		# calculation would be something like
		rgb = colorFn((paper.numPages-minWords)/(maxWords-minWords))[:3]
		hex = matplotlib.colors.rgb2hex(rgb)

		createNode(A, paper.id, paper.x, paper.y, writeBoxContents(paper), paper.url, hex)
		
		for cit in paper.citations:
			createEdge(A, paper.id, cit)

	A.node_attr['style']='filled'

	A.layout(prog='neato')
	A.draw('map.svg', format='svg')

	years = list(map(getYear, papersSorted))
	minYear = min(years)
	maxYear = max(years)

	drawTimeline(minYear, maxYear)
	createKey(minWords, maxWords)

	fig = svg.SVGFigure("3279pt", "850pt")

	fig1 = svg.fromfile('key.svg')
	fig2 = svg.fromfile('map.svg')
	fig3 = svg.fromfile('timeline.svg')

	plot1 = fig1.getroot()
	plot1.moveto(2829, 100)
	plot2 = fig2.getroot()
	plot2.moveto(0, 100)
	plot3 = fig3.getroot()
	plot3.moveto(0, 850)

	fig.append([plot2, plot3, plot1])

	fig.save(output + ".svg")
	os.remove('map.svg')
	os.remove('timeline.svg')
	os.remove('key.svg')
	

# dummyData = []

# dummyData.append(PaperData("Berry","Transitionless quantum driving","2009",1,[2,3,4,6], "http://www.google.com", 10))
# dummyData.append(PaperData("Berry","Transitionless quantum driving again","2009",7,[2,3,4,6], "http://www.google.com", 20))
# dummyData.append(PaperData("Berry","Transitionless quantum driving again again","2009",8,[2,3,4,6], "http://www.google.com", 30))
# dummyData.append(PaperData("Tseng","Counterdiabatic mode-evolution based coupled-waveguide devices","2013",2,[], "/home/aztar/Downloads/Paper.pdf", 40))
# dummyData.append(PaperData("Muga","Shortcuts to adiabaticity","2015",3,[6], "", 60))
# dummyData.append(PaperData("Tseng","Engineering of fast mode conversion in multimode waveguides","2012",4,[3], "", 70))
# dummyData.append(PaperData("Tseng","Engineering of fast mode conversion in multimode waveguides again","2012",10,[3], "", 80))
# dummyData.append(PaperData("Guo","Silicon mode (de)multiplexers with parameters optimized using shortcuts to adiabaticity","2017",5,[6], "", 90))
# dummyData.append(PaperData("Guery-Odelin","Shortcuts to adiabaticity: Concepts, methods, and applications","2019",6,[], "", 10))
# makeGraph(dummyData, "combined")

