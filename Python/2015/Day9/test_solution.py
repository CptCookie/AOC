from solution import all_route_len


def test_route():
    routes = [["L", "D", "464"], ["L", "B", "518"], ["D", "B", "141"]]
    assert min(all_route_len(routes)) == 605
    assert max(all_route_len(routes)) == 982
