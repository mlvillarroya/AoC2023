def loadData():
    with open(".\\days\\10_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    return instructions

SYMBOLS = {'|':[1,0,1,0],
           '-':[0,1,0,1],
           'L':[1,1,0,0],
           'J':[1,0,0,1],
           '7':[0,0,1,1],
           'F':[0,1,1,0],
           '.':[0,0,0,0]
           }

def lookForBeginning(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S': return i,j
    return None

def oppositeDirection(direction):
    return (direction + 2) % 4

def substituteSBySymbol(matrix,initialRow,initialColumn):
    coordinates = [0,0,0,0]
    if initialRow > 0 and SYMBOLS[matrix[initialRow - 1][initialColumn]][2]==1 : coordinates[0] = 1
    if initialRow < len(matrix) and SYMBOLS[matrix[initialRow + 1][initialColumn]][0]==1 : coordinates[2] = 1
    if initialColumn > 0 and SYMBOLS[matrix[initialRow][initialColumn-1]][1]==1 : coordinates[3] = 1
    if initialColumn < len(matrix[0]) and SYMBOLS[matrix[initialRow][initialColumn+1]][3]==1 : coordinates[1] = 1
    symbol = [symbol for symbol in SYMBOLS.keys() if SYMBOLS[symbol] == coordinates][0]
    if symbol: return symbol
    else: raise ValueError('matrix is not correct, can\'t find symbol')

def nextNode(matrix, initialRow, initialColumn, directionComeFrom, symbol = None):
    if not symbol: symbol = matrix[initialRow][initialColumn] 
    possibleDirections = SYMBOLS[symbol].copy()
    possibleDirections[oppositeDirection(directionComeFrom)] = 0
    nextDirection = [i for i in range(len(possibleDirections)) if possibleDirections[i] == 1][0]
    if nextDirection == 0: initialRow -= 1
    elif nextDirection == 1: initialColumn += 1
    elif nextDirection == 2: initialRow += 1
    else: initialColumn -= 1
    return initialRow,initialColumn,nextDirection

def execute():
    instructions = loadData()
    initialRow, initialColumn = lookForBeginning(instructions)
    startSymbol = substituteSBySymbol(instructions,initialRow, initialColumn)
    steps = 0
    startDirection = [i for i in range(len(SYMBOLS[startSymbol])) if SYMBOLS[startSymbol][i] == 1][0]
    nextSymbol = ""
    i, j, nextDirection = nextNode(instructions,initialRow,initialColumn,startDirection, symbol=startSymbol)
    while True:
        nextSymbol = instructions[i][j]
        steps += 1
        if nextSymbol == 'S': break
        i, j, nextDirection = nextNode(instructions,i,j,nextDirection)
    print(steps//2)

