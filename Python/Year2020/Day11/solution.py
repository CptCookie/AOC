from copy import deepcopy


class Floor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "."

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
        return self.state == "L"

    def take_seat(self):
        if self.state == "L":
            self.state = "#"
        else:
            raise ValueError("Seat already taken")

    def free_seat(self):
        if self.state == "#":
            self.state = "L"
        else:
            raise ValueError("Seat already free")


class Waiting_Area:
    def __init__(self, seat_states: str):
        line_states = seat_states.split("\n")
        self.width = len(line_states[0])
        self.height = len(line_states)
        self.seats = []

        for y, line in enumerate(line_states):
            for x, s in enumerate(line):
                if s == ".":
                    self.seats.append(Floor(x, y))
                else:
                    self.seats.append(Seat(x, y, s))

    def __eq__(self, other):
        return [str(n) for n in self.seats] == [str(n) for n in other.seats]

    def get_lines(self):
        return [
            self.seats[n * self.height : n * self.height + self.width]
            for n in range(self.height)
        ]

    def get_seat(self, x, y) -> Seat:
        if x < self.width and y < self.height:
            return self.seats[x + y * self.width]
        else:
            raise IndexError

    def get_adjacent(self, x, y):
        adjacent = []

        for x_ad in range(max([x - 1, 0]), x + 2):
            for y_ad in range(max([y - 1, 0]), y + 2):
                try:
                    if (
                        not (x_ad == x and y_ad == y)
                        and type(self.get_seat(x_ad, y_ad)) == Seat
                    ):
                        adjacent.append(self.get_seat(x_ad, y_ad))
                except IndexError:
                    pass
        return adjacent

    def get_seen_seats(self, x, y):
        seats = []
        for n in range(x + 1, self.width):
            if type(self.get_seat(n, y)) == Seat:
                seats.append(self.get_seat(n, y))
        for n in range(x - 1, -1, -1):
            if type(self.get_seat(n, y)) == Seat:
                seats.append(self.get_seat(n, y))

        all_seats = seats + self.get_bottom_diagonal(x, y) + self.get_top_diagonal(x, y)
        return [n for n in all_seats if n is not None]

    def get_top_diagonal(self, x, y):
        seats = [None, None, None]

        for n, line in enumerate(reversed(self.get_lines()[0:y])):
            if x - (n + 1) >= 0:
                if type(line[x - (n + 1)]) == Seat and seats[0] is None:
                    seats[0] = line[x - (n + 1)]
            if type(line[x]) == Seat and seats[1] is None:
                seats[1] = line[x]
            if x + n + 1 < self.width:
                if type(line[x + n + 1]) == Seat and seats[2] is None:
                    seats[2] = line[x + n + 1]
        return seats

    def get_bottom_diagonal(self, x, y):
        seats = [None, None, None]

        for n, line in enumerate(self.get_lines()[y + 1 :]):
            if x - (n + 1) >= 0:
                if type(line[x - (n + 1)]) == Seat and seats[0] is None:
                    seats[0] = line[x - (n + 1)]
            if type(line[x]) == Seat and seats[1] is None:
                seats[1] = line[x]
            if x + n + 1 < self.width:
                if type(line[x + n + 1]) == Seat and seats[2] is None:
                    seats[2] = line[x + n + 1]
        return seats

    def fill(self):
        while True:
            newSeats = deepcopy(self.seats)
            for n, seat in enumerate(self.seats):
                if type(seat) == Seat:
                    if (
                        all([s.free for s in self.get_adjacent(seat.x, seat.y)])
                        and seat.free
                    ):
                        newSeats[n].take_seat()
                    elif (
                        len(
                            [s for s in self.get_adjacent(seat.x, seat.y) if not s.free]
                        )
                        >= 4
                        and not seat.free
                    ):
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
                    if (
                        all([s.free for s in self.get_seen_seats(seat.x, seat.y)])
                        and seat.free
                    ):
                        newSeats[n].take_seat()
                    elif (
                        len(
                            [
                                s
                                for s in self.get_seen_seats(seat.x, seat.y)
                                if not s.free
                            ]
                        )
                        >= 5
                        and not seat.free
                    ):
                        newSeats[n].free_seat()
            if [str(n) for n in newSeats] == [str(m) for m in self.seats]:
                return
            else:
                self.seats = newSeats


def solution_1(puzzle_input):
    area = Waiting_Area(puzzle_input)
    area.fill()
    return len([1 for n in area.seats if str(n) == "#"])


def solution_2(puzzle_input):
    area = Waiting_Area(puzzle_input)
    area.fill_v2()  # incomplete
    return len([1 for n in area.seats if str(n) == "#"])
