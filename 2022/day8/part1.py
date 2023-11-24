treeLines = open("input2.txt").read().split()

nAround = 2*len(treeLines[0]) + 2*(len(treeLines)-2)

nTreelines = len(treeLines)

visibleTrees = []

for x in range(nTreelines):
	if (x == 0) or (x == nTreelines-1):
		continue
	for y in range(len(treeLines[x])):
		if (y == 0) or (y == len(treeLines[x])-1):
			continue		
		currentTreeHeight = treeLines[x][y]
		alreadySeen = False
		
		#from left
		isVisible = True
		for j in range(len(treeLines[x])):
			treeHeight = treeLines[x][j]
			if (j == y):
				break
			if (treeHeight >= currentTreeHeight):
				isVisible = False
				break
		if (isVisible and not alreadySeen):
			visibleTrees.append(currentTreeHeight)
			alreadySeen = True

		#from right
		isVisible = True
		j = len(treeLines[x])-1
		while j >= 0:
			treeHeight = treeLines[x][j]
			if (j == y):
				break
			if (treeHeight >= currentTreeHeight):
				isVisible = False
				break
			j -= 1
		if (isVisible and not alreadySeen):
			visibleTrees.append(currentTreeHeight)
			alreadySeen = True

		#from top
		isVisible = True
		j = 0
		while j < nTreelines-1:
			treeHeight = treeLines[j][y]
			if (j == x):
				break
			if (treeHeight >= currentTreeHeight):
				isVisible = False
				break
			j += 1
		if (isVisible and not alreadySeen):
			visibleTrees.append(currentTreeHeight)
			alreadySeen = True

		#from bottom
		isVisible = True
		j = nTreelines-1
		while j >= 0:
			treeHeight = treeLines[j][y]
			if (j == x):
				break
			if (treeHeight >= currentTreeHeight):
				isVisible = False
				break
			j -= 1
		if (isVisible and not alreadySeen):
			visibleTrees.append(currentTreeHeight)
			alreadySeen = True
	
print(len(visibleTrees) + nAround)