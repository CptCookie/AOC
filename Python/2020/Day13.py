import requests
from const import token 

def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/13/input", cookies={"session": token})
    return [n for n in r.content.decode().split('\n') if n != '']


def get_earlyest_bus(arival, busses: [int])-> (int, int):
    takeable = [(n, m) for n in range(arival, arival+max(busses)) for m in busses if n%m ==0]
    return min(takeable, key=lambda x: x[0])

def solution_1(puzzle_input):
    arival = int(puzzle_input[0])
    busses = [int(n) for n in puzzle_input[1].split(',') if n!='x']
    bus = get_earlyest_bus(arival, busses)
    return (bus[0]-arival) * bus[1]

def test_earlyest():
    solution = solution_1('939\n7,13,x,x,59,x,31,19'.split('\n'))
    assert solution == 295

def valid_solution(bus_Ids, start_time):
    for n, Id in enumerate(bus_Ids):
        if Id > -1:
            if not (start_time + n) % bus_Ids[n] == 0:
                return False
    return True

def soliution_2(puzzle_input):
    bus_ids = [int(n) if n!='x' else -1 for n in puzzle_input.split(',')]
    max_id = max(bus_ids)
    for time in bus_tick(max_id):
        if time/max_id % 1000000 == 0:
            print(time/max_id)
        start_time = int( time / bus_ids[0] ) * bus_ids[0]
        if valid_solution(bus_ids, start_time):
            return start_time

def bus_tick(tick):
    n = 0
    while True:
        n+=1
        yield n*tick

def test_solution2():
    p_in = '17,x,13,19'
    assert soliution_2(p_in) == 3417

def test_valid_solution():
    p_in=[17,-1,13,19]
    assert valid_solution(p_in, 3417)
    assert not valid_solution(p_in, 17)

if __name__ == "__main__":
    # print(solution_1(get_aoc_input()))
    print(soliution_2(get_aoc_input()[1]))
