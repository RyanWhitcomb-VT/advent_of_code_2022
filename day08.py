# Advent of Code 2022: Day 8


def count_visible(height, tree_list):
    visibility = 0
    for test_tree in tree_list:
        if height > test_tree:
            visibility += 1
        else:
            return visibility + 1
    return visibility


def is_visible(grid, x, y):
    tree = int(grid[y][x])
    column = [row[x] for row in grid]

    if x == 0:
        west = []
    else:
        west = [int(plot) for plot in grid[y][:x]]

    if y == 0:
        north = []
    else:
        north = [int(plot) for plot in column[:y]]

    if x == len(grid[0]):
        east = []
    else:
        east = [int(plot) for plot in grid[y][x + 1:]]

    if y == len(grid):
        south = []
    else:
        south = [int(plot) for plot in column[y+1:]]

    north_vis = count_visible(tree, north[::-1])
    south_vis = count_visible(tree, south)
    east_vis = count_visible(tree, east)
    west_vis = count_visible(tree, west[::-1])

    north.append(0)
    south.append(0)
    east.append(0)
    west.append(0)

    if tree > max(north) or tree > max(south) or tree > max(west) or tree > max(east):
        return north_vis * south_vis * east_vis * west_vis
    else:
        return 0


if __name__ == '__main__':
    with open('data/input-08.txt') as f:
        puzzle_input = f.read().splitlines()

    visible_trees = 0
    scenic_score = 0
    for x_pos in range(0, len(puzzle_input[0])):
        for y_pos in range(0, len(puzzle_input)):
            this_scenic_score = is_visible(puzzle_input, x_pos, y_pos)
            if this_scenic_score > 0:
                visible_trees += 1
            if this_scenic_score > scenic_score:
                scenic_score = this_scenic_score

    # Part 1
    print(f"Part 1: {visible_trees}")

    # Part 2
    print(f"Part 2: {scenic_score}")