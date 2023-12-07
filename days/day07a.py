import numpy as np 
from enum import Enum

def loadData():
    with open(".\\days\\07_input.txt", "r") as f:
        instructions = f.readlines()
        instructions = [instruction.strip() for instruction in instructions]
    return instructions

CARDS = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9': 8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

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

# def sortByValue(originList):
    
#      for value in originList:

def cardValue(card):
    return ([CARDS[letter] for letter in card])

def execute():
    instructions = loadData()
    for instruction in instructions:
        print(cardValue(instruction.split(" ")[0]))
    # sortedList = []
    # a = [instruction.split(" ")[0] for instruction in instructions if playAnalyze(instruction.split(" ")[0]).value == 1]
    