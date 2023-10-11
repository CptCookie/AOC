from enum import Enum


class OPS(Enum):
    SWAP_POS = "swap position"
    SWAP_LETTER = "swap letter"
    ROTATE = "rotate left/right"
    ROTATE_LETTER = "rotate letter based"
    REVERSE_SEQ = "reverse"
    MOVE = "move"


def parse_input(aoc_input: str):
    instr = []
    for line in aoc_input.splitlines():
        words = line.split(" ")
        match words[:2]:
            case ["swap", "position"]:
                instr.append((OPS.SWAP_POS, (int(words[2]), int(words[5]))))
            case ["swap", "letter"]:
                instr.append((OPS.SWAP_LETTER, (words[2], words[5])))
            case ["rotate", "right"]:
                instr.append((OPS.ROTATE, -int(words[2])))
            case ["rotate", "left"]:
                instr.append((OPS.ROTATE, int(words[2])))
            case ["rotate", "based"]:
                instr.append((OPS.ROTATE_LETTER, words[6]))
            case ["reverse", "positions"]:
                instr.append((OPS.REVERSE_SEQ, (int(words[2]), int(words[4]))))
            case ["move", "position"]:
                instr.append((OPS.MOVE, (int(words[2]), int(words[5]))))
            case _:
                print(f"UNKNOWN CASE {words}")
    return instr


def swap_pos(pw: list[str], a, b):
    pw[a], pw[b] = pw[b], pw[a]
    return pw


def swap_letter(pw: list[str], a, b):
    a_pos = pw.index(a)
    b_pos = pw.index(b)
    return swap_pos(pw, a_pos, b_pos)


def rotate(pw, amount):
    return pw[amount:] + pw[:amount]


def rotate_letter(pw, letter):
    idx = pw.index(letter)
    rotation = 1 + idx + (1 if idx >= 4 else 0)
    rotation %= len(pw)
    return rotate(pw, -rotation)


def reverse_rotate_letter(pw, letter):
    for n in range(len(pw)):
        rpw = rotate(pw, n)

        if rotate_letter(rpw, letter) == pw:
            return rpw


def reverse(pw, start, end):
    return pw[:start] + list(reversed(pw[start : end + 1])) + pw[end + 1 :]


def move(pw: list[str], a, b):
    letter = pw[a]
    del pw[a]

    pw.insert(b, letter)
    return pw


def scamble_pw(pw, instr):
    ops_mapping = {
        OPS.SWAP_POS: swap_pos,
        OPS.SWAP_LETTER: swap_letter,
        OPS.ROTATE: rotate,
        OPS.ROTATE_LETTER: rotate_letter,
        OPS.REVERSE_SEQ: reverse,
        OPS.MOVE: move,
    }

    for i in instr:
        if isinstance(i[1], tuple):
            pw = ops_mapping[i[0]](pw, *i[1])
        else:
            pw = ops_mapping[i[0]](pw, i[1])

    return pw


def unscramble_pw(pw, instr):
    for i in reversed(instr):
        match i[0]:
            case OPS.SWAP_POS:
                pw = swap_pos(pw, *i[1])
            case OPS.SWAP_LETTER:
                pw = swap_letter(pw, *i[1])
            case OPS.ROTATE:
                pw = rotate(pw, -i[1])
            case OPS.ROTATE_LETTER:
                pw = reverse_rotate_letter(pw, i[1])
            case OPS.REVERSE_SEQ:
                pw = reverse(pw, *i[1])
            case OPS.MOVE:
                pw = move(pw, *reversed(i[1]))
    return pw


def solution_1(aoc_input: str, seed="abcdefgh"):
    input = parse_input(aoc_input)
    return "".join(scamble_pw(list(seed), input))


def solution_2(aoc_input: str, seed="fbgdceah"):
    input = parse_input(aoc_input)
    return "".join(unscramble_pw(list(seed), input))
