import re


def parse_rule(rule_desription: str) -> dict:
    outer_bag = re.compile(r"\w+\s\w+\sbags contain").findall(rule_desription)[0]
    inner_bags = re.compile(r"\d\s\w+\s\w+\sbag").findall(rule_desription)

    container_color = outer_bag.split(" bag")[0]
    containing = {}

    for bag in inner_bags:
        number = int(bag[0])
        color = " ".join(bag.split(" ")[1:3])
        containing[color] = number

    return {container_color: containing}


def parse_input(aoc_input):
    out = {}
    for line in aoc_input:
        out.update(parse_rule(line))
    return out


def filter_unique(lst: list) -> list:
    filtered = []
    for n, m in enumerate(lst):
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
    return sum([number_bags(n, rules) * color_rule[n] for n in color_rule]) + 1


def solve(puzzle_input):
    rules = parse_input([n for n in puzzle_input.split("\n") if n != ""])
    print(f'solution 1: {len(contained_by("shiny gold", rules))}')
    print(f'solution 2: {number_bags("shiny gold", rules)-1}')
