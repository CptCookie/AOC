def parse_data(puzzle_input: str) -> list[str]:
    elf_package = []
    for elf in puzzle_input.split("\n\n"):
        elf_package.append([int(n) for n in elf.splitlines()])
    return elf_package


def solution_1(puzzle_input: str):
    elf_packages = parse_data(puzzle_input)
    return max([sum(e) for e in elf_packages])


def solution_2(puzzle_input: str):
    elf_packages = parse_data(puzzle_input)
    return sum(sorted([sum(e) for e in elf_packages])[-3:])
