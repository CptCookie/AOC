from enum import IntEnum
from functools import total_ordering

CARD_ORDER = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
CARD_ORDER_JOKER = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J")


class HandType(IntEnum):
    FIVE_OAK = 7
    FOUR_OAK = 6
    FULL = 5
    THREE_OAK = 4
    TWO_PAIR = 3
    TWO_OAK = 2
    ONE_OAK = 1


@total_ordering
class Hand:
    def __init__(self, cards, jokers=False):
        self.hand = cards
        self.jokers = jokers

    def __repr__(self):
        return self.hand

    @property
    def type(self) -> HandType:
        unique = set(self.hand)
        if self.jokers and "J" in unique:
            unique.remove("J")

        multiples = tuple(c for c in unique if self.hand.count(c) > 1)
        if self.jokers and self.hand.count("J") > 0 and len(multiples) == 0:
            # make the first card the multiple one b/c jokes have to go somewhere
            multiples = (self.hand[0],)

        match len(unique), len(multiples):
            case x, _ if x == 5:
                return HandType.ONE_OAK
            case x, _ if x == 4:
                return HandType.TWO_OAK
            case x, y if x == 3 and y == 1:
                return HandType.THREE_OAK
            case x, y if x == 3 and y == 2:
                return HandType.TWO_PAIR
            case x, y if x == 2 and y == 1:
                return HandType.FOUR_OAK
            case x, y if x == 2 and y == 2:
                return HandType.FULL
            case x, _ if x == 1:
                return HandType.FIVE_OAK
            case x, _ if x == 0 and self.jokers:
                # we only have jokers
                return HandType.FIVE_OAK

        raise ValueError(f"To much cards: {self.hand}")

    def __eq__(self, other):
        return self.hand == other.hand

    def __lt__(self, other):
        if self.type == other.type:
            # compare by face values
            for s, o in zip(self.hand, other.hand):
                card_orders = CARD_ORDER_JOKER if self.jokers else CARD_ORDER
                if card_orders.index(s) != card_orders.index(o):
                    return card_orders.index(s) > card_orders.index(o)
        else:
            # compare by combinations/types
            return self.type < other.type


def parse_input(aoc_input: str, jokers=False):
    pairs = []

    for line in aoc_input.strip().splitlines():
        cards, bid, *_ = line.split(" ")
        pairs.append((Hand(cards, jokers), int(bid)))

    return pairs


def solution_1(aoc_input: str):
    pairs = parse_input(aoc_input)
    pairs.sort(key=lambda x: x[0])

    value = 0
    for i, (hand, bid) in enumerate(pairs):
        value += (i + 1) * bid
    return value


def solution_2(aoc_input: str):
    pairs = parse_input(aoc_input, True)
    pairs.sort(key=lambda x: x[0])

    value = 0
    for i, (hand, bid) in enumerate(pairs):
        value += (i + 1) * bid
    return value
