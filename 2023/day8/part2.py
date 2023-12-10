import math

lines = open("input1.txt").readlines()

LEFT = "L"
RIGHT = "R"

instructions = []

for instruction in lines[0]:
	instructions.append(instruction)
instructions.pop(len(instructions) - 1)

pairs = [] #name, left, right
currentNames = []
goalNames = [] #name, leastNSteps

for line in lines:
	if line.find("=") > 0:
		lineChunks = line.split()
		pairName = lineChunks[0]
		left = lineChunks[2][1:4]
		right = lineChunks[3][0:3]
		pairs.append([pairName, left, right])
		if pairName[2] == "A":
			currentNames.append(pairName)
		if pairName[2] == "Z":
			goalNames.append([pairName, -1])

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

		for currentName in currentNames:
			for goalName in goalNames:
				if currentName == goalName[0] and goalName[1] == -1:
					goalName[1] = steps
		
		success = True
		for goalName in goalNames:
			if goalName[1] == -1:
				success = False
		
		if success:
			done = True
			break

result = math.lcm(goalNames[0][1],goalNames[1][1],goalNames[2][1],goalNames[3][1],goalNames[4][1],goalNames[5][1],)
print("Result: " + str(result))

