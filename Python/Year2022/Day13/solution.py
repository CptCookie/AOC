class ComparingList:
    def __init__(self, lst):
        self.lst = lst

    def __lt__(self, other):
        return in_order(self.lst, other.lst)

    def __eq__(self, other):
        return self.lst == other.lst


def parse_data_level_1(puzzle_input: str):
    pairs = []
    for pair_str in puzzle_input.split("\n\n"):
        if pair_str != "":
            a, b, *c = pair_str.split("\n")
            pairs.append((eval(a), eval(b)))
    return pairs


def parse_data_level_2(puzzle_input: str):
    return [
        ComparingList(eval(line)) for line in puzzle_input.splitlines() if line != ""
    ]


def in_order_int(a, b):
    if a < b:
        return True
    elif b < a:
        return False
    else:
        return None


def in_order_lst(a, b):
    for i, ai in enumerate(a):
        if i >= len(b):
            return False

        order = in_order(ai, b[i])
        if order is not None:
            return order

    if len(a) < len(b):
        return True


def in_order(a: list[int] | int, b: list[int] | int):
    if type(a) == int and type(b) == int:
        return in_order_int(a, b)

    elif type(a) == list and type(b) == list:
        return in_order_lst(a, b)

    elif type(a) == int:
        return in_order([a], b)
    else:
        return in_order(a, [b])


def solution_1(puzzle_input: str):
    pairs = parse_data_level_1(puzzle_input)
    return sum(i + 1 for i, p in enumerate(pairs) if in_order(*p))


def solution_2(puzzle_input: str):
    packets = parse_data_level_2(puzzle_input)

    packets.append(ComparingList([[2]]))
    packets.append(ComparingList([[6]]))

    packets.sort()
    return packets.index(ComparingList([[2]])) * packets.index(ComparingList([[6]]))
