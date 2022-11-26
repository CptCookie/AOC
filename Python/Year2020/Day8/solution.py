from copy import deepcopy


NOOP = "nop"
ACC = "acc"
JMP = "jmp"


def parse_bootcode(aoc_input: [str]) -> [(str, int)]:
    return [(n[0:3], int(n[4:])) for n in aoc_input]


def run_boot(boot_code):
    index = 0
    acc = 0
    done = []
    while True:
        if index in done or index == len(boot_code):
            return (index, acc)

        if boot_code[index][0] == ACC:
            done.append(index)
            acc += boot_code[index][1]
            index += 1

        elif boot_code[index][0] == JMP:
            done.append(index)
            index += boot_code[index][1]

        elif boot_code[index][0] == NOOP:
            done.append(index)
            index += 1


def fix_bootcode(boot_code):
    for n, m in enumerate(boot_code):
        mod_boot = deepcopy(boot_code)

        if m[0] is NOOP and m[1] != 0:
            mod_boot[n] = (JMP, mod_boot[n][1])

        elif m[0] == JMP:
            mod_boot[n] = (NOOP, mod_boot[n][1])

        boot = run_boot(mod_boot)
        if boot[0] == len(mod_boot):
            return boot


def solve(puzzle_input):
    boot_code = parse_bootcode([n for n in puzzle_input.split("\n") if n != ""])
    print(f"Solution 1: {run_boot(boot_code)[1]}")
    print(f"Solution 2: {fix_bootcode(boot_code)[1]}")
