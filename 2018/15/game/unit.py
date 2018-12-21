from dataclasses import dataclass


@dataclass
class Unit:
    """Class to hold attributes about the unit (elf or goblin)."""
    type_: str
    y: int
    x: int
    hp: int = 200
    attack: int = 3
    is_dead: bool = False

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

    def _get_target_type(self):
        """Return the opposite type which is a target."""
        return "E" if self.type_ == "G" else "G"

    def find_targets(self, map_):
        """Finds the units of the opposite type which are the targets."""
        return [t for t in map_.units.values() if t.type_ == self._get_target_type() and not t.is_dead]

    def find_first_adjacent_target(self, map_, targets):
        """Finds the first adjacent target with the lowest health."""
        adjacent = map_.find_adjacent_squares(self.y, self.x)
        in_range = [t for t in targets if (t.y, t.x) in adjacent]

        if not in_range:
            return None

        min_hp = min([t.hp for t in in_range])
        return sorted([t for t in in_range if t.hp == min_hp])[0]
