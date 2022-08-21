def parse_data(puzzle_input: str) -> list[str]:
    return [n for n in puzzle_input.splitlines() if n != ""]


class AssemBunnyComputer:
    def __init__(self, instr):
        self.registers = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
        }
        self.instr_pointer = 0
        self.instr = instr

    def __setitem__(self, reg, value):
        self.registers[reg] = value

    def __getitem__(self, reg):
        return self.registers[reg]

    def cpy(self, reg: str, value: str | int):
        if isinstance(value, int) or value.isnumeric():
            self[reg] = int(value)
        else:
            self[reg] = self[value]

    def inc(self, reg):
        self[reg] += 1

    def dec(self, reg):
        self[reg] -= 1

    def jnz(self, reg: str, value: str | int):
        if reg.isnumeric() and int(reg) > 0 or self[reg] > 0:
            self.instr_pointer += int(value)
        else:
            self.instr_pointer += 1

    def run_instr(self):
        while self.instr_pointer < len(self.instr):
            cur_instr = self.instr[self.instr_pointer].split()
            match cur_instr:
                case "cpy", x, y:
                    self.cpy(y, x)
                    self.instr_pointer += 1
                case "inc", x:
                    self.inc(x)
                    self.instr_pointer += 1
                case "dec", x:
                    self.dec(x)
                    self.instr_pointer += 1
                case "jnz", x, y:
                    self.jnz(x, y)


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    cmp = AssemBunnyComputer(data)
    cmp.run_instr()
    return cmp.registers["a"]


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    cmp = AssemBunnyComputer(data)
    cmp["c"] = 1
    cmp.run_instr()
    return cmp.registers["a"]
