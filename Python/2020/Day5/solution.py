import re
from const import token

FRONT_HALF = "F"
BACK_HALF = "B"
LEFT_HALF = "L"
RIGHT_HALF = "R"


def get_ID(seat_code):
    row = re.compile(r"^[FB]{7}").findall(seat_code)[0]
    col = re.compile(r"[RL]{3}$").findall(seat_code)[0]
    return get_row(row) * 8 + get_seat(col)


def get_row(seat_code):
    seat_code = seat_code.replace(BACK_HALF, "1").replace(FRONT_HALF, "0")
    return int(seat_code, base=2)


def get_seat(seat_code):
    seat_code = seat_code.replace(RIGHT_HALF, "1").replace(LEFT_HALF, "0")
    return int(seat_code, base=2)


def solve(puzzle_input):
    all_IDs = [get_ID(n) for n in puzzle_input.split("\n") if n != ""]
    all_IDs = sorted(all_IDs)

    print(f"solution 1: {max(all_IDs)}")

    for n, m in enumerate(all_IDs[:-1]):
        if all_IDs[n + 1] - m == 2:
            print(f"solution 2: {m + 1}")
