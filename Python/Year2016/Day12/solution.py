from Year2016.assembunny import AssemBunnyComputer


def parse_input(puzzle_input: str) -> list[list[str | int]]:
    instr = []
    for line in puzzle_input.splitlines():
        if line != "":
            instr.append([c if c.isalpha() else int(c) for c in line.split()])
    return instr


def solution_1(puzzle_input: str):
    data = parse_input(puzzle_input)
    cmp = AssemBunnyComputer(data)
    cmp.run_instr()
    return cmp.registers["a"]


def solution_2(puzzle_input: str):
    data = parse_input(puzzle_input)
    cmp = AssemBunnyComputer(data)
    cmp["c"] = 1
    cmp.run_instr()
    return cmp.registers["a"]
