"""
Day 5 Advent of Code 2018
"""
import sys
from string import ascii_lowercase


def main(filename):
    """Read the input file and print the results"""
    with open(filename) as f:
        polymer = f.read().strip()
    print("Part 1 length of reduced polymer: {}".format(reduce(polymer)))
    print("Part 2 length of reduced improved polymer: {}".format(improved_polymer(polymer)))


def improved_polymer(polymer):
    """Return the minimal reduced polymer when eliminating unit types."""
    return min((reduce(polymer.replace(c, '').replace(c.upper(), '')) for c in ascii_lowercase))


def reduce(polymer):
    """Reduces the polymer units."""
    found_reduction = True
    reduced = ""
    while found_reduction:
        found_reduction = False
        previous = ""
        reduced = ""
        for i, current in enumerate(polymer):
            if i == 0:
                reduced += current
                previous = current
            elif is_reactive(previous, current):
                reduced = reduced[:-1]
                found_reduction = True
                previous = reduced[-1] if reduced else ""
            else:
                reduced += current
                previous = current
        polymer = reduced
    return len(reduced)


def is_reactive(unit1, unit2):
    """Check if polymer units are reactive."""
    return unit1.lower() == unit2.lower() and unit1 != unit2


if __name__ == "__main__":
    main(sys.argv[1])
