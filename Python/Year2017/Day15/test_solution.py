from .solution import solution_1, solution_2, NumberGenerator, judge_generation


def test_next_number_A():
    gen_a_expect = [
        (1092455, 1181022009),
        (1181022009, 245556042),
        (245556042, 1744312007),
        (1744312007, 1352636452),
    ]

    for exp_start, exp_next in gen_a_expect:
        gen = NumberGenerator(exp_start, 16807)
        gen.calc_next()
        assert gen.current == exp_next


def test_next_number_B():
    gen_a_expect = [
        (430625591, 1233683848),
        (1233683848, 1431495498),
        (1431495498, 137874439),
        (137874439, 285222916),
    ]

    for exp_start, exp_next in gen_a_expect:
        gen = NumberGenerator(exp_start, 48271)
        gen.calc_next()
        assert gen.current == exp_next


def test_gen_compare():
    gen_a = NumberGenerator(245556042, 0)
    gen_b = NumberGenerator(1431495498, 0)
    assert gen_a == gen_b


def test_judge():
    assert judge_generation(1092455, 430625591, 40_000_000) == 588
