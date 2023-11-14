from copy import deepcopy
from Year2019.IntCode import IntCodeCPU


def solution_1(puzzle_input):
    instruction = [int(n) for n in puzzle_input.split(",") if n != ""]
    programm = IntCodeCPU(instruction)
    programm.memory[1] = 12
    programm.memory[2] = 2
    programm.run_program()
    return programm.memory[0]


def solution_2(puzzle_input):
    instruction = [int(n) for n in puzzle_input.split(",") if n != ""]

    for a in range(100):
        for b in range(100):
            programm = IntCodeCPU(deepcopy(instruction))
            programm.memory[1] = a
            programm.memory[2] = b
            programm.run_program()

            if programm.memory[0] == 19690720:
                return a * 100 + b
