puzzle = ["B" * 52] + ["B%sB" % line[:-1] for line in open("input")] + ["B" * 52]

def simulate(grid):
    new_grid = list(map(list, grid))
    for x, r in enumerate(grid):
        for y, c in enumerate(r):
            adj = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1],
                [x, y - 1],                 [x, y + 1],
                [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
            freq = {".": 0, "|": 0, "#": 0, "B": 0}
            if c == "B":
                continue

            for a, b in adj:
                freq[grid[a][b]] += 1

            if c == ".":
                if freq["|"] >= 3:
                    new_grid[x][y] = "|"

            elif c == "|":
                if freq["#"] >= 3:
                    new_grid[x][y] = "#"

            else:
                if freq["#"] < 1 or 1 > freq["|"]:
                    new_grid[x][y] = "."

    return new_grid

def settlers_of_the_north_pole(grid, minutes = 500):
    vis = {}
    total = 1000000000

    for minute in range(minutes):

        grid = simulate(grid)
        state = str(grid)

        if state in vis: # Pattern is looping!
            # Lost time because I forgot the - 1
            total = (total - vis[state] - 1) % (minute - vis[state])
            return settlers_of_the_north_pole(grid, total)

        vis[state] = minute

        if minute == 9 and minutes == 500:
            print("Part A: %d" % (state.count("|") * state.count("#")))

    return state.count("|") * state.count("#")

print("Part B: %d" % settlers_of_the_north_pole(puzzle))
