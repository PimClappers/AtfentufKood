def findTopIndex(stack):
	if (stack[0] == "o"):
		return -1
	if (stack[len(stack)-1] != "o"):
		return len(stack)-1
	for i in range(len(stack)):
		if (stack[i] == "o"):
			return i-1

lines = open("input.txt").readlines();
stacks = [[]]
commands = [[]]
firstLine = True
for line in lines:
	if (line[0] != "m"):
		currentStack = 0
		for i in range(len(line)):
			if (i % 4 == 1):			
				if (firstLine):
					crate = ["o"]
					stacks.append(crate)
					if (line[i] != " "):
						stacks[currentStack][0] = line[i]
				elif (line[i] != " "):
					stacks[currentStack].insert(0, line[i])
				else:
					stacks[currentStack].insert(0, "o")
				currentStack += 1
	else:
		segments = line[0:len(line)-1].split()
		segments.pop(0)
		segments.pop(1)
		segments.pop(2)
		for i in range(len(segments)):
			segments[i] = int(segments[i])

		commands.append(segments)
	firstLine = False

stacks.pop(len(stacks)-1)
commands.pop(0)

for command in commands:
	times = command[0]
	fromStack = stacks[command[1] - 1]
	toStack = stacks[command[2] - 1]	
	for i in range(times):
		if (findTopIndex(toStack) == len(toStack)-1):
			toStack.append("o")
		toStack[findTopIndex(toStack)+1] = fromStack[findTopIndex(fromStack)]
		fromStack[findTopIndex(fromStack)] = "o"

for stack in stacks:
	topIndex = findTopIndex(stack)
	if (topIndex != -1):
		print(stack[topIndex], end="")
print()

