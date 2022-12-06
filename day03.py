# Advent of Code 2022: Day 3
import pandas as pd


def split_lines(rucksack):
    rucksack_split = int(len(rucksack)/2)
    rucksack_tuple = (rucksack[:rucksack_split], rucksack[rucksack_split:])
    return rucksack_tuple


def map_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


if __name__ == '__main__':
    with open('data/input-03.txt') as f:
        puzzle_input = f.read().splitlines()

    compartments = [split_lines(sack) for sack in puzzle_input]
    common_item = [set.intersection(set(comp[0]), set(comp[1])) for comp in compartments]
    priorities = [map_priority(list(item)[0]) for item in common_item]

    # Part 1
    print(f'Part 1: {sum(priorities)}')

    # Part 2
    group_indices = range(len(puzzle_input))[::3]
    group_badges = [set.intersection(
        set(puzzle_input[idx]), set(puzzle_input[idx+1]), set(puzzle_input[idx+2])
    ) for idx in group_indices]
    group_priorities = [map_priority(list(badge)[0]) for badge in group_badges]

    print(f'Part 2: {sum(group_priorities)}')

