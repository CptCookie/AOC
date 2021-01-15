import itertools
import pprint
import copy


def parse_ingr_stats(puzzle_input):
    ingr_stats = dict()
    for line in puzzle_input:
        stats = dict()
        for n in range(0, len(line[1:]), 2):
            stats[(line[n + 1])] = int(line[n + 2])
        ingr_stats[line[0]] = stats
    return ingr_stats


def get_state_score(ingr_amount, stat, ingr_stats):
    return sum(
        [ingr_amount[ingr] * ingr_stats[ingr][stat] for ingr in ingr_amount.keys()]
    )


def get_cookie_score(
    ingr_amount: {str: int}, ingr_stats: {str: {str: int}}, weight_watch=False
):
    score = 1
    for stat in ingr_stats[list(ingr_stats.keys())[0]]:
        if stat != "calories":
            sub_score = get_state_score(ingr_amount, stat, ingr_stats)
            score *= sub_score if sub_score > 0 else 0

    if weight_watch:
        calories = get_state_score(ingr_amount, "calories", ingr_stats)
        return score if calories == 500 else 0
    else:
        return score


def max_score_cookie(ingr_stats, weight_watch=False):
    recipies = itertools.combinations_with_replacement(list(ingr_stats.keys()), r=100)
    max_score = 0
    for r in recipies:
        cookie = {i: r.count(i) for i in ingr_stats}
        score = get_cookie_score(cookie, ingr_stats, weight_watch)
        max_score = score if score > max_score else max_score
    return max_score


def solve(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    puzzle_input = [
        n.replace(":", "").replace(",", "").split(" ") for n in puzzle_input
    ]
    ingr_stats = parse_ingr_stats(puzzle_input)

    print(f"solution 1: {max_score_cookie(ingr_stats)}")
    print(f"solution 2: {max_score_cookie(ingr_stats, True)}")
