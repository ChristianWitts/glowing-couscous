from collections import defaultdict
from Queue import Queue


mappings = {
  'W': lambda (x,y): (x-1, y),
  'E': lambda (x,y): (x+1, y),
  'N': lambda (x,y): (x, y-1),
  'S': lambda (x,y): (x, y+1)
}

def make_grid(d):
  connections = defaultdict(set)
  seen_already = set()
  def explore(start, regex):
    serialized = ''.join(regex)
    if (start, serialized) in seen_already:
      return
    seen_already.add((start, serialized))

    cur_pos = start
    cur_idx = 0
    while 0 <= cur_idx < len(regex):
      if regex[cur_idx] == '^':
        cur_idx += 1
        continue
      if regex[cur_idx] in mappings:
        next_pos = mappings[regex[cur_idx]](cur_pos)
        connections[cur_pos].add(next_pos)
        connections[next_pos].add(cur_pos)
        cur_pos = next_pos
        cur_idx += 1
        continue
      elif regex[cur_idx] == '(':
        paren_depth = 0
        new_idx = cur_idx + 1
        options = []
        curr = []
        while paren_depth > 0 or regex[new_idx] != ')':
          if regex[new_idx] == '(':
            curr.append(regex[new_idx])
            paren_depth += 1
          elif regex[new_idx] == ')':
            assert paren_depth > 0
            curr.append(regex[new_idx])
            paren_depth -= 1
          elif regex[new_idx] == '|':
            if paren_depth == 0:
              options.append(curr)
              curr = []
            else:
              curr.append(regex[new_idx])
          else:
            assert regex[new_idx] in mappings
            curr.append(regex[new_idx])
          new_idx += 1

        options.append(curr)
        for option in options:
          assert regex[new_idx] == ')'
          explore(cur_pos, option + regex[new_idx + 1:])
        return
      elif regex[cur_idx] == '$':
        return
  explore((0, 0), list(d))
  return connections

def print_grid(connections):
  min_x = min(z[0] for z in connections)
  max_x = max(z[0] for z in connections)
  min_y = min(z[1] for z in connections)
  max_y = max(z[1] for z in connections)
  print '#' + '##' * (max_x - min_x + 1)
  for y in xrange(min_y, max_y+1):
    if y > min_y:
      row_above = ['#']
      for x in xrange(min_x, max_x+1):
        if (x, y-1) in connections[(x, y)]:
          row_above.append('-#')
        else:
          row_above.append('##')
      print ''.join(row_above)

    row = ['#']
    for x in xrange(min_x, max_x+1):
      if (x, y) == (0, 0):
        row.append('X')
      else:
        row.append('.')
      if (x+1, y) in connections[(x,y)]:
        row.append('|')
      else:
        row.append('#')
    print ''.join(row)
  print '#' * ((max_x - min_x + 1) * 2 + 1)

def solve(d, part_b=False):
  connections = make_grid(d)

  distances = {(0,0): 0}
  q = Queue()
  q.put((0,0))
  while not q.empty():
    u = q.get()
    for v in connections[u]:
      if v not in distances:
        distances[v] = distances[u] + 1
        q.put(v)

  if part_b:
    return len([k for k in distances if distances[k] >= 1000])
  return max(distances.values())

assert solve('^WNE$') == 3
assert solve('^ENWWW(NEEE|SSE(EE|N))$') == 10
assert solve('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$') == 18
assert solve('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$') == 23
assert solve('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$') == 31

with open('input') as fin:
    d = fin.read().strip()

# d = get_data(20)
print "a", solve(d)
print "b", solve(d, True)
