#!/usr/bin/env python
from itertools import permutations


with open('input.txt', 'r') as fin:
    _input = [
        [int(c) for c in line.strip().split()]
        for line in fin.readlines()
    ]


def part1():
    print("================== PART 1 ==================")
    _in = _input
    print(
        sum(
            max(r) - min(r)
            for r in _in
        )
    )


def part2_helper(r):
    for perm in permutations(r, 2):
        pairs = sorted(perm)
        if not perm[1] % perm[0]:
            return int(perm[1] / perm[0])


def part2():
    print("================== PART 2 ==================")
    _in = _input
    print(
        sum(
            part2_helper(r)
            for r in _in
        )
    )


if __name__ == '__main__':
    part1()
    part2()
