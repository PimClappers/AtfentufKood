lines = open("input1.txt").readlines()

Times = lines[0].split()
Times.pop(0)
Distances = lines[1].split()
Distances.pop(0)

total = 1

for i in range(len(Times)):
	time = int(Times[i])
	record = int(Distances[i])
	nWins = 0
	for hold in range(time):
		distance = (time-hold)*hold
		if distance > record:
			nWins += 1
	total = total * nWins

print("Result: " + str(total))