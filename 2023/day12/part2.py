lines = open("example1.txt").read().splitlines()

rows = []

def extractNGroups(sequence):
	sequenceString = ""
	for character in sequence:
		sequenceString += character
	sequenceChunks = sequenceString.split(".")
	nGroups = 0
	for chunk in sequenceChunks:
		if len(chunk) > 0:
			nGroups += 1
	return nGroups

for line in lines:
	lineChunks = line.split()
	sequence = lineChunks[0]
	groups = lineChunks[1].split(",")
	row = [sequence, groups]
	rows.append(row)

total = 0
rowNumber = 0

for row in rows:
	print(rowNumber)
	rowNumber += 1
	ogSequence = row[0][:]
	ogGroups = row[1][:]
	for i in range(4):
		row[0] += "?"
		row[0] += ogSequence

		for number in ogGroups:
			row[1].append(number)
	print(row)

	sequence = row[0][:]
	unknownAtIndex = []
	for i in range(len(sequence)):
		if sequence[i] == "?":
			unknownAtIndex.append(i)

	maxValue = pow(2, len(unknownAtIndex)) - 1
	# print(maxValue)

	value = -1
	while value < maxValue:
		value += 1
		print(str(value) + " / " + str(maxValue))
		byte = bin(value)
		byteString = str(byte)
		byteString = byteString[2:len(byteString)]
		delta = len(unknownAtIndex) - len(byteString)
		stringToAdd = ""
		for i in range(delta):
			stringToAdd += "0"
		byteString = stringToAdd + byteString
		# print(byteString)
		sequence = ""
		for i in range(len(row[0])):
			isUnknown = False
			for j in range(len(unknownAtIndex)):
				if unknownAtIndex[j] == i:
					isUnknown = True
					if byteString[j] == "0":
						sequence += "."
					else:
						sequence += "#"
					break
			if not isUnknown:
				sequence += row[0][i]
		# print(sequence)

		groups = sequence.split(".")
		newGroups = []
		for group in groups:
			if len(group) > 0:
				newGroups.append(group)
		groups = newGroups

		success = False
		if len(groups) == len(row[1]):
			correctGroups = True
			for i in range(len(groups)):
				if not len(groups[i]) == int(row[1][i]):
					correctGroups = False
					break
			if correctGroups:
				# print("hit")
				total += 1

print("Result: " + str(total))