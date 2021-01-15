from .solution import parse_bootcode, run_boot, fix_bootcode


def test_loop():
    bootcode = parse_bootcode(
        """nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6""".split(
            "\n"
        )
    )
    assert run_boot(bootcode) == (1, 5)


def test_fixed_bootcode():
    bootcode = parse_bootcode(
        """nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1 \nnop -4\nacc +6""".split(
            "\n"
        )
    )
    assert run_boot(bootcode) == (9, 8)


def test_fix():
    bootcode = parse_bootcode(
        """nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6""".split(
            "\n"
        )
    )
    assert fix_bootcode(bootcode) == (9, 8)


def test_parse_bootcode():
    assert parse_bootcode(["acc -99"]) == [("acc", -99)]
