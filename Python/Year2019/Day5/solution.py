from Year2019.IntCode import IntCodeCPU


def solution_1(puzzle_input):
    instructions = [int(x) for x in puzzle_input.split(",") if x != ""]
    programm = IntCodeCPU(instructions)
    programm.write_input(1)
    programm.run_program()
    return programm.output.pop()


def solution_2(puzzle_input):
    instructions = [int(x) for x in puzzle_input.split(",") if x != ""]
    programm = IntCodeCPU(instructions)
    programm.write_input(5)
    programm.run_program()
    return programm.output.pop()
