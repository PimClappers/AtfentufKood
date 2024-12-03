import re

file = open('input.txt')
inputText = file.read()

x = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", inputText)

total = 0

for s in x:
	value1 = re.findall(r"\([0-9]{1,3}", s)[0]
	value1 = int(value1[1:len(value1)])
	value2 = re.findall(r"[0-9]{1,3}\)", s)[0]
	value2 = int(value2[0:len(value2)-1])

	product = value1 * value2
	total += product

print(total)