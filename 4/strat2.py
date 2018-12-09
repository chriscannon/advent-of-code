"""
Watch Satna's sleeping guards.
"""
import sys
import re
from collections import defaultdict, Counter


def main(filename):
    """Main function for counting sleeping guards."""
    ordered = {}
    with open(filename, 'r') as fopen:
        for line in fopen:
            match = re.match(r'\[([^\]]+)\] (.+)', line)
            time, status = match.groups()
            ordered[time] = status

    sleep = defaultdict(lambda: ["." for x in range(60)])
    guard = None
    start = None
    end = None
    for key in sorted(ordered):
        status = ordered[key]
        if "#" in status:
            match = re.match(r'.+#(\d+)', status)
            guard = int(match.groups()[0])
            start = None
            end = None
        elif "falls asleep" in status:
            start = int(key.split(':')[1])
        elif "wakes up" in status:
            end = int(key.split(':')[1])
            delta = end - start - 1
            date = key.split(' ')[0]
            for i in range(delta+1):
                sleep[date, guard][i+start] = "#"

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
    print("Guard ID: {}".format(max_id))
    print("Minute: {}".format(max_min))
    print("Guard ID * Minute: {}".format(max_id * max_min))


if __name__ == "__main__":
    main(sys.argv[1])
