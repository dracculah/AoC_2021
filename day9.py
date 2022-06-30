def getMatrix(heatmap):
	matrix = []
	for line in heatmap:
		matrix_line = []
		for c in line:
			# consistency check
			assert(c in "0123456789")
			matrix_line.append(int(c))
		matrix.append(matrix_line)
	return matrix

def getLowPoints(heatmap):
	pointz={}
	# create a matrix
	matrix = getMatrix(heatmap)
	# calc low points
	for x in range(len(matrix)):
		for y in range(len(matrix[x])):
			val = matrix[x][y]
			lower = 0
			if (((x>0) and (matrix[x-1][y] > val)) or (x==0)):
				lower += 1
			if (((x<len(matrix)-1) and (matrix[x+1][y] > val)) or (x==len(matrix)-1)):
				lower += 1
			if (((y>0) and (matrix[x][y-1] > val)) or (y==0)):
				lower += 1
			if (((y<len(matrix[x])-1) and (matrix[x][y+1] > val)) or (y==len(matrix[x])-1)):
				lower += 1
			if (lower == 4):
				coord=(x,y)
				pointz[coord] = val
	return pointz

def printTableForDebug(heatmap, low_pointz):
	x=0
	y=0
	print("\n\nPrinting the table for DEBUG:")
	for line in heatmap:
		_str = ""
		y=0
		for c in line:
			coordz = (x,y)
			try:
				low_pointz[coordz]
				_str += " *{}* ".format(c)
			except:
				_str += "  {}  ".format(c)
			y += 1
		print(_str)
		x += 1
	print("\n\n")

def day9_task(heatmap):
	pointz = getLowPoints(heatmap)
	risk = 0
	for x,y in pointz.keys():
		val = pointz[(x,y)]
		print("DEBUG: val -> {}, at ({},{})".format(val,x+1,y+1))
		risk += val+1
	printTableForDebug(heatmap,pointz)
	return risk

example="""2199943210
3987894921
9856789892
8767896789
9899965678"""

risk = day9_task(example.split("\n"))
print("risk -> {}".format(risk))

