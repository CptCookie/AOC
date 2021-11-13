from .solution import solution_1, solution_2, NumberCode, RombicCode


def test_solution_1():
    pass


def test_solution_2():
    pass


def test_decode_number_U():
    code = NumberCode()
    code.decode_number("U")
    assert code.number == "2"


def test_decode_number_UU():
    code = NumberCode()
    code.decode_number("UU")
    assert code.number == "2"


def test_decode_number_R():
    code = NumberCode()
    code.decode_number("R")
    assert code.number == "6"


def test_decode_number_RR():
    code = NumberCode()
    code.decode_number("RR")
    assert code.number == "6"


def test_decode_number_D():
    code = NumberCode()
    code.decode_number("D")
    assert code.number == "8"


def test_decode_number_DD():
    code = NumberCode()
    code.decode_number("DD")
    assert code.number == "8"


def test_decode_number_L():
    code = NumberCode()
    code.decode_number("L")
    assert code.number == "4"


def test_decode_number_L():
    code = NumberCode()
    code.decode_number("LL")
    assert code.number == "4"


def test_decode_number():
    code = NumberCode()
    code.decode_number("UURR")
    assert code.number == "3"


def test_decode_rombic_U():
    code = RombicCode()
    code.decode_number("UU")
    assert code.number == "1"


def test_decode_rombic_UU():
    code = RombicCode()
    code.decode_number("UUR")
    assert code.number == "1"


def test_decode_rombic_R():
    code = RombicCode()
    code.decode_number("RR")
    assert code.number == "9"


def test_decode_rombic_RR():
    code = RombicCode()
    code.decode_number("RRU")
    assert code.number == "9"


def test_decode_rombic_D():
    code = RombicCode()
    code.decode_number("DD")
    assert code.number == "D"


def test_decode_rombic_DD():
    code = RombicCode()
    code.decode_number("DDL")
    assert code.number == "D"


def test_decode_rombic_L():
    code = RombicCode()
    code.decode_number("LL")
    assert code.number == "5"


def test_decode_rombic_L():
    code = RombicCode()
    code.decode_number("LLU")
    assert code.number == "5"
