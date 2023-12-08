import re
import math

def loadData():
    with open(".\\days\\08_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    guidelines = instructions[0]
    instructions = instructions[2:]
    pattern = r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)" # Define el patrón con tres grupos de captura
    myMap = {}
    for instruction in instructions:
        match = re.search(pattern, instruction) # Busca el patrón en el texto
        myMap[match.group(1)] = [match.group(2), match.group(3)]
    return guidelines, myMap

def searchForInitialNodes(myMaps):
    return [node for node in myMaps.keys() if node.endswith("A")]

# def allNodesAreFinal(currentStops):
#     return all(node.endswith("Z") for node in currentStops)

def execute():
    guidelines, myMap = loadData()
    currentStops = searchForInitialNodes(myMap)
    steps = 0
    # while not allNodesAreFinal(currentStops):
    #     for currentChar in guidelines:
    #         for i in range(len(currentStops)):
    #             if currentChar == 'L': 
    #                 currentStops[i] = myMap[currentStops[i]][0]
    #             else: 
    #                 currentStops[i] = myMap[currentStops[i]][1]
    #         steps += 1
    #         if allNodesAreFinal(currentStops): break
    # print(steps)
    globalSteps = []
    for i in range(len(currentStops)):
        currentStop = currentStops[i]
        steps = 0
        while not currentStop.endswith('Z'):
            for currentChar in guidelines:
                if currentChar == 'L': 
                    currentStop = myMap[currentStop][0]
                else: 
                    currentStop = myMap[currentStop][1]
                steps += 1
                if currentStop.endswith('Z'): break
        globalSteps.append(steps)
    print(math.lcm(*globalSteps))
