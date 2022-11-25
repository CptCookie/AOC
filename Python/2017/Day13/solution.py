def parse_data(puzzle_input: str) -> list[str]:
    return dict(
        [
            map(int, n.split(":"))
            for n in puzzle_input.replace(" ", "").splitlines()
            if n != ""
        ]
    )


def get_severety(firewall: dict[int, int], delay=0) -> int:
    sev = None
    for layer, depth in firewall.items():
        if (layer + delay) % (2 * depth - 2) == 0:
            if sev is not None:
                sev = 0
            sev += layer * depth
    return sev


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    return get_severety(data)


def solution_2(puzzle_input: str):
    firewall = parse_data(puzzle_input)
    delay = 0
    while True:
        delay += 1
        if get_severety(firewall, delay) == None:
            return delay
