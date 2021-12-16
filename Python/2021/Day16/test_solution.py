from .solution import *


# def test_read_value_pkg():
#     b, pkg = read_next_pkg("1101001011111110001010001")

#     assert pkg.version == 6
#     assert pkg.id == 4
#     assert pkg.value == 2021
#     assert pkg.binary == "110100101111111000101000"
#     assert b == "1"


def test_read_value_pkg_comination():
    b, pkg = read_next_pkg("110100010100101001000100100", True)

    assert pkg.version == 6
    assert pkg.id == 4
    assert pkg.value == 10
    assert pkg.binary == "11010001010"
    assert b == "0101001000100100"


def test_read_op_pkg_length():
    b, pkg = read_next_operator_pkg(
        "001110000000000001101111010001010010100100010010000000001"
    )
    assert pkg.version == 1
    assert pkg.id == 6
    assert len(pkg.pkg) == 2
    assert pkg.pkg[0].value == 10
    assert pkg.pkg[0].binary == "11010001010"
    assert pkg.pkg[1].value == 20
    assert pkg.pkg[1].binary == "0101001000100100"
    assert pkg.binary == "00111000000000000110111101000101001010010001001000000000"
    assert b == "1"


def test_read_op_pkg_number():
    b, pkg = read_next_operator_pkg(
        "111011100000000011010100000011001000001000110000011000001"
    )
    assert pkg.version == 7
    assert pkg.id == 3
    assert len(pkg.pkg) == 3
    assert pkg.pkg[0].value == 1
    assert pkg.pkg[0].binary == "01010000001"
    assert pkg.pkg[1].value == 2
    assert pkg.pkg[1].binary == "10010000010"
    assert pkg.pkg[2].value == 3
    assert pkg.pkg[2].binary == "00110000011"
    assert pkg.binary == "11101110000000001101010000001100100000100011000001100000"
    assert b == "1"


# def test_solution_1():
#     test_input = ""
#     assert False


def test_solution_2_1():
    test_input = "C200B40A82"
    assert solution_2(test_input) == 3
