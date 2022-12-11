# Advent of Code 2022: Day 9


def parse_inst(instruction, x_loc, y_loc):
    direction = instruction.split(' ')[0]
    velocity = int(instruction.split(' ')[1])
    if direction == 'R':
        x_loc += velocity
    elif direction == 'L':
        x_loc -= velocity
    elif direction == 'U':
        y_loc += velocity
    else:
        y_loc -= velocity

    return x_loc, y_loc


def check_tail(h_x, h_y, t_x, t_y):
    tail_pos = []

    diff_x = h_x - t_x
    diff_y = h_y - t_y

    if diff_x > 1 and diff_y > 1:
        print("BIG", diff_x, diff_y)
        for x_step in range(1, abs(diff_x)):
            for y_step in range(1, abs(diff_y)):
                print(diff_x, diff_y)
                t_x = t_x + (diff_x / abs(diff_x))
                t_y = t_y + (diff_y / abs(diff_y))
                tail_pos.append((t_x, int(t_y)))
    elif abs(diff_x) > 1:
        for x_step in range(1, abs(diff_x)):
            t_x = t_x + (diff_x/abs(diff_x))
            t_y = h_y
            tail_pos.append((int(t_x), t_y))
    elif abs(diff_y) > 1:
        for y_step in range(1, abs(diff_y)):
            t_y = t_y + (diff_y / abs(diff_y))
            t_x = h_x
            tail_pos.append((t_x, int(t_y)))

    return int(t_x), int(t_y), tail_pos


if __name__ == '__main__':
    with open('data/test-09-2.txt') as f:
        puzzle_input = f.read().splitlines()

    head_x = 2000
    head_y = 2000
    k1_x = 2000
    k1_y = 2000
    k2_x = 2000
    k2_y = 2000
    k3_x = 2000
    k3_y = 2000
    k4_x = 2000
    k4_y = 2000
    k5_x = 2000
    k5_y = 2000
    k6_x = 2000
    k6_y = 2000
    k7_x = 2000
    k7_y = 2000
    k8_x = 2000
    k8_y = 2000
    k9_x = 2000
    k9_y = 2000
    tail_loc_p1 = [(k2_x, k2_y)]
    tail_loc_p2 = [(k9_x, k9_y)]
    for inst in puzzle_input:
        print(inst)
        head_x, head_y = parse_inst(inst, head_x, head_y)
        k2_x, k2_y, updated_tail_p1 = check_tail(head_x, head_y, k2_x, k2_y)
        k3_x, k3_y, _ = check_tail(k2_x, k2_y, k3_x, k3_y)
        k4_x, k4_y, _ = check_tail(k3_x, k3_y, k4_x, k4_y)
        k5_x, k5_y, _ = check_tail(k4_x, k4_y, k5_x, k5_y)
        k6_x, k6_y, _ = check_tail(k5_x, k5_y, k6_x, k6_y)
        k7_x, k7_y, _ = check_tail(k6_x, k6_y, k7_x, k7_y)
        k8_x, k8_y, _ = check_tail(k7_x, k7_y, k8_x, k8_y)
        k9_x, k9_y, updated_tail_p2 = check_tail(k8_x, k8_y, k9_x, k9_y)
        tail_loc_p1 = tail_loc_p1 + updated_tail_p1
        tail_loc_p2 = tail_loc_p2 + updated_tail_p2

    # Part 1
    print(f"Part 1: {len(set(tail_loc_p1))}")

    # Part 2
    print(f"Part 2: {len(set(tail_loc_p2))}")
