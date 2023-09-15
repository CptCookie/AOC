"""
generate hash md5 from puzzleinput+index
if the hash contains triplet and hash from index+1 until index+1000 contains pentlet the hash is valid
what is the index of the 64th hash
"""
from collections import defaultdict
from hashlib import md5

hashes = {}
streched_hashes = {}


def get_hash(salt: str, index) -> str:
    if index in hashes:
        return hashes[index]
    else:
        h = md5(f"{salt}{index}".encode()).hexdigest()
        hashes[index] = h
        return h


def get_streched_hash(salt: str, index) -> str:
    if index in streched_hashes:
        return streched_hashes[index]
    else:
        h = f"{salt}{index}"
        for _ in range(2017):
            h = md5(h.encode()).hexdigest()

        streched_hashes[index] = h
        return h


def get_combo_char(string: str, number: int):
    if len(string) < number:
        raise ValueError()

    for n in range(len(string) - number + 1):
        c = string[n]
        if all([c == string[n + m] for m in range(number)]):
            return c
    return None


def hash_valid(salt: str, index: int, stretched=False):
    hash_function = get_hash if not stretched else get_streched_hash

    index_hash = hash_function(salt, index)
    combo_char = get_combo_char(index_hash, 3)
    if combo_char is None:
        return False

    for n in range(1, 1001):
        if get_combo_char(hash_function(salt, index + n), 5) == combo_char:
            return True
    return False


def get_hashes(salt: str, stretched=False):
    hash_indexes = []
    counter = 0
    while len(hash_indexes) < 64:
        if hash_valid(salt, counter, stretched):
            hash_indexes.append(counter)
            print(len(hash_indexes), end="\r")

        counter += 1

    return hash_indexes


def solution_1(puzzle_input: str):
    return get_hashes(puzzle_input.strip())[-1]


def solution_2(puzzle_input: str):
    return get_hashes(puzzle_input.strip(), stretched=True)[-1]
