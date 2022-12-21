from .solution import solution_1, solution_2, parse_input

TEST_INPUT = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""



def test_parsing():
    root, humn = parse_input(TEST_INPUT)
    assert root.name == "root"
    assert root.value == 152


def test_solution_1():
    assert solution_1(TEST_INPUT) == 152


def test_solution_2():
    assert solution_2(TEST_INPUT) == 301
