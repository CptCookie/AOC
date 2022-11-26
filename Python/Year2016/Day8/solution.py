import re

regex_rect = r"rect (\d+)x(\d+)"
regex_shift = r"rotate (row|column) [xy]=(\d+) by (\d+)"


class Display:
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self.pixels = [[False for x in range(width)] for y in range(height)]

    def rect(self, width: int, height: int):
        for row_num in range(self.height):
            for col_num in range(self.width):
                if row_num < height and col_num < width:
                    self.pixels[row_num][col_num] = True

    def shift_row(self, row_num: int, by: int):
        new_row = self.pixels[row_num][by * -1 :] + self.pixels[row_num][: by * -1]
        self.pixels[row_num] = new_row

    def shift_column(self, col_num: int, by: int):
        col = [row[col_num] for row in self.pixels]
        new_col = col[by * -1 :] + col[: by * -1]

        for row_num in range(self.height):
            self.pixels[row_num][col_num] = new_col[row_num]

    def parse_and_execute(self, instruction: str):
        rect_match = re.search(regex_rect, instruction)
        if rect_match:
            self.rect(*[int(x) for x in rect_match.groups()])

        shift_match = re.search(regex_shift, instruction)
        if shift_match:
            if shift_match.groups()[0] == "row":
                self.shift_row(*[int(x) for x in shift_match.groups()[1:]])
            else:
                self.shift_column(*[int(x) for x in shift_match.groups()[1:]])


def solution_1(puzzle_input):
    display = Display(50, 6)

    for line in puzzle_input.splitlines():
        if line != "":
            display.parse_and_execute(line)

    return sum([x for y in display.pixels for x in y])


def solution_2(puzzle_input):
    display = Display(50, 6)

    for line in puzzle_input.splitlines():
        if line != "":
            display.parse_and_execute(line)

    for line in display.pixels:
        for c in line:
            print("#" if c else "_", end="")
        print("")
