from solution import find_without_red

def test_red():
    assert find_without_red('[1,{"c":"red","b":2},3]') == [1,3]
