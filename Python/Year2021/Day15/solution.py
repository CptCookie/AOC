from copy import deepcopy


def neighbors(x, y, matrix):
    nei = []
    if x < len(matrix[0]) - 1:
        nei.append((x + 1, y))
    if x > 0:
        nei.append((x - 1, y))
    if y < len(matrix) - 1:
        nei.append((x, y + 1))
    if y > 0:
        nei.append((x, y - 1))
    return nei


def get_next_node(stack):
    return sorted(stack, key=lambda p: p[1])[0]

    def this_is_the_way(matrix: list[list[int]]) -> int:
        stack = [((0, 0), 0)]
        visited = {(0, 0): 0}

        while stack:
            (x, y), cost = get_next_node(stack)
            stack.remove(((x, y), cost))

            for nei_x, nei_y in neighbors(x, y, matrix):
                nei_cost = cost + matrix[nei_y][nei_x]
                if (nei_x, nei_y) == (len(matrix[0]) - 1, len(matrix) - 1):
                    return nei_cost

                if (nei_x, nei_y) in visited and visited[(nei_x, nei_y)] > nei_cost:
                    visited[(nei_x, nei_y)] = nei_cost

                if (nei_x, nei_y) not in visited:
                    stack.append(((nei_x, nei_y), nei_cost))
                    visited[(nei_x, nei_y)] = nei_cost

        return visited[len(matrix) - 1, len(matrix[0]) - 1]


def parse_data(puzzle_input: str) -> list[str]:
    matrix = []

    for line in puzzle_input.splitlines():
        matrix.append([int(n) for n in line])
    return matrix


def solution_1(puzzle_input: str):
    matrix = parse_data(puzzle_input)
    return this_is_the_way(matrix)


def solution_2(puzzle_input: str):
    matrix = parse_data(puzzle_input)
    matrix_2 = deepcopy(matrix)

    for mx in range(1, 5):
        for i, line in enumerate(matrix):
            matrix_2[i].extend(
                [(n + mx) if (n + mx) <= 9 else n + mx - 9 for n in line]
            )

    matrix = deepcopy(matrix_2)
    for my in range(1, 5):
        for line in matrix:
            matrix_2.append([(n + my) if (n + my) <= 9 else (n + my - 9) for n in line])

    return this_is_the_way(matrix_2)
