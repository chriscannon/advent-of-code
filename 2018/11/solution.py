"""
Day 11 Advent of Code 2018
"""
import sys

MIN_GRID_SIZE = 1
MAX_GRID_SIZE = 301


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        serial = int(f.readline().strip())
    grid = create_grid(serial)
    area = create_summed_area(grid)

    coordinates, power = find_max_power_square(area, 3)
    print("Part 1 coordinates of the largest power square with grid size 3: {},{} with power {}".format(
        coordinates[0], coordinates[1], power
    ))
    coordinates, size, power = find_max_power_all_sizes(area)
    print("Part 2 coordinates of the largest power square with the largest grid size: {},{},{} with power {}".format(
        coordinates[0], coordinates[1], size, power
    ))


def find_max_power_all_sizes(area):
    """Find the maximum power area for many grid sizes."""
    max_power = 0
    max_size = 0
    max_coordinates = None
    for square_size in range(MIN_GRID_SIZE, MAX_GRID_SIZE):
        coordinates, power = find_max_power_square(area, square_size)
        if power > max_power:
            max_power = power
            max_size = square_size
            max_coordinates = coordinates
    return max_coordinates, max_size, max_power


def find_max_power_square(area, size):
    """Find the max power area for one grid size."""
    max_power = float('-inf')
    coords = None

    for x in range(MIN_GRID_SIZE, MAX_GRID_SIZE - size):
        for y in range(MIN_GRID_SIZE, MAX_GRID_SIZE - size):
            a = area[x, y]
            b = area.get((x, y + size), 0)
            c = area.get((x + size, y), 0)
            d = area.get((x + size, y + size), 0)
            total = a - b - c + d

            if total > max_power:
                max_power = total
                coords = (x + 1, y + 1)
    return coords, max_power


def get_power(x, y, serial):
    """Compute the power of a x, y position."""
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = (power // 100) % 10
    return power - 5


def create_grid(serial):
    """Create the initial power grid."""
    grid = {}
    for x in range(MIN_GRID_SIZE, MAX_GRID_SIZE):
        for y in range(MIN_GRID_SIZE, MAX_GRID_SIZE):
            grid[x, y] = get_power(x, y, serial)
    return grid


def create_summed_area(grid):
    """Create the summed-area table (https://en.wikipedia.org/wiki/Summed-area_table)."""
    area = {}
    for (x, y), v in grid.items():
        area[x, y] = v + area.get((x, y - 1), 0) + area.get((x - 1, y), 0) - area.get((x - 1, y - 1), 0)
    return area


if __name__ == '__main__':
    main(sys.argv[1])
