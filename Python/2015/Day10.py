def get_sequences(value:int) -> [[int]]:
    sequence = []
    buffer = [str(value)[0]]
    for digit in str(value)[1:]:
        if buffer[0] == digit:
            buffer.append(digit)
        else:
            sequence.append(buffer)
            buffer = [digit]
    sequence.append(buffer)
    return sequence


def newValue(value:int):
    sequences = get_sequences(value)
    newValue = ''
    for s in sequences:
        newValue += f'{len(s)}{s[0]}'
    return newValue
    

def look_and_say(init_value:int):
    n = 0
    value = init_value
    while n <= 100 :
        value = newValue(value)
        yield value

def test_sequencing():
    assert get_sequences(1) == [['1']]
    assert get_sequences(11) == [["1","1"]]
    assert get_sequences(21) == [["2"],["1"]]
    assert get_sequences(1211) == [["1"],["2"],["1","1"]]
    assert get_sequences(111221) == [["1","1","1"],["2","2"],["1"]]

def test_new_value():
    assert newValue(1) == '11'
    assert newValue(11) == '21'
    assert newValue(21) == '1211'
    assert newValue(1211) == '111221'
    assert newValue(111221) == '312211'

def test_look_and_say():
    result = ["11","21","1211","111221","312211"]
    for n, number in enumerate(look_and_say(1)):
        try: 
            assert result[n] == number
        except IndexError:
            return
    

def solve(puzzle_input):
    puzzle_input = int(puzzle_input.split('\n')[0])

    print('testing ', end='')
    test_sequencing()
    test_new_value()
    test_look_and_say()
    print('done')

    print('solving')

    for n, elem in enumerate(look_and_say(puzzle_input)):
        if n >= 40:
            print(n)
        if n == 39:
            print(f'solution 1: {len(str(elem))}')
        if n == 49:
            print(f'solution 2: {len(str(elem))}')
        if n > 49:
            break