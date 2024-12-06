guardPosition = [0,0]
origionalGuardPosition = [0,0]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

columns = []
facing = UP

done = False
loopsFound = 0

foundObstacles = []

def copyList(list):
	newList = []
	for item in list:
		newList.append(item)
	return newList

def turnRight():
	global facing
	facing += 1
	if facing > 3:
		facing = UP

def setCharOnPosition(character, position):
	global lines
	global columns
	lines[position[1]][position[0]] = character
	columns[position[0]][position[1]] = character

def fillPathWithX(firstPosition, secondPosition):
	if facing == UP:
		delta = firstPosition[1] - secondPosition[1]
		index = firstPosition[1] - delta
		for i in range(len(columns[firstPosition[0]])):
			setCharOnPosition("X", [firstPosition[0],index])
			index += 1
			if (index == firstPosition[1] + 1):
				break
	if facing == RIGHT:
		delta = secondPosition[0] - firstPosition[0]
		index = firstPosition[0]
		for i in range(len(lines[firstPosition[1]])):
			setCharOnPosition("X", [index,firstPosition[1]])
			index += 1
			if (index > secondPosition[0]):
				break
	if facing == DOWN:
		delta = secondPosition[1] - firstPosition[1]
		index = firstPosition[1]
		for i in range(len(columns[firstPosition[0]])):
			setCharOnPosition("X", [firstPosition[0],index])
			index += 1
			if (index == secondPosition[1] + 1):
				break
	if facing == LEFT:
		delta = firstPosition[0] - secondPosition[0]
		index = secondPosition[0]
		for i in range(len(lines[firstPosition[1]])):
			setCharOnPosition("X", [index,firstPosition[1]])
			index += 1
			if (index > firstPosition[0]):
				break

def moveGuard():
	global guardPosition
	global done
	global lines
	global columns
	global facing
	global foundObstacles
	global loopsFound
	obstacleOnPath = False
	newGuardPosition = [0,0]
	origionalPosition = guardPosition

	if facing == UP:
		lastObstaclePosition = [0,0]
		for y in range(len(columns[guardPosition[0]])):
			character = columns[guardPosition[0]][y]
			if character == "#":
				lastObstaclePosition = [guardPosition[0],y]
				obstacleOnPath = True
			if character == "^":
				break
		newGuardPosition = [lastObstaclePosition[0], lastObstaclePosition[1] + 1]
		if not obstacleOnPath:
			newGuardPosition = [origionalPosition[0],-1]
		else:
			foundObstacles.append([newGuardPosition, facing])

	if facing == RIGHT:
		obstaclePosition = [0,0]
		reading = False
		for x in range(len(lines[guardPosition[1]])):
			character = lines[guardPosition[1]][x]			
			if character == "^":
				reading = True
			if character == "#" and reading:
				obstacleOnPath = True
				obstaclePosition = [x, guardPosition[1]]
				break
		newGuardPosition = [obstaclePosition[0] - 1, obstaclePosition[1]]
		if not obstacleOnPath:
			newGuardPosition = [len(lines[0])-1,origionalPosition[1]]
		else:
			foundObstacles.append([newGuardPosition, facing])

	if facing == DOWN:
		obstaclePosition = [0,0]
		reading = False
		for y in range(len(columns[guardPosition[0]])):
			character = columns[guardPosition[0]][y]
			if character == "^":
				reading = True
			if character == "#" and reading:
				obstaclePosition = [guardPosition[0],y]
				obstacleOnPath = True
				break
		newGuardPosition = [obstaclePosition[0], obstaclePosition[1] - 1]
		if not obstacleOnPath:
			newGuardPosition = [origionalPosition[0],len(columns)-1]
		else:
			foundObstacles.append([newGuardPosition, facing])

	if facing == LEFT:
		lastObstaclePosition = [0,0]
		for x in range(len(lines[guardPosition[1]])):
			character = lines[guardPosition[1]][x]
			if character == "#":
				lastObstaclePosition = [x, guardPosition[1]]
				obstacleOnPath = True
			if character == "^":
				break
		newGuardPosition = [lastObstaclePosition[0] + 1, lastObstaclePosition[1]]
		if not obstacleOnPath:
			newGuardPosition = [-1,origionalPosition[1]]
		else:
			foundObstacles.append([newGuardPosition, facing])


	fillPathWithX(origionalPosition, newGuardPosition)
	setCharOnPosition("^", newGuardPosition)
	guardPosition = newGuardPosition

	loopFound = False

	for i in range(len(foundObstacles) - 1):
		hit = foundObstacles[i]
		if (hit[0] == newGuardPosition and facing == hit[1]):
			loopsFound += 1
			loopFound = True
			done = True

	if (not obstacleOnPath):
		done = True


def parseLines():
	global lines
	global columns
	global guardPosition
	global origionalGuardPosition
	file = open('input.txt')
	lines = file.readlines()
	for x in range(len(lines[0])):
		columns.append([])

	for y in range(len(lines)):
		line = lines[y]
		lines[y] = list(line)
		lines[y].pop(len(lines[y])-1)
		for x in range(len(line)):
			character = line[x]
			columns[x].append(character)
			if (character == "^"):
				guardPosition = [x,y]
				origionalGuardPosition = guardPosition
	columns.pop(len(columns)-1)

def run():
	global done
	global guardPosition
	global origionalGuardPosition
	global facing
	global foundObstacles
	foundObstacles.clear()
	facing = UP
	guardPosition = origionalGuardPosition
	done = False
	while not done:
		moveGuard()
		turnRight()

parseLines()

origionalLines = copyList(lines)
origionalColumns = copyList(columns)

run()
potentialPositions = []

total = 0

for y in range(len(lines)):
	for x in range(len(columns)):
		character = columns[x][y]
		if character == "X" or character == "^":
			if not [x,y] == origionalGuardPosition:
				potentialPositions.append([x,y])
				total += 1

i = 0
for position in potentialPositions:
	print(str(i) + " / " + str(len(potentialPositions)))
	lines.clear()
	columns.clear()
	foundObstacles.clear()
	parseLines()
	setCharOnPosition("#", position)
	run()
	i += 1

print(loopsFound)