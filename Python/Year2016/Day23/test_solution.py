from .solution import solution_1, solution_2, parse_input, AssemBunnyComputer

TEST_INPUT = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""

TEST_DATA = [
    ["cpy", 2, "a"],
    ["tgl", "a"],
    ["tgl", "a"],
    ["tgl", "a"],
    ["cpy", 1, "a"],
    ["dec", "a"],
    ["dec", "a"],
]


def test_example():
    prog = AssemBunnyComputer(TEST_DATA)
    prog.run_instr()

    assert prog["a"] == 3


def test_tgl_inc():
    inst = [["cpy", 1, "a"], ["tgl", "a"], ["dec", "a"]]
    prog = AssemBunnyComputer(inst)
    prog.run_instr()

    assert prog.instr == [["cpy", 1, "a"], ["tgl", "a"], ["inc", "a"]]
    assert prog["a"] == 2


def test_tgl_dec():
    inst = [["cpy", 1, "a"], ["tgl", "a"], ["inc", "a"]]
    prog = AssemBunnyComputer(inst)
    prog.run_instr()

    assert prog.instr == [["cpy", 1, "a"], ["tgl", "a"], ["dec", "a"]]
    assert prog["a"] == 0


def test_tgl_self():
    inst = [["tgl", "a"]]
    prog = AssemBunnyComputer(inst)
    prog.run_instr()

    assert prog.instr == [["inc", "a"]]


def test_tgl_cpy():
    inst = [["cpy", 1, "a"], ["tgl", "a"], ["cpy", 4, "a"]]
    prog = AssemBunnyComputer(inst)
    prog.run_instr()

    assert prog.instr == [["cpy", 1, "a"], ["tgl", "a"], ["jnz", 4, "a"]]
    assert prog["a"] == 1


def test_tgl_jnz():
    inst = [["cpy", 1, "a"], ["tgl", "a"], ["jnz", 4, "a"]]
    prog = AssemBunnyComputer(inst)
    prog.run_instr()

    assert prog.instr == [["cpy", 1, "a"], ["tgl", "a"], ["cpy", 4, "a"]]
    assert prog["a"] == 4


def test_invalid():
    inst = [["cpy", 1, "a"], ["tgl", "a"], ["jnz", 4, 1]]
    prog = AssemBunnyComputer(inst)
    prog.run_instr()

    assert prog.instr == [["cpy", 1, "a"], ["tgl", "a"], ["cpy", 4, 1]]
    assert prog["a"] == 1
