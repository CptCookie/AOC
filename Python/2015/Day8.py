import re 
reghex = re.compile(r'\\x[0-9a-f]{2}')

def count_code(line:str):
    return len(line)

def count_char(line:str):
    line = line.replace(r'\\', '1')
    line = line.replace(r'\"', '2')
    for n in reghex.findall(line):
        line = line.replace(n, '0')
    return len(f'{line[1:-1]}')

def count_reencode(line:str):
    qoutes = line.count('"')
    slashes = line.count('\\')
    return (len(line) + qoutes + slashes + 2)

def test_count_code():
    assert count_code(r'""') == 2
    assert count_code(r'"abc"') == 5
    assert count_code(r'"aaa\"aaa"') == 10
    assert count_code(r'"\x27"') == 6

def test_count_char():
    assert count_char(r'""') == 0
    assert count_char(r'"abc"') == 3
    assert count_char(r'"aaa\"aaa"') == 7
    assert count_char(r'"\x27"') == 1

def test_count_reencode():
    assert count_reencode(r'""') == 6
    assert count_reencode(r'"abc"') == 9
    assert count_reencode(r'"aaa\"aaa"') == 16
    assert count_reencode(r'"\x27"') == 11
    assert count_reencode(r'"\\"') == 10

def solve(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split('\n') if n != '']

    print('testing ', end='')
    test_count_char()
    test_count_code()
    test_count_reencode()
    print('done')

    print('solving')
    sum_code = sum([count_code(n) for n in puzzle_input])
    sum_char = sum([count_char(n) for n in puzzle_input])
    print(f'solution 1: {sum_code - sum_char}')
    sum_reencode = sum([count_reencode(n) for n in puzzle_input])
    print(f'solution 2: {sum_reencode - sum_code}')