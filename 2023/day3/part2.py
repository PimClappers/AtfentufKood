lines = open("input1.txt").readlines()

numbers = [0,1,2,3,4,5,6,7,8,9]

total = 0

symbolIsStar = False
lastStarPosition = [] #line, position
starPairs = [] #line, position, number1 = -1, number2 = -1, valid

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
                if charToCheck == "*":
                    found = False
                    for pair in starPairs:
                        if (pair[0] == line-1+i) and (pair[1] == position-1+j):
                            found = True
                    if not found:
                        starPairs.append([line-1+i, position-1+j, -1, -1, True])
                    global symbolIsStar
                    symbolIsStar = True
                    global lastStarPosition
                    lastStarPosition = [line-1+i, position-1+j]
    return touching

for line in range(len(lines)):
    readingNumber = False
    number = ""
    enginePartValid = False

    for characterPos in range(len(lines[line])):
        charToCheck = lines[line][characterPos]
        readingNumber = checkIfCharacterIsNumber(charToCheck)
        if readingNumber:
            number += charToCheck
            if CheckIfTouchingSymbol(line, characterPos):
                enginePartValid = True
        else:
            if enginePartValid:
                if symbolIsStar:
                    for pair in starPairs:
                        if (pair[0] == lastStarPosition[0]) and (pair[1] == lastStarPosition[1]):
                            if (pair[4] == True):
                                if pair[2] == -1:
                                    pair[2] = int(number)
                                elif pair[3] == -1:
                                    pair[3] = int(number)
                                else:
                                    pair[4] = False
            number = ""
            enginePartValid = False
            symbolIsStar = False

for pair in starPairs:
    if (not pair[2] == -1) and (not pair[3] == -1) and (pair[4] == True):
        ratio = pair[2] * pair[3]
        total += ratio

print ("total " + str(total))