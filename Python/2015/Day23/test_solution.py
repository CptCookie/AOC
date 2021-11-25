from .solution import Computer


# def test_parse_command():
#     assert Computer(["hlf a"]).parse_command() == ("hlf", "a")
#     assert Computer(["tpl a"]).parse_command() == ("tpl", "a")
#     assert Computer(["inc a"]).parse_command() == ("inc", "a")
#     assert Computer(["jmp +12"]).parse_command() == ("jmp", "+12")
#     assert Computer(["jmp -12"]).parse_command() == ("jmp", "-12")
#     assert Computer(["jie a, -23"]).parse_command() == ("jie", "a", "-23")
#     assert Computer(["jio b, +23"]).parse_command() == ("jio", "b", "+23")


def test_hlv():
    pc = Computer(["hlf a"])
    pc.register["a"] = 42
    pc.execute_programm()
    assert pc.register["a"] == 21


def test_tpl():
    pc = Computer(["tpl a"])
    pc.register["a"] = 10
    pc.execute_programm()
    assert pc.register["a"] == 30


def test_inc():
    pc = Computer(["inc a"])
    pc.execute_programm()
    assert pc.register["a"] == 1


def test_jmp():
    pc = Computer(["inc a", "jmp 3", "inc a", "inc a"])
    pc.execute_programm()
    assert pc.register["a"] == 1


def test_jie_not():
    pc = Computer(["inc a", "jie a, 3", "inc a ", "inc a"])
    pc.execute_programm()
    assert pc.register["a"] == 3


def test_jie():
    pc = Computer(["inc a", "inc a", "jie a, 3", "inc a ", "inc a"])
    pc.execute_programm()
    assert pc.register["a"] == 2


def test_jio_not():
    pc = Computer(["inc a", "inc a", "jio a, 3", "inc a ", "inc a", "inc a"])
    pc.execute_programm()
    assert pc.register["a"] == 5


def test_jio():
    pc = Computer(["inc a", "jio a, 3", "inc a ", "inc a"])
    pc.execute_programm()
    assert pc.register["a"] == 1
