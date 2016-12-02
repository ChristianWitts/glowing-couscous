def get_data():
    with open('day_2.input', 'rb') as fin:
        return fin.readlines()

def part1():
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    x, y = 1, 1

    for instruction in get_data():
        for step in instruction:
            if   step == 'R' and x < 2: x += 1
            elif step == 'L' and x > 0: x -= 1
            elif step == 'D' and y < 2: y += 1
            elif step == 'U' and y > 0: y -= 1
        print keypad[y][x],
    print 


def part2():
    keypad = [
        [None, None,  1, None,  None],
        [None,    2,  3,    4,  None],
        [5,       6,  7,    8,     9],
        [None,  'A', 'B',  'C', None],
        [None, None, 'D', None, None]
    ]
    x, y = 3, 0

    for instruction in get_data():
        for step in instruction:
            if   step == 'R' and x < 4 and keypad[y][x+1]: x += 1
            elif step == 'L' and x > 0 and keypad[y][x-1]: x -= 1
            elif step == 'D' and y < 4 and keypad[y+1][x]: y += 1
            elif step == 'U' and y > 0 and keypad[y-1][x]: y -= 1
        print keypad[y][x],  

part1()
part2()