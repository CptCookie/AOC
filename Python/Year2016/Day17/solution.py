import heapq
from hashlib import md5

OPEN = "bcedef"
CLOSED = "0123456789a"

DPOS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
DIR = "UDLR"


def get_md5(string):
    return md5(string.encode()).hexdigest()


def get_moves(passcode, current):
    open_doors = [d in OPEN for d in get_md5(passcode)[:4]]
    next_pos = [
        (DIR[i], (DPOS[i][0] + current[0], DPOS[i][1] + current[1]))
        for i, d in enumerate(open_doors)
        if d
    ]
    next_pos = [n for n in next_pos if 0 <= n[1][0] <= 3 and 0 <= n[1][1] <= 3]
    return next_pos


def find_way(passcode, shortest=True):
    q = []
    # start position length=0, directions empty, position (0,0)
    heapq.heappush(q, (0, "", (0, 0)))
    longest = 0

    while q:
        l, d, pos = heapq.heappop(q)
        if pos == (3, 3):
            if shortest:
                return d
            elif l > longest:
                longest = l
        else:
            next_pos = get_moves(f"{passcode}{d}", pos)
            for nd, npos in next_pos:
                heapq.heappush(q, (l + 1, d + nd, npos))

    return longest


def solution_1(aoc_input: str):
    input = aoc_input.strip()
    return find_way(input)


def solution_2(aoc_input: str):
    input = aoc_input.strip()
    return find_way(input, shortest=False)
