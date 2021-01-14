import hashlib


def find_hash(puzzle_input, leeding_zeros):
    number = 0
    while number < 1e7:
        md5 = hashlib.md5()
        md5.update((puzzle_input + str(number)).encode())
        if valid_hash(md5.hexdigest(), leeding_zeros):
            return number
        number += 1


def valid_hash(hash, leeding_zeros):
    for n in hash[:leeding_zeros]:
        if n != "0":
            return False
    return True


def solve(puzzle_input):
    puzzle_input = puzzle_input.replace("\n", "")
    print(f"solution 1: {find_hash(puzzle_input, 5)}")
    print(f"solution 2: {find_hash(puzzle_input, 6)}")
