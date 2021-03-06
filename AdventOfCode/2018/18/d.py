def calc(values, steps):
    # Helper reads the input file and stores it in values, steps is hard coded based on puzzle

    # Turn the list of strings into a list of chars, with padding on the edge
    values = [" " * len(values[0])] + values + [" " * len(values[0])]
    values = [list(" " + x + " ") for x in values]

    # Make a copy
    temp = [[x for x in y] for y in values]

    # Make a simple list of offsets around a point to make for/each eacher
    wrap = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0:
                wrap.append((x, y))

    # Turn the string into ints, makes my head hurt slightly less
    conv = {".": 0, "|": 1, "#": 2, ' ': 0}

    for line in values:
        for i in range(len(line)):
            line[i] = conv[line[i]]

    # Look for loops, each time we don't find one, try a loop one iteration bigger
    loop_size = 1
    loop_left = loop_size
    loop_val = ""

    cur_step = 0
    while cur_step < steps:
        cur_step += 1

        # Calculate the next step, taking care to update each point, even if it doesn't change
        for x in range(1, len(values[0])-1):
            for y in range(1, len(values)-1):
                trees = 0
                lumber = 0
                for off in wrap:
                    temp_val = values[y+off[1]][x+off[0]]
                    if temp_val == 1:
                        trees += 1
                    elif temp_val == 2:
                        lumber += 1

                if values[y][x] == 0:
                    if trees >= 3:
                        temp[y][x] = 1
                    else:
                        temp[y][x] = 0
                elif values[y][x] == 1:
                    if lumber >= 3:
                        temp[y][x] = 2
                    else:
                        temp[y][x] = 1
                elif values[y][x] == 2:
                    if lumber == 0 or trees == 0:
                        temp[y][x] = 0
                    else:
                        temp[y][x] = 2

        # Check to see if we're looping
        loop_left -= 1
        if loop_left == 0:
            test = "\n".join(["".join(str(x)) for x in values])
            if test == loop_val:
                # We found a loop! We can skip ahead to the end based off our loop size
                cur_step += ((steps - cur_step) / loop_size) * loop_size
            else:
                # No loop, try again with one slightly larger cycle
                loop_size += 1
                loop_val = test
                loop_left = loop_size

        # Swap out the temp array and the live array
        temp, values = values, temp

    # Stupid simple way to count the number of lumber and trees
    lumber = 0
    trees = 0
    for line in values:
        for cur in line:
            if cur == 2:
                lumber += 1
            elif cur == 1:
                trees += 1

    # All done, return the result!
    return lumber * trees

with open('input') as fin:
    grid = [list(line.strip()) for line in fin.readlines()]

    print calc(grid, 10)
