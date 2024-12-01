file = open('input1.txt')
lines = file.readlines()
list1 = []
list2 = []
for line in lines:
	splittedLine = line.split()
	list1.append(int(splittedLine[0]))
	list2.append(int(splittedLine[1]))

totalScore = 0

for i in range(len(list1)):
	value1 = list1[i]
	occurances = 0
	for j in range(len(list2)):	
		value2 = list2[j]
		if (value1 == value2):
			occurances += 1
	score = value1 * occurances
	totalScore += score

print(totalScore)