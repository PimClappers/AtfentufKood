lines = open("input1.txt").read().splitlines(0)

trees = []

def allZero(sequence):
    success = True
    for number in sequence:
        if not number == 0:
            success = False
    return success

def extractDifferences(sequence):
    newSequence = []
    currentNumberIndex = 0
    done = False
    while not done:
        if currentNumberIndex == len(sequence) - 1:
            done = True
            break
        currentNumber = sequence[currentNumberIndex]
        nextNumber = sequence[currentNumberIndex + 1]
        difference = nextNumber - currentNumber
        newSequence.append(difference)
        currentNumberIndex += 1
    return newSequence

total = 0

for line in lines:
    tree = []
    ogSequence = line.split()
    for i in range(len(ogSequence)):
        number = ogSequence[i]
        ogSequence[i] = int(number)
    tree.append(ogSequence)

    done = False
    level = 0 #0 is top
    while not done:
        currentSequence = tree[level]
        newSequence = extractDifferences(currentSequence)
        if allZero(newSequence):
            newSequence.append(0)
            done = True
        tree.append(newSequence)
        level += 1

    done = False
    while not done:
        currentSequence = tree[level]
        numberToAdd = currentSequence[len(currentSequence) - 1]
        parentSequence = tree[level - 1]
        parentLastNumber = parentSequence[len(parentSequence) - 1]
        parentSequence.append(parentLastNumber + numberToAdd)

        level -= 1

        if level == 0:
            total += parentSequence[len(parentSequence) - 1]
            done = True
            break
    trees.append(tree)

print("Total: " + str(total))
