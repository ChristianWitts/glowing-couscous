# The lumber collection area is 50 acres by 50 acres; each acre can be either open ground (.), trees (|), or a lumberyard (#). You take a scan of the area (your puzzle input).

# Strange magic is at work here: each minute, the landscape looks entirely different. In exactly one minute, an open acre can fill with trees, a wooded acre can be converted to a lumberyard, or a lumberyard can be cleared to open ground (the lumber having been sent to other projects).

# The change to each acre is based entirely on the contents of that acre as well as the number of open, wooded, or lumberyard acres adjacent to it at the start of each minute. Here, "adjacent" means any of the eight acres surrounding that acre. (Acres on the edges of the lumber collection area might have fewer than eight adjacent acres; the missing acres aren't counted.)

# In particular:

# An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
# An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
# An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
# These changes happen across all acres simultaneously, each of them using the state of all acres at the beginning of the minute and changing to their new form by the end of that same minute. Changes that happen during the minute don't affect each other.

# For example, suppose the lumber collection area is instead only 10 by 10 acres with this initial configuration:

with open('input') as fin:
    grid = [list(line.strip()) for line in fin if line.strip()]

for idx, row in enumerate(grid):
    row.insert(0, None)
    row.insert(-1, None)
    grid[idx] = row
grid.insert(0, [None for _ in range(52)])
grid.insert(-1, [None for _ in range(52)])
# print(grid[:2])

def surrounds(grid, location):
    # if location[0] == 0: startX = 0
    # else:                startX = location[0] - 1
    # if location[1] == 0:
    #     startY = 0
    #     endY = 2
    # else:
    #     startY = location[1] - 1
    #     endY = location[1] + 1
    #     if endY >= 49:
    #         endY = 49

    # adjacent = []
    # adjacent.extend(grid[startX][startY:endY])
    # adjacent.extend(grid[startX+1][startY:endY])
    # if not (startX == 0 or startX == 48):
    #     adjacent.extend(grid[startX+2][startY:endY])
    # # adjacent.pop(4) # don't need self

    startX = location[0] - 1
    startY = location[1] - 1

    adjacent = []
    adjacent.extend(grid[startX][startY:startY+2])
    adjacent.extend(grid[startX+1][startY:startY+2])
    adjacent.extend(grid[startX+2][startY:startY+2])
    adjacent.pop(4) # don't need self

    return adjacent


def gridCheck(grid, location):
    newState = grid[location[0]][location[1]]
    posSurrounds = surrounds(grid, location)
    if newState == '.':
        if posSurrounds.count('|') >= 3:
            newState = '|'
    elif newState == '|':
        if posSurrounds.count('#') >= 3:
            newState = '#'
    elif newState == '#':
        if posSurrounds.count('#') >= 1 and posSurrounds.count('|') >= 1:
            newState = '#'
        else:
            newState = '.'

    return newState



for turn in range(10):
    newGenGrid = [[None for _ in range(52)] for _ in range(52)]
    for x in range(1, 51):
        for y in range(1, 51):
            newGenGrid[x][y] = gridCheck(grid, (x, y))
    grid = newGenGrid

# Wood * Lumber
wood, yard = 0, 0
for row in grid:
    wood += row.count('|')
    yard += row.count('#')

print(wood, yard, wood*yard)
