"""
Day 2 Advent of Code 2018
"""
import sys
from collections import Counter


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        ids = f.read().splitlines()

    print("Part 1 checksum of the IDs: {}".format(compute_checksum(ids)))
    print("Part 2 common letters of correct box IDs: {}".format(common_letters(ids)))


def compute_checksum(ids):
    """Computes the checksum of all the IDs."""
    two_count = 0
    three_count = 0
    for id_ in ids:
        count = Counter(id_)
        two_count += 1 if 2 in count.values() else 0
        three_count += 1 if 3 in count.values() else 0
    return two_count * three_count


def common_letters(ids):
    """Finds the common letters of the two correct box IDs."""
    identical_ids = []
    for i, current_id in enumerate(ids):
        for j, comparison_id in enumerate(ids):
            if j == i:
                continue
            diff = 0
            for t, c in enumerate(comparison_id):
                if c != current_id[t]:
                    diff += 1
            if diff == 1:
                identical_ids.append([current_id, comparison_id])

    common = []
    for i, c in enumerate(identical_ids[0][0]):
        if c == identical_ids[0][1][i]:
            common.append(c)
    return ''.join(common)


if __name__ == '__main__':
    main(sys.argv[1])
