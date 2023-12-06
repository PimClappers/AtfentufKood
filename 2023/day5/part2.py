lines = open("input2.txt").readlines()
seeds = lines[0].split()
seeds.pop(0)

def checkIfInSeeds(number):
	success = False
	for i in range(int(len(seeds)/2)):
		seedStartNumber = int(seeds[i*2])
		seedRangeNumber = int(seeds[i*2+1])
		if number >= seedStartNumber and number <= seedStartNumber + seedRangeNumber: # check if >+ is correct
			success = True
	return success


location = 60560000
source = location
done = False

while not done:
	mappedNumber = 0
	destinationStart = 0
	sourceStart = 0
	rangeLength = 0
	readingNumbers = False
	readingLines = True
	i = len(lines) - 1
	while readingLines:
		line = lines[i]
		if len(line.split()) > 0:
			if readingNumbers:
				numbers = line.split()
				destinationStart = int(numbers[1])
				sourceStart = int(numbers[0])
				rangeLength = int(numbers[2])

				if (mappedNumber == 0) and (source >= sourceStart) and (source <= sourceStart + rangeLength):
					mappedNumber = destinationStart + (source - sourceStart)
					source = mappedNumber

			containsDash = line.find("-")
			if containsDash > 0:
				lineChunks = line.split("-")
				sourceKey = lineChunks[0]
				readingNumbers = True

		else:
			if readingNumbers:
				readingNumbers = False
				if mappedNumber == 0:
					mappedNumber = source
				source = mappedNumber
				mappedNumber = 0
		i -= 1
		if i <= 1:
			readingLines = False

	if checkIfInSeeds(source):
		done = True
	else:
		location += 1
		source = location

print("Result: " + str(location))