# Advent of Code 2022: Day 2
import pandas as pd


def map_my_input(col):
    my_map = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    mapped_col = col.map(my_map)

    return mapped_col


def compare_hands(opp_col, my_col):
    if opp_col == my_col:
        return 3
    elif (opp_col == 'A' and my_col =='B') or (opp_col == 'B' and my_col =='C') or (opp_col == 'C' and my_col =='A'):
        return 6
    else:
        return 0


def map_shape(col):
    shape_map = {
        'A':1,
        'B':2,
        'C':3
    }
    mapped_col = col.map(shape_map)

    return mapped_col


def outcome_selection(opp_col, outcome_col):
    if outcome_col == 'Y':
        return opp_col
    elif outcome_col == 'X':
        if opp_col == 'A':
            return 'C'
        elif opp_col == 'B':
            return 'A'
        else:
            return 'B'
    else:
        if opp_col == 'A':
            return 'B'
        elif opp_col == 'B':
            return 'C'
        else:
            return 'A'


if __name__ == '__main__':
    with open('data/input-02.txt') as f:
        puzzle_input = f.readlines()

    opponent_input = [pair.strip().split(' ')[0] for pair in puzzle_input]
    my_input = [pair.strip().split(' ')[1] for pair in puzzle_input]
    puzzle_df = pd.DataFrame({'opponent':opponent_input, 'me':my_input})

    # Part 1
    puzzle_df['me_mapped'] = map_my_input(puzzle_df['me'])
    puzzle_df['win'] = puzzle_df.apply(lambda x: compare_hands(x['opponent'], x['me_mapped']), axis=1)
    puzzle_df['shape_points'] = map_shape(puzzle_df['me_mapped'])
    puzzle_df['round_score'] = puzzle_df['win'] + puzzle_df['shape_points']

    print(f"Total score: {puzzle_df['round_score'].sum()}")

    # Part 2
    part_2_df = pd.DataFrame({'opponent': opponent_input, 'outcome':my_input})
    part_2_df['me'] = part_2_df.apply(lambda x: outcome_selection(x['opponent'], x['outcome']), axis=1)
    part_2_df['win'] = part_2_df.apply(lambda x: compare_hands(x['opponent'], x['me']), axis=1)
    part_2_df['shape_points'] = map_shape(part_2_df['me'])
    part_2_df['round_score'] = part_2_df['win'] + part_2_df['shape_points']

    print(f"Part 2 Score: {part_2_df['round_score'].sum()}")



