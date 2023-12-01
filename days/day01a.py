def firstLastNumber(inputString):
    numbersInside = [letter for letter in inputString if letter.isnumeric()]
    if not numbersInside: raise ValueError("String does not contain any numbers")
    return int(numbersInside[0]+numbersInside[-1])

def loadData():
    with open(".\\days\\01_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.split()[0] for instruction in instructions]
    return instructions

def execute():
    instructions = loadData()
    totalSum = 0
    for instruction in instructions:
        totalSum += firstLastNumber(instruction)
    print(totalSum)