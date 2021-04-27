def get_fuel_for_mass(mass: int):
    return int(mass / 3) - 2


def get_fuel_complete(mass: int):
    fuel = 0
    while mass > 6:
        new_fuel = get_fuel_for_mass(mass)
        fuel += new_fuel
        mass = new_fuel
    return fuel


def solution_1(puzzle_input):
    puzzle_input = [int(n) for n in puzzle_input.split("\n") if n != ""]
    return sum([get_fuel_for_mass(n) for n in puzzle_input])


def solution_2(puzzle_input):
    puzzle_input = [int(n) for n in puzzle_input.split("\n") if n != ""]
    return sum([get_fuel_complete(n) for n in puzzle_input])
