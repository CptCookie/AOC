from collections import namedtuple

Command = namedtuple(
    typename="Command",
    field_names=[
        "opcode",
        "param_1",
        "param_2",
        "param_3",
    ],
)

Parameter = namedtuple("Parameter", ["address", "position_mode"])


class StopOperation(Exception):
    pass


class IntCodeProgramm:
    def __init__(self, instruction):
        self.memory = instruction
        self.pointer = 0
        self.input = []
        self.output = []

    @property
    def result(self):
        return self.memory[0]

    def get_parameter_address(self, address, position_mode):
        try:
            if position_mode:
                address = self.memory[address]
                return address
            else:
                return address
        except IndexError:
            return None

    def get_command(self):
        op_complete = f"{int(self.memory[self.pointer]):05d}"
        opcode = op_complete[-2:]
        param_1 = self.get_parameter_address(self.pointer + 1, op_complete[-3] == "0")
        param_2 = self.get_parameter_address(self.pointer + 2, op_complete[-4] == "0")
        param_3 = self.get_parameter_address(self.pointer + 3, op_complete[-5] == "0")

        return Command(opcode, param_1, param_2, param_3)

    def run_programm(self):
        while True:
            try:
                command = self.get_command()
                self.run_command(command)
            except StopOperation:
                return

    def run_command(self, cmd: Command):
        if cmd.opcode == "99":
            raise StopOperation()
        elif cmd.opcode == "01":
            self.memory[cmd.param_3] = (
                self.memory[cmd.param_1] + self.memory[cmd.param_2]
            )
            self.pointer += 4

        elif cmd.opcode == "02":
            # multiplie
            self.memory[cmd.param_3] = (
                self.memory[cmd.param_1] * self.memory[cmd.param_2]
            )
            self.pointer += 4
        elif cmd.opcode == "03":
            # read input
            value = self.input.pop()
            self.memory[cmd.param_1] = value
            self.pointer += 2
        elif cmd.opcode == "04":
            # write output
            self.output.append(self.memory[cmd.param_1])
            self.pointer += 2
        elif cmd.opcode == "05":
            # jump if true
            if self.memory[cmd.param_1] > 0:
                self.pointer = self.memory[cmd.param_2]
            else:
                self.pointer += 3
        elif cmd.opcode == "06":
            # jump if false
            if self.memory[cmd.param_1] == 0:
                self.pointer = self.memory[cmd.param_2]
            else:
                self.pointer += 3
        elif cmd.opcode == "07":
            # less then
            if self.memory[cmd.param_1] < self.memory[cmd.param_2]:
                self.memory[cmd.param_3] = 1
            else:
                self.memory[cmd.param_3] = 0
            self.pointer += 4
        elif cmd.opcode == "08":
            # equals
            if self.memory[cmd.param_1] == self.memory[cmd.param_2]:
                self.memory[cmd.param_3] = 1
            else:
                self.memory[cmd.param_3] = 0
            self.pointer += 4
        else:
            self.pointer += 1

    def write_input(self, value: int):
        self.input.append(value)

    def add(self, cmd: Command):
        value_1_address = self.get_parameter_address(cmd.param_1)
        value_2_address = self.get_parameter_address(cmd.param_2)
        value_3_address = self.get_parameter_address(cmd.param_3)