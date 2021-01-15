from .solution import Waiting_Area, Floor


def test_WaitingArea():
    area = Waiting_Area("L#\n.L")
    assert area.get_seat(0, 0).state == "L"
    assert area.get_seat(1, 0).state == "#"
    assert type(area.get_seat(0, 1)) == Floor
    assert area.get_seat(1, 1).state == "L"


def test_adjacent():
    area = Waiting_Area("#.#\nLLL\n#.#")
    assert len(area.get_adjacent(1, 1)) == 6
    assert len([1 for n in area.get_adjacent(1, 1) if n.free]) == 2
    assert len(area.get_adjacent(0, 0)) == 2
    assert len(area.get_adjacent(0, 1)) == 3
    assert len(area.get_adjacent(1, 0)) == 5


def test_compare():
    area_1 = Waiting_Area("#.#\nLLL\n#.#")
    area_52 = Waiting_Area("#.L\nLLL\n#.#")
    assert area_1 == area_1
    assert area_1 != area_52


def test_fill():
    test_data = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL"
    result_data = "#.#L.L#.##\n#LLL#LL.L#\nL.#.L..#..\n#L##.##.L#\n#.#L.LL.LL\n#.#L#L#.##\n..L.L.....\n#L#L##L#L#\n#.LLLLLL.L\n#.#L#L#.##"
    test_area = Waiting_Area(test_data)
    test_area.fill()
    assert test_area == Waiting_Area(result_data)


def test_see_seats():
    test_data = ".......#.\n...#.....\n.#.......\n.........\n..#L....#\n....#....\n.........\n#........\n...#....."
    test_area = Waiting_Area(test_data)
    assert test_area.get_seat(3, 4).__str__() == "L"
    assert len(test_area.get_seen_seats(3, 4)) == 8
    assert all([str(n) == "#" for n in test_area.get_seen_seats(3, 4)])
