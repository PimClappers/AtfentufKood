lines = open("example2.txt").read().splitlines()

possibleCharacters = ["|", "7", "F", "-", "J", "L", "S"]

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def getNextPosition(currentPosition, direction):
    nextPosition = currentPosition[:]
    if direction == NORTH:
        nextPosition[1] -= 1
    elif direction == EAST:
        nextPosition[0] += 1
    elif direction == SOUTH:
        nextPosition[1] += 1
    elif direction == WEST:
        nextPosition[0] -= 1
    return nextPosition

currentPosition = [0,0] # X, Y
direction = EAST # CHECK INPUT FILE FOR STARTING DIRECTION!!
visitedPositions = [] # X, Y

for i in range(len(lines) - 1):
    line = lines[i]
    SinDex = line.find("S")
    if SinDex > -1:
        currentPosition = [SinDex, i]

done = False
while not done:
    nextPosition = getNextPosition(currentPosition, direction)

    for character in possibleCharacters:
        if lines[nextPosition[1]][nextPosition[0]] == character:
            if character == "7":
                if direction == NORTH:
                    direction = WEST
                else:
                    direction = SOUTH

            elif character == "F":
                if direction == NORTH:
                    direction = EAST
                else:
                    direction = SOUTH
            
            elif character == "J":
                if direction == SOUTH:
                    direction = WEST
                else:
                    direction = NORTH
            
            elif character == "L":
                if direction == SOUTH:
                    direction = EAST
                else:
                    direction = NORTH
            
            elif character == "S":
                done = True
                break

    currentPosition = nextPosition
    visitedPositions.append(currentPosition)

nEnclosedtiles = 0
inLoop = False

linesCopy = []
loopCharsInRow = 0

for y in range(len(lines)):
    line = lines[y]
    newLine = list(line)
    loopCharsInRow = 0
    inLoop = False
    for x in range(len(line)):
        position = [x, y]
        isPipePiece = False
        character = line[x]
        for visitedPosition in visitedPositions:
            if position[0] == visitedPosition[0] and position[1] == visitedPosition[1]:
                isPipePiece = True
                break
        if isPipePiece:
            if character == "-":
                loopCharsInRow += 1
            if not inLoop:
                inLoop = True
            else:
                if not loopCharsInRow > 0:
                    inLoop = False
        else:
            newLine[x] = "0"
            if loopCharsInRow > 0:
                inLoop = False
            if inLoop:
                nEnclosedtiles += 1
                newLine[x] = "I"
    linesCopy.append(newLine)
    inLoop = False

for line in linesCopy:
    text = ""
    for character in line:
        text += character
    print(text)

print(nEnclosedtiles)
                