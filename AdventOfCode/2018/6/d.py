import re
from collections import defaultdict
with open('input') as fin:
    d = fin.readlines()

d = map(lambda s: map(int, re.findall(r'-?\d+', s)), d)
min_x = min(x[0] for x in d)-(10000/len(d))-1
max_x = max(x[0] for x in d)+(10000/len(d))+1
min_y = min(x[1] for x in d)-(10000/len(d))-1
max_y = max(x[1] for x in d)+(10000/len(d))+1
mapping = {}
in_region = set()
for x in xrange(min_x, max_x+1):
  for y in xrange(min_y, max_y+1):
    closest = d[0]
    closest_dist = (1 << 31)
    dist_sum = 0
    for (px, py) in d:
      dist = abs(px - x) + abs(py - y)
      dist_sum += dist
      if dist < closest_dist:
        closest = (px, py)
        closest_dist = dist
      elif dist == closest_dist and closest != (px, py):
        closest = None
    mapping[(x, y)] = closest
    if dist_sum < 10000:
      in_region.add((x, y))

rev_mapping = defaultdict(int)
for h in mapping:
  if not mapping[h]:
    continue
  if h[0] in (min_x, max_x) or h[1] in (min_y, max_y):
    rev_mapping[mapping[h]] -= (1 << 31)
  rev_mapping[mapping[h]] += 1
print "a", max(rev_mapping.values())
print "b", len(in_region)
