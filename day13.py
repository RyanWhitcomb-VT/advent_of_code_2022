# Advent of Code 2022: Day 13
from itertools import chain


def comp_item(left, right):
    if type(left) != type(right):
        if type(left) == int:
            left = [left]
        else:
            right = [right]

    if type(left) == int:
        if left != right:
            return left - right
        else:
            return 0
    else:
        for l, r in zip(left, right):
            diff = comp_item(l, r)
            if diff:
                return diff
        return len(left) - len(right)


if __name__ == '__main__':
    with open('data/input-13.txt') as f:
        puzzle_input = [list(map(eval, pair.split())) for pair in f.read().split('\n\n')]

    valid_indices = []
    for idx, packets in enumerate(puzzle_input):
        if comp_item(packets[0], packets[1]) < 0:
            valid_indices.append(idx + 1)

    # Part 1:
    print(f"Part 1: {sum(valid_indices)}")

    # Part 2:
    flat_input = list(chain.from_iterable(puzzle_input))
    low_packets = 0
    med_packets = 0
    for packet in flat_input:
        if comp_item(packet, [[2]]) < 0:
            low_packets += 1
        elif comp_item(packet, [[6]]) < 0:
            med_packets += 1

    low_div = low_packets + 1
    high_div = low_packets + med_packets + 2
    print(f"Part 2: {low_div * high_div}")
