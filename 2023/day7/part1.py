strengthOrder = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"] #strongest to weakest
letterMapping = [["T", "10"],["J", "11"],["Q", "12"],["K", "13"],["A", "14"]]

lines = open("input1.txt").readlines()

def isNofKind(hand, n):
	success = False
	foundPairs = [] # [[char, amount], [char amount]]
	for char in hand:
		alreadyFound = False
		for pair in foundPairs:
			if pair[0] == char:
				pair[1] += 1
				alreadyFound = True
		if not alreadyFound:
			foundPairs.append([char, 1])

	for pair in foundPairs:
		if pair[1] == n:
			success = True
	return success

def isFullHouse(hand):
	success = False
	if isNofKind(hand, 3) and isNofKind(hand, 2):
		success = True
	return success

def isTwoPair(hand):
	success = False
	firstPairFound = False
	foundPairs = [] # [[char, amount], [char amount]]
	for char in hand:
		alreadyFound = False
		for pair in foundPairs:
			if pair[0] == char:
				pair[1] += 1
				alreadyFound = True
		if not alreadyFound:
			foundPairs.append([char, 1])

	for pair in foundPairs:
		if pair[1] == 2:
			if not firstPairFound:
				firstPairFound = True
			else:
				success = True
	return success


hands = []
rankedHands = []

for line in lines:
	lineChunks = line.split()
	hand = lineChunks[0]
	bid = int(lineChunks[1])
	handType = 0

	if isNofKind(hand, 5): # five of a kind
		handType = 7
	elif isNofKind(hand, 4): # four of a kind
		handType = 6
	elif isFullHouse(hand): # full house
		handType = 5
	elif isNofKind(hand, 3): # three of a kind
		handType = 4
	elif isTwoPair(hand): # two pair
		handType = 3
	elif isNofKind(hand, 2): #one pair
		handType = 2
	else: #high card
		handType = 1

	hands.append([hand, bid, handType, -1, "", 0]) # hand, bid, handType, rank, handvalue(string), handvalue(int)

for i in range(7):
	typeDone = False
	characterToCheck = 0
	while not typeDone:
		handsWithSameType = []
		for hand in hands:
			if hand[2] == i+1 and hand[3] == -1:
				handsWithSameType.append(hand)

		if len(handsWithSameType) > 0:
			for hand in handsWithSameType:
				converted = False
				for pair in letterMapping:
					if hand[0][characterToCheck] == pair[0]:
						hand[4] += pair[1]
						converted = True
				if not converted:
					hand[4] += "0" + str(hand[0][characterToCheck])

			for hand in handsWithSameType:
				hand[5] = int(hand[4])

			

			handsWithSameType = sorted(handsWithSameType, key=lambda x: x[5])

			sameValue = False
			if len(handsWithSameType) > 1:
				for hand in handsWithSameType:
					for secondHand in handsWithSameType:
						if not hand[0] == secondHand[0]:
							if hand[5] == secondHand[5]:
								sameValue = True
			if not sameValue or len(handsWithSameType) == 1:
				for hand in handsWithSameType:
					hand[5] = int(hand[4])
				handsWithSameType[0][3] = 1
				rankedHands.append(handsWithSameType[0])
				characterToCheck = 0
				for hand in handsWithSameType:
					hand[4] = ""
					hand[5] = 0
			else:
				characterToCheck += 1

		else:
			typeDone = True

total = 0

for i in range(len(rankedHands)):
	hand = rankedHands[i]
	total += hand[1] * (i+1)

print("Result: " + str(total))