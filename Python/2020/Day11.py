import requests
from const import token 
from itertools import chain, combinations
from copy import deepcopy

def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/11/input", cookies={"session": token})
    return r.content.decode()


class Floor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '.'
    
    @property
    def free(self):
        return True

class Seat:
    def __init__(self, x, y, state):
        self.state = state
        self.x = x
        self.y = y
    
    def __str__(self):
        return self.state

    def __repr__(self):
        return self.state
    
    @property
    def free(self):
        return self.state == 'L'

    def take_seat(self):
        if self.state == 'L':
            self.state = '#'
        else : 
            raise ValueError('Seat already taken')
    
    def free_seat(self):
        if self.state == '#':
            self.state = 'L'
        else : 
            raise ValueError('Seat already free')
    
class Waiting_Area:
    def __init__(self, seat_states:str ):
        line_states = seat_states.split('\n')
        self.width = len(line_states[0])
        self.height = len(line_states)
        self.seats = []

        for y, line in enumerate(line_states):
            for x, s in enumerate(line):
                if s == '.':
                    self.seats.append(Floor(x, y))
                else:
                    self.seats.append(Seat(x, y, s))

    def __eq__(self, other):
        return [str(n) for n in self.seats] == [str(n) for n in other.seats]      
    
    def get_lines(self):
        return [self.seats[n*self.height:n*self.height+self.width] for n in range(self.height)]

    def get_seat(self, x, y) -> Seat:
        if x < self.width and y < self.height:
            return self.seats[x + y * self.width]
        else:
            raise IndexError

    def get_adjacent(self, x, y):
        adjacent = []

        for x_ad in range(max([x-1,0]), x+2):
            for y_ad in range(max([y-1,0]), y+2):
                try:
                    if not(x_ad==x and y_ad==y) and type(self.get_seat(x_ad, y_ad)) == Seat:
                        adjacent.append(self.get_seat(x_ad, y_ad))
                except IndexError:
                    pass
        return adjacent

    def get_seen_seats(self, x, y):
        seats = []
        for n in range(x+1, self.width):
            if type(self.get_seat(n, y)) == Seat:
                seats.append(self.get_seat(n, y))
        for n in range(x-1, -1, -1):
            if type(self.get_seat(n, y)) == Seat:
                seats.append(self.get_seat(n, y))
        
        all_seats = seats + self.get_bottom_diagonal(x,y) + self.get_top_diagonal(x,y)
        return [n for n in all_seats if n is not None]

    def get_top_diagonal(self, x, y):
        seats = [None, None, None]

        for n,line in enumerate(reversed(self.get_lines()[0:y])):
            if x-(n+1) >= 0:
                if type(line[x-(n+1)]) == Seat and seats[0] is None:
                    seats[0] = line[x-(n+1)]
            if type(line[x]) == Seat and seats[1] is None:
                seats[1] = line[x]
            if x+n+1 < self.width:
                if type(line[x+n+1]) == Seat and seats[2] is None:
                    seats[2] = line[x+n+1]
        return seats

    def get_bottom_diagonal(self, x, y):
        seats = [None, None, None]

        for n,line in enumerate(self.get_lines()[y+1:]):
            if x-(n+1) >= 0:
                if type(line[x-(n+1)]) == Seat and seats[0] is None:
                    seats[0] = line[x-(n+1)]
            if type(line[x]) == Seat and seats[1] is None:
                seats[1] = line[x]
            if x+n+1 < self.width:
                if type(line[x+n+1]) == Seat and seats[2] is None:
                    seats[2] = line[x+n+1]
        return seats
    
    def fill(self):
        while True:
            newSeats = deepcopy(self.seats)
            for n, seat in enumerate(self.seats):
                if type(seat) == Seat:
                    if all([s.free for s in self.get_adjacent(seat.x, seat.y)]) and seat.free:
                        newSeats[n].take_seat()
                    elif len([s for s in self.get_adjacent(seat.x, seat.y) if not s.free]) >= 4 and not seat.free:
                        newSeats[n].free_seat()
            if [str(n) for n in newSeats] == [str(m) for m in self.seats]:
                return
            else: 
                self.seats = newSeats

    def fill_v2(self):
        while True:
            newSeats = deepcopy(self.seats)
            for n, seat in enumerate(self.seats):
                if type(seat) == Seat:
                    if all([s.free for s in self.get_seen_seats(seat.x, seat.y)]) and seat.free:
                        newSeats[n].take_seat()
                    elif len([s for s in self.get_seen_seats(seat.x, seat.y) if not s.free]) >= 5 and not seat.free:
                        newSeats[n].free_seat()
            if [str(n) for n in newSeats] == [str(m) for m in self.seats]:
                return
            else: 
                self.seats = newSeats

def test_WaitingArea():
    area = Waiting_Area('L#\n.L')
    assert area.get_seat(0,0).state == 'L'
    assert area.get_seat(1,0).state == '#'
    assert type(area.get_seat(0,1)) == Floor
    assert area.get_seat(1,1).state == 'L'

def test_adjacent():
    area = Waiting_Area('#.#\nLLL\n#.#')
    assert len(area.get_adjacent(1,1)) == 6
    assert len([1 for n in area.get_adjacent(1,1) if n.free]) == 2
    assert len(area.get_adjacent(0,0)) == 2
    assert len(area.get_adjacent(0,1)) == 3
    assert len(area.get_adjacent(1,0)) == 5
    

def test_compare():
    area_1 = Waiting_Area('#.#\nLLL\n#.#')
    area_52 = Waiting_Area('#.L\nLLL\n#.#')
    assert area_1 == area_1
    assert area_1 != area_52

def test_fill():
    test_data = 'L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL'
    result_data = '#.#L.L#.##\n#LLL#LL.L#\nL.#.L..#..\n#L##.##.L#\n#.#L.LL.LL\n#.#L#L#.##\n..L.L.....\n#L#L##L#L#\n#.LLLLLL.L\n#.#L#L#.##'
    test_area = Waiting_Area(test_data)
    test_area.fill()
    assert test_area == Waiting_Area(result_data)

def test_see_seats():
    test_data = '.......#.\n...#.....\n.#.......\n.........\n..#L....#\n....#....\n.........\n#........\n...#.....'
    test_area = Waiting_Area(test_data)
    assert test_area.get_seat(3,4).__str__() == 'L'
    assert len(test_area.get_seen_seats(3,4)) == 8
    assert all([str(n)=='#'for n in test_area.get_seen_seats(3,4)])

if __name__ == "__main__":
    inp = get_aoc_input()
    # area = Waiting_Area(inp)
    # area.fill()
    # print(len([1 for n in area.seats if str(n)=='#']))
    area = Waiting_Area(inp)
    area.fill_v2()
    print(len([1 for n in area.seats if str(n)=='#']))