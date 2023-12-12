lines = open("input1.txt").read().splitlines()
galaxies = [] # number, x, y
emptyLines = []
emptyColumns = []
copyMultiplier = 1000000
copyMultiplier-= 1

for l in range(len(lines)):
	line = lines[l]
	allSpace = True
	for character in line:
		if not character == ".":
			allSpace = False
			break
	if allSpace:
		emptyLines.append(l)

for c in range(len(lines[0])):
	allSpace = True
	for l in range(len(lines)):
		if not lines[l][c] == ".":
			allSpace = False
	if allSpace:
		emptyColumns.append(c)

skyMap = lines

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
			newDistanceX = distanceX
			isNegative = False
			if newDistanceX < 0:
				isNegative = True
				newDistanceX = newDistanceX * -1
				distanceX = distanceX * -1
			for i in range(distanceX):
				for number in emptyColumns:
					if not isNegative:
						if galaxy[1] + i + 1 == number:
							newDistanceX += copyMultiplier
					else:
						if galaxy[1] - i - 1 == number:
							newDistanceX += copyMultiplier
			distanceX = newDistanceX

			distanceY = otherGalaxy[2] - galaxy[2]
			newDistanceY = distanceY
			isNegative = False
			if newDistanceY < 0:
				isNegative = True
				newDistanceY = newDistanceY * -1
				distanceY = distanceY * -1
			for i in range(distanceY):
				for number in emptyLines:
					if not isNegative:
						if galaxy[2] + i == number:
							newDistanceY += copyMultiplier
					else:
						if galaxy[2] - i == number:
							newDistanceY += copyMultiplier
			distanceY = newDistanceY

			distance = distanceX + distanceY
			galaxy[3].append([otherGalaxy[0], distance])
			total += distance

print("Result: " + str(int(total / 2))) # devide by 2 because every distance is calculated twice