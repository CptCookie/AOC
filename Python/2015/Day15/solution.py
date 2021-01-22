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
    ingr_amount: {str: int}, ingr_stats: {str: {str: int}}, calorie_count=None
):
    score = 1
    for stat in ingr_stats[list(ingr_stats.keys())[0]]:
        if stat != "calories":
            sub_score = get_state_score(ingr_amount, stat, ingr_stats)
            score *= sub_score if sub_score > 0 else 0

    if calorie_count is not None:
        calories = get_state_score(ingr_amount, "calories", ingr_stats)
        return score if calories == calorie_count else 0
    else:
        return score


def max_score_cookie(ingr_stats, calorie_count=None):
    recipies = itertools.combinations_with_replacement(list(ingr_stats.keys()), r=100)
    max_score = 0
    for r in recipies:
        cookie = {i: r.count(i) for i in ingr_stats}
        score = get_cookie_score(cookie, ingr_stats, calorie_count)
        max_score = score if score > max_score else max_score
    return max_score


def solution_1(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    puzzle_input = [
        n.replace(":", "").replace(",", "").split(" ") for n in puzzle_input
    ]
    ingr_stats = parse_ingr_stats(puzzle_input)
    return max_score_cookie(ingr_stats)


def solution_2(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    puzzle_input = [
        n.replace(":", "").replace(",", "").split(" ") for n in puzzle_input
    ]
    ingr_stats = parse_ingr_stats(puzzle_input)
    return max_score_cookie(ingr_stats, 500)
