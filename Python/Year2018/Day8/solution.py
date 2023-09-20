from typing import Self, Optional


class Node:
    header: (int, int)
    sequence: [int]
    childs: [Self]

    def __init__(self, header, sequence, childs):
        self.header = header
        self.sequence = sequence
        self.childs = childs

    def sum_meta(self):
        return sum(c.sum_meta() for c in self.childs) + sum(self.meta_data)

    @property
    def meta_data(self):
        return self.sequence[len(self.sequence) - self.header[1] :]

    @property
    def value(self):
        if not self.childs:
            return self.sum_meta()
        else:
            return sum(
                [
                    self.childs[n - 1].value
                    for n in self.meta_data
                    if n - 1 < len(self.childs)
                ]
            )


def build_tree(sequence: [int]) -> (Node, [int]):
    header = sequence[0], sequence[1]
    child_seq = sequence[2:]
    childs = []
    for n in range(header[0]):
        cnode, child_seq = build_tree(child_seq)
        childs.append(cnode)

    len_cseq = sum([len(c.sequence) for c in childs])
    node_seq = sequence[: 2 + len_cseq + header[1]]
    remain_seq = sequence[len(node_seq) :]

    return Node(header, node_seq, childs), remain_seq


def parse_input(aoc_input: str):
    return [int(n) for n in aoc_input.strip().split(" ")]


def solution_1(aoc_input: str):
    nodes = parse_input(aoc_input)
    root, _ = build_tree(nodes)
    return root.sum_meta()


def solution_2(aoc_input: str):
    nodes = parse_input(aoc_input)
    root, _ = build_tree(nodes)
    return root.value
