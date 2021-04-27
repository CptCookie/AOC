from .solution import solution_1, solution_2, get_fuel_for_mass, get_fuel_complete


def test_fuel_v1_1():
    assert get_fuel_for_mass(12) == 2
    assert get_fuel_for_mass(14) == 2
    assert get_fuel_for_mass(1969) == 654
    assert get_fuel_for_mass(100756) == 33583


def test_fuel_v2_1():
    assert get_fuel_complete(12) == 2
    assert get_fuel_complete(14) == 2
    assert get_fuel_complete(1969) == 966
    assert get_fuel_complete(100756) == 50346


def test_solution_1():
    test_input = "12\n14\n1969\n100756"
    assert solution_1(test_input) == 2 + 2 + 654 + 33583


def test_solution_2():
    test_input = "12\n14\n1969\n100756"
    assert solution_2(test_input) == 2 + 2 + 966 + 50346
