def main():
	file = open('input.txt')
	lines = file.readlines()
	sum = 0
	elves = []
	for line in lines:
	    print(line)	    
	    if line != "\n":
	    	value = int(line)
	    	sum += value
	    else:
	    	elves.append(sum)
	    	print("Sum:" + str(sum))
	    	sum = 0
	elves.sort();
	print("#1 " + str(elves[len(elves)-1]))
	print("#2 " + str(elves[len(elves)-2]))
	print("#3 " + str(elves[len(elves)-3]))
	print("Total top 3: " + str(elves[len(elves)-1] + elves[len(elves)-2] + elves[len(elves)-3]))


if __name__ == "__main__":
    main()