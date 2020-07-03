# `nimble install itertools` for 3rd party dependencies
# nim c -r -d:release

import strutils
import sequtils
import math
import sets
import re

type
  Position = tuple[x, y: int]
  Velocity = tuple[x, y: int]
  Record = tuple[position: Position, velocity: Velocity]

proc parseLine(s: string): Record =
  var
    line = s.findAll(re"\d+").map(parseInt)
  result = ((line[0], line[1]), (line[2], line[3]))

# parse and store at compile time
# Can't make this a `const` due to the `re` package being impure
var lines = readFile("input").strip().splitlines().map(parseLine)

proc part1(): int =
  var
    t: int
    mut: seq[Record]


  # from collections import defaultdict
  # import re

  # with open('input') as fin:
  #     data = fin.readlines()

  # d = map(tuple, map(lambda s: map(int, re.findall(r'-?\d+', s)), data))

  # t = 0
  # while True:
  #   new_d = []
  #   for (pos_x, pos_y, vel_x, vel_y) in d:
  #     new_d.append((pos_x + vel_x, pos_y + vel_y, vel_x, vel_y))
  #   d = new_d
  #   t += 1
  #   no_solos = True
  #   mapping = defaultdict(bool)
  #   for (pos_x, pos_y, _, _) in d:
  #     mapping[(pos_x, pos_y)] = True
  #   for (pos_x, pos_y) in mapping:
  #     if not any((pos_x + delta, pos_y + delta2) in mapping for delta in xrange(-1, 2) for delta2 in xrange(-1, 2) if (delta, delta2) != (0, 0)):
  #       no_solos = False
  #       break
  #   if no_solos:
  #     min_x = min(z[0] for z in mapping)
  #     min_y = min(z[1] for z in mapping)
  #     max_x = max(z[0] for z in mapping)
  #     max_y = max(z[1] for z in mapping)
  #     for y in xrange(min_y, max_y+1):
  #       s = []
  #       for x in xrange(min_x, max_x+1):
  #         if mapping[(x, y)]:
  #           s.append('#')
  #         else:
  #           s.append('.')
  #       print ''.join(s)
  #     print t


# proc part2(): int =


when isMainModule:
  echo(part1())
  # echo(part2())
