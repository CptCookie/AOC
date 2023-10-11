TRAP_COND = ["^^.", ".^^", "^..", "..^"]


def build_map(first_row, depth):
    map = [first_row]
    for y in range(depth - 1):
        row = ""

        for x in range(len(first_row)):
            match x:
                case n if n == 0:
                    prev = "." + map[-1][:2]
                case n if n == len(first_row) - 1:
                    prev = map[-1][n - 1 :] + "."
                case n:
                    prev = map[-1][n - 1 : n + 2]

            if prev in TRAP_COND:
                row += "^"
            else:
                row += "."

        map.append(row)

    return map


def solution_1(aoc_input: str):
    first_row = aoc_input.strip()
    map = build_map(first_row, 40)
    return sum(line.count(".") for line in map)


def solution_2(aoc_input: str):
    first_row = aoc_input.strip()
    map = build_map(first_row, 400000)
    return sum(line.count(".") for line in map)
