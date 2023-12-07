import numpy as np 
from enum import Enum

def loadData():
    with open(".\\days\\07_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    return instructions

CARDS = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9': 8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
DIFFERENT_PLAYS = 7

class Play(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

def playAnalyze(play):
    charsInPlay = {}
    for eachChar in play:
        if eachChar in charsInPlay.keys(): charsInPlay[eachChar] += 1
        else: charsInPlay[eachChar] = 1
    if 5 in charsInPlay.values(): return Play.FIVE_OF_A_KIND
    elif 4 in charsInPlay.values(): return Play.FOUR_OF_A_KIND
    elif 3 in charsInPlay.values() and 2 in charsInPlay.values(): return Play.FULL_HOUSE
    elif 3 in charsInPlay.values(): return Play.THREE_OF_A_KIND
    elif 2 in charsInPlay.values() and len(charsInPlay) == 3: return Play.TWO_PAIR
    elif 2 in charsInPlay.values(): return Play.ONE_PAIR
    else: return Play.HIGH_CARD

def cardValue(card):
    return ([CARDS[letter] for letter in card])

def getSortedValuesIndex(cardValueList):
    if not cardValueList: return
    cardValueList = [[i] + cardValueList[i] for i in range(len(cardValueList))]
    cardValueNp = np.array(cardValueList)
    cardValueNp = cardValueNp[np.lexsort((cardValueNp[:,5],cardValueNp[:,4],cardValueNp[:,3],cardValueNp[:,2],cardValueNp[:,1]))] 
    return [value[0] for value in cardValueNp]

def execute():
    instructions = loadData()
    listByPlayValue = np.array([])
    for i in range(1,DIFFERENT_PLAYS+1):
        samePointsList = [instruction for instruction in instructions if playAnalyze(instruction.split(" ")[0]).value == i]
        cardValueList = [cardValue(play.split(" ")[0]) for play in samePointsList]
        if getSortedValuesIndex(cardValueList): 
            listByPlayValue = np.append(listByPlayValue,np.array(samePointsList)[getSortedValuesIndex(cardValueList)])
    total = 0
    for i in range(len(listByPlayValue)):
        total += int(listByPlayValue[i].split(" ")[1]) * (1+i)
    print(total)