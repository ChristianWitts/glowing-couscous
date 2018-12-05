# nim c -r -d:release day2.nim
import strutils
import sequtils
import math
import sets
import tables

# parse and store at compile time
const lines = readFile("input").strip().splitlines()

proc scan(s: string, n: int): bool =
  result = false
  var
    counter = initTable[char, int]()
  for c in s:
    if c notin counter:
      counter[c] = 1
    else:
      counter[c] += 1
  for _, v in counter:
    if v == n:
      result = true
      break

proc part1(): int =
  var
    twos, threes: int
  for line in lines:
    if scan(line, 2) == true:
      twos += 1
    if scan(line, 3) == true:
      threes += 1
  result = twos * threes

proc diff(s1, s2: string): int =
  var
    n, pos, idx: int
  result = -1
  while idx <= s1.len:
    if s1[idx] != s2[idx]:
      n += 1
      if n >= 2:
        break
      pos = idx
    idx += 1
  if n == 1:
    return pos

proc part2(): int =
  var
    p: int
  for l1 in lines:
    for l2 in lines:
      p = diff(l1, l2)
      if p != -1:
        echo(l1)
        echo(l2)
        return p

when isMainModule:
  echo(part1())
  echo(part2())
