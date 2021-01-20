from .solution import parse_substitutions, get_all_products, get_number_of_steps_to


def test_parse():
    test_input = ["H => HO", "H => OH", "O => HH"]
    assert parse_substitutions(test_input) == [
        ("H", "HO"),
        ("H", "OH"),
        ("O", "HH"),
    ]


def test_all_prod():
    test_subs = [
        ("H", "HO"),
        ("H", "OH"),
        ("O", "HH"),
    ]

    expected = [
        "HOOH",
        "HOHO",
        "OHOH",
        "HOOH",
        "HHHH",
    ]
    assert get_all_products("HOH", test_subs) == expected
