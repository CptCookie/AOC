from .solution import solution_1, solution_2, parse_routing, get_routing_code

TEST_INPUT = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 

"""

TEST_DATA = [
    "     |          ",
    "     |  +--+    ",
    "     A  |  C    ",
    " F---|----E|--+ ",
    "     |  |  |  D ",
    "     +B-+  +--+ ",
]


def test_parsing():
    assert parse_routing(TEST_INPUT) == TEST_DATA


def test_get_routing_code():
    assert get_routing_code(TEST_DATA) == ("ABCDEF", 38)


def test_solution_1():
    assert solution_1(TEST_INPUT) == "ABCDEF"


def test_solution_2():
    assert solution_2(TEST_INPUT) == 38
