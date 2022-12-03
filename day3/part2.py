priorityList = open("alphabet.txt").read()
lines = open("input.txt").readlines()
totalPriority = 0
for i in range(len(lines)):
    if (i % 3):
        continue
    line = lines[i]
    for j in range(len(line)):
        if ((lines[i+1].find(line[j]) != -1) and (lines[i+2].find(line[j]) != -1)):
            totalPriority += priorityList.find(line[j]) + 1
            break
print(totalPriority)