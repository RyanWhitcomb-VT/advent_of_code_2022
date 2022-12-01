# Advent of Code 2022: Day 1

# Class for an Elf carrying items with calorie counts
class Elf:
    def __init__(self, cal_list):
        self.cal_list = cal_list
        self.tot_cal = sum(cal_list)
        self.tot_item = len(cal_list)


# Format data to a list of Elves
def create_elf_list(lines):
    class_list = []
    for line in lines:
        elf = Elf(line)
        class_list.append(elf)

    return class_list


if __name__ == '__main__':
    with open('data/input-01.txt') as f:
        puzzle_input = f.read().strip().split('\n\n')
    int_input = [[int(cal) for cal in cal_list.split('\n')] for cal_list in puzzle_input]

    elf_list = create_elf_list(int_input)

    # Part 1
    most_carried = max([elf.tot_cal for elf in elf_list])
    print(f"Part 1: {most_carried}")

    # Part 2
    top_three = sorted([elf.tot_cal for elf in elf_list])[-3:]
    print(f"Part 2: {sum(top_three)}")
