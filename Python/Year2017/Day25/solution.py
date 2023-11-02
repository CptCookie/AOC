from collections import defaultdict
from itertools import count
import re

PATTERN = r"If the current value is (\d):\n.*value (\d).\n.*to the (right|left).\n.*state ([A-Z])"


def parse_input(aoc_input: str) -> list[str]:
    head, *tail = aoc_input.split("\n\n")
    steps = int(re.search(r"(\d)+", head).group(0))
    instr = {}
    for state in tail:
        state_name = re.search("In state ([A-Z]):", state).group(1)
        state_inst = []
        for m in re.finditer(PATTERN, state):
            cv, nv, dp, ns = m.groups()
            state_inst.append((int(nv), 1 if dp == "right" else -1, ns))
        instr[state_name] = state_inst

    return steps, instr


def run_turing_machine(instr, end):
    current_state = "A"
    pntr = 0
    tape = defaultdict(lambda: 0)

    for n in count():
        cvalue = tape[pntr]
        nvalue, dpntr, next_state = instr[current_state][cvalue]

        tape[pntr] = nvalue
        pntr = pntr + dpntr
        current_state = next_state

        if n == end - 1:
            return len([k for k, v in tape.items() if v == 1])


def solution_1(aoc_input: str):
    steps, instr = parse_input(aoc_input)
    return run_turing_machine(instr, steps)


def solution_2(aoc_input: str):
    return "Merry Chistmas"
