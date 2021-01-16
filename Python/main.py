import requests
import argparse
import os
import importlib
import pytest
from time import perf_counter
from config import token


parser = argparse.ArgumentParser()
parser.add_argument("--year", "-y", help="year", type=int, required=True)
parser.add_argument("--day", "-d", help="day", type=int)


def get_http_input(year, day):
    r = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token}
    )
    if r.status_code == 200:
        return r.content.decode()
    else:
        raise requests.exceptions.ConnectionError("Token might be too old.")


def read_cached_input(year, day):
    with open(f"./python/cache/{year}-{day}.txt", "r") as f:
        return f.read()


def write_cached_input(year, day, data):
    with open(f"./python/cache/{year}-{day}.txt", "w") as f:
        f.write(data)


def is_cached_input(year, day):
    return f"{year}-{day}.txt" in os.listdir("./python/cache")


def get_input(year, day):
    if is_cached_input(year, day):
        return read_cached_input(year, day)
    else:
        aoc_input = get_http_input(year, day)
        write_cached_input(year, day, aoc_input)
        return aoc_input


def run_solution(year, day):
    puzzle_input = get_input(year, day)
    try:
        pytest.main(["-x", "-q", "--disable-warnings", f"python/{year}/Day{day}"])
        solution = importlib.import_module(f"{year}.Day{day}.solution")

        timer = perf_counter()
        solution.solve(puzzle_input)
        run_time = round((perf_counter() - timer) * 1000, 2)

        print(f"time to run: {run_time}ms")
    except (ModuleNotFoundError) as e:
        print(f"No Solution for the day found. {e}")
    except (SyntaxError, AttributeError) as e:
        print(f"Solution not ready: {e}")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.day is None:
        for day in range(26):
            if f"Day{day}" in os.listdir(f"./python/{args.year}"):
                print(f"Running Day {day}")
                run_solution(args.year, day)
                print("\n")
    else:
        run_solution(args.year, args.day)
