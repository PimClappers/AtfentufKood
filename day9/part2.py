commands = open("input3.txt").read().split("\n")

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

TOPRIGHT = 'TR'
BOTTOMRIGHT = 'BR'
TOPLEFT = 'TL'
BOTTOMLEFT = 'BL'

knotPositions = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
Hposition = knotPositions[0]
Tposition = knotPositions[9]
visited = [[0,0]]

def getDirectionToMove(knotIndex):
	global knotPositions
	knotToCheck = knotPositions[knotIndex]
	parentKnot = knotPositions[knotIndex-1]
	if (knotToCheck[0] == parentKnot[0]):
		if (knotToCheck[1] < parentKnot[1]):
			return UP
		else:
			return DOWN
	elif (knotToCheck[1] == parentKnot[1]):
		if (knotToCheck[0] < parentKnot[0]):
			return RIGHT
		else:
			return LEFT

	elif (parentKnot[0] > knotToCheck[0]):
		if (parentKnot[1] > knotToCheck[1]):
			return TOPRIGHT
		else:
			return BOTTOMRIGHT
	elif (parentKnot[0] < knotToCheck[0]):
		if (parentKnot[1] > knotToCheck[1]):
			return TOPLEFT
		else:
			return BOTTOMLEFT

def checkIfTouchingParent(knotIndex):
	global Hposition
	global Tposition
	global knotPositions
	knotToCheck = knotPositions[knotIndex]
	parentKnot = knotPositions[knotIndex-1]
	if (knotToCheck == parentKnot):
		return True
	if (knotToCheck[0] - parentKnot[0] <= 1 and knotToCheck[0] - parentKnot[0] >= -1):
		if (knotToCheck[1] - parentKnot[1] <= 1 and knotToCheck[1] - parentKnot[1] >= -1):
			return True
	if (knotToCheck[1] - parentKnot[1] <= 1 and knotToCheck[1] - parentKnot[1] >= -1):
		if (knotToCheck[0] - parentKnot[0] <= 1 and knotToCheck[0] - parentKnot[0] >= -1):
			return True
	return False

def moveT(knotIndex, direction):
	global Hposition
	global Tposition
	global visited
	global knotPositions
	knotToMove = knotPositions[knotIndex]
	parentKnot = knotPositions[knotIndex-1]
	if (direction == RIGHT):
		knotToMove[0] += 1
		knotToMove[1] = parentKnot[1]
	elif (direction == LEFT):
		knotToMove[0] -= 1
		knotToMove[1] = parentKnot[1]
	elif (direction == UP):
		knotToMove[1] += 1
		knotToMove[0] = parentKnot[0]
	elif (direction == DOWN):
		knotToMove[1] -= 1
		knotToMove[0] = parentKnot[0]
	elif (direction == TOPRIGHT):
		knotToMove[0] += 1
		knotToMove[1] += 1
	elif (direction == TOPLEFT):
		knotToMove[0] -= 1
		knotToMove[1] += 1
	elif (direction == BOTTOMRIGHT):
		knotToMove[0] += 1
		knotToMove[1] -= 1
	elif (direction == BOTTOMLEFT):
		knotToMove[0] -= 1
		knotToMove[1] -= 1
	locationVisited = False
	if (knotIndex == 9):
		for location in visited:
			if (Tposition == location):
				locationVisited = True
				break
		if (locationVisited == False):
			newLocation = [Tposition[0], Tposition[1]]
			visited.append(newLocation)


for command in commands:
	if (command == ""):
		continue
	direction = command.split()[0]
	times = int(command.split()[1])
	for i in range(times):
		if (direction == RIGHT):
			Hposition[0] += 1
		if (direction == LEFT):
			Hposition[0] -= 1
		if (direction == UP):
			Hposition[1] += 1
		if (direction == DOWN):
			Hposition[1] -= 1
		for i in range(len(knotPositions)):
			if (i != 0):	
				if (not checkIfTouchingParent(i)):
					newDirection = getDirectionToMove(i)
					moveT(i, newDirection)

highestX = 0
lowestX = 0
highestY = 0
lowestY = 0
for location in visited:
	if (location[0] > highestX):
		highestX = location[0]
	if (location[0] < lowestX):
		lowestX = location[0]
	if (location[1] > highestY):
		highestY = location[1]
	if (location[1] < lowestY):
		lowestY = location[1]

y = highestY
while y >= lowestY:
	x = lowestX
	while x <= highestX:
		location = [x, y]
		match = False
		for visitedPlace in visited:
			if (location == visitedPlace):
				match = True
				break
		if (location == [0, 0]):
			print("s", end="")
		elif (match):
			print("#", end="")
		else:
			print(".", end="")
		x += 1
	y -= 1
	print()

print(len(visited))