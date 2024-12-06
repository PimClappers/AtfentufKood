file = open('input.txt')
lines = file.readlines()

guardPosition = [0,0]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

columns = []
facing = UP

done = False

def turnRight():
	global facing
	facing += 1
	if facing > 3:
		facing = UP

def setXOnPosition(position):
	lines[position[1]][position[0]] = "X"
	columns[position[0]][position[1]] = "X"

def fillPathWithX(firstPosition, secondPosition):
	if facing == UP:
		delta = firstPosition[1] - secondPosition[1]
		index = firstPosition[1] - delta
		for i in range(len(columns[firstPosition[0]])):
			setXOnPosition([firstPosition[0],index])
			index += 1
			if (index == firstPosition[1] + 1):
				break
	if facing == RIGHT:
		delta = secondPosition[0] - firstPosition[0]
		index = firstPosition[0]
		for i in range(len(lines[firstPosition[1]])):
			setXOnPosition([index,firstPosition[1]])
			index += 1
			if (index > secondPosition[0]):
				break
	if facing == DOWN:
		delta = secondPosition[1] - firstPosition[1]
		index = firstPosition[1]
		for i in range(len(columns[firstPosition[0]])):
			setXOnPosition([firstPosition[0],index])
			index += 1
			if (index == secondPosition[1] + 1):
				break
	if facing == LEFT:
		delta = firstPosition[0] - secondPosition[0]
		index = secondPosition[0]
		for i in range(len(lines[firstPosition[1]])):
			setXOnPosition([index,firstPosition[1]])
			index += 1
			if (index > firstPosition[0]):
				break

def moveGuard():
	global guardPosition
	global done
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


	fillPathWithX(origionalPosition, newGuardPosition)
	columns[newGuardPosition[0]][newGuardPosition[1]] = "^"
	lines[newGuardPosition[1]][newGuardPosition[0]] = "^"
	guardPosition = newGuardPosition

	done = not obstacleOnPath


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
columns.pop(len(columns)-1)

total = 0

while not done:
	moveGuard()
	turnRight()

for line in lines:
	for character in line:
		if character == "X":
			total += 1
print(total + 1)
