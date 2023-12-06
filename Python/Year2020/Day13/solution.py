def get_earlyest_bus(arival, busses: list[int]) -> tuple[int, int]:
    takeable = [
        (n, m)
        for n in range(arival, arival + max(busses))
        for m in busses
        if n % m == 0
    ]
    return min(takeable, key=lambda x: x[0])


def part_1(puzzle_input):
    arival = int(puzzle_input[0])
    busses = [int(n) for n in puzzle_input[1].split(",") if n != "x"]
    bus = get_earlyest_bus(arival, busses)
    return (bus[0] - arival) * bus[1]


def valid_solution(bus_Ids, start_time):
    for n, Id in enumerate(bus_Ids):
        if Id > -1:
            if not (start_time + n) % bus_Ids[n] == 0:
                return False
    return True


def part_2(puzzle_input):
    bus_ids = [int(n) if n != "x" else -1 for n in puzzle_input.split(",")]
    max_id = max(bus_ids)
    for time in bus_tick(max_id):
        start_time = int(time / bus_ids[0]) * bus_ids[0]
        if valid_solution(bus_ids, start_time):
            return start_time


def bus_tick(tick):
    n = 0
    while True:
        n += 1
        yield n * tick


def solution_1(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    return part_1(puzzle_input)


def solution_2(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    return part_2(puzzle_input[1])  # incomplete
