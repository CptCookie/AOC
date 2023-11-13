class StopOperation(Exception):
    pass


class IntCodeProgramm:
    def __init__(self, instruction: list[int]):
        self.memory = instruction
        self.pointer = 0
        self.input = []
        self.output = []

    @property
    def cmd(self):
        return f"{self.memory[self.pointer]:05d}"

    @property
    def opcode(self):
        return self.cmd[-2:]

    def address(self, pos):
        address = self.pointer + 1 + pos
        if self.cmd[2 - pos] == "0":
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
            case "99":
                raise StopOperation()
            case "01":
                self.memory[self.address(2)] = (
                    self.memory[self.address(0)] + self.memory[self.address(1)]
                )
                self.pointer += 4
            case "02":
                # multiplie
                self.memory[self.address(2)] = (
                    self.memory[self.address(0)] * self.memory[self.address(1)]
                )
                self.pointer += 4
            case "03":
                # read input
                value = self.input.pop()
                self.memory[self.address(0)] = value
                self.pointer += 2
            case "04":
                # write output
                self.output.append(self.memory[self.address(0)])
                self.pointer += 2
            case "05":
                # jump if true
                if self.memory[self.address(0)] > 0:
                    self.pointer = self.memory[self.address(1)]
                else:
                    self.pointer += 3
            case "06":
                # jump if false
                if self.memory[self.address(0)] == 0:
                    self.pointer = self.memory[self.address(1)]
                else:
                    self.pointer += 3
            case "07":
                # less than
                if self.memory[self.address(0)] < self.memory[self.address(1)]:
                    self.memory[self.address(2)] = 1
                else:
                    self.memory[self.address(2)] = 0
                self.pointer += 4
            case "08":
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
