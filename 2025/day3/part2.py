lines = open("input.txt").read().splitlines()

jolts = 0

for bank in lines:
	array = []
	for battery in bank:
		array.append(str(battery))

	joltArray = []
	numbersLeft = 12
	lastAddedIndex = -1
	done = False

	while not done:
		subArray = array[lastAddedIndex+1:len(array)-(numbersLeft-1)]
		indexOfHighest = 0
		for y in range(len(subArray)):
			if (int(subArray[y]) > int(subArray[indexOfHighest])):
				indexOfHighest = y
		joltArray.append(subArray[indexOfHighest])
		lastAddedIndex = lastAddedIndex + indexOfHighest + 1
		numbersLeft -= 1

		if (numbersLeft == 0):
			done = True

	joltString = ""
	for number in joltArray:
		joltString += number
	jolts = jolts + int(joltString)

print(jolts)
