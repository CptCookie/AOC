from .solution import solution_1, solution_2, Memory


test_input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


def test_solution_mem():
    mem = Memory()
    mem.execute(("utc", "dec", "-736", "p", ">", "-7"))
    assert mem.registers["utc"] == 736


def test_solution_1():
    assert solution_1(test_input) == 1


def test_solution_2():
    assert solution_2(test_input) == 10
