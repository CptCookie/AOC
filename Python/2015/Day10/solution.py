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
   

def solve(puzzle_input):
    puzzle_input = int(puzzle_input.split('\n')[0])

    print('solving')
    for n, elem in enumerate(look_and_say(puzzle_input)):
        if n == 39:
            print(f'solution 1: {len(str(elem))}')
        if n == 49:
            print(f'solution 2: {len(str(elem))}')
        if n > 49:
            break