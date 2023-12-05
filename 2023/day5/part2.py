lines = open("input1.txt").readlines()
seeds = lines[0].split()
seeds.pop(0)

iterations = 100000000

for i in range(iterations):
	location = iteration
	source = location
	mappedNumber = 0
	destinationStart = 0
	sourceStart = 0
	rangeLength = 0
	readingNumbers = False

	done = False
	j = len(lines) - 1
	while not done:
		line = lines[j]
		if len(line.split()) > 0:
			if readingNumbers:
				numbers = line.split()
				destinationStart = int(numbers[0])
				sourceStart = int(numbers[1])
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

	locations.append(source)
	j -= 1
	if j < 0:
		done = True
locations.sort()
print(locations[0])

			