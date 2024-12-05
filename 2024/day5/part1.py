import re
import math

newLine = '\n'

file = open('input.txt')
lines = file.readlines()

rules = []
updates = []
validUpdates = []

for line in lines:
	rule = re.findall(r"[0-9]*\|[0-9]*", line)
	if rule:
		ruleString = rule[0]
		ruleString = ruleString.split('|')
		newRule = []
		for number in ruleString:
			newRule.append(int(number))
		rules.append(newRule)
	else:
		update = line.split(",") 
		newUpdate = []
		if not "\n" in update[0]:
			for number in update:
				if "\n" in number:
					number = number.split('\n')[0]
				newUpdate.append(int(number))
			updates.append(newUpdate)

for update in updates:
	updateValid = True
	index = 0
	for number in update:
		ruleMatches = []
		for rule in rules:
			if rule[0] == number:
				ruleMatches.append(rule[1])
		for match in ruleMatches:
			for pastNumber in update[0:index]:
				if pastNumber == match:
					updateValid = False
					break
			if not updateValid:
				break
		if not updateValid:
			break
		index += 1
	if updateValid:
		validUpdates.append(update)

total = 0

for update in validUpdates:
	midIndex = math.ceil(len(update)/2) - 1
	total += update[midIndex]

print(total)