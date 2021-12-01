from .solution import hand_over, handle_chips, input_chips, parse_instr

test_data = """value 5 goes to bot 2
bot 0 gives low to output 2 and high to output 0
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
value 2 goes to bot 2
"""


def test_parse():
    instr = parse_instr(test_data)

    assert instr == [
        ("5", "bot 2"),
        ("bot 0", "output 2", "output 0"),
        ("bot 2", "bot 1", "bot 0"),
        ("3", "bot 1"),
        ("bot 1", "output 1", "bot 0"),
        ("2", "bot 2"),
    ]


def test_hand_over():
    result = hand_over(("bot 1", "bot 4", "bot 3"), {"bot 1": [2, 4], "bot 4": [1]})
    assert result == {"bot 1": [2, 4], "bot 4": [1, 2], "bot 3": [4]}


def test_input_chips():
    inst = parse_instr(test_data)
    start_bots = input_chips(inst)

    assert start_bots == {
        "bot 2": [5, 2],
        "bot 1": [3],
    }


def test_handle():
    inst = parse_instr(test_data)
    bots = input_chips(inst)
    bots = handle_chips(inst, bots)

    expected = {
        "output 0": [5],
        "output 1": [2],
        "output 2": [3],
        "bot 2": [5, 2],
        "bot 1": [3, 2],
        "bot 0": [5, 3],
    }

    for key in expected:
        assert key in bots
        assert expected[key] == bots[key]
