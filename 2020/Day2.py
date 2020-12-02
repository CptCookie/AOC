import requests
from const import token


def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/2/input", cookies={"session": token})
    return [n.split(': ') for n in r.content.decode().split('\n') if n != '']

def parse_range(string: str):
    r = string.split(' ')[0].split('-')
    return range(int(r[0]), int(r[1])+1)

def parse_positions(string: str):
    r = string.split(' ')[0].split('-')
    print(string, int(r[0])-1, int(r[1])-1)
    return (int(r[0])-1, int(r[1])-1)

def parse_letter(string: str):
    return string.split(' ')[1]

def count_old_policy(data_input):
    counter = 0
    for param, string in data_input:
        if string.count(parse_letter(param)) in parse_range(param):
            counter += 1
    return counter

def count_new_policy(data_input):
    counter = 0
    for param, string in data_input:
        pos_1, pos_2 = parse_positions(param)
        letter = parse_letter(param)
        if (string[pos_1] == letter) ^ (string[pos_2] == letter):
            counter += 1

    return counter 


if __name__ == "__main__":
    print(count_new_policy(get_aoc_input()))
        
    
    

