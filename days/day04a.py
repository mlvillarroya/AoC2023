def loadData():
    with open(".\\days\\04_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
        card1 = [[int(element) for element in line if element != ''] for line in [line.split(':')[1].split('|')[0].split(" ") for line in instructions]]
        card2 = [[int(element) for element in line if element != ''] for line in [line.split(':')[1].split('|')[1].split(" ") for line in instructions]]
    return card1, card2


def execute():
    result = 0
    card1, card2 = loadData()
    for i in range(len(card1)):
        occurrences = 0
        for number in card1[i]:
            if number in card2[i]: occurrences += 1
        if occurrences>0: result += 2 ** (occurrences - 1)
    print(result)