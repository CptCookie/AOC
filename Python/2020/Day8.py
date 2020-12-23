import requests
from copy import deepcopy
from const import token

NOOP = "nop"
ACC = "acc"
JMP = "jmp"

def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/8/input", cookies={"session": token})
    return [n for n in r.content.decode().split('\n') if n != '']

def parse_bootcode(aoc_input: [str]) -> [(str, int)]:
    return [(n[0:3], int(n[4:])) for n in aoc_input]

def run_boot(boot_code):
    index = 0
    acc = 0
    done = []
    while True:
        if index in done or index == len(boot_code):
            return (index, acc)

        if boot_code[index][0] == ACC:
            done.append(index)
            acc += boot_code[index][1]
            index += 1

        elif boot_code[index][0] == JMP:
            done.append(index)
            index += boot_code[index][1]

        elif boot_code[index][0] == NOOP:
            done.append(index)
            index += 1

def fix_bootcode(boot_code):
    for n, m in enumerate(boot_code):
        mod_boot = deepcopy(boot_code)

        if m[0] is NOOP and m[1] != 0:
            mod_boot[n] = (JMP, mod_boot[n][1])

        elif m[0] == JMP:
            mod_boot[n] = (NOOP, mod_boot[n][1])
    
        boot = run_boot(mod_boot)
        if boot[0] == len(mod_boot):
            return boot


def test_loop():
    bootcode = parse_bootcode("""nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6""".split("\n"))
    assert run_boot(bootcode) == (1,5)

def test_fixed_bootcode():
    bootcode = parse_bootcode("""nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1 \nnop -4\nacc +6""".split("\n"))
    assert run_boot(bootcode) == (9,8)

def test_fix():
    bootcode = parse_bootcode("""nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6""".split("\n"))
    assert fix_bootcode(bootcode) == (9,8)

def test_parse_bootcode():
    assert parse_bootcode(['acc -99']) == [('acc', -99)]

if __name__ == "__main__":
    boot_code = parse_bootcode(get_aoc_input())
    print( f"Solution 1: {run_boot(boot_code)[1]}" )
    print( f"Solution 2: {fix_bootcode(boot_code)[1]}" )