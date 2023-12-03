class number:
    def __init__(self, value, ogIndex):
        self.value = value
        self.ogIndex = ogIndex
        self.currentIndex = ogIndex
    
    value = 0
    ogIndex = 0
    currentIndex = 0

numberList = open("input2.txt").read().split()

numbers = []
for i in range(len(numberList)):
    numbers.append(number(int(numberList[i]), i))

for i in range(len(numbers)):
    numberToMove = numbers[0]
    for j in range(len(numbers)):
        if (numbers[j].ogIndex == i):
            numberToMove = numbers[j]
            if numberToMove.value == 0:
                break
            newIndex = j + numberToMove.value
            for p in range(4):
                if (newIndex > len(numbers)-1):
                    newIndex = newIndex - len(numbers)
            
            numbers.insert(newIndex, numberToMove)
            if (newIndex < j):
                numbers.pop(j + 1)
            elif (newIndex > j):
                numbers.pop(j)
            
            for number in numbers:
                print(number.value)
            print()
            break

for number in numbers:
    print(number.value, end="")
    print()

# newList = []
# for n in numbers:
#     newList.append(0)

# for n in numbers:
#     newList[n.currentIndex] = n.value

# startIndex = 0
# for i in range(len(newList)):
#     if (numbers[i].value == 0):
#         startIndex = i

# moduloIndex = 1000 % (len(newList))
# moduloIndex += startIndex
# thousandValue = newList[moduloIndex % (len(newList))]

# moduloIndex = 2000 % (len(newList))
# moduloIndex += startIndex
# twoThousandValue = newList[moduloIndex % (len(newList))]

# moduloIndex = 3000 % (len(newList))
# moduloIndex += startIndex
# threeThousandValue = newList[moduloIndex % (len(newList))]

# print(thousandValue + twoThousandValue + threeThousandValue)