"""
Day 3 Advent of Code 2018
"""
import re
import sys

MAX_FABRIC_SIZE = 1000


def main(filename):
    """Parse the input file and output the results."""
    claims = []
    p = re.compile(r'(\d+)')
    with open(filename) as f:
        for l in f:
            id_, left, top, width, height = map(int, p.findall(l))
            claims.append([id_, left, top, width, height])
    fabric = create_fabric(claims)
    print("Part 1 inches of overlapping fabric: {}".format(sum([r.count("X") for r in fabric])))
    print("Part 2 non-overlapping claim ID: {}".format(find_non_overlapping_claim(fabric, claims)))


def create_fabric(claims):
    """Creates the fabric and populates the claims."""
    fabric = [['.' for _ in range(MAX_FABRIC_SIZE)] for _ in range(MAX_FABRIC_SIZE)]
    for (id_, left, top, width, height) in claims:
        for x in range(height):
            for y in range(width):
                current = fabric[top - 1 + x][left - 1 + y]
                if current == ".":
                    fabric[top - 1 + x][left - 1 + y] = id_
                else:
                    fabric[top - 1 + x][left - 1 + y] = "X"
    return fabric


def find_non_overlapping_claim(fabric, claims):
    """Locates the only claim that does not overlap with another claim."""
    for (id_, left, top, width, height) in claims:
        found_overlap = False
        for x in range(height):
            for y in range(width):
                if fabric[top - 1 + x][left - 1 + y] == "X":
                    found_overlap = True
        if not found_overlap:
            return id_


if __name__ == '__main__':
    main(sys.argv[1])
