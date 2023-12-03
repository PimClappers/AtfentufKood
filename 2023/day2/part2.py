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

total = 0

games = open("input1.txt").readlines()

for i in range(len(games)):
    game = games[i]

    numbersOfRed = findNumbersOfColor(game, "red")
    numbersOfRed.sort(reverse=True)
    if (len(numbersOfRed) > 0):
        highestRed = numbersOfRed[0]

    numbersOfGreen = findNumbersOfColor(game, "gree")
    numbersOfGreen.sort(reverse=True)
    if (len(numbersOfGreen) > 0):
        highestGreen = numbersOfGreen[0]
    
    numbersOfBlue = findNumbersOfColor(game, "blue")
    numbersOfBlue.sort(reverse=True)
    if (len(numbersOfBlue) > 0):
        highestBlue = numbersOfBlue[0]

    total += highestRed * highestGreen * highestBlue

print("Total: " + str(total))
