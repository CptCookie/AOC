from .solution import (
    solution_1,
    solution_2,
    first_closing_index,
    parse_brackets,
    calc_points,
)


def test_closing_bracket_errors():
    assert parse_brackets("{([(<{}[<>[]}>{[]{[(<()>") == 12
    assert parse_brackets("[[<[([]))<([[{}[[()]]]") == 8
    assert parse_brackets("[{[{({}]{}}([{[{{{}}([]") == 7
    assert parse_brackets("[<(<(<(<{}))><([]([]()") == 10
    assert parse_brackets("<{([([[(<>()){}]>(<<{{") == 16


def test_closing_pos():
    first_closing_index("{([(<{}[<>[]}>{[]{[(<()>") == 7
    first_closing_index("{([(<[<>[]}>{[]{[(<()>") == 7
    first_closing_index("{([(<[[]}>{[]{[(<()>") == 7
    first_closing_index("{([(<[}>{[]{[(<()>") == 6
    first_closing_index("{([(<>{[]{[(<()>") == 5
    first_closing_index("{([({[]{[(<()>") == 6
    first_closing_index("{([({{[(<()>") == 10
    first_closing_index("{([({{[(<>") == 10
    first_closing_index("{([({{[(") == "{([({{[("
    first_closing_index("") == None


def test_calc_poitns():
    assert calc_points("[({([[{{") == 288957


# def test_solution_1():
#     test_input = ""
#     assert False


def test_solution_2():
    test_input = """[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n(((({<>}<{<{<>}{[]{[]{}\n{<[[]]>}<{[{[{[]{()[[[]\n<{([{{}}[<[[[<>{}]]]>[]]"""
    assert solution_2(test_input) == 288957
