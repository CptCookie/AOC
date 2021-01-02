import itertools

def route_len(route, map_routes):
    distance = 0
    
    for n, stop in enumerate(route[1:]):
        for maped in map_routes:
            if maped[0] == stop and maped[1] == route[n]:
                distance += int(maped[2])
                break
            elif maped[1] == stop and maped[0] == route[n]:
                distance += int(maped[2])
                break
    return distance

def all_route_len(routes: [[str]]) -> int:
    unique_locations = [n[0:2] for n in routes]
    unique_locations = set([n for m in unique_locations for n in m])
    return [route_len(r, routes) for r in itertools.permutations(unique_locations, len(unique_locations))]
        
def test_route():
    routes = [
        ["L", "D", "464"],
        ["L", "B", "518"],
        ["D", "B", "141"]
    ]
    assert min(all_route_len(routes)) == 605
    assert max(all_route_len(routes)) == 982
    

def solve(puzzle_input):
    puzzle_input = [n.replace(' to ', ' ').replace(' = ', ' ').split(' ') 
                    for n in puzzle_input.split('\n') if n != '']

    print('testing ', end='')
    test_route()
    print('done')

    print('solving')
    all_routes = all_route_len(puzzle_input)
    print(f'solution 1: {min(all_routes)}')
    print(f'solution 2: {max(all_routes)}')