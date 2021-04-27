from copy import deepcopy


class IntCodeProgramm:
    def __init__(self, instruction):
        self.memory = instruction
        self.pointer = 0

    @property
    def result(self):
        return self.memory[0]

    def run_programm(self):
        while True:
            opcode = self.memory[self.pointer]
            if opcode == 99:
                return
            elif opcode == 1:
                self.add(*self.memory[self.pointer + 1 : self.pointer + 4])
            elif opcode == 2:
                self.multiplie(*self.memory[self.pointer + 1 : self.pointer + 4])
            self.pointer += 4

    def add(self, param_1: int, param_2: int, param_3: int):
        self.memory[param_3] = self.memory[param_1] + self.memory[param_2]

    def multiplie(self, param_1: int, param_2: int, param_3: int):
        self.memory[param_3] = self.memory[param_1] * self.memory[param_2]


def solution_1(puzzle_input):
    instruction = [int(n) for n in puzzle_input.split(",") if n != ""]
    programm = IntCodeProgramm(instruction)
    programm.memory[1] = 12
    programm.memory[2] = 2
    programm.run_programm()
    return programm.result


def solution_2(puzzle_input):
    instruction = [int(n) for n in puzzle_input.split(",") if n != ""]

    for a in range(100):
        for b in range(100):
            programm = IntCodeProgramm(deepcopy(instruction))
            programm.memory[1] = a
            programm.memory[2] = b
            programm.run_programm()

            if programm.result == 19690720:
                return a * 100 + b
