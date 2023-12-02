def loadData():
    with open(".\\days\\02_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    return instructions

def readInstruction(instruction: str):
    gameId = int(instruction.split(': ')[0].split(' ')[1])
    gameSets = instruction.split(': ')[1].split('; ')
    gameSetsList = [{cubeRevealed.split(' ')[1]:int(cubeRevealed.split(' ')[0]) for cubeRevealed in gameSet.split(', ')} for gameSet in gameSets]
    return [gameId, gameSetsList]

def setContainsSet(originalSet, setToCompare):
    for key in originalSet.keys():
        if key in setToCompare.keys() and originalSet[key] < setToCompare[key]: return False
    return True

def execute():
    #12 red cubes, 13 green cubes, and 14 blue cubes
    bagContent = {"red":12, "green":13, "blue":14}
    instructions = loadData()
    response = 0
    for instruction in instructions:
        [gameId, gameSetList] = readInstruction(instruction)
        gameSetExaminations = [setContainsSet(bagContent,gameSet) for gameSet in gameSetList]
        if all(gameSetExaminations): response += gameId
    print(response)