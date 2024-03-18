import heapq

Coord2D = tuple[int, int]
Direction = tuple[int, int]

DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def find_warmest_route(map: list[str], min_direction=1, max_direction=3) -> int:
    q = []
    qed = set()
    heapq.heapify(q)

    max_x, max_y = len(map[0]) - 1, len(map) - 1
    start = (0, 0)
    fininsh = (max_x, max_y)
    best_heat = 9 * max_x * max_y

    # start with all 4 directions
    for direct in DIRECTIONS:
        heapq.heappush(
            q, (0, (start, direct, 0))
        )  # pos, direction, direction counter, heat loss
        qed.add((start, direct, 0))

    # iterate
    while q:
        heat_loss, ((x, y), (dx, dy), dir_cnt) = heapq.heappop(q)
        (nx, ny) = x + dx, y + dy

        if (x, y) == fininsh:
            # reached the end point
            if heat_loss < best_heat:
                best_heat = heat_loss
            continue

        if heat_loss > best_heat:
            # we already lost to0 much heat
            continue

        if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
            # position out of bound
            continue

        for new_direct in DIRECTIONS:
            new_dir_cnt = dir_cnt + 1

            if new_direct == (-dx, -dy):
                # can not reverse
                continue

            if new_direct != (dx, dy):
                # turning if possible
                if new_dir_cnt < min_direction:
                    continue
                else:
                    new_dir_cnt = 0

            new_pos = (nx, ny)
            new_state = (new_pos, new_direct, new_dir_cnt)

            if new_direct == (dx, dy) and new_dir_cnt >= max_direction:
                # ignore direction when limit is reached
                continue

            if new_state not in qed:
                new_heat_loss = heat_loss + int(map[ny][nx])
                heapq.heappush(q, (new_heat_loss, new_state))
                qed.add(new_state)

    return best_heat


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    return find_warmest_route(input, max_direction=3)


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return find_warmest_route(input, min_direction=4, max_direction=10)
