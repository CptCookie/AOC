from .solution import parse_data, solution_1, solution_2, Cave

start = "start"
A = "A"
b = "b"
c = "c"
d = "d"
end = "end"


def test_connections():
    data = parse_data("start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end\n")
    nodes = Cave.build_network(data)
    pathes = nodes["start"].find_all_pathes_to(nodes["end"])
    expected = [
        ["start", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "end"],
        ["start", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "end"],
        ["start", "A", "end"],
        ["start", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "end"],
        ["start", "b", "end"],
    ]

    assert len(expected) == len(pathes)
    for n in expected:
        assert n in pathes


def test_double_connection():
    data = parse_data("start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end\n")
    nodes = Cave.build_network(data)
    pathes = nodes["start"].find_all_pathes_to(nodes["end"], single_cave_twice=True)

    expected = [
        [start, A, b, A, b, A, c, A, end],
        [start, A, b, A, b, A, end],
        [start, A, b, A, b, end],
        [start, A, b, A, c, A, b, A, end],
        [start, A, b, A, c, A, b, end],
        [start, A, b, A, c, A, c, A, end],
        [start, A, b, A, c, A, end],
        [start, A, b, A, end],
        [start, A, b, d, b, A, c, A, end],
        [start, A, b, d, b, A, end],
        [start, A, b, d, b, end],
        [start, A, b, end],
        [start, A, c, A, b, A, b, A, end],
        [start, A, c, A, b, A, b, end],
        [start, A, c, A, b, A, c, A, end],
        [start, A, c, A, b, A, end],
        [start, A, c, A, b, d, b, A, end],
        [start, A, c, A, b, d, b, end],
        [start, A, c, A, b, end],
        [start, A, c, A, c, A, b, A, end],
        [start, A, c, A, c, A, b, end],
        [start, A, c, A, c, A, end],
        [start, A, c, A, end],
        [start, A, end],
        [start, b, A, b, A, c, A, end],
        [start, b, A, b, A, end],
        [start, b, A, b, end],
        [start, b, A, c, A, b, A, end],
        [start, b, A, c, A, b, end],
        [start, b, A, c, A, c, A, end],
        [start, b, A, c, A, end],
        [start, b, A, end],
        [start, b, d, b, A, c, A, end],
        [start, b, d, b, A, end],
        [start, b, d, b, end],
        [start, b, end],
    ]

    for n in expected:
        assert n in pathes


def test_double_connection_BIG_TIME():
    data = parse_data("start-A\nA-c\nA-end\n")
    nodes = Cave.build_network(data)
    pathes = nodes["start"].find_all_pathes_to(nodes["end"], single_cave_twice=True)

    expected = [
        ["start", "A", "end"],
        ["start", "A", "c", "A", "end"],
        ["start", "A", "c", "A", "c", "A", "end"],
    ]

    assert len(expected) == len(pathes)
    for n in expected:
        assert n in pathes


def test_solution_1():
    test_input = "start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end\n"
    assert solution_1(test_input) == 10


def test_solution_2():
    test_input = "start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end\n"
    assert solution_2(test_input) == 36


def test_solution_2_slightly_larger():
    test_input = "dc-end\nHN-start\nstart-kj\ndc-start\ndc-HN\nLN-dc\nHN-end\nkj-sa\nkj-HN\nkj-dc"
    assert solution_2(test_input) == 103
