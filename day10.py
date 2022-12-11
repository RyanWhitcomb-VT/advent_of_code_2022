# ADvent of Code 2022: Day 10


def draw_crt(signal_list):
    sprite_pos = signal_list[0]
    sprite_loc = [sprite_pos-1, sprite_pos, sprite_pos+1]

    crt_output = []
    for idx, signal_val in enumerate(signal_list[1:]):
        if idx == 0:
            continue
        if idx % 40 in sprite_loc:
            crt_output.append('#')
        else:
            crt_output.append('.')
        sprite_pos = signal_val
        sprite_loc = [sprite_pos - 1, sprite_pos, sprite_pos + 1]

        if idx % 40 == 0 and idx != 0:
            crt_output.append('\n')

    # for idx in [40, 80, 120, 160, 200]:
    #     crt_output.insert(idx, '\n')

    return crt_output


if __name__ == '__main__':
    with open('data/input-10.txt') as f:
        puzzle_input = f.read().splitlines()

    signal = 1
    cycles = [signal]
    for line in puzzle_input:
        if line == 'noop':
            cycles.append(signal)
        else:
            v = int(line.split(' ')[1])
            cycles.append(signal)
            cycles.append(signal + v)
            signal += v

    signal_samples = [20, 60, 100, 140, 180, 220]
    signal_strength = 0
    for sample in signal_samples:
        sample_strength = sample * cycles[sample - 1]
        signal_strength += sample_strength

    # Part 1
    print(f"Part 1: {signal_strength}")

    # Part 2
    crt_display = draw_crt(cycles)
    decoded_string = bytes(''.join(crt_display), "utf-8").decode("unicode_escape")
    print(decoded_string)
