def loadData():
    with open(".\\days\\04_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
        card1 = [[int(element) for element in line if element != ''] for line in [line.split(':')[1].split('|')[0].split(" ") for line in instructions]]
        card2 = [[int(element) for element in line if element != ''] for line in [line.split(':')[1].split('|')[1].split(" ") for line in instructions]]
    return card1, card2

def howManyOccurrences(lineCard1, lineCard2):
    occurrences = 0
    for number in lineCard1:
            if number in lineCard2: occurrences += 1
    return occurrences

def execute():
    result = 0
    card1, card2 = loadData()
    cards = {i+1:1 for i in range(len(card1))}
    for i in range(len(card1)):
        for j in range(howManyOccurrences(card1[i],card2[i])):
            cards[i+j+2] += (1 * cards[i+1])
    print(sum(num for num in cards.values()))
    