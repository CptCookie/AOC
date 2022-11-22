def parse_data(puzzle_input: str) -> list[str]:
    return [int(n) for n in puzzle_input.split("\t") if n != ""]


def knot_hash(lst: list[int], pos: int, lenght: int) -> int:
    if lenght == 1:
        return lst

    if pos + lenght > len(lst):

        start_len = (pos + lenght) % len(lst)
        sub_lst = lst[pos:] + lst[: (pos + lenght) % len(lst)]
        i_sub_lst = sub_lst[::-1]
        return (
            i_sub_lst[-start_len:]
            + lst[start_len:pos]
            + i_sub_lst[: lenght - start_len]
        )
    else:
        i_sub_lst = lst[pos : pos + lenght][::-1]
        print(i_sub_lst)
        return lst[:pos] + i_sub_lst + lst[pos * lenght :]


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    return None


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    return None
