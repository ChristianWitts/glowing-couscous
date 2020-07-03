with open("input.txt") as file:
    inp = file.read().strip()

orbits = [l.split(")") for l in inp.split("\n")]

objs = set()

parents = {}
for o in orbits:
    parents[o[1]] = o[0]
    objs.add(o[0])
    objs.add(o[1])

orbs = {}

def get_orb(p):
    if p not in orbs:
        if p in parents:
            orbs[p] = 1 + get_orb(parents[p])
        else:
            orbs[p] = 0
    return orbs[p]

print(sum(get_orb(p) for p in objs))

you_path = ["YOU"]
while you_path[-1] in parents:
    you_path.append(parents[you_path[-1]])

san_path = ["SAN"]
while san_path[-1] in parents:
    san_path.append(parents[san_path[-1]])

for i,p in enumerate(you_path):
    if p in san_path:
        print(i + san_path.index(p) - 2)
        break

