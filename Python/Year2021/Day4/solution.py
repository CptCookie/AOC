class BingoBoard:
    def __init__(self, board_str: str):
        self.board = self._parse_board(board_str)

    @staticmethod
    def _parse_board(board_str: str) -> list[list[int]]:
        return [
            [int(cell) for cell in row.split(" ") if cell != ""]
            for row in board_str.splitlines()
        ]

    def complete(self) -> bool:
        row = any(all(cell < 0 for cell in row) for row in self.board)
        col = any(all(self.board[y][x] < 0 for y in range(5)) for x in range(5))
        return row or col

    def mark(self, number: int):
        self.board = [
            [cell if cell != number else -1 for cell in row] for row in self.board
        ]

    def value(self) -> int:
        return sum([cell for row in self.board for cell in row if cell >= 0])


def win_bingo(numbers: list[int], boards: list[BingoBoard]) -> int:
    for n in numbers:
        for b in boards:
            b.mark(n)
            if b.complete():
                return b.value() * n


def loos_bingo(numbers: list[int], boards: list[BingoBoard]) -> int:
    for n in numbers:
        new_boards = []
        for b in boards:
            b.mark(n)
            if not b.complete():
                new_boards.append(b)
            elif b.complete() and len(boards) == 1:
                return b.value() * n
        boards = new_boards


def solution_1(puzzle_input: str) -> int:
    nums = [int(i) for i in puzzle_input.splitlines()[0].split(",")]
    boards = [BingoBoard(b) for b in puzzle_input.split("\n\n")[1:]]
    return win_bingo(nums, boards)


def solution_2(puzzle_input: str) -> int:
    nums = [int(i) for i in puzzle_input.splitlines()[0].split(",")]
    boards = [BingoBoard(b) for b in puzzle_input.split("\n\n")[1:]]
    return loos_bingo(nums, boards)
