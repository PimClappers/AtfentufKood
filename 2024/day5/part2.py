import re
import math

file = open('input.txt')
lines = file.readlines()

rules = []
updates = []
validUpdates = []
invalidUpdates = []
fixedUpdates = []

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
	done = False
	updateWasOnceInvalid = False
	while not done:
		updateValid = True
		index = 0
		fixedUpdate = []
		for number in update:
			numberValid = True
			ruleMatches = []
			for rule in rules:
				if rule[0] == number:
					ruleMatches.append(rule[1])
			highestPastNumberIndex = 0
			for match in ruleMatches:
				pastNumberIndex = 0
				for pastNumber in update[0:index]:
					if pastNumber == match:
						updateValid = False
						numberValid = False
						if pastNumberIndex > highestPastNumberIndex:
							highestPastNumberIndex = pastNumberIndex
					pastNumberIndex += 1
			if numberValid:
				fixedUpdate.append(number)
			else:
				updateWasOnceInvalid = True
				fixedUpdate.insert(highestPastNumberIndex, number)
			index += 1
		if updateValid:
			done = True
		else:
			update = fixedUpdate
	if updateWasOnceInvalid:
		fixedUpdates.append(update)

total = 0

for update in fixedUpdates:
	midIndex = math.ceil(len(update) / 2) - 1
	total += update[midIndex]
print(total)
