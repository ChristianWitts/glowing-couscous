# `nimble install itertools` for 3rd party dependencies
# nim c -r day1.nim

import strutils
import sequtils
import math
import sets

from itertools import cycle

# parse and store at compile time
const lines = readFile("input").strip().splitlines().map(parseInt)

proc part1(): int =
  result = lines.sum

proc part2(): int =
  var
    seen = initSet[int](2 ^ 17)
    freq = 0

  seen.incl(freq)

  for i in lines.cycle():
    freq += i
    if freq notin seen:
      seen.incl(freq)
    else:
      break

  result = freq

when isMainModule:
  echo(part1())
  echo(part2())
