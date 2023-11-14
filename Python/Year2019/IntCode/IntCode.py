from collections import defaultdict

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2


class StopOperation(Exception):
    pass


class InputEmpty(Exception):
    pass


class IntCodeCPU:
    def __init__(self, instruction: list[int]):
        self.memory = defaultdict(lambda: 0, zip(range(len(instruction)), instruction))
        self._relative_base = 0
        self.pointer = 0
        self.input = []
        self.output = []

    @property
    def memlist(self):
        return list([self.memory[m] for m in range(max(self.memory.keys()) + 1)])

    def __repr__(self):
        return f"{self.pointer} - {self.input} - {self.output}"

    @property
    def cmd(self):
        return self.memory[self.pointer]

    @property
    def opcode(self):
        return self.memory[self.pointer] % 100

    def address(self, pos):
        mode = (self.cmd // (10 ** (pos + 2))) % 10
        base_address = self.pointer + 1 + pos

        if mode == POSITION_MODE:
            return self.memory[base_address]
        elif mode == IMMEDIATE_MODE:
            return base_address
        elif mode == RELATIVE_MODE:
            return self._relative_base + self.memory[base_address]
        else:
            raise ValueError("unknown address mode")

    def run_program(self):
        while True:
            try:
                self.run_command()
            except StopOperation:
                return

    def run_command(self):
        match self.opcode:
            case 99:
                raise StopOperation()
            case 1:
                self.memory[self.address(2)] = (
                    self.memory[self.address(0)] + self.memory[self.address(1)]
                )
                self.pointer += 4
            case 2:
                # multiplie
                self.memory[self.address(2)] = (
                    self.memory[self.address(0)] * self.memory[self.address(1)]
                )
                self.pointer += 4
            case 3:
                # read input
                if not self.input:
                    raise InputEmpty()

                value = self.input.pop(0)  # popleft fifo
                self.memory[self.address(0)] = value
                self.pointer += 2
            case 4:
                # write output
                self.output.append(self.memory[self.address(0)])
                self.pointer += 2
            case 5:
                # jump if true
                if self.memory[self.address(0)] > 0:
                    self.pointer = self.memory[self.address(1)]
                else:
                    self.pointer += 3
            case 6:
                # jump if false
                if self.memory[self.address(0)] == 0:
                    self.pointer = self.memory[self.address(1)]
                else:
                    self.pointer += 3
            case 7:
                # less than
                if self.memory[self.address(0)] < self.memory[self.address(1)]:
                    self.memory[self.address(2)] = 1
                else:
                    self.memory[self.address(2)] = 0
                self.pointer += 4
            case 8:
                # equals
                if self.memory[self.address(0)] == self.memory[self.address(1)]:
                    self.memory[self.address(2)] = 1
                else:
                    self.memory[self.address(2)] = 0
                self.pointer += 4
            case 9:
                self._relative_base += self.memory[self.address(0)]
                self.pointer += 2
            case _:
                self.pointer += 1

    def write_input(self, value: int):
        self.input.append(value)
