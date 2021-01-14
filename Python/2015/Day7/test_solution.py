from .solution import Programm


def test_execute():
    instruction = ["1 -> a", "a LSHIFT 1 -> b", "a OR b -> c"]
    prog = Programm(instruction)
    prog.run()
    assert prog.mem == {"a": 1, "b": 2, "c": 3}

    instruction = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]
    prog = Programm(instruction)
    prog.run()
    assert prog.mem == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }
