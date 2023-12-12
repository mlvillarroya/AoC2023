def loadData():
    with open(".\\days\\11_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    return instructions

def emptyRow(universe, rowIndex):
    return all(item == '.' for item in universe[rowIndex])

def emptyColumn(universe, colIndex):
    return all(universe[i][colIndex] == '.' for i in range(len(universe)))

def insertNewRow(universe, rowIndex):
    row = "".join(["." for i in range(len(universe[rowIndex]))])
    universe.insert(rowIndex, row)

def insertNewColumn(universe, columnIndex):
    for i in range(len(universe)):
        universe[i] = universe[i][:columnIndex] + '.' + universe[i][columnIndex:]

def universeExpansion(universe):
    extra = 0
    for rowIndex in range(len(universe)):
        if emptyRow(universe, rowIndex+extra): 
            insertNewRow(universe, rowIndex+extra)
            extra += 1
    extra = 0
    for columnIndex in range(len(universe[0])):
        if emptyColumn(universe, columnIndex+extra): 
            insertNewColumn(universe, columnIndex+extra)
            extra += 1

def getGalaxyCoordinates(universe):
    map = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                map.append([i,j])
    return map

def distanceBetweenGalaxies(galaxy1, galaxy2):
    return abs(galaxy1[0]-galaxy2[0])+abs(galaxy1[1]-galaxy2[1])

def execute():
    universe = loadData()
    universeExpansion(universe)
    galaxyMap = getGalaxyCoordinates(universe)
    lenghtSum = 0
    for i in range(len(galaxyMap)):
        lenghtSum += sum(distanceBetweenGalaxies(galaxyMap[i],galaxyMap[j]) for j in range(len(galaxyMap)) if i != j)
    print(lenghtSum//2)


