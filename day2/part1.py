lines = open("input2.txt").readlines();
oponents = []
responses = []

ROCKo = "A"
ROCKr = "X"

PAPERo = "B"
PAPERr = "Y"

SCISSORSo = "C"
SCISSORSr = "Z"

WIN = 6
DRAW = 3
LOSE = 0

for line in lines:
	oponents.append(line.split()[0])
	responses.append(line.split()[1])

totalpoints = 0
for i in range(len(oponents)):
	points = 0
	if oponents[i] == ROCKo:
		if responses[i] == ROCKr:
			points += 1
			points += DRAW
		if responses[i] == PAPERr:
			points += 2
			points += WIN
		if responses[i] == SCISSORSr:
			points += 3
			points += LOSE
	if oponents[i] == PAPERo:
		if responses[i] == ROCKr:
			points += 1
			points += LOSE
		if responses[i] == PAPERr:
			points += 2
			points += DRAW
		if responses[i] == SCISSORSr:
			points += 3
			points += WIN
	if oponents[i] == SCISSORSo:
		if responses[i] == ROCKr:
			points += 1
			points += WIN
		if responses[i] == PAPERr:
			points += 2
			points += LOSE
		if responses[i] == SCISSORSr:
			points += 3
			points += DRAW
	totalpoints += points
print(totalpoints)

