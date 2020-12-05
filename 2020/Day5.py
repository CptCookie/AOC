import requests
import re
from const import token

SEATS_ROWS = [n for n in range(128)]
SEATS_COLS = [n for n in range(8)]

FRONT_HALF = 'F'
BACK_HALF = 'B'

LEFT_HALF = 'L'
RIGHT_HALF = 'R'

def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/5/input", cookies={"session": token})
    return [n for n in r.content.decode().split('\n') if n != '']

def get_ID(seat_code):
    row = re.compile(r'^[FB]{7}').findall(seat_code)[0]
    col = re.compile(r'[RL]{3}$').findall(seat_code)[0]
    return get_row(row) * 8 + get_col(col)

def get_row(seat_code, area=SEATS_ROWS):
    if seat_code == '': 
        if len(area) == 1:
            return area[0] 
        else: 
            raise IndexError('Incorrect seat_code')

    elif seat_code[0] == FRONT_HALF:
        return get_row(seat_code[1:], area=area[:int(len(area)/2)])
    elif seat_code[0] == BACK_HALF:
        return get_row(seat_code[1:], area=area[int(len(area)/2):])
        
    

def get_col(seat_code, area=SEATS_COLS):
    if seat_code == '': 
        if len(area) == 1:
            return area[0] 
        else: 
            raise IndexError('Incorrect seat_code')

    elif seat_code[0] == LEFT_HALF:
        return get_col(seat_code[1:], area=area[:int(len(area)/2)])
    elif seat_code[0] == RIGHT_HALF:
        return get_col(seat_code[1:], area=area[int(len(area)/2):])

def test_row():
    assert(get_row('FBFBBFF') == 44)
    assert(get_row('BFFFBBF') == 70)
    assert(get_row('FFFBBBF') == 14)
    assert(get_row('BBFFBBF') == 102)


def test_col():
    assert(get_col('RLR') == 5)
    assert(get_col('RRR') == 7)
    assert(get_col('RRR') == 7)
    assert(get_col('RLL') == 4)

def test_ID():
    assert(get_ID('FBFBBFFRLR') == 357)
    assert(get_ID('BFFFBBFRRR') == 567)
    assert(get_ID('FFFBBBFRRR') == 119)
    assert(get_ID('BBFFBBFRLL') == 820)

if __name__ == "__main__":
    all_IDs = [get_ID(n) for n in get_aoc_input()]
    all_IDs = sorted(all_IDs)

    print(f'solution 1: {max(all_IDs)}')

    for n,m in enumerate(all_IDs[:-1]):
        if all_IDs[n+1] - m == 2:
            print(f'solution 2: {m + 1}')