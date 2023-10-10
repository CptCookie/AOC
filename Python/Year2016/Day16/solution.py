def inflate_dragon(start: str, length: int):
    data = start
    while len(data) < length:
        b = "".join(["1" if c == "0" else "0" for c in data[-1::-1]])
        data = data + "0" + b

    return data[:length]


def checksum(data: str) -> str:
    csum = data

    while len(csum) % 2 == 0:
        new_sum = ""
        for a, b in zip(*([iter(csum)] * 2)):
            if a == b:
                new_sum += "1"
            else:
                new_sum += "0"
        csum = new_sum
    return csum


def solution_1(aoc_input: str):
    input = aoc_input.strip()
    data = inflate_dragon(input, 272)
    return checksum(data)


def solution_2(aoc_input: str):
    input = aoc_input.strip()
    data = inflate_dragon(input, 35651584)
    return checksum(data)
