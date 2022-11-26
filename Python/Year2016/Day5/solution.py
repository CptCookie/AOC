from hashlib import md5


def get_md5_hash(string: str) -> str:
    return md5(string.encode()).hexdigest()


def get_pw(door_id: str):
    pw = ""
    counter = -1
    while True:
        counter += 1
        hash_step = get_md5_hash(f"{door_id}{counter}")

        if hash_step[:5] == "00000":
            pw += hash_step[5]

        if len(pw) >= 8:
            return pw


def get_pw_v2(door_id: str):
    pw = ["_"] * 8
    counter = -1
    while True:
        counter += 1
        hash_step = get_md5_hash(f"{door_id}{counter}")
        if hash_step[:5] == "00000":

            try:
                index = int(hash_step[5])
                if pw[index] == "_":
                    pw[index] = hash_step[6]
            except (ValueError, IndexError):
                pass

        if len([n for n in pw if n.isalnum()]) >= 8:
            return "".join(pw)


def solution_1(puzzle_input: str):
    return get_pw(puzzle_input.strip())


def solution_2(puzzle_input: str):
    return get_pw_v2(puzzle_input.strip())
