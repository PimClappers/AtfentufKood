import re

file = open('input.txt')
inputText = file.read()

total = 0
doMultiply = True
done = False

while not done:
	multiplyNextLoop = True
	startIndex = 0
	endIndex = 0
	nextDont = re.search(r"don't\(\)", inputText)
	if (nextDont):
		nextDontIndex = nextDont.start()
	nextDo = re.search(r"do\(\)", inputText)
	if (nextDo):
		nextDoIndex = nextDo.start()

	if (nextDoIndex and nextDontIndex):
		if nextDontIndex < nextDoIndex:
			endIndex = nextDontIndex
			multiplyNextLoop = False
		else:
			endIndex = nextDoIndex
			multiplyNextLoop = True
	elif (nextDoIndex):
		endIndex = nextDoIndex
		multiplyNextLoop = True
	elif (nextDontIndex):
		endIndex = nextDontIndex
		multiplyNextLoop = False
	else:
		endIndex = len(inputText)
		done = True

	subString = inputText[startIndex:endIndex]

	matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", subString)
	
	if (doMultiply):
		for s in matches:
			value1 = re.findall(r"\([0-9]{1,3}", s)[0]
			value1 = int(value1[1:len(value1)])
			value2 = re.findall(r"[0-9]{1,3}\)", s)[0]
			value2 = int(value2[0:len(value2)-1])

			product = value1 * value2
			total += product

	inputText = inputText[endIndex:len(inputText)]

	doMultiply = multiplyNextLoop

print(total)