operations = open("input.txt").read().split("\n")

value = 1
cycle = 1

totalStrengt = 0
currentPixel = 0

def calculateStrength():
    global totalStrengt
    global value
    global cycle
    if (cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
        totalStrengt += (cycle * value)

def drawPixels():
    global value
    global currentPixel
    if (currentPixel == value or currentPixel == value - 1 or currentPixel == value + 1):
        print("#", end="")
    else:
        print(".", end="")
    currentPixel += 1
    if (currentPixel > 39):
        print()
        currentPixel = 0

def cycleOperation():
    calculateStrength()
    drawPixels()

for operation in operations:
    command = operation.split()[0]
    number = 0
    cycleOperation()
    if (command == "noop"):
        lol = 0
    else:
        number = int(operation.split()[1])
        cycle += 1
        cycleOperation()
    value += number
    cycle += 1

print("Total strength: " + str(totalStrengt))