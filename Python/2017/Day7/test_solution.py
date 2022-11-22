from .solution import solution_1, solution_2
test_data = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

def test_solution_1():
    assert solution_1(test_data) == 'tknk'

def test_solution_2():
    assert solution_2(test_data) == 60
