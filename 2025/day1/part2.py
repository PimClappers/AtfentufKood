lines = open("input1.txt").read().splitlines()

position = 50
total = 0

for line in lines:
	startPosition = position
	direction = line[0]
	movement = int(line[1:])
	forward = True
	if (direction == 'L'):
		forward = False
	if (direction == 'R'):
		forward = True

	for x in range(movement):
		if (forward):
			position += 1
		else:
			position -= 1

		if (position < 0):
			position = 100 + position
		elif (position > 99):
			position = position - 100

		if (position == 0):
			total += 1
print(total)

