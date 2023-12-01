def lookForStringNumbers(inputString):
    stringNumbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for stringNumber in stringNumbers.keys():
        if stringNumber in inputString: 
            inputString = inputString.replace(stringNumber,stringNumber[0]+stringNumbers[stringNumber]+stringNumber[-1])
    # for i in range(len(inputString)):
    #     for stringNumber in stringNumbers.keys():
    #         if stringNumber in inputString[0:i]: 
    #             inputString = inputString.replace(stringNumber,stringNumbers[stringNumber])
    return inputString

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
    instructions = [lookForStringNumbers(instruction) for instruction in instructions]
    totalSum = 0
    for instruction in instructions:
        totalSum += firstLastNumber(instruction)
    print(totalSum)