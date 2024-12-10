from typing import Optional


Block = tuple[Optional[int], int]


def parse_input(aoc_input: str) -> list[Block]:
    # list of id and length of block
    # empty block has no id
    blocks = []

    next_id = 0
    value_block = True

    for n in aoc_input:
        if not n.isdigit():
            continue

        if value_block:
            blocks.append((next_id, int(n)))
            next_id += 1
            value_block = False
        else:
            if n != "0":
                blocks.append((None, int(n)))
            value_block = True

    return blocks


def defrag_sectors(blocks: list[Block]) -> list[Block]:
    empty_idx = 1

    try:
        while True:
            # get new block
            id, size = blocks.pop()

            if id is None:
                continue

            while size > 0:
                empty_size = blocks[empty_idx][1]
                # put the block somewhere

                if empty_size <= size:
                    # fill the entire empty block
                    blocks[empty_idx] = (id, empty_size)
                    size -= empty_size
                    empty_idx = get_next_empty_idx(blocks, empty_idx)

                elif blocks[empty_idx][1] > size:
                    # split the empty block
                    blocks[empty_idx] = (None, empty_size - size)
                    blocks = blocks[:empty_idx] + [(id, size)] + blocks[empty_idx:]
                    empty_idx += 1
                    size = 0

    except IndexError:
        # add the remaing size to the end again
        if size > 0 and blocks[-1][0] == id:
            blocks[-1] = (id, blocks[-1][1] + size)
        elif size > 0:
            blocks.append((id, size))
        return [b for b in blocks if b[1] > 0]


def defrag_blocks(blocks: list[Block]) -> list[Block]:
    idx = len(blocks) - 1
    while idx > 0:
        id, size = blocks[idx]
        if id is None:
            idx -= 1
            continue

        for target_idx in range(idx):
            target_id, target_size = blocks[target_idx]

            if target_id is None and target_size == size:
                blocks[target_idx] = (id, size)
                blocks[idx] = (None, size)
                break

            elif target_id is None and target_size > size:
                blocks[target_idx] = (None, target_size - size)
                blocks[idx] = (None, size)
                blocks = blocks[:target_idx] + [(id, size)] + blocks[target_idx:]
                idx += 1  # because we got an extra element
                break

        idx -= 1

    return blocks


def get_next_empty_idx(blocks: list[Block], current_idx: int) -> int:
    while True:
        if blocks[current_idx][0] is None:
            return current_idx
        current_idx += 1


def calculate_checksum(blocks: list[Block]) -> int:
    sector_idx = 0
    value = 0
    for id, size in blocks:
        if id is None:
            sector_idx += size
            continue
        for n in range(size):
            value += id * sector_idx
            sector_idx += 1
    return value


def solution_1(aoc_input: str):
    blocks = parse_input(aoc_input)
    blocks = defrag_sectors(blocks)
    return calculate_checksum(blocks)


def solution_2(aoc_input: str):
    blocks = parse_input(aoc_input)
    blocks = defrag_blocks(blocks)
    return calculate_checksum(blocks)
