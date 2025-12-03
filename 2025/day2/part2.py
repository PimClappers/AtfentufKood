import re
import math

lines = open("input.txt").read().split(',')

total = 0

for line in lines:
	startingNumber = int(line.split('-')[0])
	endNumber = int(line.split('-')[1])
	currentNumber = startingNumber
	while(currentNumber != (endNumber+1)):
		numberString = str(currentNumber)
		valid = True
		for x in range(len(numberString)):
			subString = numberString[x:]
			numberOfMatches = len(re.findall(subString, numberString))
			if (numberOfMatches > 1):
				if ((len(subString) * numberOfMatches) == len(numberString)):
					total = total + currentNumber
					break
		currentNumber += 1
		print(str(currentNumber) + "/" + str(endNumber))

print(total)