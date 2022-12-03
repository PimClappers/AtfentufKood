priorityList = open("alphabet.txt").read()
lines = open("input.txt").readlines()
totalPriority = 0
for line in lines:
    lastIndex = len(line) - 1
    compartement1 = line[0:int(lastIndex/2)]
    compartement2 = line[int(lastIndex/2):lastIndex]
    for i in range(len(compartement1)):
        if (compartement2.find(compartement1[i]) != -1):
            totalPriority += priorityList.find(compartement1[i]) + 1
            break
print(totalPriority)