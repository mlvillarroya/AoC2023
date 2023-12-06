def loadData():
    with open(".\\days\\06_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
        time = int(''.join(number for number in instructions[0].split(":")[1].split()))
        distance = int(''.join(number for number in instructions[1].split(":")[1].split()))
        return time, distance

def recordWithButtonTime(time, distance, buttonTime) -> bool:
    if buttonTime*(time-buttonTime) > distance: return True
    else: return False

def execute():
    time, distance = loadData()
    successfulTimes = 0
    for j in range(time):
        if recordWithButtonTime(time,distance,j): successfulTimes += 1
    print(successfulTimes)