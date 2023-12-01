availableDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lines = open("input1.txt").readlines();

total = 0

for line in lines:
	digitsInLine = ""
	calibrationValue = ""
	for character in line:
		for availableDigit in availableDigits:
			if (character == str(availableDigit)):
				digitsInLine += character
	calibrationValue += digitsInLine[0]
	calibrationValue += digitsInLine[len(digitsInLine) - 1]
	total += int(calibrationValue)
print("Total: " + str(total))