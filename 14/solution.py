"""
Day 14 Advent of Code 2018
"""
import itertools
import sys


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        recipes = int(f.read().strip())
    score = [3, 7]
    index1, index2 = 0, 1
    recipes_look_ahead = recipes + 5 + 1
    recipes_length = len(str(recipes)) + 1
    recipes_str = str(recipes)

    for i in itertools.count(0):
        val1, val2 = score[index1], score[index2]
        sum_ = val1 + val2
        score.extend(divmod(sum_, 10) if sum_ >= 10 else (sum_,))
        index1 = (val1 + 1 + index1) % len(score)
        index2 = (val2 + 1 + index2) % len(score)

        if i == recipes_look_ahead:
            sequence = ''.join(map(str, score[recipes:recipes + 10]))
            print(f'Part 1 ten recipes after puzzle input: {sequence}')

        if recipes_str == ''.join(map(str, score[-recipes_length:-1])):
            recipes_before = len(score) - len(str(recipes)) - 1
            print(f'Part 2 number of recipes before the puzzle input: {recipes_before}')
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
