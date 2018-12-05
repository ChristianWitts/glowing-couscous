# nim c -r -d:release

import strutils
import sequtils
import math
import sets
import strformat

# parse and store at compile time
const lines = readFile("input").strip()

proc decompose(s: string): string =
  var
    start, `end`: int
    setList = s.toLower().toSet()
    charStr = newStringOfCap(1)
    polymer = s

  start = polymer.len()
  while start != `end`:
    `end` = start
    for c in setList:
      add(charStr, c)

      polymer = replace(polymer, fmt"{charStr}{charStr.toUpper()}")
      polymer = replace(polymer, fmt"{charStr.toUpper()}{charStr}")
      charStr = ""
    start = polymer.len()

  return polymer

proc preDecompose(s: string, c: char): string =
  var
    polymer = s
    charStr = newStringOfCap(1)

  add(charStr, c)
  polymer = replace(polymer, charStr)
  polymer = replace(polymer, charStr.toUpper())

  return decompose(polymer)

proc part1(): int =
  var newPolymer = decompose(lines)
  return newPolymer.len()

proc part2(): int =
  var
    newPolymer = decompose(lines)
    shortest: int = newPolymer.len()

  for c in newPolymer.toLower().toSet():
    var testStr = preDecompose(newPolymer, c)
    if testStr.len() < shortest:
      shortest = testStr.len()

  return shortest

when isMainModule:
  echo(part1())
  echo(part2())
