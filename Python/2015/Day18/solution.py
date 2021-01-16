from copy import deepcopy


class Lights:
    def __init__(self, dimension, stuck_corners=False):
        self.dimension = dimension
        self.light = [False] * dimension * dimension
        self.stuck_corners = stuck_corners

    def parse_instr(self, instr):
        instr = instr.replace("\n", "")
        for n, state in enumerate(instr):
            if state == "#":
                self.turn_on_line(n)

        if self.stuck_corners:
            self.fix_corners()

    def turn_on_line(self, row_position):
        self.light[row_position] = True

    def set_pos(self, x, y, value):
        self.light[y * self.dimension + x] = value

    def fix_corners(self):
        self.set_pos(0, 0, True)
        self.set_pos(self.dimension - 1, 0, True)
        self.set_pos(0, self.dimension - 1, True)
        self.set_pos(self.dimension - 1, self.dimension - 1, True)

    def get_light(self, x, y):
        if x < 0 or x > self.dimension - 1:
            raise IndexError
        elif y < 0 or y > self.dimension - 1:
            raise IndexError
        else:
            return self.light[y * self.dimension + x]

    def get_adicent_lights(self, linear_pos):
        x = linear_pos % self.dimension
        y = int(linear_pos / self.dimension)
        adjacent = []

        for x_ad in range(x - 1, x + 2):
            for y_ad in range(y - 1, y + 2):
                try:
                    if x_ad != x or y_ad != y:
                        adjacent.append(self.get_light(x_ad, y_ad))
                except IndexError:
                    pass
        return adjacent

    def animate(self, animation_steps):
        for step in range(animation_steps):
            buffer_state = deepcopy(self.light)

            for n, light in enumerate(self.light):
                adicent = self.get_adicent_lights(n)

                if light:
                    if not (2 <= sum(self.get_adicent_lights(n)) <= 3):
                        # light turns off
                        buffer_state[n] = False
                else:
                    if sum(adicent) == 3:
                        # light turns on
                        buffer_state[n] = True

            self.light = buffer_state

            if self.stuck_corners:
                self.fix_corners()


def solve(puzzle_input):
    light_wall = Lights(100)
    light_wall.parse_instr(puzzle_input)
    light_wall.animate(100)
    print(f"solution 1: {sum(light_wall.light)}")

    light_wall = Lights(100, stuck_corners=True)
    light_wall.parse_instr(puzzle_input)
    light_wall.animate(100)
    print(f"solution 2: {sum(light_wall.light)}")
