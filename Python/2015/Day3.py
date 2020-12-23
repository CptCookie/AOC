
UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'

def map_moves(puzzel_input):
    pos = [[0,0]]
    for direction in puzzel_input:
        current = pos[-1]
        if direction is UP:
            pos.append([current[0], current[1]+1])
        elif direction is DOWN:
            pos.append([current[0], current[1]-1])
        elif direction is RIGHT:
            pos.append([current[0]+1, current[1]])
        elif direction is LEFT:
            pos.append([current[0]-1, current[1]])
    return pos

def get_unique(lst: []):
    return [x for n, x in enumerate(lst) if lst.index(x) == n]

def test_map_moves():
    assert map_moves('^>v<') == [[0,0], [0,1], [1,1], [1,0], [0,0]]

def test_unique():
    assert get_unique(map_moves('^v^v^v^v')) == [[0,0], [0,1]]

def solve(puzzle_input):
    print('testing')
    test_map_moves()
    test_unique()

    print('solving')
    print(f'solution 1: {len(get_unique(map_moves(puzzle_input)))}')

    santa = puzzle_input[::2]
    robo = puzzle_input[1::2]
    print(f'solution 2: {len(get_unique(map_moves(santa) + map_moves(robo)))}')


