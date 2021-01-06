import itertools

def unique_guests(puzzle_input):
    return set([r[0] for r in puzzle_input])


def parse_relations(puzzle_input: [[str]]) -> {str: {str: int}}:
    relations = {}
    for guest in unique_guests(puzzle_input):
        relations.update({guest: {}})
        for rel in [n for n in puzzle_input if n[0]==guest]:
            if rel[2] == 'lose':
                relations[guest].update({rel[-1]: int(rel[3])*-1})
            else:
                relations[guest].update({rel[-1]: int(rel[3])})
    return relations


def calc_all_seatorders(relations, seat_self=False):
    guests = unique_guests(relations)
    if seat_self:
        guests.update({'Me'})

    tables = []
    for seat_order in itertools.permutations(guests, len(guests)):
        tables.append({
            "order": seat_order,
            "hapiness": calculate_happienes(seat_order, parse_relations(relations))
        })
    return tables


def calculate_happienes(seat_order, relations):
    happienes = 0
    for n, guest in enumerate(seat_order[1:] + seat_order[:1]):
        if guest in relations and seat_order[n] in relations[guest]:
            happienes += relations[guest][seat_order[n]]
        if seat_order[n] in relations and guest in relations[seat_order[n]]:
            happienes += relations[seat_order[n]][guest]
    return happienes

def test_unique():
    guests = unique_guests([
        ["Alice", "would", "lose", "2", "happiness", "units", "by", "sitting", "next", "to", "Bob"],
        ["Bob", "would", "gain", "93", "happiness", "units", "by", "sitting", "next", "to", "Alice"]
    ])
    assert guests == {"Alice", "Bob"}

def test_parse_relation():
    rel = parse_relations([
        ["Alice", "would", "lose", "2", "happiness", "units", "by", "sitting", "next", "to", "Bob"],
        ["Bob", "would", "gain", "93", "happiness", "units", "by", "sitting", "next", "to", "Alice"]
    ])
    assert rel == {'Alice': {'Bob': -2}, "Bob": {"Alice": 93}}

def test_calc_happy():
    rel = {'A': {'B': -2, "C": 5}, "B": {"A": 93, "C": 1}, "C": {"A": 1, "B": -35}}
    seat_order = ["A", "B", "C"]
    assert calculate_happienes(seat_order, rel) == 63

def solve(puzzle_input):
    puzzle_input = [n.split(' ') for n in puzzle_input.replace('.', '').split('\n') if n != '']
    print('testing ', end='')
    test_unique()
    test_parse_relation()
    test_calc_happy()
    print('done')

    print('solving')
    print(f'solution 1: {max(calc_all_seatorders(puzzle_input), key=lambda x: x["hapiness"])}')
    print(f'solution 2: {max(calc_all_seatorders(puzzle_input, True), key=lambda x: x["hapiness"])}')