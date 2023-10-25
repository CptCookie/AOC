from copy import deepcopy


class AssemBunnyComputer:
    def __init__(self, instr: list[list[str | int]], cache_jnz=False):
        self.registers = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
        }
        self.instr_pointer = 0
        self.instr = instr

        self.cache_jnz = cache_jnz
        self.jnz_cache = {}

        self.output = []
        self.know_states = set()

    def __setitem__(self, reg, value):
        self.registers[reg] = value

    def __getitem__(self, reg):
        return self.registers[reg]

    def cpy(self, reg: str, value: str | int):
        if not isinstance(reg, str):
            return

        if isinstance(value, int):
            self[reg] = value
        else:
            self[reg] = self[value]

    def inc(self, reg):
        self[reg] += 1

    def dec(self, reg):
        self[reg] -= 1

    def jnz_cached(self, a, b):
        if self.instr_pointer in self.jnz_cache:
            dif_reg = {
                key: self[key] - self.jnz_cache[self.instr_pointer][key]
                for key in self.registers
            }
            i = self[a] // (dif_reg[a] * -1)
            self.registers = {
                key: value + i * dif_reg[key] for key, value in self.registers.items()
            }

            del self.jnz_cache[self.instr_pointer]

        if isinstance(a, int) and a != 0 or self[a] != 0:
            jump = b if isinstance(b, int) else self[b]
            if jump < 0 and isinstance(a, str):
                self.jnz_cache[self.instr_pointer] = deepcopy(self.registers)

            self.instr_pointer += jump

        else:
            self.instr_pointer += 1

    def jnz(self, a: str | int, b: str | int):
        if isinstance(a, int) and a != 0 or isinstance(a, str) and self[a] != 0:
            if isinstance(b, int):
                self.instr_pointer += b
            else:
                self.instr_pointer += self[b]
        else:
            self.instr_pointer += 1

    def tgl(self, reg: str):
        if self[reg] == 0:
            self.instr[self.instr_pointer][0] = "inc"
        elif self.instr_pointer + self[reg] < len(self.instr):
            instr = self.instr[self.instr_pointer + self[reg]]
            match instr[0], len(instr):
                case "inc", 2:
                    instr[0] = "dec"
                case _, 2:
                    instr[0] = "inc"
                case "jnz", 3:
                    instr[0] = "cpy"
                case _, 3:
                    instr[0] = "jnz"

    def out(self, a: str | int):
        if self.detect_loop():
            raise LoopException()
        if isinstance(a, str):
            self.output.append(self[a])
        else:
            self.output.append(a)

    def detect_loop(self):
        state = (tuple(self.registers.values()), self.instr_pointer)
        if state in self.know_states:
            return True
        else:
            self.know_states.add(state)

    def run_instr(self):
        while self.instr_pointer < len(self.instr):
            cur_instr = self.instr[self.instr_pointer]
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
                    if self.cache_jnz:
                        self.jnz_cached(x, y)
                    else:
                        self.jnz(x, y)
                case "tgl", x:
                    self.tgl(x)
                    self.instr_pointer += 1
                case "out", x:
                    self.out(x)
                    self.instr_pointer += 1


class LoopException(ValueError):
    pass
