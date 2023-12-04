cards = open("input1.txt").readlines()

total = 0

for card in cards:
	newLineIndex = card.find("\n")
	card = card[0:newLineIndex]
	cardChunks = card.split(": ")
	card = cardChunks[1]
	cardChunks = card.split("|")

	for i in range(len(cardChunks)):
		cardChunks[i] = cardChunks[i].split()
		for j in range(len(cardChunks[i])):
			cardChunks[i][j] = int(cardChunks[i][j])

	cardScore = 0

	for winningNumber in cardChunks[0]:
		for ownNumber in cardChunks[1]:
			if winningNumber == ownNumber:
				if cardScore == 0:
					cardScore += 1
				else:
					cardScore = cardScore * 2

	total += cardScore
	print(cardScore)

print ("total " + str(total))