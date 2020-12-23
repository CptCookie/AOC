import requests
from const import token


def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/1/input", cookies={"session": token})
    return [int(n) for n in r.content.decode().split('\n') if n != '']



if __name__ == "__main__":
    data = get_aoc_input() 

    for n in data:
        for m in data:
            if n + m == 2020:
                print(f'two numbers: {n * m}')

            for o in data: 
                if n + m + o == 2020:
                    print(f'three numbers: {n*m*o}')

