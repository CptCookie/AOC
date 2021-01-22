from .solution import Lights

INITAL_TEST_STATE = ".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####.."
STEP_1 = "..##..\n..##.#\n...##.\n......\n#.....\n#.##.."
STEP_1_CORNER = "#.##.#\n####.#\n...##.\n......\n#...#.\n#.####"


def test_parse():
    l = Lights(6)
    l.parse_instr(INITAL_TEST_STATE)
    # fmt: off
    expected = [
        False ,True  ,False ,True  ,False ,True  ,
        False ,False ,False ,True  ,True  ,False ,
        True  ,False ,False ,False ,False ,True  ,
        False ,False ,True  ,False ,False ,False ,
        True  ,False ,True  ,False ,False ,True  ,
        True  ,True  ,True  ,True  ,False ,False 
    ]
    # fmt: on
    assert l.light == expected


def test_adisent():
    l = Lights(6)
    l.light = list(range(36))
    assert l.get_adicent_lights(0) == [6, 1, 7]
    assert l.get_adicent_lights(5) == [4, 10, 11]
    assert l.get_adicent_lights(7) == [0, 6, 12, 1, 13, 2, 8, 14]
    assert l.get_adicent_lights(2) == [1, 7, 8, 3, 9]
    assert l.get_adicent_lights(6) == [0, 12, 1, 7, 13]


def test_animate():
    l = Lights(6)
    l.parse_instr(INITAL_TEST_STATE)
    l.animate(1)
    expect = Lights(6)
    expect.parse_instr(STEP_1)

    assert l.light == expect.light


def test_animate_corners():
    l = Lights(6, stuck_corners=True)
    l.parse_instr(INITAL_TEST_STATE)
    l.animate(1)
    expect = Lights(6)
    expect.parse_instr(STEP_1_CORNER)

    assert l.light == expect.light
