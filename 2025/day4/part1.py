import copy

lines = open("input.txt").read().splitlines()

data = []
dataCopy = []

def replaceWithX(coords):
	x = coords[0]
	y = coords[1]
	dataCopy[y][x] = 'x'

def getIsRoll(x, y, width ,height):
	if (x > -1 and x < width and y > -1 and y < height):
		if (data[y][x] == '@'):
			return True
		else:
			return False
	else:
		return False

def checkSurroundingCoords(coords, widht, height):
	x = coords[0]
	y = coords[1]
	numberOfRolls = 0
	if (getIsRoll(x-1, y-1, width, height)):
		numberOfRolls += 1
	if (getIsRoll(x, y-1, width, height)):
		numberOfRolls += 1
	if (getIsRoll(x+1, y-1, width, height)):
		numberOfRolls += 1
	if (getIsRoll(x-1, y, width, height)):
		numberOfRolls += 1
	if (getIsRoll(x+1, y, width, height)):
		numberOfRolls += 1
	if (getIsRoll(x-1, y+1, width, height)):
		numberOfRolls += 1
	if (getIsRoll(x, y+1, width, height)):
		numberOfRolls += 1
	if (getIsRoll(x+1, y+1, width, height)):
		numberOfRolls += 1

	if numberOfRolls < 4:
		return True;
	else:
		return False;


def nextCoords(coords, width, height):
	newCoords = [0, 0]
	x = coords[0]
	y = coords[1]
	if (x < width-1):
		newCoords = [x + 1, y]
	elif (y < height - 1):
		newCoords = [0, y + 1]
	else:
		newCoords = [-1, -1]
	return newCoords

for r in range(len(lines)):
	row = lines[r]
	rowData = []
	for x in range(len(row)):
		rowData.append(row[x])
	data.append(rowData)

dataCopy = copy.deepcopy(data)

width = len(data[0])
height = len(data)

currentCoords = [0,0]

total = 0

while (currentCoords != [-1, -1]):
	if (getIsRoll(currentCoords[0], currentCoords[1], width, height)):
		if (checkSurroundingCoords(currentCoords, width, height)):
			replaceWithX(currentCoords)
			total += 1
	currentCoords = nextCoords(currentCoords, width, height)

print(total)
