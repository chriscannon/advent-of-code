"""
Day 9 Advent of Code 2018
"""
import re
import sys
from collections import defaultdict, deque


def main(filename):
    """Parse the input file and output the results"""
    with open(filename) as f:
        players, last_marble = map(int, re.findall(r'(\d+)', f.readline()))
    print("Part 1 winning elf's score: {}".format(play(players, last_marble)))
    print("Part 2 winning elf's score with 100x marbles: {}".format(play(players, last_marble * 100)))


def play(players, last_marble):
    """Plays the marble game given a set number of players and the last marble."""
    scores = defaultdict(int)
    marbles = deque([0])

    for m in range(1, last_marble + 1):
        if m % 23 == 0:
            marbles.rotate(7)
            players_turn = m % players
            scores[players_turn] += m + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(m)
    return max(scores.values())


if __name__ == '__main__':
    main(sys.argv[1])
