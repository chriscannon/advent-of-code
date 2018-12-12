"""
Day 7 Advent of Code
"""
import re
import sys
from collections import defaultdict


def main(filename):
    """Parses the dependencies from the file and prints the instruction order."""
    pairs = set()
    pattern = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.')
    with open(filename) as f:
        for l in f:
            pairs.add(pattern.match(l).groups())
    graph, dependencies, starts = build_graphs(pairs)
    ordered_steps = traverse_graph(graph, dependencies, starts)
    print("Part 1 the steps in order are: {}".format(ordered_steps))
    total_time = calculate_time(graph, dependencies, starts)
    print("Part 2 the total seconds with 5 workers: {}".format(total_time))


def calculate_time(graph, dependencies, starts):
    """Calculates the amount of time workers can simultaneously complete construction."""
    visited = set()
    frontier = list(starts)
    workers = {
        "1": [None, 0],
        "2": [None, 0],
        "3": [None, 0],
        "4": [None, 0],
        "5": [None, 0]
    }
    total_steps = 0
    still_work = True
    while frontier or still_work:
        frontier = sorted(set(frontier))
        for parent in frontier:
            free_worker_ids = get_free_worker_ids(workers)
            if is_dependency_met(parent, visited, dependencies) and free_worker_ids:
                workers[free_worker_ids.pop()] = [parent, ord(parent) - 64 + 60]
                if parent not in graph:
                    break
                for child in graph[parent]:
                    frontier.append(child)
        still_work = False
        for wid, w in workers.items():
            if w[0] is None:
                continue

            still_work = True
            if w[0] in frontier:
                frontier.remove(w[0])

            current_time = w[1] - 1
            if current_time == 0:
                visited.add(w[0])
                workers[wid] = [None, 0]
            else:
                workers[wid][1] = current_time

        total_steps += 1
    return total_steps - 1


def get_free_worker_ids(workers):
    """Finds the free workers."""
    free = []
    for id_, w in workers.items():
        if w[0] is None:
            free.append(id_)
    return free


def traverse_graph(graph, dependencies, starts):
    """Traverse the graph using breadth-first search."""
    visited = set()
    frontier = list(starts)
    result = []
    while frontier:
        frontier = sorted(set(frontier))
        for parent in frontier:
            if is_dependency_met(parent, visited, dependencies):
                frontier.remove(parent)
                visited.add(parent)
                result.append(parent)
                if parent not in graph:
                    break  # Last dependency
                for child in graph[parent]:
                    frontier.append(child)
                break
    return ''.join(result)


def is_dependency_met(node, visited, dependencies):
    """Determine if the current node's dependent nodes have been visited."""
    if node not in dependencies:
        return True
    if dependencies[node].issubset(visited):
        return True
    return False


def build_graphs(pairs):
    """Builds a dependency graph from the instructions and identifies the start instruction."""
    graph = defaultdict(set)
    dependencies = defaultdict(set)
    for pair in pairs:
        graph[pair[0]].add(pair[1])
        dependencies[pair[1]].add(pair[0])
    starts = {p[0] for p in pairs if p[0] not in dependencies}
    return graph, dependencies, starts


if __name__ == '__main__':
    main(sys.argv[1])
