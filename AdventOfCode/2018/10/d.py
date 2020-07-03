import collections
import re

#with open('day10test.txt') as f:
with open('input') as f:
  lines = [l.rstrip('\n') for l in f]
  lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]
#   print lines

  smallest = 2 ** 20
  idx = -1

  for i in xrange(0 and 20000):
    minx = min(x + i * vx for (x, y, vx, vy) in lines)
    maxx = max(x + i * vx for (x, y, vx, vy) in lines)
    miny = min(y + i * vy for (x, y, vx, vy) in lines)
    maxy = max(y + i * vy for (x, y, vx, vy) in lines)

    if (maxx - minx + maxy - miny) < smallest:
      idx = i
    # print i, maxx - minx + maxy - miny

  map = [[' '] * 200 for j in xrange(400)]
#   i = 10946
  for (x, y, vx, vy) in lines:
    map[y + idx * vy][x + idx * vx - 250] = '*'

  for m in map:
    print ''.join(m)
