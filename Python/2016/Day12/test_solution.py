from .solution import parse_data, solution_1, solution_2, AssemBunnyComputer


def test_cpy_int():
    c = AssemBunnyComputer([])
    c.cpy("a", 12)
    assert c.registers["a"] == 12


def test_cpy_str():
    c = AssemBunnyComputer([])
    c.cpy("a", "23")
    assert c.registers["a"] == 23


def test_cpy_mem():
    c = AssemBunnyComputer([])
    c.cpy("a", 23)
    c.cpy("b", "a")
    assert c.registers["b"] == 23


def test_inr():
    c = AssemBunnyComputer([])
    c.inc("b")
    assert c.registers["b"] == 1


def test_dec():
    c = AssemBunnyComputer([])
    c.cpy("c", 24)
    c.dec("c")
    assert c.registers["c"] == 23


def test_jnz():
    c = AssemBunnyComputer([])
    c.cpy("a", 12)
    c.jnz("a", 2)
    assert c.instr_pointer == 2


def test_jnz_int():
    c = AssemBunnyComputer([])
    c.jnz("2", "2")
    assert c.instr_pointer == 2


def test_run_instr():
    c = AssemBunnyComputer(["cpy 41 a", "inc a", "inc a", "dec a", "jnz a 2", "dec a"])
    c.run_instr()

    assert c.registers["a"] == 42


def test_parser():
    data = parse_data("cpy 41 a\ninc a\ninc a\ndec a\njnz a 2\ndec a\n")
    expected = ["cpy 41 a", "inc a", "inc a", "dec a", "jnz a 2", "dec a"]
    assert data == expected


def test_solution_1():
    test_input = "cpy 41 a\ninc a\ninc a\ndec a\njnz a 2\ndec a\n"
    assert solution_1(test_input) == 42
