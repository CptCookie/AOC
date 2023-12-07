from .solution import solution_1, solution_2, parse_input, CARD_ORDER, Hand, HandType

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

TEST_DATA = [
    (Hand("32T3K"), 765),
    (Hand("T55J5"), 684),
    (Hand("KK677"), 28),
    (Hand("KTJJT"), 220),
    (Hand("QQQJA"), 483),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_hand_type():
    assert Hand("KKKKK").type == HandType.FIVE_OAK
    assert Hand("AKKKK").type == HandType.FOUR_OAK
    assert Hand("KKKKA").type == HandType.FOUR_OAK
    assert Hand("KKAAA").type == HandType.FULL
    assert Hand("KAKAK").type == HandType.FULL
    assert Hand("KKKAJ").type == HandType.THREE_OAK
    assert Hand("KAKJK").type == HandType.THREE_OAK
    assert Hand("TTT98").type == HandType.THREE_OAK
    assert Hand("KKQQJ").type == HandType.TWO_PAIR
    assert Hand("KQKQJ").type == HandType.TWO_PAIR
    assert Hand("23432").type == HandType.TWO_PAIR
    assert Hand("A23A4").type == HandType.TWO_OAK
    assert Hand("A2364").type == HandType.ONE_OAK


def test_compare_type():
    assert Hand("KKKKA") < Hand("KKKKK")
    assert Hand("KKKKK") > Hand("KKKKA")
    assert Hand("33332") > Hand("2AAAA")


def test_solution_1():
    assert solution_1(TEST_INPUT) == 6440


def test_solution_2():
    assert solution_2(TEST_INPUT) == 5905
