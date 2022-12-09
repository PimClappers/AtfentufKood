commands = open("input.txt").read().split("\n")

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

Hposition = [0,0]
Tposition = [0,0]
visited = [[0,0]]

def checkIfTouching():
	global Hposition
	global Tposition
	if (Hposition == Tposition):
		return True
	if (Hposition[0] - Tposition[0] <= 1 and Hposition[0] - Tposition[0] >= -1):
		if (Hposition[1] - Tposition[1] <= 1 and Hposition[1] - Tposition[1] >= -1):
			return True
	if (Hposition[1] - Tposition[1] <= 1 and Hposition[1] - Tposition[1] >= -1):
		if (Hposition[0] - Tposition[0] <= 1 and Hposition[0] - Tposition[0] >= -1):
			return True
	return False

def moveT(direction):
	global Hposition
	global Tposition
	global visited
	if (direction == RIGHT):
		Tposition[0] += 1
		Tposition[1] = Hposition[1]
	elif (direction == LEFT):
		Tposition[0] -= 1
		Tposition[1] = Hposition[1]
	elif (direction == UP):
		Tposition[1] += 1
		Tposition[0] = Hposition[0]
	elif (direction == DOWN):
		Tposition[1] -= 1
		Tposition[0] = Hposition[0]
	locationVisited = False
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
		if (not checkIfTouching()):
			moveT(direction)

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
		if (match):
			print("#", end="")
		else:
			print(".", end="")
		x += 1
	y -= 1
	print()

print(Hposition)
print(Tposition)
print(len(visited))