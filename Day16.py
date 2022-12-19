# Advent of Code 2022: Day 16
import re


def get_current_pressure(val_list, val_dict):
    curr_pressure = 0
    for val in val_list:
        curr_pressure += val_dict[val]['flow_rate']

    return curr_pressure


if __name__ == "__main__":
    with open('data/test-16.txt') as f:
        puzzle_input = f.read().splitlines()

    valve_dict = {}
    for line in puzzle_input:
        source_valve = line.split(' ')[1]
        flow_rate = int(re.findall("=(\d*)", line)[0])
        tunnel_valves = line.replace(',', '').split(' ')[9:]
        valve_dict[source_valve] = {'flow_rate': flow_rate, 'tunnel_valves': tunnel_valves}

    pressure = 0
    open_valves = []
    priority = ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']
    for t in range(30):
        pressure += get_current_pressure(open_valves, valve_dict)


