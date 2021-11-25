import re


class Computer:
    def __init__(self, memory) -> None:
        self.memory = memory
        self.index = 0
        self.register = {"a": 0, "b": 0}

    def execute_programm(self):
        while self.index < len(self.memory):
            self.execute_index()

    def execute_index(self):
        try:
            command = self.parse_command()
            self.COMMANDS[command[0]](self, *command[1:])
        except Exception as e:
            raise e

    def parse_command(self):
        patterns = [
            r"(hlf|tpl|inc) (a|b)",
            r"(jmp) ([\+\-\d]+)",
            r"(jie|jio) (a|b), ([\+\-\d]+)",
        ]

        for p in patterns:
            match = re.search(p, self.memory[self.index])
            if match:
                return match.groups()
        print(self.memory[self.index])

    def halve(self, register: str):
        self.register[register] = int(self.register[register] / 2)
        self.index += 1

    def triple(self, register: str):
        self.register[register] *= 3
        self.index += 1

    def increment(self, register: str):
        self.register[register] += 1
        self.index += 1

    def jump(self, offset: str):
        self.index += int(offset)

    def jump_if_even(self, register: str, offset: str):
        if self.register[register] % 2 == 0:
            self.index += int(offset)
        else:
            self.index += 1

    def jump_if_one(self, register: str, offset: str):
        if self.register[register] == 1:
            self.index += int(offset)
        else:
            self.index += 1

    COMMANDS = {
        "hlf": halve,
        "tpl": triple,
        "inc": increment,
        "jmp": jump,
        "jie": jump_if_even,
        "jio": jump_if_one,
    }


def solution_1(puzzle_input: str):
    programm = [cmd for cmd in puzzle_input.splitlines() if cmd != ""]
    state_of_the_art = Computer(programm)
    state_of_the_art.execute_programm()
    return state_of_the_art.register["b"]


def solution_2(puzzle_input: str):
    programm = [cmd for cmd in puzzle_input.splitlines() if cmd != ""]
    state_of_the_art = Computer(programm)
    state_of_the_art.register["a"] = 1
    state_of_the_art.execute_programm()
    return state_of_the_art.register["b"]
