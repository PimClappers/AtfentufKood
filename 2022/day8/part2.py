treeLines = open("input.txt").read().split()

nAround = 2*len(treeLines[0]) + 2*(len(treeLines)-2)

nTreelines = len(treeLines)

visibleTrees = []
scores = []

for x in range(nTreelines):
	if (x == 0) or (x == nTreelines-1):
		continue
	for y in range(len(treeLines[x])):
		if (y == 0) or (y == len(treeLines[x])-1):
			continue		
		currentTreeHeight = treeLines[x][y]
		alreadySeen = False
		score  = []
		
		#right
		isVisible = True
		tempScore = 0
		j = y + 1
		while j < len(treeLines[x]):
			treeHeight = treeLines[x][j]			
			if (j == y):
				j+=1
				continue
			tempScore += 1
			if (treeHeight >= currentTreeHeight):
				isVisible = False
				break
			j += 1			
		if (isVisible and not alreadySeen):
			visibleTrees.append(currentTreeHeight)
			alreadySeen = True
		score.append(tempScore)

		#left
		isVisible = True
		tempScore = 0
		j = y - 1
		while j >= 0:
			treeHeight = treeLines[x][j]
			if (j == y):
				j-=1
				continue
			tempScore += 1
			if (treeHeight >= currentTreeHeight):
				isVisible = False
				break
			j -= 1
		if (isVisible and not alreadySeen):
			visibleTrees.append(currentTreeHeight)
			alreadySeen = True
		score.append(tempScore)

		#bottom
		isVisible = True
		tempScore = 0
		j = x + 1
		while j < nTreelines:
			treeHeight = treeLines[j][y]
			if (j == x):
				j+=1
				continue
			tempScore += 1
			if (treeHeight >= currentTreeHeight):
				isVisible = False
				break
			j += 1
		if (isVisible and not alreadySeen):
			visibleTrees.append(currentTreeHeight)
			alreadySeen = True
		score.append(tempScore)

		#top
		isVisible = True
		tempScore = 0
		j = x - 1
		while j >= 0:
			treeHeight = treeLines[j][y]
			if (j == x):
				j-=1
				continue
			tempScore += 1
			if (treeHeight >= currentTreeHeight):
				isVisible = False
				break
			j -= 1
		if (isVisible and not alreadySeen):
			visibleTrees.append(currentTreeHeight)
			alreadySeen = True
		score.append(tempScore)
		print(score)

		scores.append(score[0]*score[1]*score[2]*score[3])
	
print(max(scores))