lines = open("input.txt").readlines();
oponents = []
outcomes = []

ROCKo = "A"
PAPERo = "B"
SCISSORSo = "C"

OUTCOMEl = "X"
OUTCOMEd = "Y"
OUTCOMEw = "Z"

ROCKp = 1
PAPERp = 2
SCISSORSp = 3

WIN = 6
DRAW = 3
LOSE = 0

for line in lines:
	oponents.append(line.split()[0])
	outcomes.append(line.split()[1])

totalpoints = 0
for i in range(len(oponents)):
	points = 0
	if oponents[i] == ROCKo:
		if outcomes[i] == OUTCOMEw:
			points += PAPERp
			points += WIN
		if outcomes[i] == OUTCOMEd:
			points += ROCKp
			points += DRAW
		if outcomes[i] == OUTCOMEl:
			points += SCISSORSp
			points += LOSE

	if oponents[i] == PAPERo:
		if outcomes[i] == OUTCOMEw:
			points += SCISSORSp
			points += WIN
		if outcomes[i] == OUTCOMEd:
			points += PAPERp
			points += DRAW
		if outcomes[i] == OUTCOMEl:
			points += ROCKp
			points += LOSE

	if oponents[i] == SCISSORSo:
		if outcomes[i] == OUTCOMEw:
			points += ROCKp
			points += WIN
		if outcomes[i] == OUTCOMEd:
			points += SCISSORSp
			points += DRAW
		if outcomes[i] == OUTCOMEl:
			points += PAPERp
			points += LOSE
	totalpoints += points
print(totalpoints)

