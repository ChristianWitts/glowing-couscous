# nim c -r -d:release

import strutils
import sequtils
import math
import sets
import sugar

# parse and store at compile time
const gridSerial = readFile("input").strip().parseInt()

type
  GridArray = array[1..300, int]
  Grid2DArray = array[1..300, GridArray]
  Coords = tuple[x, y: int]
  CoordSize = tuple[x, y, size: int]

proc generateGrid(): Grid2DArray =
  var
    grid: Grid2DArray
    rackId, powerLevel: int
    powerString: string

  for y in 1..300:
    for x in 1..300:
      rackId = x + 10
      powerLevel = rackId * y
      powerLevel += gridSerial
      powerLevel *= rackId
      powerString = intToStr(powerLevel, 3)
      powerLevel = int(powerString[powerString.len - 3]) - 48
      powerLevel -= 5
      grid[x][y] = powerLevel

  return grid

# Generate the grid and store at compile time
const grid = generateGrid()

proc part1(): Coords =
  var
    maxValue: int
    coords: Coords
    sumInterim: int

  for y in 1..298:
    for x in 1..298:
      sumInterim = sum(grid[x][y..y+2])
      sumInterim += sum(grid[x+1][y..y+2])
      sumInterim += sum(grid[x+2][y..y+2])

      if sumInterim > maxValue:
        coords = (x, y)
        maxValue = sumInterim

  return coords

proc part2(): CoordSize =
  var
    maxValue, sumInterim, previousValue: int
    coords: CoordSize

  for size in 0..299:
    for y in 1..300-size:
      for x in 1..300-size:
        sumInterim = 0
        for s in 0..size:
          sumInterim += sum(grid[x+s][y..y+size])

        if sumInterim > maxValue:
          coords = (x, y, size+1)
          maxValue = sumInterim

    if maxValue != previousValue:
      echo(maxValue, " -> ", coords)
      previousValue = maxValue

  return coords

when isMainModule:
  echo(part1())
  echo(part2())
