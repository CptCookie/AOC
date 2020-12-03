import requests
import numpy
from const import token


def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/3/input", cookies={"session": token})
    return [n for n in r.content.decode().split('\n') if n != '']


class Map:
    def __init__(self, rows: [str]):
        self.width = len(rows[0])
        self.rows = rows

    def is_tree(self, row: int, col: int):
        return self.rows[row][int(col%self.width)] == '#'

    def trees_on_track(self, offset_right):
        counter = 0
        for n in range(len(self.rows)):
            if offset_right*n % 1 == 0:
                if self.is_tree(n, n*offset_right):
                    counter += 1
        return counter

if __name__ == "__main__":
    track_map = Map(get_aoc_input())
    tracks = [track_map.trees_on_track(n) for n in [1,3,5,7,0.5]]
    print(numpy.prod(tracks))
    