file = open('input1.txt')
lines = file.readlines()
list1 = []
list2 = []
for line in lines:
	splittedLine = line.split()
	list1.append(int(splittedLine[0]))
	list2.append(int(splittedLine[1]))

list1.sort()
list2.sort()

totalDistance = 0

i = 0
for i in range(len(list1)):
	value1 = list1[i]
	value2 = list2[i]
	highest = 0
	lowest = 0
	if (value1 >= value2):
		highest = value1
		lowest = value2
	else:
		highest = value2
		lowest = value1
	distance = highest - lowest
	totalDistance += distance

print(totalDistance)