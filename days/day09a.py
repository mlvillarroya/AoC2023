def loadData():
    with open(".\\days\\09_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [[int(stringNumber) for stringNumber in instruction.strip().split(" ")] for instruction in instructions]
    return instructions

def computeNextNumber(history):
    historyEvolution = []
    historyEvolution.append(history)
    while not all(member == 0 for member in historyEvolution[-1]):
        newMember = [historyEvolution[-1][i+1] - historyEvolution[-1][i] for i in range(len(historyEvolution[-1])-1)]
        historyEvolution.append(newMember)
    pass

def execute():
    histories = loadData()
    computeNextNumber(histories[2])
    pass