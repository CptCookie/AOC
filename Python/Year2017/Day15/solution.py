def parse_data(puzzle_input: str) -> tuple[int, int]:
    return tuple(
        int(s) for s in puzzle_input.replace("\n", " ").split(" ") if s.isnumeric()
    )


class NumberGenerator:
    def __init__(self, start_number, factor, picky_mod=None):
        self.current = start_number
        self.factor = factor
        self.picky_mod = picky_mod

    @property
    def last_16_bit(self):
        return self.current & 65535

    def __eq__(self, other):
        return self.last_16_bit == other.last_16_bit

    def calc_next(self, picky=False):
        self.current = (self.current * self.factor) % 2147483647

        while self.picky_mod and self.current % self.picky_mod != 0:
            self.current = (self.current * self.factor) % 2147483647


def judge_generation(gen_a, gen_b, rounds):
    count = 0
    for _ in range(rounds):
        gen_a.calc_next()
        gen_b.calc_next()
        if gen_a == gen_b:
            count += 1
    return count


def solution_1(puzzle_input: str):
    start_a, start_b = parse_data(puzzle_input)
    gen_a = NumberGenerator(start_a, 16807)
    gen_b = NumberGenerator(start_b, 48271)

    return judge_generation(gen_a, gen_b, 40_000_000)


def solution_2(puzzle_input: str):
    start_a, start_b = parse_data(puzzle_input)
    gen_a = NumberGenerator(start_a, 16807, 4)
    gen_b = NumberGenerator(start_b, 48271, 8)

    return judge_generation(gen_a, gen_b, 5_000_000)
