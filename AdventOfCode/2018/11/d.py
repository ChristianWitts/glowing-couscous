_input = 6042

# Find the fuel cell's rack ID, which is its X coordinate plus 10.
# Begin with a power level of the rack ID times the Y coordinate.
# Increase the power level by the value of the grid serial number (your puzzle input).
# Set the power level to itself multiplied by the rack ID.
# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
# Subtract 5 from the power level.

grid = [[0] * 300] * 300
grid = [[None for _ in range(300)] for _ in range(300)]

for y in range(1, 301):
    for x in range(1, 301):
        # if y < 4 and x < 4:
        #     print(x, y)
        #     rack_id = x + 10
        #     print(rack_id)
        #     power_level = rack_id * y
        #     print(power_level)
        #     power_level += _input
        #     print(power_level)
        #     power_level *= rack_id
        #     print(power_level)
        #     power_level = int(str(power_level).zfill(3)[-3])
        #     print(power_level)
        #     power_level -= 5
        #     print(power_level)
        #     grid[x-1][y-1] = power_level
        # else:

        # print(x, y)
        rack_id = x + 10
        # print(rack_id)
        power_level = rack_id * y
        # print(power_level)
        power_level += _input
        # print(power_level)
        power_level *= rack_id
        # print(power_level)
        power_level = int(str(power_level).zfill(3)[-3])
        # print(power_level)
        power_level -= 5
        # print(power_level)
        grid[x-1][y-1] = power_level
    #     break
    # break

# print(grid[0][0])
# r = 11
# p = 11
# p = 6053
# p = 6053

_max = 0
coords = None

for y in range(298):
    for x in range(298):
        # print(x, y)
        # print(grid[x][y:y+3], grid[x+1][y:y+3], grid[x+2][y:y+3])
        _sum = sum(grid[x][y:y+3])
        _sum += sum(grid[x+1][y:y+3])
        _sum += sum(grid[x+2][y:y+3])

        if _sum > _max:
            coords = (x+1, y+1)
            _max = _sum

    #     break
    # break

print(_max, coords)

_max = -1000000000
coords = None

for size in range(1, 300):
    for y in range(300-size):
        for x in range(300-size):
            _sum = sum(grid[x_][y_] for x_ in range(x, x+size) for y_ in range(y, y+size))
            # for s in range(size):
            #     _sum += sum(grid[x+s][y:y+s])
            if _sum > _max:
                coords = (x+1, y+1, size)
                _max = _sum
                print(_max, coords)

print(_max, coords)
