import itertools


def unique_guests(puzzle_input):
    return set([r[0] for r in puzzle_input])


def parse_relations(puzzle_input: [[str]]) -> {str: {str: int}}:
    relations = {}
    for guest in unique_guests(puzzle_input):
        relations.update({guest: {}})
        for rel in [n for n in puzzle_input if n[0] == guest]:
            if rel[2] == "lose":
                relations[guest].update({rel[-1]: int(rel[3]) * -1})
            else:
                relations[guest].update({rel[-1]: int(rel[3])})
    return relations


def calc_all_seatorders(relations, seat_self=False):
    guests = unique_guests(relations)
    if seat_self:
        guests.update({"Me"})

    tables = []
    for seat_order in itertools.permutations(guests, len(guests)):
        tables.append(
            {
                "order": seat_order,
                "hapiness": calculate_happienes(seat_order, parse_relations(relations)),
            }
        )
    return tables


def calculate_happienes(seat_order, relations):
    happienes = 0
    for n, guest in enumerate(seat_order[1:] + seat_order[:1]):
        if guest in relations and seat_order[n] in relations[guest]:
            happienes += relations[guest][seat_order[n]]
        if seat_order[n] in relations and guest in relations[seat_order[n]]:
            happienes += relations[seat_order[n]][guest]
    return happienes


def solution_1(puzzle_input):
    puzzle_input = [
        n.split(" ") for n in puzzle_input.replace(".", "").split("\n") if n != ""
    ]
    return max(calc_all_seatorders(puzzle_input), key=lambda x: x["hapiness"])


def solution_2(puzzle_input):
    puzzle_input = [
        n.split(" ") for n in puzzle_input.replace(".", "").split("\n") if n != ""
    ]
    return max(calc_all_seatorders(puzzle_input, True), key=lambda x: x["hapiness"])
