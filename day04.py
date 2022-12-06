# Advent of Code 2022: Day 4
import pandas as pd


if __name__ == '__main__':
    with open('data/input-04.txt') as f:
        puzzle_input = f.read().splitlines()

    pairs = [line.split(',') for line in puzzle_input]
    ranges = [pair[0].split('-')+pair[1].split('-') for pair in pairs]
    range_df = pd.DataFrame(ranges, columns=['elf1_min', 'elf1_max', 'elf2_min', 'elf2_max']).astype(int)

    overlap_df = range_df[
        ((range_df['elf1_min'] >= range_df['elf2_min']) & (range_df['elf1_max'] <= range_df['elf2_max'])) |
        ((range_df['elf2_min'] >= range_df['elf1_min']) & (range_df['elf2_max'] <= range_df['elf1_max']))
    ]

    # Part 1
    print(f"Part 1: {len(overlap_df)}")

    # Part 2
    overlap_df_2 = range_df[
        ((range_df['elf1_max'] >= range_df['elf2_min']) & (range_df['elf1_max'] <= range_df['elf2_max'])) |
        ((range_df['elf2_max'] >= range_df['elf1_min']) & (range_df['elf2_max'] <= range_df['elf1_max']))
    ]
    print(f"Part 2: {len(overlap_df_2)}")