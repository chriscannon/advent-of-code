"""
Day 4 Advent of Code 2018
"""
import operator
import re
import sys
from collections import defaultdict, Counter


def main(filename):
    """Main function for counting sleeping guards."""
    ordered = {}
    with open(filename) as f:
        for line in f:
            match = re.match(r'\[([^\]]+)\] (.+)', line)
            time, status = match.groups()
            ordered[time] = status
    guards, sleep = compute_guard_and_sleep(ordered)
    print("Part 1 Strategy 1 guard # * max sleep minute: {}".format(strategy_1(guards, sleep)))
    print("Part 2 Strategy 2 most frequently asleep guard * minute: {}".format(strategy_2(sleep)))


def compute_guard_and_sleep(ordered):
    """Compute sleep minutes and guard total sleep time."""
    sleep = defaultdict(lambda: ["." for _ in range(60)])
    guards = defaultdict(int)
    guard = None
    start = None
    for key in sorted(ordered):
        status = ordered[key]
        if "#" in status:
            match = re.match(r'.+#(\d+)', status)
            guard = int(match.groups()[0])
            start = None
        elif "falls asleep" in status:
            start = int(key.split(':')[1])
        elif "wakes up" in status:
            end = int(key.split(':')[1])
            delta = end - start - 1
            guards[guard] += delta
            date = key.split(' ')[0]
            for i in range(delta + 1):
                sleep[date, guard][i + start] = "#"
    return guards, sleep


def strategy_1(guards, sleep):
    """Calculate the guard with the sleepiest minute."""
    sleepiest_guard = max(guards.items(), key=operator.itemgetter(1))[0]
    minutes = [0] * 60
    for k, v in sleep.items():
        if k[1] == sleepiest_guard:
            for i, s in enumerate(v):
                if s == "#":
                    minutes[i] += 1
    max_sleep_minute = minutes.index(max(minutes))
    return sleepiest_guard * max_sleep_minute


def strategy_2(sleep):
    """Calculate the guard that was asleep the most on the same minute."""
    sleepiest_minute = defaultdict(list)
    for k, v in sleep.items():
        for i, _ in enumerate(v):
            if v[i] == "#":
                sleepiest_minute[i].append(k[1])

    max_id = 0
    max_min = 0
    for k, v in sleepiest_minute.items():
        totals = Counter(v)
        for id_, count in totals.items():
            if count > max_min:
                max_id = id_
                max_min = k
    return max_id * max_min


if __name__ == "__main__":
    main(sys.argv[1])
