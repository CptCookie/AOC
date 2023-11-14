class StopOperation(Exception):
    pass


class InputEmpty(Exception):
    pass


class IntCodeProgramm:
    def __init__(self, instruction: list[int]):
        self.memory = instruction
        self.pointer = 0
        self.input = []
        self.output = []

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
        address = self.pointer + 1 + pos
        if mode == 0:
            return self.memory[address]
        else:
            return address

    def run_programm(self):
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
            case _:
                self.pointer += 1

    def write_input(self, value: int):
        self.input.append(value)
