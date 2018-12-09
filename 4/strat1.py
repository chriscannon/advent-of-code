"""
Watch Satna's sleeping guards.
"""
import sys
import re
from collections import defaultdict
import operator


def main(filename):
    """Main function for counting sleeping guards."""
    ordered = {}
    with open(filename, 'r') as fopen:
        for line in fopen:
            match = re.match(r'\[([^\]]+)\] (.+)', line)
            time, status = match.groups()
            ordered[time] = status

    sleep = defaultdict(lambda: ["." for x in range(60)])
    guards = defaultdict(int)
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
            guards[guard] += delta
            date = key.split(' ')[0]
            for i in range(delta+1):
                sleep[date, guard][i+start] = "#"

    sleepiest_guard = max(guards.items(), key=operator.itemgetter(1))[0]
    print("Guard that slept the most: {}".format(sleepiest_guard))
    minutes = [0 for x in range(60)]
    for k, v in sleep.items():
        if k[1] == sleepiest_guard:
            for i, s in enumerate(v):
                if s == "#":
                    minutes[i] += 1
    max_sleep_minute = minutes.index(max(minutes))
    print("Maximum sleep minute: {}".format(minutes.index(max(minutes))))
    print("Guard # * Max Sleep Minute: {}".format(sleepiest_guard * max_sleep_minute))


if __name__ == "__main__":
    main(sys.argv[1])
