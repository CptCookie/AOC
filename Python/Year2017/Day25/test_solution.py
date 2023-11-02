from .solution import solution_1, solution_2, parse_input, run_turing_machine

TEST_INPUT = """
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
"""

TEST_DATA = {
    "A": [(1, 1, "B"), (0, -1, "B")],
    "B": [(1, -1, "A"), (1, 1, "A")],
}


def test_parsing():
    steps, instr = parse_input(TEST_INPUT)
    assert steps == 6
    assert instr == TEST_DATA


def test_turing_machine():
    assert run_turing_machine(TEST_DATA, 6) == 3


def test_solution_1():
    assert solution_1(TEST_INPUT) == 3


def test_solution_2():
    assert solution_2(TEST_INPUT)
