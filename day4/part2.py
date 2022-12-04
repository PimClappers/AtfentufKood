lines = open("input.txt").read().split()
pairs = []

for line in lines:  
    elves = []
    for elf in line.split(","):
        sections = elf.split("-")
        sections[0] = int(sections[0])
        sections[1] = int(sections[1])
        elves.append(sections)
    pairs.append(elves)

matchCounter = 0
for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    if(elf1[0] >= elf2[0] and elf1[0] <= elf2[1] and elf1[1] <= elf2[1] and elf1[1] >= elf2[0]):
        matchCounter += 1
    elif(elf2[0] >= elf1[0] and elf2[0] <= elf1[1] and elf2[1] <= elf1[1] and elf2[1] >= elf1[0]):
        matchCounter += 1
    elif(elf1[0] >= elf2[0] and elf1[0] <= elf2[1] and elf1[1] >= elf2[1]):
        matchCounter += 1
    elif(elf2[0] >= elf1[0] and elf2[0] <= elf1[1] and elf2[1] >= elf1[1]):
        matchCounter += 1
print(matchCounter)