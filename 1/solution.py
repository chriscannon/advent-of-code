"""
Day 1 Advent of Code 2018
"""
import sys


def main(filename):
    """Outputs the resulting frequency and the frequency reached twice."""
    with open(filename) as f:
        frequencies = list(map(int, f.readlines()))
    print("Part 1 resulting frequency: {}".format(sum(frequencies)))

    previous = {0}
    current = 0
    while True:
        for f in frequencies:
            current += f
            if current in previous:
                print("Part 2 first frequency reached twice: {}".format(current))
                return
            previous.add(current)


if __name__ == '__main__':
    main(sys.argv[1])
