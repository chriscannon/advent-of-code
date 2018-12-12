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
    coordinates, power = find_max_power_square(grid, 3)
    print("Part 1 the top-left fuel cell of the largest power square with grid size 3: {},{}".format(
        coordinates[0], coordinates[1]
    ))
    coordinates, size, power = find_max_power_all_sizes(grid)
    print("Part 2 the top-left fuel cell of the largest power square with the largest grid size: {},{},{}".format(
        coordinates[0], coordinates[1], size
    ))


def find_max_power_all_sizes(grid):
    """Find the maximum power area for many grid sizes."""
    max_power = 0
    max_size = 0
    max_coordinates = 0, 0
    for square_size in range(1, 20):  # Data shows that after 20 iterations power degrades
        coordinates, power = find_max_power_square(grid, square_size)
        if power > max_power:
            max_power = power
            max_size = square_size
            max_coordinates = coordinates
    return max_coordinates, max_size, max_power


def find_max_power_square(grid, size):
    """Find the max power area for one grid size."""
    max_power = -1000
    coords = None

    for x in range(MIN_GRID_SIZE, MAX_GRID_SIZE - size):
        for y in range(MIN_GRID_SIZE, MAX_GRID_SIZE - size):
            total = 0
            for x1 in range(size):
                for y1 in range(size):
                    total += grid.get((x + x1, y + y1))
            if total > max_power:
                max_power = total
                coords = (x, y)
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


if __name__ == '__main__':
    main(sys.argv[1])
