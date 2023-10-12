from Year2016.assembunny import AssemBunnyComputer


def parse_input(puzzle_input: str) -> list[list[str]]:
    instr = []
    for line in puzzle_input.splitlines():
        if line != "":
            instr.append([c if c.isalpha() else int(c) for c in line.split()])
    return instr


def solution_1(puzzle_input: str):
    input = parse_input(puzzle_input)
    prog = AssemBunnyComputer(input, cache_jnz=True)
    prog["a"] = 7
    prog.run_instr()

    return prog["a"]


def solution_2(puzzle_input: str):
    input = parse_input(puzzle_input)
    prog = AssemBunnyComputer(input, cache_jnz=True)
    prog["a"] = 12
    prog.run_instr()

    return prog["a"]
