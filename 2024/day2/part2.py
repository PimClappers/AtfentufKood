file = open('input.txt')
lines = file.readlines()

records = []

totalSafeRecords = 0

for line in lines:
	splittedLine = line.split()
	record = []
	safe = False
	decreasing = False
	previousLevel = 0

	if (int(splittedLine[0]) > int(splittedLine[1])):
		decreasing = True
		previousLevel = int(splittedLine[0]) + 1
	else:
		decreasing = False
		previousLevel = int(splittedLine[0]) - 1

	for levelString in splittedLine:
		levelInt = int(levelString)
		record.append(levelInt)

	for level in record:
		if (not decreasing):
			if ((level > previousLevel) and (level - previousLevel < 4)):
				safe = True
			else:
				safe = False
				break
		else:
			if ((level < previousLevel) and (previousLevel - level < 4)):
				safe = True
			else:
				safe = False
				break

		previousLevel = level

	if (not safe):
		numberOfLevels = len(record)
		for i in range(numberOfLevels):
			recordToTry = record[:]
			recordToTry.pop(i)

			if (recordToTry[0] > recordToTry[1]):
				decreasing = True
				previousLevel = recordToTry[0] + 1
			else:
				decreasing = False
				previousLevel = recordToTry[0] - 1

			for level in recordToTry:
				if (not decreasing):
					if ((level > previousLevel) and (level - previousLevel < 4)):
						safe = True
					else:
						safe = False
						break
				else:
					if ((level < previousLevel) and (previousLevel - level < 4)):
						safe = True
					else:
						safe = False
						break

				previousLevel = level
			if (safe):
				break

	if (safe):
		totalSafeRecords += 1

	records.append(record)
		
print(totalSafeRecords)