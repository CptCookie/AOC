"""
fall, push, rest
"""
from utils.list_tools import CircleList


def parse_input(puzzle_input: str) -> list[str]:
    return [n for n in puzzle_input.splitlines() if n != ""]


class Tetris:
    pieces = [
        ((2, 0), (3, 0), (4, 0), (5, 0)),  # horizontal piece
        ((2, 1), (3, 1), (4, 1), (3, 2), (3, 0)),  # plus piece
        ((2, 0), (3, 0), (4, 0), (4, 1), (4, 2)),  # inverted L piece
        ((2, 0), (2, 1), (2, 2), (2, 3), (2, 4)),  # vertical piece
        ((2, 0), (3, 0), (2, 1), (3, 1)),  # block piece
    ]

    def __init__(self, jets):
        self.jets = CircleList(jets)
        self.jet_pnt = 0
        self.rested_piece = []
        self.current_piece = []
        self.next_piece = 0
        self.current_height = 0

    def fall(self):
        self.current_piece = [(x, y - 1) for x, y in self.current_piece]

    def push(self):
        d = -1 if self.jets[self.jet_pnt] == "<" else 1

        collision = (
            (x + d, y) in self.rested_piece or not 0 < x + d <= 6
            for x, y in self.current_piece
        )
        if not any(collision):
            self.current_piece = [(x + d, y) for x, y in self.current_piece]

        self.jet_pnt += 1

    def rest(self):
        if any(
            [(x, y - 1) in self.rested_piece or y == 0 for x, y in self.current_piece]
        ):
            self.rested_piece.extend(self.current_piece)
            self.current_height = max(
                [y for _, y in self.current_piece] + [self.current_height]
            )
            return True
        return False

    def place_next_piece(self):
        self.current_piece = [
            (x, y + self.current_height + 3) for x, y in self.pieces[self.next_piece]
        ]
        self.next_piece = (self.next_piece + 1) % len(self.pieces)

    def play_stone(self):
        self.place_next_piece()
        self.push()
        while not self.rest():
            self.fall()
            self.push()


def solution_1(puzzle_input: str):
    input = parse_input(puzzle_input)
    return None


def solution_2(puzzle_input: str):
    input = parse_input(puzzle_input)
    return None
