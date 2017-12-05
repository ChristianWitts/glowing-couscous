#!/usr/bin/env python

with open('input.txt', 'r') as fin:
    _input = [
        int(c)
        for c in fin.read().strip()
    ]


def part1():
    print("================== PART 1 ==================")
    _in = _input + [_input[0]]
    l_in = len(_in)
    print(
        sum(
            _in[i]
            for i in range(l_in-1)
            if _in[i] == _in[i+1]
        )
    )


def part2():
    print("================== PART 1 ==================")
    _in = _input
    l_in = int(len(_in)/2)
    print(
        sum(
            _in[i]*2
            for i in range(l_in)
            if _in[i] == _in[i+l_in]
        )
    )


if __name__ == '__main__':
    part1()
    part2()
