import requests
from collections import namedtuple
from typing import Callable
import argparse
import os
import importlib
import pytest
from time import perf_counter
from config import token


parser = argparse.ArgumentParser()
parser.add_argument("--year", "-y", help="year", type=int, required=True)
parser.add_argument("--day", "-d", help="day", type=int)
parser.add_argument(
    "--tests",
    "-t",
    help="Skip the tests",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--runtime",
    "-r",
    help="shows the runtime of the solution",
    action="store_true",
    default=False,
)


def read_input_from_http(year, day):
    r = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token}
    )
    if r.status_code == 200:
        return r.content.decode()
    else:
        raise requests.exceptions.ConnectionError("Token might be too old.")


def read_input_from_file(year, day):
    with open(f"./cache/{year}-{day}.txt", "r") as f:
        return f.read()


def write_input_to_file(year, day, data):
    with open(f"./cache/{year}-{day}.txt", "w") as f:
        f.write(data)


def get_puzzel_input(year, day):
    try:
        return read_input_from_file(year, day)
    except FileNotFoundError:
        puzzle_input = read_input_from_http(year, day)
        write_input_to_file(year, day, puzzle_input)
        return puzzle_input


def solve_puzzle(year, day, run_test=False, measure_runtime=False):
    if run_test:
        pytest.main(["-q", f"{year}/Day{day}"])
    else:
        puzzle_string = get_puzzel_input(year, day)

        try:
            puzzle_solution = importlib.import_module(f"{year}.Day{day}.solution")
            print(f"Solving Advent of Code {year} Day {day}:")
            run_solution(puzzle_solution.solution_1, puzzle_string, measure_runtime)
            run_solution(puzzle_solution.solution_2, puzzle_string, measure_runtime)

        except (ModuleNotFoundError) as e:
            print(f"No Solution for the day found. {e}")
        except (SyntaxError, AttributeError) as e:
            print(f"Solution not ready: {e}")


def run_solution(solve_function: Callable, puzzle_string: str, measure_runtime=False):
    start_time = perf_counter()

    solution = solve_function(puzzle_string)
    run_time = round((perf_counter() - start_time) * 1000, 2)

    print(f"{solve_function.__name__}: {solution}", end="")
    if measure_runtime:
        print(f"\ttook: {run_time}ms")
    else:
        print("")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.day is None:
        for day in range(26):
            if f"Day{day}" in os.listdir(f"./{args.year}"):
                solve_puzzle(args.year, day, args.tests, args.runtime)
                print("\n")
    else:
        solve_puzzle(args.year, args.day, args.tests, args.runtime)
