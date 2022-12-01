from collections import defaultdict
from typing import Optional

Instruction = tuple[str, str, Optional[str]]


class Processor:
    def __init__(self, instuctions):
        self.registers = defaultdict(lambda: 0)
        self.instructions = instuctions
        self.pc = 0

    @property
    def op(self):
        return self.instructions[self.pc][0]

    @property
    def addr(self):
        return self.instructions[self.pc][1:]

    def _get_value(self, address: str) -> int:
        if address.isalpha():
            return self.registers[address]
        else:
            return int(address)

    def execute_basic_command(self):
        # general instructions
        if self.op == "jgz":
            if self.registers[self.addr[0]] > 0:
                self.pc = self.pc + self._get_value(self.addr[1])
            else:
                self.pc += 1

        elif self.op == "set":
            self.registers[self.addr[0]] = self._get_value(self.addr[1])
            self.pc += 1

        elif self.op == "add":
            self.registers[self.addr[0]] += self._get_value(self.addr[1])
            self.pc += 1

        elif self.op == "mul":
            self.registers[self.addr[0]] *= self._get_value(self.addr[1])
            self.pc += 1

        elif self.op == "mod":
            self.registers[self.addr[0]] = self.registers[
                self.addr[0]
            ] % self._get_value(self.addr[1])
            self.pc += 1


class SoundProcessor(Processor):
    def __init__(self, instuctions):
        super().__init__(instuctions)
        self.play = 0

    def execute_pointer(self):

        if self.op == "rcv":
            if self._get_value(self.addr[0]) > 0:
                return self.play
            self.pc += 1

        elif self.op == "snd":
            self.play = self._get_value(self.addr[0])
            self.pc += 1

        else:
            self.execute_basic_command()

    def run_operations(self):
        while True:
            result = self.execute_pointer()

            if result:
                return result


class Worker(Processor):
    def __init__(self, id, instructions):
        super().__init__(instructions)
        self.input_buffer = []
        self.waiting = False
        self.receiver = None
        self.sending_counter = 0
        self.registers["p"] = id

    def execute_pointer(self):
        if self.op == "rcv" and self.input_buffer:
            self.registers[self.addr[0]] = self.input_buffer.pop(0)
            self.pc += 1
            self.waiting = False

        elif self.op == "rcv" and not self.input_buffer:
            self.waiting = True

        elif self.op == "snd" and self.receiver:
            self.receiver.input_buffer.append(self.registers[self.addr[0]])
            self.sending_counter += 1
            self.pc += 1

        else:
            self.execute_basic_command()


def parse_data(puzzle_input: str) -> list[str]:
    return [n.strip().split(" ") for n in puzzle_input.splitlines() if n != ""]


def solution_1(puzzle_input: str):
    instr = parse_data(puzzle_input)
    sound = SoundProcessor(instr)
    return sound.run_operations()


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)

    program_0 = Worker(0, data)
    program_1 = Worker(1, data)

    program_0.receiver = program_1
    program_1.receiver = program_0

    while not program_0.waiting or not program_1.waiting:

        print(len(program_0.input_buffer), len(program_1.input_buffer))
        program_0.execute_pointer()
        program_1.execute_pointer()

    return program_1.sending_counter
