"""
Day 6 Advent of Code 2018
"""
import sys
from collections import Counter


def main(filename):
    """Parse the coordinates from the file and prints the results."""
    with open(filename) as f:
        coordinates = [list(map(int, x.split(","))) for x in f.readlines()]
    area_matrix = generate_largest_area_matrix(coordinates)
    count = count_maximum_areas(area_matrix)
    infinite_indices = find_infinite_indices(area_matrix)
    for index in infinite_indices:
        del count[index]
    print("Part 1 the maximum area of the coordinates: {}".format(max(count.values())))
    safe_matrix = generate_safe_area_matrix(coordinates)
    print("Part 2 the total safe area of the coordinates: {}".format(sum([r.count("#") for r in safe_matrix])))


def count_maximum_areas(matrix):
    """Calculates the size of the maximum area given in the matrix."""
    rows = iter(matrix)
    counter = Counter(next(rows))
    for row in rows:
        counter += Counter(row)
    del counter["."]
    return counter


def init_matrix(coordinates):
    """Initialize the matrix by creating it and determining the maximum x and y coordinates."""
    max_x = max(x[0] for x in coordinates) + 1
    max_y = max(x[1] for x in coordinates) + 1
    matrix = [["." for _ in range(max_x)] for _ in range(max_y)]
    return matrix, max_x, max_y


def generate_safe_area_matrix(coordinates):
    """Generate the matrix for the safest area."""
    matrix, max_x, max_y = init_matrix(coordinates)
    for y in range(max_y):
        for x in range(max_x):
            total = sum([compute_taxicab_distance(x, y, *coordinate) for coordinate in coordinates])
            if total < 10000:
                matrix[y][x] = "#"
    return matrix


def generate_largest_area_matrix(coordinates):
    """Generates a matrix containing the area of each coordinate using taxicab distance."""
    matrix, max_x, max_y = init_matrix(coordinates)
    for y in range(max_y):
        for x in range(max_x):
            distances = [compute_taxicab_distance(x, y, *coordinate) for coordinate in coordinates]
            indices = [i for i, v in enumerate(distances) if v == min(distances)]
            if len(indices) > 1:
                matrix[y][x] = "."
            else:
                matrix[y][x] = indices[0]
    return matrix


def find_infinite_indices(matrix):
    """Finds the infinite indices in the matrix."""
    infinite_indices = set()
    for y, row in enumerate(matrix):
        for x, index in enumerate(row):
            if y == 0 or y == len(matrix) - 1:
                infinite_indices.add(index)
            elif x == 0 or x == len(row) - 1:
                infinite_indices.add(index)
    return infinite_indices


def is_infinite(x, y, max_x, max_y):
    """Check if the coordinate is in an infinite position."""
    if x == 0 or y == 0:
        return True
    if x == (max_x - 1) or y == (max_y - 1):
        return True
    return False


def compute_taxicab_distance(x1, y1, x2, y2):
    """Compute taxicab distance"""
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    main(sys.argv[1])
