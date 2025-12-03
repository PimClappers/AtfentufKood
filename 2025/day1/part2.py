lines = open("input.txt").read().splitlines()

position = 50
total = 0

for line in lines:
	direction = line[0]
	movement = int(line[1:])

	for x in range(movement):
		if (direction == 'L'):
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