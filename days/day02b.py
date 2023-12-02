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

def minimumSet(gameSetsList):
    response = {}
    for gameSet in gameSetsList:
        for key in gameSet.keys():
            if key not in response or response[key] < gameSet[key]: response[key] = gameSet[key]
    return response
            

def execute():
    instructions = loadData()
    result = 0
    for instruction in instructions:
        minSet = minimumSet(readInstruction(instruction)[1])
        minSetPower = 1
        for item in minSet.values(): minSetPower *= item
        result += minSetPower
    print(result)