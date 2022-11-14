from copy import deepcopy


def parse_data(puzzle_input: str) -> list[int]:
    return [int(n) for n in puzzle_input.split("\t") if n != ""]


def redistribute_memory(memory: list[int]) -> list[int]:
    index = memory.index(max(memory))
    banks = len(memory)

    number = memory[index]
    memory[index] = 0

    for n in range(1, number + 1):
        memory[(n + index) % banks] += 1

    return memory


def solution_1(puzzle_input: str):
    memory = parse_data(puzzle_input)
    seen_memory = [deepcopy(memory)]
    counter = 0
    while True:
        counter += 1
        new_memory = redistribute_memory(memory)
        if new_memory in seen_memory:
            return counter
        else:
            seen_memory.append(deepcopy(new_memory))
            memory = new_memory


def solution_2(puzzle_input: str):
    memory = parse_data(puzzle_input)
    seen_memory = [deepcopy(memory)]
    counter = None
    loop_mem = None
    while True:
        new_memory = redistribute_memory(memory)

        if counter is not None:
            counter += 1

        if new_memory in seen_memory and loop_mem is None:
            loop_mem = deepcopy(new_memory)
            counter = 0

        elif new_memory == loop_mem:
            return counter

        elif loop_mem is None:
            seen_memory.append(deepcopy(new_memory))

        memory = new_memory
