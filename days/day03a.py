def loadData():
    with open(".\\days\\03_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    return instructions

def lookForNumber(instructions: list[list[str]], row:int, startColumn:int):
    catchedNumber = False
    foundNumberStartColumn = -1
    foundNumberEndColumn = -1
    for j in range (startColumn, len(instructions[row])):
        if not catchedNumber and instructions[row][j].isnumeric():
            foundNumberStartColumn = j
            catchedNumber = True
        if catchedNumber and instructions[row][j].isnumeric() and j == len(instructions[row])-1:
            foundNumberEndColumn = j
        if catchedNumber and not instructions[row][j].isnumeric():
            foundNumberEndColumn = j-1
            break
    return [foundNumberStartColumn, foundNumberEndColumn]

def adjacentToASimbol(instructions, numberRow, numberStart, numberEnd):
    if numberRow == 0: startRow = numberRow
    else: startRow = numberRow - 1
    if numberRow == len(instructions)-1: endRow = numberRow
    else: endRow = numberRow + 1
    if numberStart == 0: startColumn = numberStart
    else: startColumn = numberStart - 1
    if numberEnd == len(instructions[numberRow]) - 1: endColumn = numberEnd
    else: endColumn = numberEnd + 1
    for row in range(startRow,endRow+1):
        for column in range(startColumn,endColumn + 1):
            if instructions[row][column] != '.' and not instructions[row][column].isnumeric(): return True
    return False

def execute():
    inputData = loadData()
    total = 0
    for i in range(len(inputData)):
        [startColumn, endColumn] = lookForNumber(inputData,i,0)
        while startColumn != -1:
            if adjacentToASimbol(inputData,i,startColumn,endColumn): total += int(inputData[i][startColumn:endColumn+1])
            [startColumn, endColumn] = lookForNumber(inputData,i,endColumn + 1)

    print(total)