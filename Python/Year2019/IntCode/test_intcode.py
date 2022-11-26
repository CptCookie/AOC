from .IntCode import IntCodeProgramm


def test_add():
    programm = IntCodeProgramm([1, 1, 1, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [1, 1, 1, 5, 99, 2]


def test_multiplie():
    programm = IntCodeProgramm([2, 0, 3, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [2, 0, 3, 5, 99, 10]


def test_input():
    programm = IntCodeProgramm([3, 3, 99, 0])
    programm.write_input(22)
    programm.run_programm()
    assert programm.memory == [3, 3, 99, 22]


def test_output():
    programm = IntCodeProgramm([4, 3, 99, 43])
    programm.run_programm()
    assert programm.output == [43]


def test_jump_if_true():
    programm = IntCodeProgramm([1005, 3, 7, 1, 0, 0, 8, 99, 0])
    programm.run_programm()
    assert programm.memory == [1005, 3, 7, 1, 0, 0, 8, 99, 0]


def test_jump_if_true_not():
    programm = IntCodeProgramm([1005, 4, 7, 1, 0, 0, 8, 99, 0])
    programm.run_programm()
    assert programm.memory == [1005, 4, 7, 1, 0, 0, 8, 99, 2010]


def test_jump_if_false():
    programm = IntCodeProgramm([1006, 4, 7, 1, 0, 0, 8, 99, 0])
    programm.run_programm()
    assert programm.memory == [1006, 4, 7, 1, 0, 0, 8, 99, 0]


def test_jump_if_false_not():
    programm = IntCodeProgramm([1006, 3, 7, 1, 0, 0, 8, 99, 0])
    programm.run_programm()
    assert programm.memory == [1006, 3, 7, 1, 0, 0, 8, 99, 2012]


def test_less_then():
    programm = IntCodeProgramm([7, 1, 0, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [7, 1, 0, 5, 99, 1]


def test_less_ten_not():
    programm = IntCodeProgramm([7, 0, 1, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [7, 0, 1, 5, 99, 0]


def test_equal():
    programm = IntCodeProgramm([8, 0, 0, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [8, 0, 0, 5, 99, 1]


def test_equal_not():
    programm = IntCodeProgramm([8, 0, 1, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [8, 0, 1, 5, 99, 0]


def test_address_add_immediate():
    programm = IntCodeProgramm([1101, 3, 4, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [1101, 3, 4, 5, 99, 7]


def test_address_multi_immediate():
    programm = IntCodeProgramm([1102, 3, 4, 5, 99, 0])
    programm.run_programm()
    assert programm.memory == [1102, 3, 4, 5, 99, 12]


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


def test_jump_sequence_1():
    programm = IntCodeProgramm([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8])
    programm.write_input(1)
    programm.run_programm()
    assert programm.output.pop() == 0


def test_jump_sequence_2():
    programm = IntCodeProgramm([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8])
    programm.write_input(8)
    programm.run_programm()
    assert programm.output.pop() == 1


def test_jump_sequence_3():
    programm = IntCodeProgramm([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8])
    programm.write_input(1)
    programm.run_programm()
    assert programm.output.pop() == 1


def test_jump_sequence_4():
    programm = IntCodeProgramm([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8])
    programm.write_input(8)
    programm.run_programm()
    assert programm.output.pop() == 0


def test_jump_sequence_immeadiate_1():
    programm = IntCodeProgramm([3, 3, 1108, -1, 8, 3, 4, 3, 99])
    programm.write_input(8)
    programm.run_programm()
    assert programm.output.pop() == 1


def test_jump_sequence_immeadiate_2():
    programm = IntCodeProgramm([3, 3, 1108, -1, 8, 3, 4, 3, 99])
    programm.write_input(1)
    programm.run_programm()
    assert programm.output.pop() == 0


def test_jump_sequence_immeadiate_3():
    programm = IntCodeProgramm([3, 3, 1107, -1, 8, 3, 4, 3, 999])
    programm.write_input(7)
    programm.run_programm()
    assert programm.output.pop() == 1


def test_jump_sequence_immeadiate_4():
    programm = IntCodeProgramm([3, 3, 1107, -1, 8, 3, 4, 3, 999])
    programm.write_input(8)
    programm.run_programm()
    assert programm.output.pop() == 0


def test_jump_bigger_sequence_1():
    programm = IntCodeProgramm(
        [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    )
    programm.write_input(0)
    programm.run_programm()
    assert programm.output.pop() == 0


def test_jump_bigger_sequence_2():
    programm = IntCodeProgramm(
        [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    )
    programm.write_input(20)
    programm.run_programm()
    assert programm.output.pop() == 1


def test_jump_bigger_sequence_3():
    programm = IntCodeProgramm([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1])
    programm.write_input(0)
    programm.run_programm()
    assert programm.output.pop() == 0


def test_jump_bigger_sequence_4():
    programm = IntCodeProgramm([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1])
    programm.write_input(23)
    programm.run_programm()
    assert programm.output.pop() == 1


def test_jump_biggest_sequence_1():
    # fmt: off
    programm = IntCodeProgramm(
        [
            3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
        ]
    )
    # fmt: on
    programm.write_input(7)
    programm.run_programm()
    assert programm.output.pop() == 999


def test_jump_biggest_sequence_2():
    # fmt: off
    programm = IntCodeProgramm(
        [
            3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
        ]
    )
    # fmt: on
    programm.write_input(8)
    programm.run_programm()
    assert programm.output.pop() == 1000


def test_jump_biggest_sequence_3():
    # fmt: off
    programm = IntCodeProgramm(
        [
            3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
        ]
    )
    # fmt: on
    programm.write_input(9)
    programm.run_programm()
    assert programm.output.pop() == 1001
