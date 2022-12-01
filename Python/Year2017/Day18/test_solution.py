from .solution import solution_1, solution_2, Worker


TEST_DATA = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""


def test_solution_1():
    assert solution_1(TEST_DATA) == 4


def test_receive():
    w = Worker(2, [("rcv", "a")])
    w.input_buffer.append(22)
    w.execute_pointer()

    assert w.registers["p"] == 2
    assert w.registers["a"] == 22
    assert w.pc == 1


def test_receive_empty():
    w = Worker(2, [("rcv", "a")])
    w.execute_pointer()

    assert w.registers["a"] == 0
    assert w.pc == 0


def test_send():
    w_receive = Worker(1, [])
    w_send = Worker(2, [("snd", "a")])
    w_send.registers["a"] = 22
    w_send.receiver = w_receive
    w_send.execute_pointer()

    assert w_send.pc == 1
    assert w_receive.input_buffer == [22]


def test_solution_2():
    test_input = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""
    assert solution_2(test_input) == 3
