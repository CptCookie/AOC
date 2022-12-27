from .solution import solution_1, solution_2, parse_input, mix_decrypt, Node

TEST_INPUT = """1
2
-3
3
-2
0
4
"""

TEST_DATA = [1, 2, -3, 3, -2, 0, 4]


def built_test_nodes():
    a = Node(0)
    b = Node(1)
    c = Node(-1)
    d = Node(0)

    a.next = b
    b.next = c
    c.next = d
    d.next = a

    a.prev = d
    b.prev = a
    c.prev = b
    d.prev = c

    return a,b,c,d

def test_move_next():
    a,b,c,d = built_test_nodes()
    b.move()

    assert c.prev == a
    assert a.next == c

    assert b.next == d
    assert d.prev == b

    assert b.prev == c
    assert c.next == b

def test_move_prev():
    a,b,c,d = built_test_nodes()
    c.move()

    assert c.prev == a
    assert a.next == c

    assert b.next == d
    assert d.prev == b

    assert b.prev == c
    assert c.next == b


def test_parsing():
    nodes = parse_input(TEST_INPUT)
    for i, n in enumerate(nodes):
        assert TEST_DATA[i] == n.value

        if i > 0:
            assert n.prev == nodes[i-1]

        if i < len(nodes) - 1:
            assert n.next == nodes[i+1]

    assert nodes[0].prev == nodes[-1]
    assert nodes[-1].next == nodes[0]

def test_510():
    nodes = parse_input("5\n1\n0")
    mix_decrypt(nodes)
    assert nodes[0].value == 5
    assert nodes[0].next.value == 1
    assert nodes[0].next.next.value == 0

def test_solution_1():
    assert solution_1(TEST_INPUT) == 3

#
# def test_solution_2():
#     assert solution_2(TEST_INPUT)
