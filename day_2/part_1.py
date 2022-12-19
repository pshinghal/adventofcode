#!/usr/bin/env python3

import sys

ROCK = 0
PAPER = 1
SCISSORS = 2

WIN = "WIN"
LOSE = "LOSE"
DRAW = "DRAW"

# r = theirs, c = mine
RESULTS = [
    [DRAW, WIN, LOSE],
    [LOSE, DRAW, WIN],
    [WIN, LOSE, DRAW],
]

RESULTSCORE = {WIN: 6, DRAW: 3, LOSE: 0}

IN_2_MOVE = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

MOVE_2_VALUE = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}


def judge(theirs: int, mine: int) -> str:
    return RESULTS[theirs][mine]


def score(theirs: int, mine: int) -> int:
    result = judge(theirs, mine)
    return RESULTSCORE[result] + MOVE_2_VALUE[mine]


total = 0
for line in sys.stdin:
    theirs, mine = line.rstrip().split()
    total += score(IN_2_MOVE[theirs], IN_2_MOVE[mine])
print(total)
