from .solution import (
    solution_1,
    solution_2,
    parse_workflow,
    parse_parts,
    get_flow_outcome,
    get_ranged_flow_outcome,
    calculate_ranged_value,
)

TEST_INPUT = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

TEST_PARTS = [
    {"x": 787, "m": 2655, "a": 1222, "s": 2876},
    {"x": 1679, "m": 44, "a": 2067, "s": 496},
    {"x": 2036, "m": 264, "a": 79, "s": 2244},
    {"x": 2461, "m": 1339, "a": 466, "s": 291},
    {"x": 2127, "m": 1623, "a": 2188, "s": 1013},
]

TEST_WORKFLOWS = {
    "px": ["a<2006:qkq", "m>2090:A", "rfg"],
    "pv": ["a>1716:R", "A"],
    "lnx": ["m>1548:A", "A"],
    "rfg": ["s<537:gd", "x>2440:R", "A"],
    "qs": ["s>3448:A", "lnx"],
    "qkq": ["x<1416:A", "crn"],
    "crn": ["x>2662:A", "R"],
    "in": ["s<1351:px", "qqz"],
    "qqz": ["s>2770:qs", "m<1801:hdj", "R"],
    "gd": ["a>3333:R", "R"],
    "hdj": ["m>838:A", "pv"],
}


def test_parsing():
    assert parse_workflow(TEST_INPUT) == TEST_WORKFLOWS
    assert parse_parts(TEST_INPUT) == TEST_PARTS


def test_flow_outcome():
    assert get_flow_outcome(TEST_PARTS[0], TEST_WORKFLOWS["px"]) == "qkq"
    assert get_flow_outcome(TEST_PARTS[1], TEST_WORKFLOWS["px"]) == "rfg"
    assert get_flow_outcome(TEST_PARTS[4], TEST_WORKFLOWS["qqz"]) == "hdj"


def test_ranged_flow_outcome():
    test_part = {k: range(1, 4001) for k in "xmas"}
    result = get_ranged_flow_outcome(test_part, ["x>2023:A", "m<13:A", "A"])
    assert (
        sum(calculate_ranged_value(p) for f, p in result if f == "A") == 256000000000000
    )


def test_value_ranged():
    test_part = {"a": range(1, 10), "m": range(1, 10), "x": range(1, 2)}
    assert calculate_ranged_value(test_part) == 81


def test_solution_1():
    assert solution_1(TEST_INPUT)


def test_solution_2():
    assert solution_2(TEST_INPUT) == 167409079868000
