from collections import defaultdict

from Year2019.IntCode import IntCodeCPU, StopOperation

MOVES = [(0, -1), (1, 0), (0, 1), (-1, 0)]

WHITE = 1
BLACK = 0


def parse_input(aoc_input: str) -> list[int]:
    return [int(n) for n in aoc_input.split(",") if n != "\n"]


def drive_bot(instr, inital_color):
    cpu = IntCodeCPU(instr)
    plane = defaultdict(lambda: 0)
    pos = (0, 0)
    plane[pos] = inital_color
    orient = 0

    try:
        while True:
            cpu.input = [plane[pos]]

            while len(cpu.output) < 2:
                cpu.run_command()

            new_color, turn = cpu.output
            cpu.output = []
            plane[pos] = new_color

            if turn == 0:
                orient = (4 + orient - 1) % 4
            else:
                orient = (orient + 1) % 4

            pos = (pos[0] + MOVES[orient][0], pos[1] + MOVES[orient][1])
    except StopOperation:
        return plane


def solution_1(aoc_input: str):
    instr = parse_input(aoc_input)
    plane = drive_bot(instr, BLACK)
    return len(plane)


def solution_2(aoc_input: str):
    instr = parse_input(aoc_input)
    plane = drive_bot(instr, WHITE)
    xs = [k[0] for k in plane.keys()]
    ys = [k[1] for k in plane.keys()]

    for y in range(min(ys), max(ys) + 1):
        line = ""
        for x in range(min(xs), max(xs) + 1):
            if plane[(x, y)] == 1:
                line += "\u2588"
            else:
                line += "\u2007"
        print(line)
