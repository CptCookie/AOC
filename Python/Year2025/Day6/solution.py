from typing import Iterator

Problem = list[str]


def parse_part_1(aoc_input: str) -> list[Problem]:
    problem_lines = []

    for line in aoc_input.splitlines():
        problem_lines.append([c for c in line.split(" ") if c != ""])

    problems = []
    for x in range(len(problem_lines[0])):
        problems.append([problem_lines[y][x] for y in range(len(problem_lines))])

    return problems


def parse_part_2(aoc_input: str) -> list[Problem]:
    lines = [list(line) for line in aoc_input.splitlines()]
    transformed_problems = []
    problem = []

    while True:
        try:
            col = [line.pop(0) for line in lines]
            op = col.pop()
            num = "".join(col).strip()
            if num == "" and op == " " and problem:
                transformed_problems.append(problem)
                problem = []
                continue

            if op != " ":
                problem.append(op)
                # operation marks the begining of a new problem

            problem.append(num)
        except IndexError:
            transformed_problems.append(problem)
            return [
                list(reversed(problem))
                for problem in transformed_problems
                if problem != []
            ]


def is_left(numbers: list[str]):
    return len(numbers[0]) >= len(numbers[-1])


def prod(iter: Iterator[int]):
    a = next(iter)
    b = next(iter)
    prod = a * b
    for c in iter:
        prod *= c
    return prod


def solve_problem(problem: Problem) -> int:
    op = problem[-1]
    if op == "+":
        return sum(int(n) for n in problem[:-1])
    if op == "*":
        return prod(int(n) for n in problem[:-1])

    raise ValueError(f"Unknown OP: {op}")


def solution_1(aoc_input: str):
    #
    problems = parse_part_1(aoc_input)
    return sum(solve_problem(p) for p in problems)


def solution_2(aoc_input: str):
    problems = parse_part_2(aoc_input)
    return sum(solve_problem(p) for p in problems)
