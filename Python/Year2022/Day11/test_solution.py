from .solution import (
    Monkey,
    parse_data,
    run_monkey,
    run_round,
    solution_1,
    solution_2,
)

TEST_INPUT = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def test_parse_data():
    data = parse_data(TEST_INPUT)

    for name in ["monkey 0", "monkey 1", "monkey 2", "monkey 3"]:
        assert name in data

    assert data["monkey 0"].items == [79, 98]
    assert data["monkey 0"].operation == "old * 19"
    assert data["monkey 0"].division == 23
    assert data["monkey 0"].true == "monkey 2"
    assert data["monkey 0"].false == "monkey 3"


def test_operate():
    m = Monkey([], "", 0, "", "")
    assert m.new_value(11, "old * 6") == 22
    assert m.new_value(9, "old * old") == 27
    assert m.new_value(2, "old + 3") == 1

    m.manage_worry = lambda x: x
    assert m.new_value(11, "old * 6") == 66
    assert m.new_value(9, "old * old") == 81
    assert m.new_value(2, "old + 3") == 5


def test_run_monkey():
    data = parse_data(TEST_INPUT)

    run_monkey(data["monkey 0"], data)

    assert data["monkey 0"].items == []
    assert data["monkey 0"].inspected == 2
    assert 500 in data["monkey 3"].items
    assert 620 in data["monkey 3"].items


def test_run_all_monkeys():
    data = parse_data(TEST_INPUT)

    run_round(data)

    assert data["monkey 0"].items == [20, 23, 27, 26]
    assert data["monkey 1"].items == [2080, 25, 167, 207, 401, 1046]
    assert data["monkey 2"].items == []
    assert data["monkey 3"].items == []


def test_solution_1():
    assert solution_1(TEST_INPUT) == 10605


def test_solution_2():
    assert solution_2(TEST_INPUT) == 2_713_310_158
