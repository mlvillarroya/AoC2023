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

def howManyAdjacentsNumbers(instructions, numberRow, numberColumn):
    if numberRow == 0: startRow = numberRow
    else: startRow = numberRow - 1
    if numberRow == len(instructions)-1: endRow = numberRow
    else: endRow = numberRow + 1
    howManyAdjacentsNumbers = 0
    adjacentNumbers = []
    for i in range(startRow,endRow + 1):
        [numberStartColumn, numberEndColumn] = lookForNumber(instructions,i,0)
        while numberStartColumn != -1:
            if numberStartColumn <= numberColumn + 1 and numberEndColumn >= numberColumn - 1:
                howManyAdjacentsNumbers += 1
                adjacentNumbers.append(int(instructions[i][numberStartColumn:numberEndColumn+1]))
            [numberStartColumn, numberEndColumn] = lookForNumber(instructions,i,numberEndColumn + 1)
    return [howManyAdjacentsNumbers,adjacentNumbers]

def execute():
    inputData = loadData()
    total = 0
    for i in range(len(inputData)):
        for j in range(len(inputData[i])):
            if inputData[i][j] == '*':
                howMany, numbers = howManyAdjacentsNumbers(inputData,i,j)
                if howMany == 2: total += (numbers[0] * numbers[1])
    print(total)
