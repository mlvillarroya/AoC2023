import re

FIRST_STOP = 'AAA'
LAST_STOP = 'ZZZ'

def loadData():
    with open(".\\days\\08_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    guidelines = instructions[0]
    instructions = instructions[2:]
    pattern = r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)" # Define el patrón con tres grupos de captura
    myMap = {}
    for instruction in instructions:
        match = re.search(pattern, instruction) # Busca el patrón en el texto
        myMap[match.group(1)] = [match.group(2), match.group(3)]
    return guidelines, myMap

def execute():
    guidelines, myMap = loadData()
    currentStop = FIRST_STOP
    steps = 0
    while currentStop != LAST_STOP:
        for currentChar in guidelines:
            if currentChar == 'L': 
                currentStop = myMap[currentStop][0]
            else: 
                currentStop = myMap[currentStop][1]
            steps += 1
            if currentStop == LAST_STOP: break
    print(steps)
