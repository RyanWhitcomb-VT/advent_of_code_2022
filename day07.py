# Advent of Code 2022: Day 7
import re


def parse_directory(dir_text):
    dir_info_dict = {}
    prefix = []
    for line in input_lines:
        if line.startswith('$ cd'):
            if '..' in line:
                prefix.pop()
            else:
                prefix.append(line.split(' ')[-1])
        elif line.startswith('$ ls'):
            dir_name = f"/{'/'.join(prefix[1:])}"
            dir_info_dict[dir_name] = {'sub_dirs': [], 'file_sizes': 0}
        elif line.startswith('dir'):
            if dir_name != '/':
                sub_dir_name = '/'.join([dir_name, line.split(' ')[1]])
            else:
                sub_dir_name = f"{dir_name}{line.split(' ')[1]}"
            dir_info_dict[dir_name]['sub_dirs'].append(sub_dir_name)
        else:
            dir_info_dict[dir_name]['file_sizes'] += int(line.split(' ')[0])

    return dir_info_dict


def full_size(info_dict, full_info_dict):
    info_dict['full_size'] = info_dict['file_sizes']
    if not info_dict['sub_dirs']:
        return info_dict
    else:
        for subdir in info_dict['sub_dirs']:
            try:
                info_dict['full_size'] = info_dict['full_size'] + full_info_dict[subdir]['full_size']
            except KeyError:
                info_dict['full_size'] = \
                    info_dict['full_size'] + full_size(full_info_dict[subdir], full_info_dict)['full_size']
    return info_dict


if __name__ == '__main__':
    with open('data/input-07.txt') as f:
        puzzle_input = f.read()
    input_lines = puzzle_input.splitlines()

    dir_dict = parse_directory(input_lines)
    for key in list(dir_dict.keys()):
        full_size(dir_dict[key], dir_dict)

    # Part 1
    small_dict_total = 0
    for dir_key, dir_values in dir_dict.items():
        dir_full_size = dir_values['full_size']
        if dir_full_size <= 100000:
            small_dict_total += dir_full_size
    print(small_dict_total)

    # Part 2
    total_space = 70000000
    available_space = total_space - dir_dict['/']['full_size']
    needed_space = 30000000 - available_space

    min_file = []
    for dir_key, dir_values in dir_dict.items():
        dir_full_size = dir_values['full_size']
        if dir_full_size >= needed_space:
            min_file.append(dir_full_size)
    print(min(min_file))
