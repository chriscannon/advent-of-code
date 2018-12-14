"""
Day 14 Advent of Code 2018
"""
import sys

RECIPE_LOOK_AHEAD = 5

def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        recipes = int(f.read().strip())
    score = [3, 7]
    elf1_i, elf2_i = 0, 1

    # show_score(score, elf1_i, elf2_i)

    # recipes = 2018
    for i in range(recipes + RECIPE_LOOK_AHEAD + 1):
        elf1_r, elf2_r = score[elf1_i], score[elf2_i]
        sum = score[elf1_i] + score[elf2_i]
        for d in str(sum):
            score.append(int(d))
        elf1_i = (elf1_r + 1 + elf1_i) % len(score)
        elf2_i = (elf2_r + 1 + elf2_i) % len(score)
        # show_score(score, elf1_i, elf2_i)
    print(''.join(map(str, score[recipes:recipes+10])))
    loc = ''.join(score).find(str(recipes))
    print(''.join(map(str, score[loc-5:loc])))


def show_score(score, elf1, elf2):
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
