import requests
from const import token
import re

def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/7/input", cookies={"session": token})
    return [n for n in r.content.decode().split('\n') if n != '']

def parse_rule(rule_desription: str) -> dict:
    outer_bag = re.compile(r'\w+\s\w+\sbags contain').findall(rule_desription)[0]
    inner_bags = re.compile(r'\d\s\w+\s\w+\sbag').findall(rule_desription)

    container_color = outer_bag.split(' bag')[0]
    containing = {}

    for bag in inner_bags:
        number = int(bag[0])
        color = ' '.join(bag.split(' ')[1:3])
        containing[color] = number

    return {container_color: containing}

def parse_input(aoc_input):
    out = {}
    for line in aoc_input:
        out.update(parse_rule(line))
    return out
    
def filter_unique(lst: list) -> list:
    filtered = []
    for n,m in enumerate(lst):
        if lst.index(m) == n:
            filtered.append(m)
    return filtered

def contained_by(search_color, rules):
    colors = []
    for c in rules:
        if search_color in rules[c]:
            colors.append(c)

            contianers = contained_by(c, rules)
            if len(contianers) > 0:
                for con in contianers:
                    colors.append(con)
    return filter_unique(colors)

def number_bags(search_color, rules) -> int:
    color_rule = rules[search_color]
    return sum( [ number_bags(n, rules)*color_rule[n] for n in color_rule ] ) + 1

def test_parser_rule():
    assert parse_rule('posh black bags contain 2 dotted blue bags, 3 muted crimson bags.') == \
        {'posh black': {'dotted blue': 2, 'muted crimson': 3}}
    assert parse_rule('vibrant cyan bags contain 5 pale black bags, 5 vibrant violet bags, 1 mirrored red bag.') == \
        {'vibrant cyan': {'pale black': 5, 'vibrant violet': 5, 'mirrored red': 1}} 
    assert parse_rule('striped olive bags contain no other bags.') == \
        {'striped olive': {}} 

def test_parser_input():
    assert (
        parse_input([
            'posh black bags contain 2 dotted blue bags, 3 muted crimson bags.',
            'vibrant cyan bags contain 5 pale black bags, 5 vibrant violet bags, 1 mirrored red bag.',
            'striped olive bags contain no other bags.']) == 
        
        {
            'posh black': {'dotted blue': 2, 'muted crimson': 3},
            'vibrant cyan': {'pale black': 5, 'vibrant violet': 5, 'mirrored red': 1},
            'striped olive': {}
        } 
    )
    
def test_bag_numbers_1():
    rules = parse_input([
        'shiny gold bags contain 2 dark red bags.',
        'dark red bags contain 2 dark orange bags.',
        'dark orange bags contain 2 dark yellow bags.',
        'dark yellow bags contain 2 dark green bags.',
        'dark green bags contain 2 dark blue bags.',
        'dark blue bags contain 2 dark violet bags.',
        'dark violet bags contain no other bags.',
    ])
    assert number_bags('shiny gold', rules) == 127

def test_bag_numbers_2():
    rules = parse_input([
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.',
    ])
    assert number_bags('shiny gold', rules) == 33

if __name__ == "__main__":
    rules = parse_input(get_aoc_input())
    print(len(contained_by('shiny gold', rules)))
    print(number_bags('shiny gold', rules)-1)