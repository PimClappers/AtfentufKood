xmas = ['M', 'A', 'S']

file = open('input.txt')
lines = file.readlines()
columns = []

totalMatches = 0

for x in range(len(lines[0])):
	columns.append([])

for x in range(len(lines)):
	line = lines[x]
	for y in range(len(line)):
		character = line[y]
		columns[y].append(character)

for y in range(len(lines)):
	line = lines[y]
	for x in range(len(line)):
		currentCharacter = line[x]

		if (currentCharacter == "A"):
			if (x > 0 and x+1 < len(columns) and y > 0 and y+1 < len(lines)):
		 		if (lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S"):
		 			if (lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S") or (lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M"):
		 				totalMatches += 1

		 		if (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M"):
		 			if (lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S") or (lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M"):
		 				totalMatches += 1

print(totalMatches)