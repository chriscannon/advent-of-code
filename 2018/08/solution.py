"""
Day 8 Advent of Code
"""
import sys


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        data = list(map(int, f.readline().split(" ")))
    print("Part 1 sum of the metadata: {}".format(sum_metadata(iter(data))))
    print("Part 2 sum of the root node: {}".format(sum_root_node(iter(data))))


def sum_metadata(data):
    """Sum the metadata of each node."""
    child_nodes = next(data)
    metadata = next(data)

    total = 0
    for _ in range(child_nodes):
        total += sum_metadata(data)

    for _ in range(metadata):
        total += next(data)
    return total


def sum_root_node(data):
    """Sum the metadata of the root node."""
    child_nodes = next(data)
    metadata = next(data)

    children = []
    for i in range(child_nodes):
        children.append(sum_root_node(data))

    total = 0
    if children:
        for i in range(metadata):
            try:
                index = next(data) - 1
                total += children[index]
            except IndexError:
                total += 0
        return total
    else:
        for i in range(metadata):
            total += next(data)
        return total


if __name__ == '__main__':
    main(sys.argv[1])
