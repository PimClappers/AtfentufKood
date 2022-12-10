operations = open("input.txt").read().split("\n")

value = 1
cycle = 1

totalStrengt = 0

def calculateStrength():
    global totalStrengt
    global value
    global cycle
    if (cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
        print(cycle)
        print(cycle * value)
        totalStrengt += (cycle * value)

for operation in operations:
    command = operation.split()[0]
    number = 0
    calculateStrength()
    if (command == "noop"):
        lol = 0
    else:
        number = int(operation.split()[1])
        cycle += 1
        calculateStrength()
    value += number
    cycle += 1

print("Total: " + str(totalStrengt))