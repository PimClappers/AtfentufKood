availableDigits = [["zero",0], ["one",1], ["two",2], ["three",3], ["four",4], ["five",5], ["six",6], ["seven",7], ["eight",8], ["nine",9]]

lines = open("input2.txt").readlines();

total = 0

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


for line in lines:
	digitsIndexesInLine = []
	firstAndLastIndex = []
	callibrationValue = ""
	for availableDigitPair in availableDigits:
		foundDigitIndexes = find_all(line, availableDigitPair[0])
		for foundDigitIndex in foundDigitIndexes:
			if (foundDigitIndex >= 0):
				digitsIndexesInLine.append(foundDigitIndex)		
		foundDigitIndexes = find_all(line, str(availableDigitPair[1]))
		for foundDigitIndex in foundDigitIndexes:
			if (foundDigitIndex >= 0):
				digitsIndexesInLine.append(foundDigitIndex)	
	digitsIndexesInLine.sort()
	firstAndLastIndex.append(digitsIndexesInLine[0])
	firstAndLastIndex.append(digitsIndexesInLine[len(digitsIndexesInLine) - 1])


	for i in range(len(firstAndLastIndex)):
		lengthToSearch = 0
		found = False
		while (not found):
			subString = line[firstAndLastIndex[i]: lengthToSearch]
			for availableDigitPair in availableDigits:
				foundDigitIndexes = find_all(subString, availableDigitPair[0])
				for foundDigitIndex in foundDigitIndexes:
					if (foundDigitIndex >= 0):
						callibrationValue += str(availableDigitPair[1])
						found = True
						break
				foundDigitIndexes = find_all(subString, str(availableDigitPair[1]))
				for foundDigitIndex in foundDigitIndexes:
					if (foundDigitIndex >= 0):
						callibrationValue += str(availableDigitPair[1])
						found = True
						break
			lengthToSearch += 1

		lengthToSearch = 0
		found = False
	print(callibrationValue)
	total += int(callibrationValue)

print("Total: " + str(total))

