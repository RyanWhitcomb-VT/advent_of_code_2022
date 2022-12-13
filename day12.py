# Advent of Code 2022: Day 12
import collections


def step(cur_pos, new_pos, elev, visit_set, pos_loc):
    new_x = new_pos[0]
    new_y = new_pos[1]
    cur_dist = cur_pos[2]

    if (0 <= new_y < len(elev)) and (0 <= new_x < len(elev[new_y])):
        if elev[new_y][new_x] - elev[cur_pos[1]][cur_pos[0]] <= 1:
            valid_loc = (new_x, new_y, cur_dist+1)
            pos_loc.append(valid_loc)
            visit_set.add(valid_loc[:2])
    return


if __name__ == '__main__':
    with open('data/input-12.txt') as f:
        puzzle_input = f.read().splitlines()

    elevation = [[ord(char) for char in line] for line in puzzle_input]
    current_position, end = 0, 0
    for row, line in enumerate(elevation):
        if ord('S') in line:
            current_position = (line.index(ord('S')), row, 0)
            elevation[row][line.index(ord('S'))] = ord('a')
        if ord('E') in line:
            end = (line.index(ord('E')), row, 0)
            elevation[row][line.index(ord('E'))] = ord('z')

    possible_locations = collections.deque()
    # Loop for part 2
    for j in range(len(elevation)):
        for i in range(len(elevation[j])):
            if elevation[j][i] == ord('a'):
                possible_locations.append((i, j, 0))

    visited = {current_position[:2]}
    while current_position[:2] != end[:2]:
        x = current_position[0]
        y = current_position[1]
        if (x + 1, y) not in visited:
            step(current_position, (x + 1, y), elevation, visited, possible_locations)
        if (x, y + 1) not in visited:
            step(current_position, (x, y + 1), elevation, visited, possible_locations)
        if (x - 1, y) not in visited:
            step(current_position, (x - 1, y), elevation, visited, possible_locations)
        if (x, y - 1) not in visited:
            step(current_position, (x, y - 1), elevation, visited, possible_locations)

        current_position = possible_locations.popleft()

    # Part 1
    print(f"{current_position[2]}")


