line = open("input.txt").read()

print(line)
lastFour = []

startIndex = 0
for n in range(len(line)):
	letter = line[n]
	lastFour.append(letter)
	if (len(lastFour) > 4):
		lastFour.pop(0)
		dupe = False		
		for i in range(len(lastFour)):
			for j in range(len(lastFour)):
				if (i != j):
					if (lastFour[i] == lastFour[j]):
						dupe = True
		if (dupe == False):
			startIndex = n + 1
			break

print(startIndex)