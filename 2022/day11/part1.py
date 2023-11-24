lines = open("input.txt").read().split("\n")

monkeys = [] # [0]factor, [1]operator, [2]modulo, [3]if true, [4]if false, [5]items, [6]counter
FACTOR = 0
OPERATOR = 1
MODULO = 2
IF_TRUE = 3
IF_FALSE = 4
ITEMS = 5
COUNTER = 6

for i in range(len(lines)):
    line = lines[i]
    if (line != ""):
        if (line.split()[0] == "Monkey"):
            monkeys.append([0, 0, 0, 0, 0, [], 0])

            factor = lines[i+2].split()[-1]
            monkeys[-1][FACTOR] = factor

            operator = lines[i+2].split()[-2]
            monkeys[-1][OPERATOR] = operator

            modulo = lines[i+3].split()[-1]
            monkeys[-1][MODULO] = int(modulo)

            if_true = lines[i+4].split()[-1]
            monkeys[-1][IF_TRUE] = int(if_true)

            if_false = lines[i+5].split()[-1]
            monkeys[-1][IF_FALSE] = int(if_false)

            items = lines[i+1].split()
            items.pop(0)
            items.pop(0)
            for item in items:
                if (item[-1] == ","):
                    item = item[0: -1]
                monkeys[-1][ITEMS].append(int(item))

round = 0

while round < 20:
    for monkey in monkeys:
        for item in monkey[ITEMS]:
            if (monkey[OPERATOR] == "+"):
                if (monkey[FACTOR] != "old"):
                    item = item + int(monkey[FACTOR])
                else:
                    item = item + item
            if (monkey[OPERATOR] == "*"):
                if (monkey[FACTOR] != "old"):
                    item = item * int(monkey[FACTOR])
                else:
                    item = item * item
            item = int(item / 3)
            if (item % monkey[MODULO] == 0):
                monkeys[monkey[IF_TRUE]][ITEMS].append(item)
            else:
                monkeys[monkey[IF_FALSE]][ITEMS].append(item)
            monkey[COUNTER] += 1
        monkey[ITEMS].clear()
    round += 1

counters = []
for monkey in monkeys:
    counters.append(monkey[COUNTER])

counters.sort()
print(counters[-1] * counters[-2])