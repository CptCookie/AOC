from .solution import solution_1, solution_2, IntCodeProgramm


def test_intcode_sequence_1():
    programm = IntCodeProgramm([1, 0, 0, 0, 99])
    programm.run_programm()
    assert programm.memory == [2, 0, 0, 0, 99]


def test_intcode_sequence_2():
    programm = IntCodeProgramm([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    programm.run_programm()
    assert programm.memory == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_intcode_sequence_3():
    programm = IntCodeProgramm([2, 3, 0, 3, 99])
    programm.run_programm()
    assert programm.memory == [2, 3, 0, 6, 99]


def test_intcode_sequence_4():
    programm = IntCodeProgramm([2, 4, 4, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [2, 4, 4, 5, 99, 9801]


def test_intcode_sequence_5():
    programm = IntCodeProgramm([1, 1, 1, 4, 99, 5, 6, 0, 99])
    programm.run_programm()
    assert programm.memory == [30, 1, 1, 4, 2, 5, 6, 0, 99]
