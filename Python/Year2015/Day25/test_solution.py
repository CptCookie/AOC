from .solution import get_number, get_table_number


def test_table_number():
    assert get_table_number(1, 1) == 1
    assert get_table_number(1, 2) == 2
    assert get_table_number(1, 3) == 4
    assert get_table_number(1, 4) == 7
    assert get_table_number(1, 5) == 11
    assert get_table_number(2, 1) == 3
    assert get_table_number(2, 2) == 5
    assert get_table_number(2, 3) == 8
    assert get_table_number(2, 4) == 12
    assert get_table_number(2, 5) == 17
    assert get_table_number(3, 1) == 6
    assert get_table_number(3, 2) == 9
    assert get_table_number(3, 3) == 13
    assert get_table_number(3, 4) == 18
    assert get_table_number(3, 5) == 24
    assert get_table_number(4, 1) == 10
    assert get_table_number(4, 2) == 14
    assert get_table_number(4, 3) == 19
    assert get_table_number(4, 4) == 25
    assert get_table_number(4, 5) == 32
    assert get_table_number(5, 1) == 15
    assert get_table_number(5, 2) == 20
    assert get_table_number(5, 3) == 26
    assert get_table_number(5, 4) == 33
    assert get_table_number(5, 5) == 41


def test_get_number():
    assert get_number(1, 1) == 20151125
    assert get_number(1, 2) == 31916031
    assert get_number(1, 3) == 16080970
    assert get_number(1, 4) == 24592653
    assert get_number(1, 5) == 77061
    assert get_number(2, 1) == 18749137
    assert get_number(2, 2) == 21629792
    assert get_number(2, 3) == 8057251
    assert get_number(2, 4) == 32451966
    assert get_number(2, 5) == 17552253
    assert get_number(3, 1) == 17289845
    assert get_number(3, 2) == 16929656
    assert get_number(3, 3) == 1601130
    assert get_number(3, 4) == 21345942
    assert get_number(3, 5) == 28094349
    assert get_number(4, 1) == 30943339
    assert get_number(4, 2) == 7726640
    assert get_number(4, 3) == 7981243
    assert get_number(4, 4) == 9380097
    assert get_number(4, 5) == 6899651
    assert get_number(5, 1) == 10071777
    assert get_number(5, 2) == 15514188
    assert get_number(5, 3) == 11661866
    assert get_number(5, 4) == 10600672
    assert get_number(5, 5) == 9250759
