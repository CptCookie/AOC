from .solution import (
    solution_1,
    solution_2,
    parse_floors,
    dist,
    hashable,
    valid_floor,
    valid_floors,
)

TEST_INPUT = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
"""

TEST_DATA = [
    [
        ("hydrogen", "microchip"),
        ("lithium", "microchip"),
    ],
    [
        ("hydrogen", "generator"),
    ],
    [
        ("lithium", "generator"),
    ],
    [],
]


def test_parsing():
    assert parse_floors(TEST_INPUT) == TEST_DATA


def test_dist():
    assert dist(TEST_DATA) == 9
    assert dist([[], [], [], [1, 2, 3]]) == 0


def test_hashable():
    try:
        set(hashable(TEST_DATA))
    except TypeError:
        raise AssertionError("not hashble")

    assert hashable(
        [
            [("hydrogen", "microchip"), ("lithium", "microchip")],
            [("hydrogen", "generator"), ("lithium", "generator")],
        ]
    ) == hashable(
        [
            [("lithium", "microchip"), ("hydrogen", "microchip")],
            [("lithium", "generator"), ("hydrogen", "generator")],
        ]
    )


def test_valid_floor():
    assert valid_floor([("hydrogen", "microchip"), ("lithium", "microchip")])
    assert not valid_floor(
        [("hydrogen", "microchip"), ("lithium", "microchip"), ("lithium", "generator")]
    )
    assert valid_floor([("lithium", "microchip"), ("lithium", "generator")])


def test_valid_floors():
    assert valid_floors(
        [
            [],
            [],
            [("lithium", "microchip"), ("hydrogen", "microchip")],
            [("lithium", "generator"), ("hydrogen", "generator")],
        ]
    )


def test_solution_1():
    assert solution_1(TEST_INPUT) == 11
