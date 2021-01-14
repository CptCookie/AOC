from solution import unique_guests, parse_relations, calculate_happienes


def test_unique():
    guests = unique_guests(
        [
            [
                "Alice",
                "would",
                "lose",
                "2",
                "happiness",
                "units",
                "by",
                "sitting",
                "next",
                "to",
                "Bob",
            ],
            [
                "Bob",
                "would",
                "gain",
                "93",
                "happiness",
                "units",
                "by",
                "sitting",
                "next",
                "to",
                "Alice",
            ],
        ]
    )
    assert guests == {"Alice", "Bob"}


def test_parse_relation():
    rel = parse_relations(
        [
            [
                "Alice",
                "would",
                "lose",
                "2",
                "happiness",
                "units",
                "by",
                "sitting",
                "next",
                "to",
                "Bob",
            ],
            [
                "Bob",
                "would",
                "gain",
                "93",
                "happiness",
                "units",
                "by",
                "sitting",
                "next",
                "to",
                "Alice",
            ],
        ]
    )
    assert rel == {"Alice": {"Bob": -2}, "Bob": {"Alice": 93}}


def test_calc_happy():
    rel = {"A": {"B": -2, "C": 5}, "B": {"A": 93, "C": 1}, "C": {"A": 1, "B": -35}}
    seat_order = ["A", "B", "C"]
    assert calculate_happienes(seat_order, rel) == 63
