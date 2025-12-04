import numpy as np

lines = open("example.txt").read().splitlines()

total = 0

for bank in lines:
	array = []
	jolts = 0
	highestWasLast = False
	for battery in bank:
		array.append(str(battery))
	arraySorted = array[:]
	arraySorted.sort(reverse=True)
	highest = arraySorted[0]
	highestIndex = bank.find(highest)
	subArray = array[highestIndex+1:]
	if (len(subArray) == 0):
		highestWasLast = True
		subArray = array[:highestIndex]
	subArraySorted = subArray[:]
	subArraySorted.sort(reverse=True)
	highest2 = subArraySorted[0]
	if (not highestWasLast):
		jolts = str(highest) + str(highest2)
	else:
		jolts = str(highest2) + str(highest)
	total = total + int(jolts)

print(total)
