import re

VALIDATION = {
    "byr": r"19[2-9]\d|200[0-2]",
    "iyr": r"20[1]\d|2020",
    "eyr": r"20[2]\d|2030",
    "hgt": r"(1[5-8]\d|19[0-3])cm|(59|7[0-6]|6\d)in",
    "hcl": r"#[a-f\d]{6}",
    "ecl": r"amb|blu|brn|gry|grn|hzl|oth",
    "pid": r"\d{9}",
}


def parse_passports(puzzle_input):
    passports = [{}]

    for line in puzzle_input:
        if line == "":
            passports.append({})
        else:
            passports[-1].update(dict([n.split(":") for n in line.split(" ")]))
    return passports


def check_passport(passport, validation=False):
    for n in VALIDATION:
        if not n in passport:
            return False

        if validation:
            if not validate_field(n, passport[n]):
                return False
    return True


def validate_field(field, value):
    match = re.compile(VALIDATION[field]).match(value)
    return match is not None and match.group() == value


def solution_1(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n")][:-1]
    passports = parse_passports(puzzle_input)
    return sum([check_passport(n) for n in passports])


def solution_2(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n")][:-1]
    passports = parse_passports(puzzle_input)
    return sum([check_passport(n, validation=True) for n in passports])
