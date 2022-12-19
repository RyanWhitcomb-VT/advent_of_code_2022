# Advent of Code: Day 17
TUNNEL_WIDTH = 7


class Rock:
    def __init__(self, shape, y):
        self.shape = shape
        self.left = 3
        self.bottom = y + 4
        self.falling = True

        if shape == 'horiz':
            self.right = self.left + 3
            self.top = self.bottom
        elif shape == 'plus':
            self.right = self.left + 2
            self.top = self.bottom + 2
        elif shape == 'back_ell':
            self.right = self.left + 2
            self.top = self.bottom + 2
        elif shape == 'vert':
            self.right = self.left
            self.top = self.bottom + 3
        elif shape == 'square':
            self.right = self.left + 1
            self.top = self.bottom + 1

    def push(self, direction):
        if direction == '>' and self.right < TUNNEL_WIDTH:
            self.left = self.left + 1
            self.right = self.right + 1
        elif direction == '<' and self.left > 1:
            self.left = self.left - 1
            self.right = self.right - 1

    def drop(self):
        self.bottom = self.bottom - 1
        self.top = self.top - 1

    def get_locs(self):
        if self.shape == 'horiz':
            return [
                (self.left, self.top),
                (self.left + 1, self.top),
                (self.left + 2, self.top),
                (self.right, self.top)
            ]
        elif self.shape == 'plus':
            return[
                (self.left, self.top - 1),
                (self.left + 1, self.top - 1),
                (self.right, self.top - 1),
                (self.left + 1, self.top),
                (self.left + 1, self.bottom)
            ]
        elif self.shape == 'back_ell':
            return [
                (self.left, self.bottom),
                (self.left + 1, self.bottom),
                (self.right, self.bottom),
                (self.right, self.top - 1),
                (self.right, self.top)
            ]
        elif self.shape == 'vert':
            return [
                (self.left, self.top),
                (self.left, self.top - 1),
                (self.left, self.top - 2),
                (self.left, self.bottom),
            ]
        elif self.shape == 'square':
            return [
                (self.left, self.top),
                (self.right, self.top),
                (self.left, self.bottom),
                (self.right, self.bottom),
            ]


def print_shapes(rock_locs):
    full_string = ""
    for y in range(max(x[1] for x in rock_locs) + 1):
        for x in range(1,8):
            if (x,y) in rock_locs:
                full_string += "#"
            else:
                full_string += "_"
        full_string += "\n"
    print(full_string)


if __name__ == "__main__":
    with open('data/input-17.txt') as f:
        puzzle_input = f.read().strip()

    height = 0
    shape_cycle = ['horiz', 'plus', 'back_ell', 'vert', 'square']
    step = 0
    rock_locs = {(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)}
    for fall in range(200):
        rock_shape = shape_cycle[fall % len(shape_cycle)]
        falling_rock = Rock(rock_shape, height)

        while falling_rock.falling:
            air = puzzle_input[step % len(puzzle_input)]
            if falling_rock.bottom > height + 1:
                falling_rock.push(air)
                falling_rock.drop()
            else:
                temp_locs = falling_rock.get_locs()
                falling_rock.push(air)
                if any(x in rock_locs for x in falling_rock.get_locs()):
                    if air == '>':
                        falling_rock.push('<')
                    else:
                        falling_rock.push('>')
                temp_locs = falling_rock.get_locs()
                falling_rock.drop()
                if any(x in rock_locs for x in falling_rock.get_locs()):
                    falling_rock.falling = False
                    height = max(falling_rock.top + 1, height)
                    rock_locs |= set(temp_locs)

            step += 1

    print(height)
