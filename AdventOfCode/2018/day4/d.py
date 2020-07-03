with open('input') as fin:
    lines = [line.strip() for line in fin]
#     attribs = [line.split() for line in lines]

# a = [[0] * 1000] * 1000

# #1 @ 335,861: 14x10
# #2 @ 97,613: 24x14
# #3 @ 118,29: 25x13

# for att in attribs:
#     coords = att[2].replace(':', '').split(',')
#     coords = (int(coords[0]), int(coords[1]))
#     size = att[3].split('x')
#     size = (int(size[0]), int(size[1]))

#     for j in range(size[1]):
#         for i in range(size[0]):
#             a[coords[0] + i][coords[1] + j] += 1

# count = 0

# for i in a:
#     for j in i:
#         if j >= 2:
#             count += 1

# print(count)


# from util import get_data
# from collections import defaultdict
# import re

# # data = get_data(3)
# claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
# m = defaultdict(list)
# overlaps = {}
# for (claim_number, start_x, start_y, width, height) in claims:
#   overlaps[claim_number] = set()
#   for i in xrange(start_x, start_x + width):
#     for j in xrange(start_y, start_y + height):
#       if m[(i,j)]:
#         for number in m[(i, j)]:
#           overlaps[number].add(claim_number)
#           overlaps[claim_number].add(number)
#       m[(i,j)].append(claim_number)

# print "a", len([k for k in m if len(m[k]) > 1])
# print "b", [k for k in overlaps if len(overlaps[k]) == 0][0]


from collections import defaultdict

def parse(line):
    ids, _, offset, d = line.split()
    left, top = offset[:-1].split(",")
    width, height = d.split("x")
    return ids, int(left), int(top), int(width), int(height)

def solve(lines):
    data = [parse(line) for line in lines]
    overlaps = defaultdict(int)
    for _, l, t, w, h in data:
        for i in range(w):
            for j in range(h):
                overlaps[(i + l, j + t)] += 1

    total = 0
    for v in overlaps.values():
        if v > 1:
            total += 1

    # Part 1
    print(total)

    for ids, l, t, w, h in data:
        isValid = True
        for i in range(w):
            for j in range(h):
                if overlaps[(i + l, j + t)] != 1:
                    isValid = False
                    break
            if not isValid:
                break
        if isValid:
            # Part 2
            print(ids[1:])

solve(lines)
