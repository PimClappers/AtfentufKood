lines = open("input1.txt").readlines()

numbers = [0,1,2,3,4,5,6,7,8,9]

total = 0

def checkIfCharacterIsNumber(character):
    isNumber = False
    for number in numbers:
        if character == str(number):
            isNumber = True
            break
    return isNumber

def CheckIfTouchingSymbol(line, position):
    touching = False
    for i in range(3):
        for j in range(3):
            if (line-1+i < 0):
                continue
            if line-1+i > len(lines)-1:
                continue
            if (position-1+j < 0):
                continue
            if position-1+j > len(lines[i])-1:
                continue
            charToCheck = lines[line-1+i][position-1+j]
            if (not checkIfCharacterIsNumber(charToCheck)) and (not charToCheck == ".") and (not charToCheck == "\n"):
                touching = True
                break
        if touching:
            break
    return touching

for line in range(len(lines)):
    readingNumber = False
    number = ""
    enginePartValid = False

    for characterPos in range(len(lines[line])):
        charToCheck = lines[line][characterPos]
        readingNumber = checkIfCharacterIsNumber(charToCheck)
        if (readingNumber):
            number += charToCheck
            if (not enginePartValid):
                if (CheckIfTouchingSymbol(line, characterPos)):
                    enginePartValid = True
        else:
            if enginePartValid:
                print(number)
                total += int(number)
            number = ""
            enginePartValid = False

print ("total " + str(total))