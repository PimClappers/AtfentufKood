xmas = ['X', 'M', 'A', 'S']
LEFT_TO_RIGHT = 0
RIGHT_TO_LEFT = 1
TOP_LEFT_TO_BOTTOM_RIGHT = 2
TOP_RIGHT_TO_BOTTOM_LEFT = 3
BOTTOM_LEFT_TO_TOP_RIGHT = 4
BOTTOM_RIGHT_TO_TOP_LEFT = 5
TOP_TO_BOTTOM = 6
BOTTOM_TO_TOP = 7

file = open('input.txt')
lines = file.readlines()
columns = []

totalMatches = 0

for x in range(len(lines[0])):
	columns.append([])

for x in range(len(lines)):
	line = lines[x]
	for y in range(len(line)):
		character = line[y]
		columns[y].append(character)

for y in range(len(lines)):
	line = lines[y]
	for x in range(len(line)):
		currentCharacter = line[x]
		xmasIndex = 0
		coordinatesToCheck = [0,0]
		direction = LEFT_TO_RIGHT

		if (xmasIndex == 0):
			if (currentCharacter == xmas[xmasIndex]):
				xmasIndex += 1

				doneSearchingDirection = False
				directionFound = False
				attemptDirection = LEFT_TO_RIGHT
				done = False
				previousCoordinates = coordinatesToCheck

				while (not done):
					xmasIndex = 1
					doneSearchingDirection = False
					while (not doneSearchingDirection):
						directionFound = False
						if (attemptDirection == LEFT_TO_RIGHT):
							coordinatesToCheck = [x + 1, y]
							if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
								if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
									direction = LEFT_TO_RIGHT
									xmasIndex += 1
									directionFound = True
									previousCoordinates = coordinatesToCheck
						elif (attemptDirection == RIGHT_TO_LEFT):
							coordinatesToCheck = [x - 1, y]
							if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
								if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
									direction = RIGHT_TO_LEFT
									xmasIndex += 1
									directionFound = True
									previousCoordinates = coordinatesToCheck
						elif (attemptDirection == TOP_LEFT_TO_BOTTOM_RIGHT):
							coordinatesToCheck = [x + 1, y + 1]
							if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
								if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
									direction = TOP_LEFT_TO_BOTTOM_RIGHT
									xmasIndex += 1
									directionFound = True
									previousCoordinates = coordinatesToCheck
						elif (attemptDirection == TOP_RIGHT_TO_BOTTOM_LEFT):
							coordinatesToCheck = [x - 1, y + 1]
							if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
								if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
									direction = TOP_RIGHT_TO_BOTTOM_LEFT
									xmasIndex += 1
									directionFound = True
									previousCoordinates = coordinatesToCheck
						elif (attemptDirection == BOTTOM_LEFT_TO_TOP_RIGHT):
							coordinatesToCheck = [x + 1, y - 1]
							if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
								if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
									direction = BOTTOM_LEFT_TO_TOP_RIGHT
									xmasIndex += 1
									directionFound = True
									previousCoordinates = coordinatesToCheck
						elif (attemptDirection == BOTTOM_RIGHT_TO_TOP_LEFT):
							coordinatesToCheck = [x - 1, y - 1]
							if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
								if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
									direction = BOTTOM_RIGHT_TO_TOP_LEFT
									xmasIndex += 1
									directionFound = True
									previousCoordinates = coordinatesToCheck
						elif (attemptDirection == TOP_TO_BOTTOM):
							coordinatesToCheck = [x, y + 1]
							if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
								if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
									direction = TOP_TO_BOTTOM
									xmasIndex += 1
									directionFound = True
									previousCoordinates = coordinatesToCheck
						elif (attemptDirection == BOTTOM_TO_TOP):
							coordinatesToCheck = [x, y - 1]
							if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
								if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
									direction = BOTTOM_TO_TOP
									xmasIndex += 1
									directionFound = True
									previousCoordinates = coordinatesToCheck

						if (not directionFound):
							attemptDirection += 1
							xmasIndex = 1
						else:
							doneSearchingDirection = True

						if (attemptDirection > BOTTOM_TO_TOP):
							doneSearchingDirection = True
							directionFound = False
							done = True

					if (directionFound):
						doneFindingFullMatch = False
						fullMatchFound = False


						while (not doneFindingFullMatch):
							indexBeforeSearch = xmasIndex
							if (direction == LEFT_TO_RIGHT):
								coordinatesToCheck = [previousCoordinates[0] + 1, previousCoordinates[1]]
								if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
									if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
										xmasIndex += 1
										previousCoordinates = coordinatesToCheck
							elif (direction == RIGHT_TO_LEFT):
								coordinatesToCheck = [previousCoordinates[0] - 1, previousCoordinates[1]]
								if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
									if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
										xmasIndex += 1
										previousCoordinates = coordinatesToCheck
							elif (direction == TOP_LEFT_TO_BOTTOM_RIGHT):
								coordinatesToCheck = [previousCoordinates[0] + 1, previousCoordinates[1] + 1]
								if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
									if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
										xmasIndex += 1
										previousCoordinates = coordinatesToCheck
							elif (direction == TOP_RIGHT_TO_BOTTOM_LEFT):
								coordinatesToCheck = [previousCoordinates[0] - 1, previousCoordinates[1] + 1]
								if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
									if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
										xmasIndex += 1
										previousCoordinates = coordinatesToCheck
							elif (direction == BOTTOM_LEFT_TO_TOP_RIGHT):
								coordinatesToCheck = [previousCoordinates[0] + 1, previousCoordinates[1] - 1]
								if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
									if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
										xmasIndex += 1
										previousCoordinates = coordinatesToCheck
							elif (direction == BOTTOM_RIGHT_TO_TOP_LEFT):
								coordinatesToCheck = [previousCoordinates[0] - 1, previousCoordinates[1] - 1]
								if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
									if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
										xmasIndex += 1
										previousCoordinates = coordinatesToCheck
							elif (direction == TOP_TO_BOTTOM):
								coordinatesToCheck = [previousCoordinates[0], previousCoordinates[1] + 1]
								if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
									if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
										xmasIndex += 1
										previousCoordinates = coordinatesToCheck
							elif (direction == BOTTOM_TO_TOP):
								coordinatesToCheck = [previousCoordinates[0], previousCoordinates[1] - 1]
								if (coordinatesToCheck[0] < len(columns)-1 and coordinatesToCheck[1] < len(lines) and coordinatesToCheck[0] >= 0 and coordinatesToCheck[1] >= 0):
									if (columns[coordinatesToCheck[0]][coordinatesToCheck[1]] == xmas[xmasIndex]):
										xmasIndex += 1
										previousCoordinates = coordinatesToCheck

							if (xmasIndex == indexBeforeSearch):
								doneFindingFullMatch = True
								fullMatchFound = False

							if (xmasIndex == len(xmas)):
								doneFindingFullMatch = True
								fullMatchFound = True
								totalMatches += 1
								attemptDirection += 1
								doneSearchingDirection = False

						if (not fullMatchFound):
							direction = LEFT_TO_RIGHT
							attemptDirection += 1
							doneSearchingDirection = False
							done = False

print(totalMatches)