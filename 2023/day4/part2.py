cards = open("input1.txt").readlines()

total = 0

for c in range(len(cards)):
	# Get numbers in cards
	card = cards[c]
	newLineIndex = card.find("\n")
	card = card[0:newLineIndex]
	cardChunks = card.split(": ")
	card = cardChunks[1]
	cardChunks = card.split("|")
	for i in range(len(cardChunks)):
		cardChunks[i] = cardChunks[i].split()
		for j in range(len(cardChunks[i])):
			cardChunks[i][j] = int(cardChunks[i][j])
	cards[c] = cardChunks
	cards[c].append(1) #number of instances of card

	winningNumbers = cards[c][0]
	ownNumbers = cards[c][1]
	nMatches = 0
	for winningNumber in winningNumbers:
		for ownNumber in ownNumbers:
			if winningNumber == ownNumber:
				nMatches += 1
	cards[c].append(nMatches) # number of matches in card

for c in range(len(cards)):
	card = cards[c]
	for i in range(card[3]):
		cards[c+i+1][2] += card[2] # add the numer of instances of current card to the instances of sequenctial cards
	total += card[2] # add the number of instances of current card to total

print("Total number of cards: " + str(total))