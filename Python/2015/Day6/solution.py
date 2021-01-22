import re

pos_regex = re.compile(r"\d{1,},\d{1,}")

TOOGLE = "toggle"
ON = "turn on"
OFF = "turn off"


class Lights:
    def __init__(self, bin=True):
        self.light = [0] * 1000 * 1000
        self.bin = bin

    @property
    def brightness(self):
        return sum(self.light)

    def actuate(self, start: [int, int], end: [int, int], action: str):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if action == TOOGLE and self.bin:
                    self.light[x + y * 1000] = abs(self.light[x + y * 1000] - 1)
                elif action == ON and self.bin:
                    self.light[x + y * 1000] = 1
                elif action == OFF and self.bin:
                    self.light[x + y * 1000] = 0
                if action == TOOGLE and not self.bin:
                    self.light[x + y * 1000] += 2
                elif action == ON and not self.bin:
                    self.light[x + y * 1000] += 1
                elif action == OFF and not self.bin:
                    self.light[x + y * 1000] -= 1 if self.light[x + y * 1000] > 0 else 0


def parse_line(line):
    pos = []
    for n in pos_regex.findall(line):
        x, y = n.split(",")
        pos.append([int(x), int(y)])

    for n in [TOOGLE, OFF, ON]:
        if n in line:
            return pos + [n]


def solution_1(puzzle_input):
    deko = Lights()
    for n, line in enumerate([n for n in puzzle_input.split("\n") if n != ""]):
        deko.actuate(*parse_line(line))
    return deko.brightness


def solution_2(puzzle_input):
    deko = Lights(bin=False)
    for n, line in enumerate([n for n in puzzle_input.split("\n") if n != ""]):
        deko.actuate(*parse_line(line))
    return deko.brightness
