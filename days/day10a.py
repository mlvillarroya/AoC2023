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

def substituteSBySymbol(matrix,initialRow,initialColumn):
    coordinates = [0,0,0,0]
    if initialRow > 0 and SYMBOLS[matrix[initialRow - 1][initialColumn]][2]==1 : coordinates[0] = 1
    if initialRow < len(matrix) and SYMBOLS[matrix[initialRow + 1][initialColumn]][0]==1 : coordinates[2] = 1
    if initialColumn > 0 and SYMBOLS[matrix[initialRow][initialColumn-1]][1]==1 : coordinates[3] = 1
    if initialColumn < len(matrix[0]) and SYMBOLS[matrix[initialRow][initialColumn+1]][3]==1 : coordinates[1] = 1
    symbol = [symbol for symbol in SYMBOLS.keys() if SYMBOLS[symbol] == coordinates][0]
    if symbol: return symbol
    else: raise ValueError('matrix is not correct, can\'t find symbol')

# def nextNode(matrix, initialRow, initialColumn):


def execute():
    instructions = loadData()
    initialRow, initialColumn = lookForBeginning(instructions)
    startSymbol = substituteSBySymbol(instructions,initialRow, initialColumn)
    steps = 0
    
    pass
