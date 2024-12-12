from .solution import (
    solution_1,
    solution_2,
    parse_input,
    get_all_plots,
    get_number_faces,
)

TEST_INPUT_EASY = """AAAA
BBCD
BBCC
EEEC
"""
TEST_INPUT_COMPLEX = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

TEST_REDDIT_1 = """AAXXX
AAXAX
AAAAX
AAXAX
AAXXX
"""

TEST_REDDIT_2 = """
OOHHH
HOHOH
HHHOH
"""

TEST_REDDIT_3 = """AAAAAAAA
AACBBDDA
AACBBAAA
ABBAAAAA
ABBADDDA
AAAADADA
AAAAAAAA
"""

TEST_REDDIT_4 = """CCAAA
CCAAA
AABBA
AAAAA
"""


def test_get_plots():
    assert get_all_plots(parse_input(TEST_INPUT_EASY)) == [
        {(0, 0), (1, 0), (2, 0), (3, 0)},  # A
        {(0, 1), (1, 1), (0, 2), (1, 2)},  # B
        {(2, 1), (2, 2), (3, 2), (3, 3)},  # C
        {(3, 1)},  # D
        {(0, 3), (1, 3), (2, 3)},  # E
    ]
    pass


def test_get_number_faces_A():
    test_data = {(0, 0), (1, 0), (2, 0), (3, 0)}
    assert get_number_faces(test_data) == 4


def test_get_number_faces_B():
    test_data = {(0, 1), (1, 1), (0, 2), (1, 2)}
    assert get_number_faces(test_data) == 4


def test_get_number_faces_C():
    # fmt: off
    test_data = {
        (2, 1),
        (2, 2), (3, 2),
                (3, 3)
    }
    # fmt: on
    assert get_number_faces(test_data) == 8


def test_get_number_faces_D():
    test_data = {(3, 1)}
    assert get_number_faces(test_data) == 4


def test_get_number_faces_E():
    test_data = {(0, 3), (1, 3), (2, 3)}
    assert get_number_faces(test_data) == 4


def test_get_number_faces_E_shape():
    # fmt: off
    test_data = {
        (0, 0), (1, 0),
        (0, 1),
        (0, 2), (1, 2),
        (0, 3),
        (0, 4), (1, 4)}
    # fmt: on
    assert get_number_faces(test_data) == 12


def test_get_number_faces_V():
    # fmt: off
    test_data = {
        (0, 2), (1, 2),
        (0, 3), (1, 3),
        (0, 4), (1, 4), (2, 4), (3, 4),
        (0, 5), (1, 5),         (3, 5),
        (0, 6), (1, 6),
    }
    # fmt: on
    assert get_number_faces(test_data) == 10


def test_get_number_faces_O_shape():
    # fmt: off
    test_data = {
        (0, 2), (1, 2), (2, 2),
        (0, 3),         (2, 3),
        (0, 4), (1, 4), (2, 4),

    }
    # fmt: on
    assert get_number_faces(test_data) == 8


def test_get_number_faces_J():
    # fmt: off
    test_data = {
                (6, 3),
        (5, 4), (6, 4),
                (6, 5), (7, 5),
                (6, 6), (7, 6),
                (6, 7), (7, 7),
                (6, 8),
                (6, 9),
    }
    # fmt: on
    assert get_number_faces(test_data) == 12


def test_solution_1():
    assert solution_1(TEST_INPUT_EASY) == 140


def test_solution_2():
    assert solution_2(TEST_INPUT_EASY) == 80
    assert solution_2(TEST_INPUT_COMPLEX) == 1206
    assert solution_2(TEST_REDDIT_1) == 300
    assert solution_2(TEST_REDDIT_2) == 146
    assert solution_2(TEST_REDDIT_3) == 946
    assert solution_2(TEST_REDDIT_4) == 164
