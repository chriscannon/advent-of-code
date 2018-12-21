"""
Day 15 Advent of Code 2018

Close, but no cigar on this one. I have all the samples working, but the
actual input does not produce the correct round and summed hit point score.
"""
import sys

from game.map import Map


def main(filename):
    """Parse the input file and output the results."""
    with open(filename) as f:
        map_ = [list(l) for l in f.read().splitlines()]
    map_ = Map(map_)
    map_.init()
    print("Initial")
    show_map(map_)
    round_ = 0
    while True:
        round_ += 1
        if not start_round(map_):
            break
        print(f"Finished Round {round_}")
        show_map(map_)
    show_map(map_)
    total_hp = sum([u.hp for u in map_.units.values() if not u.is_dead])
    round_ -= 1
    print(f"Rounds {round_}, Total HP: {total_hp}, Outcome: {round * total_hp}")


def start_round(map_):
    """Start a new round of combat."""
    for (y, x), unit in sorted(map_.units.items()):
        if unit.is_dead:
            continue
        targets = unit.find_targets(map_)
        if not targets:
            print("Game over!")
            return False

        if not attack(map_, unit, targets):
            show_map(map_)
            path = get_attack_path(targets, map_, y, x)
            if path is None:
                continue
            move_unit(map_, unit, *path)
            targets = unit.find_targets(map_)
            attack(map_, unit, targets)

    dead_units = [loc for loc, unit in map_.units.items() if unit.is_dead]
    for loc in dead_units:
        del map_.units[loc]

    return True


def attack(map_, unit, targets):
    """Attacks a target on the map."""
    attack_target = unit.find_first_adjacent_target(map_, targets)
    if attack_target is None:
        return False

    attack_target.hp -= unit.attack

    if attack_target.hp <= 0:
        attack_target.is_dead = True
        map_.open.add((attack_target.y, attack_target.x))
        map_.matrix[attack_target.y][attack_target.x] = "."
    return True


def show_map(map_):
    """Prints the map to stdout."""
    for r in map_.matrix:
        print(''.join(r))
    print()


def move_unit(map_, unit, dy, dx):
    """Moves the unit to the new location."""
    # Modify open spaces
    map_.open.remove((dy, dx))
    map_.matrix[unit.y][unit.x] = "."
    map_.open.add((unit.y, unit.x))

    # Modify units
    map_.matrix[dy][dx] = unit.type_
    del map_.units[unit.y, unit.x]
    unit.y = dy
    unit.x = dx
    map_.units[dy, dx] = unit
    return map_


def get_attack_path(targets, map_, y, x):
    """Gets the minimum distance path to the target."""
    target_path = {}
    for t in targets:
        adjacent = map_.find_adjacent_open_squares(t.y, t.x)
        paths = []
        for (dy, dx) in adjacent:
            path = map_.bfs(y, x, dy, dx)
            if path is not None:
                paths.append(path)
        if not paths:
            continue
        target_path[dy, dx] = (t, min(paths, key=len))
    if not target_path:
        return None, None
    min_len = min([len(p[1]) for p in target_path.values()])
    min_paths = {k: v for (k, v) in target_path.items() if len(v[1]) == min_len}
    for k, v in sorted(min_paths.items()):
        return v[1][0]


if __name__ == '__main__':
    main(sys.argv[1])
