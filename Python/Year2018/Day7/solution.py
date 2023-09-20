import re


ALPHA = "ABCDEFGHIJKLMONPQRSTUVWXYZ"


def get_letter_time(letter):
    return ALPHA.index(letter) + 1


def parse_input(aoc_input: str) -> list[(str, str)]:
    pattern = r"Step ([A-Z]) .* step ([A-Z]) .*"
    return [n.groups() for n in re.finditer(pattern, aoc_input)]


def get_path_serial(steps):
    path = ""
    s_from, s_to = list(zip(*steps))
    ends = set(s_to).difference(s_from)

    steps += [(e, "") for e in ends]
    while steps:
        s_from, s_to = list(zip(*steps))
        current_step = sorted(set(s_from).difference(s_to))[0]
        path += current_step
        steps = [s for s in steps if s[0] != current_step]
    return path


def get_route_parallel(steps: [(str, str)], workers: int, step_time=60):
    path = ""
    workers = [(None, None)] * workers

    # add ends as steps
    s_from, s_to = list(zip(*steps))
    ends = set(s_to).difference(s_from)
    steps += [(e, "") for e in ends]

    for ctime in range((step_time + 14) * len(steps)):
        # check for completed workers
        for i, w in enumerate(workers):
            if (
                w is not (None, None)
                and ctime >= get_letter_time(w[1]) + step_time + w[0]
            ):
                path += w[1]
                steps = [s for s in steps if s[0] != w[1]]
                workers[i] = (None, None)

        # check if work is left
        if not steps:
            return ctime

        # assign new work
        s_from, s_to = list(zip(*steps))
        open_steps = sorted(
            set(s_from).difference(s_to, [w[1] for w in workers]), reverse=True
        )
        for i, w in enumerate(workers):
            if w == (None, None) and open_steps:
                workers[i] = (ctime, open_steps.pop())


def solution_1(aoc_input: str):
    steps = parse_input(aoc_input)
    return get_path_serial(steps)


def solution_2(aoc_input: str):
    steps = parse_input(aoc_input)
    return get_route_parallel(steps, 5, 60)
