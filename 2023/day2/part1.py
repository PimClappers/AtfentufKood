RED = 12
GREEN = 13
BLUE = 14

def find_all(input, searchterm):
	done = False
	searchFrom = 0
	foundIndexes = []
	while not done:
		index = input.find(searchterm, searchFrom)
		if (index >= 0):
			foundIndexes.append(index)
			searchFrom = index + 1
		else:
			done = True
	return foundIndexes

def findNumbersOfColor(game, color):
    numbers = []
    redLocations = find_all(game, color)
    for location in redLocations:
        setOfColor = ""
        setOfColor += game[location - 3]
        setOfColor += game[location - 2]
        numbers.append(int(setOfColor))
    return numbers

def checkIfColorIsValid(numbers, color):
    valid = True
    for number in numbers:
        if (number > color):
            valid = False
            break
    return valid

total = 0

games = open("input1.txt").readlines()

for i in range(len(games)):
    game = games[i]

    valid = True

    numbersOfRed = findNumbersOfColor(game, "red")
    if not checkIfColorIsValid(numbersOfRed, RED):
        valid = False

    numbersOfRed = findNumbersOfColor(game, "green")
    if not checkIfColorIsValid(numbersOfRed, GREEN):
        valid = False
    
    numbersOfRed = findNumbersOfColor(game, "blue")
    if not checkIfColorIsValid(numbersOfRed, BLUE):
        valid = False
    
    if valid:
        total += i + 1

print("Total: " + str(total))
