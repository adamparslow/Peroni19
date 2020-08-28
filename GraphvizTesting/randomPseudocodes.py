# random functions for flowchart


def getTimescale(stuff):
	timeBounds = [min(years),max(years)]

	widthPerYear = 300
	imageWidth = widthPerYear*(timeBounds[2]-timeBounds[1])
	edgeWidth = 50
	# want a function that maps year to pixel location
	timescale = widthPerYear*(year - timeBounds[1]) + edgeWidth
	return

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


def writeBoxContents(stuff):
	stringToWrite = author + "(" + year + ")\n" "\"" + title "\"" 
	# make it a link somehow...

	# write to .dot file

	return


def addTimescale():
	# happens after all the graphviz stuff is done and saved as svg
	dwg = svgwrite.Drawing('test.svg', profile='tiny')
	dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))

	# add years:
	dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
	dwg.save()

	return



