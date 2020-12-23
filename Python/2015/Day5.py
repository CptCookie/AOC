alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowls = 'aeiuo'
doubles = [n+n for n in alphabet]
disalow = ['ab', 'cd', 'pq', 'xy']

def is_naughty_old(text:str):
    if sum([text.count(n) for n in vowls]) < 3:
        return True
    if not any([n in text for n in doubles]):
        return True
    if any([n in text for n in disalow]):
        return True
    return False

def has_double(text):
    pairs = [text[n]+elem for n, elem in enumerate(text[1:])]
    return any([text.index(n)+1 < text.rindex(n) for n in pairs])

def has_two_apart(text):
    return any([text[n] == elem for n, elem in enumerate(text[2:])])

def is_naughty_new(text):
    return not has_double(text) or not has_two_apart(text)

def test_has_double():
    assert has_double('xxyxx') == True
    assert has_double('abxxxjf') == False
    assert has_double('xx') == False

def test_two_apart():
    assert has_two_apart('xyx') == True
    assert has_two_apart('qjhvhtzxzqqjkmpb') == True
    assert has_two_apart('uurcxstgmygtbstg') == False

def test_naughty_old():
    assert is_naughty_old('ugknbfddgicrmopn') == False
    assert is_naughty_old('jchzalrnumimnmhp') == True
    assert is_naughty_old('haegwjzuvuyypxyu') == True
    assert is_naughty_old('dvszwmarrgswjxmb') == True

def test_naughty_new():
    assert is_naughty_new('qjhvhtzxzqqjkmpb') == False
    assert is_naughty_new('xxyxx') == False
    assert is_naughty_new('uurcxstgmygtbstg') == True
    assert is_naughty_new('ieodomkazucvgmuy') == True

def solve(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split('\n') if n != '']
    
    print('testing')
    test_naughty_old()
    test_has_double()
    test_two_apart()
    test_naughty_new()

    print('solving')
    print(f'solution 1: {len([n for n in puzzle_input if not is_naughty_old(n)])}')
    print(f'solution 2: {len([n for n in puzzle_input if not is_naughty_new(n)])}')

