"""
Day 17 Advent of Code 2018
"""
import fileinput
import sys


def main():
    """Parse the input file and output the results."""
    ground = init_ground()
    show_ground(ground)

def init_ground():
    ground = {(0, 500): '+'}
    with fileinput.input() as f:
        for line in f:
            parts = line.rstrip().split(', ')
            y, x = None, None
            for p in parts:
                key, val = p.split('=')
                if '..' in val:
                    start, stop = list(map(int, val.split('..')))
                    values = list(range(start, stop + 1))
                else:
                    values = [int(val)]
                if key == "x":
                    x = values
                elif key == "y":
                    y = values
                else:
                    raise Exception('Unknown key')
            for dy in y:
                for dx in x:
                    ground[(dy, dx)] = '#'
    return ground

def show_ground(ground):
    min_x = min(g[1] for g in ground.keys())
    max_x = max(g[1] for g in ground.keys())
    min_y = min(g[0] for g in ground.keys())
    max_y = max(g[0] for g in ground.keys())

    for y in range(min_y - 1, max_y + 2):
        row = []
        for x in range(min_x - 1, max_x + 2):
            row.append(ground.get((y, x), '.'))
        print(''.join(row))




if __name__ == '__main__':
    sys.exit(main())
