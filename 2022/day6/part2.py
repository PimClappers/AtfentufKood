line = open("input.txt").read()

print(line)
lastFourteen = []

startIndex = 0
for n in range(len(line)):
	letter = line[n]
	lastFourteen.append(letter)
	if (len(lastFourteen) > 14):
		lastFourteen.pop(0)
		dupe = False		
		for i in range(len(lastFourteen)):
			for j in range(len(lastFourteen)):
				if (i != j):
					if (lastFourteen[i] == lastFourteen[j]):
						dupe = True
		if (dupe == False):
			startIndex = n + 1
			break

print(startIndex)