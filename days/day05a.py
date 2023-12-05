def loadData():
    with open(".\\days\\05_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
        seeds = [int(number) for number in instructions.pop(0).split(":")[1].split(" ") if number]
        mapNumber = -1
        maps = []
        for i in range(len(instructions)):
            if not instructions[i]: continue
            if not instructions[i][0].isnumeric():
                mapNumber += 1
                maps.append([])
            else: maps[mapNumber].append([int(number) for number in instructions[i].split(" ")])
        return seeds, maps

def goThroughMap(number, maps):
    for map in maps:
        for line in map:
            if number >= line[1] and number <= line[1] + line[2]:
                number = number + line[0] - line[1]
                break
    return number

def execute():
    seeds, maps = loadData()
    print(min([goThroughMap(seed,maps) for seed in seeds]))