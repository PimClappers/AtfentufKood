lines = open("input1.txt").read().splitlines()
linesCopy = lines[:]
nLinesInserted = 0
nCharsInserted = 0
galaxies = [] # number, x, y

for l in range(len(lines)):
	line = lines[l]
	allSpace = True
	for character in line:
		if not character == ".":
			allSpace = False
			break
	if allSpace:
		linesCopy.insert(l + nLinesInserted, lines[l])
		nLinesInserted += 1

for c in range(len(lines[0])):
	allSpace = True
	for l in range(len(lines)):
		if not lines[l][c] == ".":
			allSpace = False
	if allSpace:
		for l in range(len(linesCopy)):
			newLine = str(linesCopy[l])
			newLine = newLine[0: c + nCharsInserted] + "." + newLine[c+nCharsInserted:len(newLine)]
			linesCopy[l] = newLine
		nCharsInserted += 1

skyMap = linesCopy

for y in range(len(skyMap)):
	line = skyMap[y]
	for x in range(len(line)):
		character = skyMap[y][x]
		if character == "#":
			galaxies.append([len(galaxies), x, y, []]) # number, x, y

total = 0

for galaxy in galaxies:
	for otherGalaxy in galaxies:
		if not galaxy[0] == otherGalaxy[0]:
			distanceX = otherGalaxy[1] - galaxy[1]
			distanceY = otherGalaxy[2] - galaxy[2]
			if distanceX < 0:
				distanceX = distanceX * -1
			if distanceY < 0:
				distanceY = distanceY * -1
			distance = distanceX + distanceY
			galaxy[3].append([otherGalaxy[0], distance])
			total += distance

print("Result: " + str(int(total / 2))) # devide by 2 because every distance is calculated twice