import hashlib


def find_hash_with_leeding_zeros(string: str, leeding_zeros: int):
    extra_number = 0
    while extra_number < 1e7:
        md5 = hashlib.md5()
        md5.update((string + str(extra_number)).encode())
        if is_valid_hash(md5.hexdigest(), leeding_zeros):
            return extra_number
        extra_number += 1


def is_valid_hash(hash: str, leeding_zeros: int):
    for n in hash[:leeding_zeros]:
        if n != "0":
            return False
    return True


def solution_1(puzzle_input):
    puzzle_input = puzzle_input.replace("\n", "")
    return find_hash_with_leeding_zeros(puzzle_input, 5)


def solution_2(puzzle_input):
    puzzle_input = puzzle_input.replace("\n", "")
    return find_hash_with_leeding_zeros(puzzle_input, 6)
