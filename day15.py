# Advent of Code: Day 15
import re
import numpy as np


def get_l1_norm(sen, bec):
    sen_array = np.array([sen.real, sen.imag])
    bec_array = np.array([bec.real, bec.imag])
    dist = np.linalg.norm(sen_array - bec_array, ord=1)

    return dist


if __name__ == '__main__':
    with open('data/input-15.txt') as f:
        puzzle_input = f.read().splitlines()

    no_beacon = []
    beacon_count = set()
    row_num = 2_000_000
    for line in puzzle_input:
        matches = re.findall("\=(\-?\d*)", line)
        sensor = complex(int(matches[0]), int(matches[1]))
        beacon = complex(int(matches[2]), int(matches[3]))
        if beacon.imag == row_num:
            beacon_count.add(beacon.real)
        man_dist = get_l1_norm(sensor, beacon)

        if (sensor - complex(0, man_dist)).imag < row_num < (sensor + complex(0, man_dist)).imag:
            width = int(man_dist - abs(row_num - sensor.imag))
            no_beacon = no_beacon + list(range(int(sensor.real) - width, int(sensor.real) + width + 1))

    # Part 1
    print(f"Part 1: {len(set(no_beacon)) - len(beacon_count)}")
