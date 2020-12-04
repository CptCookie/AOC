import requests
import re
from const import token

VALIDATION = {
        'byr': r'19[2-9]\d|200[0-2]',
        'iyr': r'20[1]\d|2020',
        'eyr': r'20[2]\d|2030',
        'hgt': r'(1[5-8]\d|19[0-3])cm|(59|7[0-6]|6\d)in',
        'hcl': r'#[a-f\d]{6}',
        'ecl': r'amb|blu|brn|gry|grn|hzl|oth',
        'pid': r'\d{9}'
}

def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/4/input", cookies={"session": token})
    return [n for n in r.content.decode().split('\n')][:-1]


def parse_passports(puzzle_input):
    passports = [{}]

    for line in puzzle_input:
        if line == '':
            passports.append({})
        else: 
            passports[-1].update(
                dict([n.split(':') for n in line.split(' ')])
            )
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


def test_byr_validation():
    assert(validate_field('byr', '1920'))
    assert(validate_field('byr', '2002'))
    assert(validate_field('byr', '2000'))
    assert(validate_field('byr', '1999'))
    assert(not validate_field('byr', '2003'))
    assert(not validate_field('byr', '1919'))

def test_iyr_validation():   
    assert(validate_field('iyr', '2010'))
    assert(validate_field('iyr', '2020'))
    assert(not validate_field('iyr', '2000'))
    assert(not validate_field('iyr', '2025'))

def test_ecl_validation():
    assert(validate_field('ecl', 'brn'))
    assert(not validate_field('ecl', 'wat'))

def test_pid_validation():
    assert(validate_field('pid', '000000001'))
    assert(not validate_field('pid', '0123456789'))

def test_hcl_validation():
    assert(validate_field('hcl', '#123abc'))
    assert(not validate_field('hcl', '#123abz'))
    assert(not validate_field('hcl', '123abc'))

if __name__ == "__main__":
    passports = parse_passports(get_aoc_input())
    print(f'solution 1: {sum([check_passport(n) for n in passports])}')
    print(f'solution 2: {sum([check_passport(n, validation=True) for n in passports])}')
