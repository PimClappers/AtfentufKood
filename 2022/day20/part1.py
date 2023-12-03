class number:
    def __init__(self, value, ogIndex):
        self.value = value
        self.ogIndex = ogIndex
        self.currentIndex = ogIndex
    
    value = 0
    ogIndex = 0
    currentIndex = 0

numberList = open("input.txt").read().split()

numbers = []
for i in range(len(numberList)):
    numbers.append(number(int(numberList[i]), i))

itemNumber = 0
for n in numbers:
    itemNumber += 1
    print(str(round(itemNumber / len(numberList) * 100, 2)) + "%")
    numberValue = n.value
    numberValuePositive = numberValue
    if numberValuePositive < 0:
        numberValuePositive = 0 - numberValuePositive
    for i in range(numberValuePositive):
        # print(i)
        newIndex = 0
        if (numberValue > 0):
            newIndex = n.currentIndex + 1
        elif (numberValue < 0):
            newIndex = n.currentIndex - 1

        if newIndex > len(numbers) - 1:        
            newIndex = newIndex - len(numbers)
        if newIndex < 0:
            newIndex = len(numbers) + newIndex        

        for numberToMove in numbers:
            if numberToMove.currentIndex == newIndex:
                numberToMove.currentIndex = n.currentIndex
        n.currentIndex = newIndex

newList = []
for n in numbers:
    newList.append(0)

for n in numbers:
    newList[n.currentIndex] = n.value

newList.append(newList[0])
newList.pop(0)

startIndex = 0
for i in range(len(newList)):
    if (newList[i] == 0):
        startIndex = i

moduloIndex = 1000 % (len(newList))
moduloIndex += startIndex
thousandValue = newList[moduloIndex % (len(newList))]

moduloIndex = 2000 % (len(newList))
moduloIndex += startIndex
twoThousandValue = newList[moduloIndex % (len(newList))]

moduloIndex = 3000 % (len(newList))
moduloIndex += startIndex
threeThousandValue = newList[moduloIndex % (len(newList))]

print(thousandValue + twoThousandValue + threeThousandValue)