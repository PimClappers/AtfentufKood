import math

lines = open("input1.txt").readlines()

times = lines[0].split()
times.pop(0)

time = ""
distance = ""

for t in times:
	time += t
time = int(time)

distances = lines[1].split()
distances.pop(0)

for d in distances:
	distance += d
distance = int(distance)

minDistance = distance + 1

# minHold = minDistance / (time-2)
# minHold = math.ceil(minHold)

done = False
winning = True
wonOnce = False
nWins = 0
hold = 0

traveled = (time-hold)*hold

while not done:
    traveled = (time-hold)*hold
    if traveled >= minDistance:
        wonOnce = True
        nWins += 1
    if wonOnce and traveled < minDistance:
        done = True
    hold += 1

print("Result: " + str(nWins))