def loadData():
    with open(".\\days\\06_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
        time = [int(number) for number in (' '.join(instructions[0].split(":")[1].split())).split(" ")]
        distance = [int(number) for number in (' '.join(instructions[1].split(":")[1].split())).split(" ")]
        return time, distance

def recordWithButtonTime(time, distance, buttonTime) -> bool:
    if buttonTime*(time-buttonTime) > distance: return True
    else: return False

def execute():
    time, distance = loadData()
    totalSuccessfulTimes = 1
    for i in range(len(time)):
        successfulTimes = 0
        for j in range(time[i]):
            if recordWithButtonTime(time[i],distance[i],j): successfulTimes += 1
        totalSuccessfulTimes *= successfulTimes
    print(totalSuccessfulTimes)