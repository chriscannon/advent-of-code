"""
Day 12 Advent of Code 2018
"""
import itertools
import sys

FIVE_DOTS = '.' * 5
SIX_DOTS = '.' * 6


def main(filename):
    """Parse the input file and output the results."""
    plants = FIVE_DOTS
    rules = {}
    with open(filename) as f:
        plants += f.readline().split(': ')[1].strip()
        f.readline()

        for line in f.read().splitlines():
            k, v = line.split(' => ')
            rules[k] = v
    plants += FIVE_DOTS

    new_gen_plants, index = apply_generations(plants, rules, 20)
    print("Part 1 the sum after 20 generations: {}".format(sum_plants(new_gen_plants, index)))
    print("Part 2 the sum after 50B generations: {}".format(find_50b_generations(plants, rules)))


def find_50b_generations(plants, rules):
    """Finds the sum pattern and extrapolates out to 50B generations."""
    index = 5
    previous_sum = 0
    duplicates = 0
    previous_diff = 0
    for t in itertools.count(1):
        plants, index = apply_generation(plants, rules, index)
        current_sum = sum_plants(plants, index)
        diff = current_sum - previous_sum
        if diff == previous_diff:
            duplicates += 1
        else:
            duplicates = 0

        if duplicates == 5:  # If we see the same sum difference 5 times it's a fair assumption we can stop.
            break
        previous_sum = current_sum
        previous_diff = diff
    return current_sum + ((50000000000 - t) * diff)


def sum_plants(plants, index):
    """Sum the potted plants given a starting index."""
    total = 0
    for i, current in enumerate(plants):
        if current == "#":
            total += i - index
    return total


def apply_generations(plants, rules, n):
    """Apply n generations to the plants."""
    index = 5
    for i in range(1, n + 1):
        plants, index = apply_generation(plants, rules, index)
    return plants, index


def apply_generation(plants, rules, index):
    """Apply a single generation to the plants."""
    next_gen = []
    for i, current in enumerate(plants):
        l1 = plants[i - 1] if i - 1 >= 0 else "."
        l2 = plants[i - 2] if i - 2 >= 0 else "."
        r1 = plants[i + 1] if i + 1 <= len(plants) - 1 else "."
        r2 = plants[i + 2] if i + 2 <= len(plants) - 1 else "."

        state = l2 + l1 + current + r1 + r2
        next_gen.append(rules.get(state, "."))

    # Extends and retracts the outer empty plants.
    if next_gen[-5:] != FIVE_DOTS:
        next_gen.append(".")

    if next_gen[-6:] == SIX_DOTS:
        next_gen.pop()

    if next_gen[:5] != FIVE_DOTS:
        next_gen.insert(0, '.')
        index += 1

    if next_gen[:6] == SIX_DOTS:
        next_gen.pop(0)
        index -= 1

    return next_gen, index


if __name__ == '__main__':
    main(sys.argv[1])
