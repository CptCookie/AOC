from itertools import islice

alpha = "abcdefghijklmnopqrstuvwxyz"


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def collapse_poly(poly: str) -> str:
    before_len = 0
    while before_len != len(poly):
        before_len = len(poly)
        for c in set(poly.lower()):
            poly = poly.replace(f"{c}{c.upper()}", "")
            poly = poly.replace(f"{c.upper()}{c}", "")
    return poly


def solution_1(aoc_input):
    return len(collapse_poly(aoc_input.strip()))


def solution_2(aoc_input):
    poly = aoc_input.strip()
    results = []
    for c in set(poly.lower()):
        test_poly = poly.replace(c, "")
        test_poly = test_poly.replace(c.upper(), "")
        results.append(len(collapse_poly(test_poly)))

    return min(results)
