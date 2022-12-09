MOVES = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}


class Rope:
    def __init__(self, knots=2):
        self.knots = [(0, 0) for _ in range(knots)]
        self.tail_pos = set()

    def move_all(self, instr_lst):
        for instr in instr_lst:
            self.move(instr)

    def move(self, instr):
        for _ in range(int(instr[1])):
            self._move_head(instr[0])
            self._move_tail()
            self.__log_tail_pos()

    @property
    def head(self):
        return self.knots[0]

    def _move_head(self, move):
        d_pos_x, d_pos_y = MOVES[move]
        self.knots[0] = (self.head[0] + d_pos_x, self.head[1] + d_pos_y)

    def _move_tail(self):
        for i, knot in enumerate(self.knots[1:]):
            dx = self.knots[i][0] - knot[0]
            dy = self.knots[i][1] - knot[1]

            if abs(dx) > 1 or abs(dy) > 1:
                dx_tail = dx if abs(dx) == 1 else dx // 2
                dy_tail = dy if abs(dy) == 1 else dy // 2
                self.knots[i + 1] = (knot[0] + dx_tail, knot[1] + dy_tail)

    def __log_tail_pos(self):
        self.tail_pos.add(self.knots[-1])


def parse_data(puzzle_input: str) -> list[str]:
    return [n.split(" ") for n in puzzle_input.splitlines() if n != ""]


def solution_1(puzzle_input: str):
    instr_lst = parse_data(puzzle_input)
    r = Rope(2)
    r.move_all(instr_lst)
    return len(r.tail_pos)


def solution_2(puzzle_input: str):
    instr_lst = parse_data(puzzle_input)
    r = Rope(10)
    r.move_all(instr_lst)
    return len(r.tail_pos)
