"""
Day 14 Advent of Code 2018
"""
import itertools
import sys

RECIPE_LOOK_AHEAD = 5


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        recipes = int(f.read().strip())
    score = [3, 7]
    elf1_i, elf2_i = 0, 1

    for i in itertools.count(0):
        elf1_r, elf2_r = score[elf1_i], score[elf2_i]
        sum_ = score[elf1_i] + score[elf2_i]
        for d in str(sum_):
            score.append(int(d))
        elf1_i = (elf1_r + 1 + elf1_i) % len(score)
        elf2_i = (elf2_r + 1 + elf2_i) % len(score)

        if i == (recipes + RECIPE_LOOK_AHEAD + 1):
            sequence = ''.join(map(str, score[recipes:recipes + 10]))
            print(f'Part 1 ten recipes after puzzle input: {sequence}')

        if str(recipes) in ''.join(map(str, score[-7:])):
            recipes_before = ''.join(map(str, score)).index(str(recipes))
            print(f'Part 2 # of recipes before the puzzle input: {recipes_before}')
            break


def show_score(score, elf1, elf2):
    """Helper function to output the score board."""
    out = []
    for i, s in enumerate(score):
        if i == elf1:
            out.append("({})".format(score[elf1]))
        elif i == elf2:
            out.append("[{}]".format(score[elf2]))
        else:
            out.append(str(s))
    print(' '.join(out))


if __name__ == '__main__':
    main(sys.argv[1])
