EMPTY_CELL_SIZE = 10**6
def loadData():
    with open(".\\days\\11_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    return instructions

def emptyRow(universe, rowIndex):
    return all(item == '.' for item in universe[rowIndex])

def emptyColumn(universe, colIndex):
    return all(universe[i][colIndex] != '#' for i in range(len(universe)))

def fillRowWithZeroes(universe, rowIndex):
    for i in range(len(universe[rowIndex])):
        universe[rowIndex] = "".join(["0" for _ in range(len(universe[rowIndex]))])

def fillColumnWithZeroes(universe, colIndex):
    for i in range(len(universe)):
        universe[i] = universe[i][:colIndex] + '0' + universe[i][colIndex + 1:]

def universeExpansion(universe):
    for rowIndex in range(len(universe)):
        if emptyRow(universe, rowIndex): 
            fillRowWithZeroes(universe, rowIndex)

    for columnIndex in range(len(universe[0])):
        if emptyColumn(universe, columnIndex): 
            fillColumnWithZeroes(universe, columnIndex)

def getGalaxyCoordinates(universe):
    map = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                map.append([i,j])
    return map

def distanceBetweenGalaxies(universe, originCoordinates, destinationCoordinates):
    i1, j1 = originCoordinates
    i2, j2 = destinationCoordinates

    i1, i2 = min(i1, i2), max(i1, i2)
    j1, j2 = min(j1, j2), max(j1, j2)

    ans = 0
    for i in range(i1, i2):
        ans += 1
        if universe[i][j1] == '0':
            ans += EMPTY_CELL_SIZE - 1
    for j in range(j1, j2):
        ans += 1
        if universe[i2][j] == '0':
            ans += EMPTY_CELL_SIZE - 1

    return ans    

def execute():
    universe = loadData()
    universeExpansion(universe)
    galaxyMap = getGalaxyCoordinates(universe)
    lenghtSum = 0
    for i in range(len(galaxyMap)):
        for j in range(i+1, len(galaxyMap)):
            lenghtSum += distanceBetweenGalaxies(universe, galaxyMap[i],galaxyMap[j])
    print(lenghtSum)
