from queue import PriorityQueue


def parse_data(puzzle_input: str) -> list[str]:
    start = ()
    end = ()
    map = []
    for y, line in enumerate(puzzle_input.splitlines()):
        map_line = []
        for x, cell in enumerate(line):
            if cell == "S":
                start = (x, y)
                map_line.append("a")
            elif cell == "E":
                end = (x, y)
                map_line.append("z")
            else:
                map_line.append(cell)
        map.append(map_line)
    return map, start, end


def get_next_states(pos: tuple[int, int], map: list[list[int]]):
    x, y = pos
    new_pos = []
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        try:
            if ord(map[y + dy][x + dx]) - ord(map[y][x]) <= 1:
                new_pos.append((x + dx, y + dy))
        except IndexError:
            pass
    return new_pos


def walk(map: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    next_state = PriorityQueue()
    next_state.put((1, (start, 0)))
    known_states = dict()


    while not next_state.empty():
        prio, (state, steps) = next_state.get()
        if state in known_states and steps >= known_states[state]:
            continue

        known_states[state] = steps
        potential_next_states = get_next_states(state, map)

        for next in potential_next_states:
            if next not in known_states or known_states[next] > steps + 1:
                prio = steps + abs(end[0] - next[0]) + abs(end[1] - next[1])
                next_state.put((prio, (next, steps + 1)))

    if end in known_states:
        return known_states[end]
    else:
        return 9001


def solution_1(puzzle_input: str):
    map, start, end = parse_data(puzzle_input)
    return walk(map, start, end)


def solution_2(puzzle_input: str):
    map, start, end = parse_data( puzzle_input )
    all_starts = [(x,y) for y, line in enumerate(map) for x,c in enumerate(line) if c == "a"]
    return min(walk(map, s, end) for s in all_starts)
