"""
Day 10 Advent of Code 2018
"""
import itertools
import re
import sys


def main(filename):
    """Parse the input file and output the results."""
    p = re.compile(r'<([^>]+)>')
    vectors = []
    with open(filename) as f:
        for l in f:
            match = p.findall(l)
            x, y = map(int, match[0].split(','))
            vx, vy = map(int, match[1].split(','))
            vectors.append([x, y, vx, vy])
    second, coordinates = find_smallest_bounding_box(vectors)
    print("Part 1 stars message:")
    show_stars(vectors, second, coordinates)
    print("Part 2 message appeared at second: {}".format(second))


def find_smallest_bounding_box(vectors):
    """Find the smallest bounding box when applying the vectors to know when the
    stars have converged into letters."""
    min_area = float('inf')
    for second in itertools.count(1):
        area, coordinates = compute_area_bounding_box(vectors, second)
        if min_area < area:
            return second, coordinates
        min_area = area


def compute_area_bounding_box(vectors, second):
    """Compute the bounding box given the initial vectors at the second specified."""
    max_x = max([v[0] + second * v[2] for v in vectors])
    min_x = min([v[0] + second * v[2] for v in vectors])
    max_y = max([v[1] + second * v[3] for v in vectors])
    min_y = min([v[1] + second * v[3] for v in vectors])
    return (max_x + abs(min_x)) * (max_y + abs(min_y)), (max_x, min_x, max_y, min_y)


def show_stars(vectors, second, coordinates):
    """Print the stars to stdout at the specified second."""
    max_x, min_x, max_y, min_y = coordinates
    grid = [[' '] * (max_x - min_x + 1) for _ in range(min_y, max_y + 1)]
    for (x, y, vx, vy) in vectors:
        grid[y + second * vy - min_y][x + second * vx - min_x] = '#'
    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    main(sys.argv[1])
