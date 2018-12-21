from dataclasses import dataclass
from typing import List, Dict, Set, Tuple

from .unit import Unit


@dataclass
class Map:
    """Class to hold the map information."""
    matrix: List[List[int]]
    walls: Set = None
    open: Set = None
    units: Dict[Tuple[int, int], Unit] = None

    def init(self):
        """Initialize the walls, open spaces, and units."""
        self.walls = set()
        self.open = set()
        self.units = {}

        for y, row in enumerate(self.matrix):
            for x, val in enumerate(row):
                if val == "#":
                    self.walls.add((y, x))
                elif val == ".":
                    self.open.add((y, x))
                elif val in {"G", "E"}:
                    self.units[y, x] = Unit(val, y, x)

    def find_adjacent_squares(self, y, x):
        """Finds the adjacent squares to a coordinate in reading order."""
        return [(y - 1, x), (y, x + 1), (y, x - 1), (y + 1, x)]

    def find_adjacent_open_squares(self, y, x):
        """Finds only the open adjacent squares."""
        squares = self.find_adjacent_squares(y, x)
        return [s for s in squares if s in self.open]

    def bfs(self, starty, startx, endy, endx):
        """Breadth-first search of the game space."""
        frontier = [[(starty, startx), []]]
        visited = {(starty, startx)}

        while frontier:
            current, path = frontier.pop(0)
            if current == (endy, endx):
                return path
            for child in self.find_adjacent_open_squares(*current):
                if child not in visited:
                    frontier.append([child, path + [child]])
                    visited.add(child)
        return None
