#!/usr/bin/env python3

import sys

ROCK = 0
PAPER = 1
SCISSORS = 2

LOSE = 0
DRAW = 1
WIN = 2

# r = theirs, c = outcome
MYMOVE = [
    [SCISSORS, ROCK, PAPER],
    [ROCK, PAPER, SCISSORS],
    [PAPER, SCISSORS, ROCK],
]

RESULTSCORE = {WIN: 6, DRAW: 3, LOSE: 0}

IN_2_MOVE = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

IN_2_OUTCOME = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

MOVE_2_VALUE = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}


def score(theirs: int, outcome: int) -> int:
    mine = MYMOVE[theirs][outcome]
    return RESULTSCORE[outcome] + MOVE_2_VALUE[mine]


total = 0
for line in sys.stdin:
    theirs, mine = line.rstrip().split()
    total += score(IN_2_MOVE[theirs], IN_2_OUTCOME[mine])
print(total)
