# nim c -r -d:release

import strutils
import sequtils
import math
import sets
import tables

type
  Claim = tuple[claimId, x, y, xSize, ySize: int]
  Coords = tuple[x, y: int]

proc `range`(c: Claim, w: char): seq[int] {.inline.} =
  result = newSeq[int]()
  if w == 'x':
    for i in c.x .. c.x + c.xSize:
      result.add(i)
  else:
    for i in c.y .. c.y + c.ySize:
      result.add(i)

proc translate(s: string): seq[int] =
  var
    translationTable: seq[(string, string)]
  for c in 0..255:
    if c <= 47 or c >= 58:
      translationTable.add(($char(c), " "))
  # Poor mans `s.findAll(re"\d+").map(parseInt)` as the `re` module is impure
  # and thus can't be used for compile time consts

  for token in tokenize(s.multiReplace(translationTable)):
    if not token.isSep:
      result.add(token.token.parseInt)

proc parseLine(s: string): Claim =
  var r = translate(s)
  result = (r[0], r[1], r[2], r[3], r[4])

# parse and store at compile time
const claims = readFile("input").strip().splitlines().map(parseLine)

# echo claims[0]

proc part1(): int =
  var
    mapping: array[2048, array[2048, int]]
  echo claims[0]
    # mapping = initTable[string, array[0..1024, int]]
    # overlaps = initTable[int, initSet[int](2 ^ 8)]
    # overlaps = initTable[int, HashSet[int]]
    # coords: Coords

  # for claim in claims:
  #   # echo claim
  #   # break
  #   for x in `range`(claim, 'x'):
  #     for y in `range`(claim, 'y'):
  #       # echo coords
  #       # mapping[x][y] += 1
  #       # coords = (x, y)
  #       # # echo mapping[$x & "|" & $y]
  #       # echo mapping[x][y]
  #       # echo coords

  #       # echo mapping[coords]
  #       # if mapping[coords].len > 0:
  #       #   echo "greater than zero"

  #   #     echo coords
  #       break
  #     break
  #   break

  #   # overlaps[claim.claimId] = initSet[int](2 ^ 8)
  #   # overlaps[claim.claimId] = HashSet[int]
  #   for x in claim.x..claim.x+claim.xSize:
  #     for y in claim.y..claim.y+claim.ySize:
  #       coords = (x, y)

  #       if mapping[coords].len > 0:
  #         for num in mapping[coords]:
  #           overlaps[num].incl(claim.claimId)
  #           overlaps[claimId].incl(num)
  #       mapping[coords].incl(claim.claimId)

  var i: int
  # for k in mapping:
  #   if mapping[k].len > 1:
  #     i += 1

  # result = [x | (x <- )]

  # echo claims[0]
  return 0

  # from util import get_data
  # from collections import defaultdict
  # import re

  # data = get_data(3)
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

# proc part2(): int =


when isMainModule:
  echo(part1())
  # echo(part2())
