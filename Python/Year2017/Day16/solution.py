def parse_data(puzzle_input: str) -> list[str]:
    return [n for n in puzzle_input.split(",") if n != ""]


class DanceGroup:
    def __init__(self):
        self.dancers = [chr(97 + i) for i in range(16)]
        self.og_pos = self.dancers

    @property
    def dancer_order(self):
        return "".join(self.dancers)

    def dance(self, steps: list[str]):
        for step in steps:
            if step[0] == "s":
                self.spin(int(step[1:]))
            elif step[0] == "x":
                a, b = step[1:].split("/")
                self.excange(int(a), int(b))
            elif step[0] == "p":
                a, b = step[1:].split("/")
                self.partner(a, b)

    def spin(self, amount: int):
        self.dancers = self.dancers[amount * -1 :] + self.dancers[: amount * -1]

    def excange(self, a: int, b: int):
        a_value = self.dancers[a]

        self.dancers[a] = self.dancers[b]
        self.dancers[b] = a_value

    def partner(self, a: str, b: str):
        a_index = self.dancers.index(a)
        b_index = self.dancers.index(b)
        self.excange(a_index, b_index)


def solution_1(puzzle_input: str) -> str:
    data = parse_data(puzzle_input)
    d = DanceGroup()
    d.dance(data)
    return d.dancer_order


def solution_2(puzzle_input: str) -> str:
    data = parse_data(puzzle_input)
    d = DanceGroup()
    known = set()

    for _ in range(1_000_000_000):
        # find the loop
        if d.dancer_order in known:
            break
        else:
            known.add(d.dancer_order)

    for _ in range(1_000_000_000 % 60):
        # iterate the rest
        d.dance(data)

    return d.dancer_order
