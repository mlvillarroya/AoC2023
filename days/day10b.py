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
           'S':[0,0,0,0]
           }

def evenNumberSymbolsEveryWhere(instructions, i, j):
    return sum((instructions[i][k] in SYMBOLS.keys()) * 1 for k in range(0,j)) % 2 == 1 and \
            sum((instructions[i][k] in SYMBOLS.keys()) * 1 for k in range(j+1,len(instructions[i]))) % 2 == 1 and \
            sum((instructions[k][j] in SYMBOLS.keys()) * 1 for k in range(0,i)) % 2 == 1 and \
            sum((instructions[k][j] in SYMBOLS.keys()) * 1 for k in range(i+1,len(instructions))) % 2 == 1


def execute():
    instructions = loadData()
    total = 0
    for i in range(len(instructions)):
        for j in range(len(instructions[i])):
            if instructions[i][j] in SYMBOLS.keys(): continue
            else: 
                if evenNumberSymbolsEveryWhere(instructions,i,j): total += 1
    print(total)

