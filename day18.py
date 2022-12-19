# Advent of Code 2022: Day 18


def neighbors(cord):
    x = cord[0]
    y = cord[1]
    z = cord[2]

    return [[x-1, y, z], [x+1, y, z],
            [x, y-1, z], [x, y+1, z],
            [x, y, z-1], [x, y, z+1]]


if __name__ == '__main__':
    with open('data/input-18.txt') as f:
        puzzle_input = f.read().splitlines()

    cords_list = [list(map(int, line.split(','))) for line in puzzle_input]

    empty_sides = 0
    for cord in cords_list:
        empty_sides += len([point for point in neighbors(cord) if point not in cords_list])

    # Part 1
    print(f"Part 1: {empty_sides}")

    # Part 2
    min_x = min(x[0] for x in cords_list) - 1
    max_x = max(x[0] for x in cords_list) + 1
    min_y = min(x[1] for x in cords_list) - 1
    max_y = max(x[1] for x in cords_list) + 1
    min_z = min(x[2] for x in cords_list) - 1
    max_z = max(x[2] for x in cords_list) + 1

    outside_cubes = [[min_x, min_y, min_z]]
    visited = []
    while outside_cubes:
        this_cube = outside_cubes.pop()
        visited.append(this_cube)

        adj_cords = neighbors(this_cube)
        for test_cord in adj_cords:
            if (min_x <= test_cord[0] <= max_x) and (min_y <= test_cord[1] <= max_y) and (min_z <= test_cord[2] <= max_z):
                if test_cord not in visited and test_cord not in cords_list:
                    outside_cubes.append(test_cord)

    outside_surface = 0
    for cord in cords_list:
        outside_surface += len([neigh for neigh in neighbors(cord) if neigh in visited])

    print(f"Part 2: {outside_surface}")

