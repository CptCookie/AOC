from Year2019.IntCode import IntCodeCPU


def parse_input(aoc_input: str) -> list[int]:
    return [int(n) for n in aoc_input.split(",") if n != ""]


def solution_1(aoc_input: str):
    instr = parse_input(aoc_input)
    cpu = IntCodeCPU(instr)
    cpu.input.append(1)
    cpu.run_program()

    if len(cpu.output) > 1:
        raise ValueError("Program did not run correctly")

    return cpu.output.pop()


def solution_2(aoc_input: str):
    instr = parse_input(aoc_input)
    cpu = IntCodeCPU(instr)
    cpu.input.append(2)
    cpu.run_program()

    return cpu.output.pop()
