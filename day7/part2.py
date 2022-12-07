tree = [["/", 0, 0]]
currentDir = 0
lines = open("input.txt").read().split("\n")
levelsDeep = 0

def calcTotalSize(directory):
	fileSum = 0
	for i in range(len(directory)):
		if (i > 2):
			fileSum += int(directory[i])
	return fileSum

def moveTo(directory):
	global currentDir
	global tree
	global levelsDeep
	for i in range(len(tree)):
		if (directory == ".."):
			fileSum = calcTotalSize(tree[currentDir])
			tree[currentDir][2] += fileSum
			parentDir = tree[currentDir][1]
			tree[parentDir][2] += tree[currentDir][2]
			currentDir = tree[currentDir][1]
			levelsDeep -= 1
			break
		if (directory == "/"):
			currentDir = 0
			break
		if (tree[i][0] == directory+str(currentDir)):
			currentDir = i;
			levelsDeep += 1
			break

for line in lines:
	if (line[0] == "$"):
		command = line.split()[1]
		if (command == "cd"):
			moveTo(line.split()[2])
	elif (line.split()[0] == "dir"):
		tree.append([line.split()[1]+str(currentDir), currentDir, 0])
	else:
		tree[currentDir].append(line.split()[0])

for i in range(levelsDeep):
	moveTo("..")

tree[0][2] += calcTotalSize(tree[0])

freeSpace = 70000000 - tree[0][2]
spaceToDelete = 30000000 - freeSpace

smallestFittingFolder = tree[0]
for folder in tree:
	if (folder[2] >= spaceToDelete):
		if (folder[2] < smallestFittingFolder[2]):
			smallestFittingFolder = folder

print(smallestFittingFolder[2])