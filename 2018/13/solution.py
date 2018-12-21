"""
Day 13 Advent of Code 2018
"""
import copy
import sys


class Cart:
    """A class to hold the state of a cart."""
    def __init__(self, state):
        self.state = state
        self.turns = 0
        self.is_ghost = False

    def next_coordinate(self, y, x):
        """Get the next coordinate depending on the current direction."""
        if self.state == "^":
            return y - 1, x
        elif self.state == "v":
            return y + 1, x
        elif self.state == "<":
            return y, x - 1
        elif self.state == ">":
            return y, x + 1

        raise Exception('Unknown track state: {}'.format(self.state))

    def change_direction(self, track):
        """Change the direction of the cart depending on the track type which it resides."""
        if track == "\\":
            if self.state == ">":
                self.state = "v"
            elif self.state == "^":
                self.state = "<"
            elif self.state == "v":
                self.state = ">"
            elif self.state == "<":
                self.state = "^"
        elif track == "/":
            if self.state == ">":
                self.state = "^"
            elif self.state == "^":
                self.state = ">"
            elif self.state == "v":
                self.state = "<"
            elif self.state == "<":
                self.state = "v"
        elif track == "+":
            if self.turns == 0:
                if self.state == ">":
                    self.state = "^"
                elif self.state == "^":
                    self.state = "<"
                elif self.state == "v":
                    self.state = ">"
                elif self.state == "<":
                    self.state = "v"
                self.turns = 1
            elif self.turns == 1:
                self.turns = 2
            elif self.turns == 2:
                if self.state == ">":
                    self.state = "v"
                elif self.state == "^":
                    self.state = ">"
                elif self.state == "v":
                    self.state = "<"
                elif self.state == "<":
                    self.state = "^"
                self.turns = 0


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        tracks = [list(t) for t in f.read().splitlines()]
    tracks, carts = find_carts(tracks)
    x, y = find_first_collision(tracks, copy.deepcopy(carts))
    print("Part 1 the first track collision: {},{}".format(x, y))
    x, y = find_last_cart(tracks, carts)
    print("Part 2 the last cart without collision: {},{}".format(x, y))


def find_last_cart(tracks, carts):
    """Find the position of the last cart that has not crashed."""
    while True:
        for (y, x), cart in sorted(carts.items()):
            if cart.is_ghost:
                continue

            dy, dx = cart.next_coordinate(y, x)
            if (dy, dx) in carts and not carts[dy, dx].is_ghost:
                carts[dy, dx].is_ghost = True
                cart.is_ghost = True
            else:
                del carts[y, x]
                cart.change_direction(tracks[dy][dx])
                carts[dy, dx] = cart
        carts_left = [(dx, dy) for (dy, dx), c in carts.items() if not c.is_ghost]
        if len(carts_left) == 1:
            return carts_left[0]


def find_first_collision(tracks, carts):
    """Find the first collision of carts"""
    while True:
        for (y, x), cart in sorted(carts.items()):
            dy, dx = cart.next_coordinate(y, x)
            del carts[y, x]
            if (dy, dx) in carts:
                return dx, dy
            cart.change_direction(tracks[dy][dx])
            carts[dy, dx] = cart


def show_tracks(tracks, carts):
    """Ouput the track and cart state to stdout."""
    for y, r in enumerate(tracks):
        row = []
        for x, v in enumerate(r):
            row.append(carts[y, x].state if (y, x) in carts else v)
        print(''.join(row))


def find_carts(tracks):
    """Find the carts in the initial state."""
    carts = {}
    for y, row in enumerate(tracks):
        for x, val in enumerate(row):
            if val in {"^", "v", ">", "<"}:
                carts[y, x] = Cart(val)
                if val in {"^", "v"}:
                    tracks[y][x] = "|"
                else:
                    tracks[y][x] = "-"
    return tracks, carts


if __name__ == '__main__':
    main(sys.argv[1])
