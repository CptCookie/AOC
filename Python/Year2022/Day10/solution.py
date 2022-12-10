def parse_data(puzzle_input: str) -> list[str]:
    return [n.split(" ") for n in puzzle_input.splitlines() if n != ""]


def calc_timeline(instr):
    register = [1]
    for i in instr:
        if i[0] == "noop":
            register.append(register[-1])
        elif i[0] == "addx":
            register.append(register[-1])
            register.append(register[-1] + int(i[1]))
        else:
            raise AttributeError("Unknown op code")
    return register


def get_cycle_signal(timeline, cycle):
    return timeline[cycle - 1] * cycle


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    timeline = calc_timeline(data)
    signal = [get_cycle_signal(timeline, i) for i in [20, 60, 100, 140, 180, 220]]
    return sum(signal)


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    timeline = calc_timeline(data)

    display = ["\n"]
    for y in range(6):
        for x in range(40):
            if x - 1 <= timeline[x + y * 40] <= x + 1:
                display.append("#")
            else:
                display.append(" ")
        display.append("\n")

    return "".join(display)
