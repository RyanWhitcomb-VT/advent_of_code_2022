# Advent of Code 2022: Day 6


def is_unique(substr):
    return len(set(substr)) == len(substr)


def find_marker(signal, length):
    for idx in range(len(signal)):
        if is_unique(signal[idx:idx+length]):
            return idx+length


if __name__ == '__main__':
    with open('data/input-06.txt') as f:
        puzzle_input = f.read()

    # Part 1
    print(find_marker(puzzle_input, 4))

    # Part 2
    print(find_marker(puzzle_input, 14))



