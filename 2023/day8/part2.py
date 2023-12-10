lines = open("input1.txt").readlines()

LEFT = "L"
RIGHT = "R"

instructions = []

for instruction in lines[0]:
	instructions.append(instruction)
instructions.pop(len(instructions) - 1)

pairs = [] #name, left, right
currentNames = []

for line in lines:
	if line.find("=") > 0:
		lineChunks = line.split()
		pairName = lineChunks[0]
		left = lineChunks[2][1:4]
		right = lineChunks[3][0:3]
		pairs.append([pairName, left, right])
		if pairName[2] == "A":
			currentNames.append(pairName)

steps = 0

done = False
while not done:
	for instruction in instructions:
		newCurrentNames = []
		for currentName in currentNames:
			for pair in pairs:
				pairName = pair[0]
				if pairName == currentName:
					if instruction == LEFT:
						newCurrentNames.append(pair[1])
					elif instruction == RIGHT:
						newCurrentNames.append(pair[2])
		steps += 1
		currentNames = newCurrentNames
		allEndWithZ = True
		for currentName in currentNames:
			if not currentName[2] == "Z":
				allEndWithZ = False
		if allEndWithZ:
			done = True
			break
		if steps == 10000:
			print(steps)

print(steps)

