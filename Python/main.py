import requests
import argparse
import os
import importlib
import pytest
from config import token

parser = argparse.ArgumentParser()
parser.add_argument("--year", '-y', help="year", type=int)
parser.add_argument("--day", '-d', help="day", type=int)

def get_http_input(year, day):
    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token})
    if r.status_code == 200:
        return r.content.decode()
    else:
        raise requests.exceptions.ConnectionError('Token might be too old.')

def read_cached_input(year, day):
    with open(f'./python/cache/{year}-{day}.txt', 'r') as f:
        return f.read()

def write_cached_input(year, day, data):
    with open(f'./python/cache/{year}-{day}.txt', 'w') as f:
            f.write(data)

def is_cached_input(year, day):
    return f'{year}-{day}.txt' in os.listdir('./python/cache')

def get_input(year, day):
    if is_cached_input(year, day):
        return read_cached_input(year, day)
    else:
        aoc_input = get_http_input(year, day)
        write_cached_input(year, day, aoc_input)
        return aoc_input
        

if __name__ == "__main__":
    args = parser.parse_args()
    puzzle_input = get_input(args.year, args.day)
    try: 
        pytest.main(['-x', '-q', '--disable-warnings', f'python/{args.year}/Day{args.day}'])
        solution = importlib.import_module(f'{args.year}.Day{args.day}.solution')
        solution.solve(puzzle_input)
        print('\n')
    except (ModuleNotFoundError) as e:
        print(f'No Solution for the year and day. {e}')
    except (SyntaxError) as e:
        print(f'solution is not ready: {e}')
    
    