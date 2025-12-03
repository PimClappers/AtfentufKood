lines = open("input.txt").read().split(',')

total = 0

for line in lines:
	startingNumber = int(line.split('-')[0])
	endNumber = int(line.split('-')[1])
	currentNumber = startingNumber
	while(currentNumber != (endNumber+1)):
		numberString = str(currentNumber)
		firstPart = numberString[0:int(len(numberString)/2)]
		secondPart = numberString[int(len(numberString)/2):]
		if firstPart == secondPart:
			total = total + currentNumber
		currentNumber += 1

print(total)