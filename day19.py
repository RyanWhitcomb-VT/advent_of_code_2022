# Advent of Code 2022: Day 19


def optimized_produce(active_robots, active_resources):

    return active_robots, active_resources


if __name__ == "__main__":
    with open('data/test-19.txt') as f:
        puzzle_input = f.read().splitlines()

    blueprint_dict = {}
    for line in puzzle_input:
        robot_dict = {}
        for robot_blueprint in line.split(':')[1].strip().split('. '):
            robot_type = robot_blueprint.split(' ')[1]
            if robot_type in ['ore', 'clay']:
                robot_dict[robot_type] = {robot_blueprint.split(' ')[-1]: int(robot_blueprint.split(' ')[-2])}
            else:
                robot_dict[robot_type] = {robot_blueprint.split(' ')[-1]: int(robot_blueprint.split(' ')[-2]),
                                          robot_blueprint.split(' ')[-4]: int(robot_blueprint.split(' ')[-5])}
        blueprint_dict[int(line.split(' ')[1].strip(':'))] = robot_dict

    for blueprint in blueprint_dict.keys():
        current_robots = {'ore': 1}
        current_resources = {
            'ore': 0,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }

        for time in range(24):
            current_robots, current_resources = optimized_produce(current_robots, current_resources)
            for prod_robot in current_robots.keys():
                current_resources[prod_robot] += current_robots[prod_robot]
