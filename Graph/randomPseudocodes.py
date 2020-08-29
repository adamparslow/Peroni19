# random functions for flowchart

def getYears(paper):
	return paper.year

def getTimescale(papers, widthPerYear=3, edgeWidth=0.5):
	years = map(getYears, papers)
	
	print(years)
	timeBounds = [min(years),max(years)]

	imageWidth = widthPerYear*(timeBounds[1]-timeBounds[0])
	# want a function that maps year to pixel location
	xCoords = []
	for paper in papers:
		timescale = widthPerYear*(year - timeBounds[0]) + edgeWidth
		xCoords.append(timescale)
	return xCoords

def setAreaFactors(scalingConstant):
	# for size scaling, desire that numpages/box area is constant over the svg
	# have to first see which one is the constraining box for title length
	# or just hardcode...
	for index in range():
		# get min sizes 
		height = scalingConstant*np.sqrt(numPages[index])
		width = scalingConstant*np.sqrt(numPages[index])

		# write to .dot file
	return


def writeBoxContents(paper):
	stringToWrite = paper.author + "(" + paper.year + ")\n" "\"" + paper.title "\"" 
	# make it a link somehow...

	return stringToWrite


def addTimescale():
	# happens after all the graphviz stuff is done and saved as svg
	dwg = svgwrite.Drawing('test.svg', profile='tiny')
	dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))

	# add years:
	dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
	dwg.save()

	return



