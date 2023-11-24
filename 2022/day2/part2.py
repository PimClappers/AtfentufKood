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
	if oponents[i] == ROCKo:
		if outcomes[i] == OUTCOMEw:
			totalpoints += PAPERp + WIN
		if outcomes[i] == OUTCOMEd:
			totalpoints += ROCKp + DRAW
		if outcomes[i] == OUTCOMEl:
			totalpoints += SCISSORSp + LOSE

	if oponents[i] == PAPERo:
		if outcomes[i] == OUTCOMEw:
			totalpoints += SCISSORSp + WIN
		if outcomes[i] == OUTCOMEd:
			totalpoints += PAPERp + DRAW
		if outcomes[i] == OUTCOMEl:
			totalpoints += ROCKp + LOSE

	if oponents[i] == SCISSORSo:
		if outcomes[i] == OUTCOMEw:
			totalpoints += ROCKp + WIN
		if outcomes[i] == OUTCOMEd:
			totalpoints += SCISSORSp + DRAW
		if outcomes[i] == OUTCOMEl:
			totalpoints += PAPERp + LOSE
print("Total: " + str(totalpoints))