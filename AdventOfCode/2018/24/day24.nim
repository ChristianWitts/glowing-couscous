# nim c -r -d:release

import strutils
import sequtils
import math
import sets

# parse and store at compile time
const lines = readFile("input").strip().splitlines()

proc part1(): int =


# proc part2(): int =


when isMainModule:
  echo(part1())
  # echo(part2())
