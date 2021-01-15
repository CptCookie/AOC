import numpy


class Map:
    def __init__(self, rows: [str]):
        self.width = len(rows[0])
        self.rows = rows

    def is_tree(self, row: int, col: int):
        return self.rows[row][int(col % self.width)] == "#"

    def trees_on_track(self, offset_right):
        counter = 0
        for n in range(len(self.rows)):
            if offset_right * n % 1 == 0:
                if self.is_tree(n, n * offset_right):
                    counter += 1
        return counter


def solve(puzzle_input):
    track_map = Map([n for n in puzzle_input.split("\n") if n != ""])

    print(f"solution 1: {track_map.trees_on_track(3)}")

    tracks = [track_map.trees_on_track(n) for n in [1, 3, 5, 7, 0.5]]
    print(f"solution 2: {numpy.prod(tracks)}")
