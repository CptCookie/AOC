from .solution import number_valid_triange_col, solution_2, hundred


def test_hundred():
    assert hundred(1129) == 1
    assert hundred(1000) == 0
    assert hundred(10) == 0


def test_number_triangle_col():
    test_values = [101, 102, 103, 201, 202, 203]
    assert number_valid_triange_col(test_values) == 2


def test_solution_2():
    test_input = """  101 301 501
                102 302 502
                103 303 503
                201 401 601
                202 402 602
                203 403 603"""

    assert solution_2(test_input) == 6