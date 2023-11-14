from copy import deepcopy
from itertools import permutations

from Year2019.IntCode import IntCodeProgramm, StopOperation, InputEmpty


def parse_input(aoc_input: str) -> list[int]:
    return [int(x) for x in aoc_input.split(",") if x != ""]


def run_amps(instr: list[int], inputs: list[int]):
    last_value = 0
    for n in inputs:
        cpu = IntCodeProgramm(instr)
        cpu.input.append(n)
        cpu.input.append(last_value)
        cpu.run_programm()
        last_value = cpu.output.pop()

    return last_value


def run_amps_loop(instr: list[int], inputs: list[int]):
    amp_loop = []

    # build and connect amps
    for i, p in enumerate(inputs):
        cpu = IntCodeProgramm(deepcopy(instr))

        if i > 0:
            cpu.input = amp_loop[i - 1].output

        if i == len(inputs) - 1:
            cpu.output = amp_loop[0].input

        cpu.input.append(p)

        if i == 0:
            cpu.input.append(0)

        amp_loop.append(cpu)

    # run the amps
    while True:
        done_cnt = 0
        for i, amp in enumerate(amp_loop):
            try:
                while True:
                    amp.run_command()
            except StopOperation:
                done_cnt += 1
            except InputEmpty:
                pass

        if done_cnt >= len(inputs):
            return amp_loop[-1].output.pop()


def solution_1(aoc_input: str):
    instructions = parse_input(aoc_input)
    return max(run_amps(instructions, n) for n in permutations([0, 1, 2, 3, 4], 5))


def solution_2(aoc_input: str):
    instructions = parse_input(aoc_input)
    return max(run_amps_loop(instructions, n) for n in permutations([5, 6, 7, 8, 9], 5))
