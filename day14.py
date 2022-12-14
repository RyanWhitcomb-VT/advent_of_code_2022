# Advent of Code 2022: Day 14


def draw_rock(cords_list):
    rock_list = [(cords_list[0][0], cords_list[0][1])]
    for idx, cord in enumerate(cords_list[1:]):
        end_rock = cords_list[idx]
        if cord[0] == end_rock[0]:
            min_y = min(cord[1], end_rock[1])
            max_y = max(cord[1], end_rock[1])
            for y in range(min_y, max_y + 1):
                rock_list.append((cord[0], y))
        else:
            min_x = min(cord[0], end_rock[0])
            max_x = max(cord[0], end_rock[0])
            for x in range(min_x, max_x + 1):
                rock_list.append((x, cord[1]))
    return list(set(rock_list))


def drop_sand(rocks_list, min_y):
    sand_loc = (500, 0)
    while sand_loc not in rocks_list and sand_loc[1] < min_y:
        if (sand_loc[0], sand_loc[1] + 1) not in rocks_list:
            sand_loc = (sand_loc[0], sand_loc[1] + 1)
        elif (sand_loc[0] - 1, sand_loc[1] + 1) not in rocks_list:
            sand_loc = (sand_loc[0] - 1, sand_loc[1] + 1)
        elif (sand_loc[0] + 1, sand_loc[1] + 1) not in rocks_list:
            sand_loc = (sand_loc[0] + 1, sand_loc[1] + 1)
        else:
            rocks_list.append(sand_loc)


if __name__ == '__main__':
    with open('data/test-14.txt') as f:
        puzzle_input = f.read().splitlines()

    paths = [line.split(' -> ') for line in puzzle_input]
    cords = []
    for path in paths:
        cords.append([list(map(int, pair.split(','))) for pair in path])

    rocks = []
    for rock in cords:
        rocks = rocks + draw_rock(rock)
    rocks = list(set(rocks))
    init_rocks = len(rocks)

    bottom_row = list(map(max, zip(*rocks)))[1]
    while rocks[-1][1] != bottom_row:
        drop_sand(rocks, bottom_row)

    # Part 1
    print(f"Part 1: {len(rocks) - init_rocks - 1}")

    # Part 2
    # rocks.pop()
    # floor = bottom_row + 2
    # print(floor)
    #
    # for floor_x in range(0, 1000):
    #     rocks.append((floor_x, floor))
    #
    # while temp_sand[1] != 0:
    #     rocks.append(drop_sand(rocks, floor))

    # print(f"Part 2: {len(sand)}")
