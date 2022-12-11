# Advent of Code: Day 11
import operator

OPS = {
    '+' : operator.add,
    '*' : operator.mul
}


def parse_monkey(monkey_input):
    monkey_output = {int(monkey_input[0][-2]):
                         {'starting_items': [int(item) for item in monkey_input[1].strip().replace(',', '').split(' ')[2:]],
                             'operation': monkey_input[2].strip().split(' ')[1:],
                             'test': int(monkey_input[3].split(' ')[-1]),
                             'if_true': int(monkey_input[4].split(' ')[-1]),
                             'if_false': int(monkey_input[5].split(' ')[-1]),
                             'items_inspected': 0}
                     }

    return monkey_output


def inspect_item(monkey_items, worried, mod_val):
    inspection_list = []
    for item in monkey_items['starting_items']:
        ops_vals = monkey_items['operation']
        try:
            operation = OPS[ops_vals[-2]](item, int(ops_vals[-1]))
        except ValueError:
            operation = OPS[ops_vals[-2]](item, item)

        # For part 2 shenanigans
        if worried:
            bored_val = int(operation/3)
        else:
            bored_val = operation % mod_val

        if bored_val % monkey_items['test'] == 0:
            toss_monkey = monkey_items['if_true']
        else:
            toss_monkey = monkey_items['if_false']

        # print(item, operation, bored_val, monkey_items['test'], toss_monkey)
        inspection_list.append((toss_monkey, bored_val))
        monkey_items['items_inspected'] += 1

    monkey_items['starting_items'] = []
    return inspection_list


if __name__ == '__main__':
    with open('data/input-11.txt') as f:
        puzzle_input = f.read()

    monkey_inputs = [puzzle.splitlines() for puzzle in puzzle_input.split('\n\n')]
    monkey_dict = {}
    for monkey_info in monkey_inputs:
        monkey_dict.update(parse_monkey(monkey_info))

    # for round_num in range(20):
    #     for monkey_num in monkey_dict.keys():
    #         toss_results = inspect_item(monkey_dict[monkey_num], worried=True)
    #         for toss in toss_results:
    #             monkey_dict[toss[0]]['starting_items'].append(toss[1])
    #
    # # Part 1
    # final_list = sorted([monkey_dict[key]['items_inspected'] for key in monkey_dict.keys()])
    # print(f"Part 1: {final_list[-2] * final_list[-1]}")

    # Part 2
    modulo = 1
    mod_vals = [monkey_dict[key]['test'] for key in monkey_dict.keys()]
    for mod in mod_vals:
        modulo *= mod

    for round_num in range(10000):
        for monkey_num in monkey_dict.keys():
            toss_results = inspect_item(monkey_dict[monkey_num], worried=False, mod_val=modulo)
            for toss in toss_results:
                monkey_dict[toss[0]]['starting_items'].append(toss[1])

    final_list = sorted([monkey_dict[key]['items_inspected'] for key in monkey_dict.keys()])
    print(f"Part 2: {final_list[-2] * final_list[-1]}")
