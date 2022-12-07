# Advent of Code 2022: Day 5
import re


def parse_instructions(instruction):
    m = re.search("move (.+?) from (.+?) to (.+?)", instruction)
    if m:
        return int(m[1]), int(m[2]), int(m[3])


def parse_stacks(stack_text):
    stack_num = int(stack_text[-1].strip()[-1])
    col_iterator = 1
    stack_list = []
    for idx in range(stack_num):
        stack_list.append([col[col_iterator] for col in stack_text[:-1][::-1] if col[col_iterator] != ' '])
        col_iterator += 4
    return stack_list


def move_stacks_9000(stack_list, ins_list):
    output_list = stack_list
    for ins in ins_list:
        amt = ins[0]
        src = ins[1] - 1
        tar = ins[2] - 1

        output_list[tar] = output_list[tar] + output_list[src][-amt:][::-1]
        output_list[src] = output_list[src][:-amt]
    return output_list


def move_stacks_9001(stack_list, ins_list):
    output_list = stack_list
    for ins in ins_list:
        amt = ins[0]
        src = ins[1] - 1
        tar = ins[2] - 1

        output_list[tar] = output_list[tar] + output_list[src][-amt:]
        output_list[src] = output_list[src][:-amt]
    return output_list


if __name__ == '__main__':
    with open('data/input-05.txt') as f:
        puzzle_input = f.read().splitlines()

    ins_index = puzzle_input.index('')
    instructions = puzzle_input[ins_index+1:]
    ins_values = [parse_instructions(ins) for ins in instructions]
    stacks = parse_stacks(puzzle_input[:ins_index])
    new_stacks = move_stacks_9000(stacks, ins_values)

    # Part 1
    print(f"New Stacks: {new_stacks}")
    print(f"Part 1: {''.join([stack[-1] for stack in new_stacks])}")

    # Part 2
    part2_stacks = parse_stacks(puzzle_input[:ins_index])
    part2_new_stacks = move_stacks_9001(part2_stacks, ins_values)
    print(f"Part 2: {''.join([stack[-1] for stack in part2_new_stacks])}")
