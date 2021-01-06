import requests
import argparse
import os
import importlib
from config import token

parser = argparse.ArgumentParser()
parser.add_argument("--year", '-y', help="year", type=int)
parser.add_argument("--day", '-d', help="day", type=int)

def get_input_http(year, day):
    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token})
    if r.status_code == 200:
        return r.content.decode()
    else:
        raise requests.exceptions.ConnectionError('Token might be too old.')

def get_input(year, day):
    if f'{year}-{day}.txt' in os.listdir('./python/cache'):
        with open(f'./python/cache/{year}-{day}.txt', 'r') as f:
            return f.read()
    else:
        with open(f'./python/cache/{year}-{day}.txt', 'w') as f:
            aoc_input = get_input_http(year, day)
            f.write(aoc_input)
        return aoc_input

if __name__ == "__main__":
    args = parser.parse_args()
    puzzle_input = get_input(args.year, args.day)
    try: 
        solution = importlib.import_module(f'{args.year}.Day{args.day}')
        solution.solve(puzzle_input)
    except (ModuleNotFoundError) as e:
        print(f'No Solution for the year and day. {e}')
    except (SyntaxError) as e:
        print(f'solution is not ready: {e}')
    
    