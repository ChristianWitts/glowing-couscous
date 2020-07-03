# All of this was written beforehand.
import re
def ints(s: str):
    return list(map(int, re.findall(r"-?\d+", s)))  # thanks mserrano!

def psub(x, y):
    if len(x) == 2: return [x[0] - y[0], x[1] - y[1]]
    return [a-b for a, b in zip(x, y)]

def pdist1(x, y=None):
    if y is not None: x = psub(x, y)
    if len(x) == 2: return abs(x[0]) + abs(x[1])
    return sum(map(abs, x))

class UnionFind:
    # n: int
    # parents: List[Optional[int]]
    # ranks: List[int]
    # num_sets: int

    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [None] * n
        self.ranks = [1] * n
        self.num_sets = n

    def find(self, i: int) -> int:
        p = self.parents[i]
        if p is None:
            return i
        p = self.find(p)
        self.parents[i] = p
        return p

    def in_same_set(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)

    def merge(self, i: int, j: int) -> None:
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return

        i_rank = self.ranks[i]
        j_rank = self.ranks[j]

        if i_rank < j_rank:
            self.parents[i] = j
        elif i_rank > j_rank:
            self.parents[j] = i
        else:
            self.parents[j] = i
            self.ranks[i] += 1
        self.num_sets -= 1

# Here begins the actual code for today:
# inp = """
# 0,0,0,0
# 3,0,0,0
# 0,3,0,0
# 0,0,3,0
# 0,0,0,3
# 0,0,0,6
# 9,0,0,0
# 12,0,0,0
# """.strip()

with open('input') as fin:
    lines = [line.strip() for line in fin.readlines()]

# lines = inp.splitlines()

to_i = dict()

uf = UnionFind(len(lines))

for i, line in enumerate(lines):
    p = tuple(ints(line))
    to_i[p] = i

    for point in to_i:
        if pdist1(p, point) <= 3:
            uf.merge(i, to_i[point])
print(uf.num_sets)
