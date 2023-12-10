lines = open("input1.txt").readlines()

LEFT = "L"
RIGHT = "R"

instructions = []

for instruction in lines[0]:
	instructions.append(instruction)
instructions.pop(len(instructions) - 1)

pairs = [] #name, left, right

for line in lines:
	if line.find("=") > 0:
		lineChunks = line.split()
		pairName = lineChunks[0]
		left = lineChunks[2][1:4]
		right = lineChunks[3][0:3]
		pairs.append([pairName, left, right])

currentName = "AAA"
goalName = "ZZZ"
steps = 0


done = False
while not done:
	for instruction in instructions:
		for pair in pairs:
			pairName = pair[0]
			if pairName == currentName:
				if instruction == LEFT:
					currentName = pair[1]
				elif instruction == RIGHT:
					currentName = pair[2]
				break
		steps += 1
		if currentName == goalName:
			done = True

print(steps)

