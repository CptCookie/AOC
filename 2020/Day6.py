import requests
from const import token

def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/6/input", cookies={"session": token})
    return [n.split('\n') for n in r.content.decode().split('\n\n') if n != '']

def get_unique_answers(passengers: [str]) -> int:
    answers = [n for m in passengers for n in list(m)]
    return set(answers)

def get_unanimous_answers(passengers: [str]) -> int:
    unique_answers = get_unique_answers(passengers)
    unanimous = set()
    for answer in unique_answers:
        if all([answer in n for n in passengers]):
            unanimous.add(answer)
    return unanimous

if __name__ == "__main__":
    passengers = get_aoc_input()
    print(sum([len(get_unique_answers(n)) for n in passengers]))
    print(sum([len(get_unanimous_answers(n)) for n in passengers]))