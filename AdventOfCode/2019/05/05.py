# from util import get_data
# orig_data = get_data(5)

orig_data = open('input', 'r').read()

def solve(part_b=False):
  data = map(int, orig_data.split(','))

  def get_param(data, pos, idx, modes):
    if modes[idx-1] == 1:
      return data[pos + idx]
    else:
      return data[data[pos + idx]]

  outputs = []

  pos = 0
  opcode = data[pos]
  while opcode != 99:
    opcode = data[pos]
    modes = []
    if opcode > 100:
      mode_opcode = opcode / 100
      opcode = opcode % 100
      while mode_opcode > 0:
        modes.append(mode_opcode % 10)
        mode_opcode /= 10
    while len(modes) < 4:
      modes.append(0)
    if opcode == 1:
      left = get_param(data, pos, 1, modes)
      right = get_param(data, pos, 2, modes)
      data[data[pos+3]] = left + right
      pos += 4
    elif opcode == 2:
      left = get_param(data, pos, 1, modes)
      right = get_param(data, pos, 2, modes)
      data[data[pos+3]] = left * right
      pos += 4
    elif opcode == 3:
      data[data[pos+1]] = 5 if part_b else 1 # int(raw_input('Input: '))
      pos += 2
    elif opcode == 4:
      outputs.append(get_param(data, pos, 1, modes)) # print get_param(data, pos, 1, modes)
      pos += 2
    elif opcode == 5:
      param = get_param(data, pos, 1, modes)
      addr = get_param(data, pos, 2, modes)
      if param != 0:
        pos = addr
      else:
        pos += 3
    elif opcode == 6:
      param = get_param(data, pos, 1, modes)
      addr = get_param(data, pos, 2, modes)
      if param == 0:
        pos = addr
      else:
        pos += 3
    elif opcode == 7:
      first = get_param(data, pos, 1, modes)
      second = get_param(data, pos, 2, modes)
      data[data[pos+3]] = int(first < second)
      pos += 4
    elif opcode == 8:
      first = get_param(data, pos, 1, modes)
      second = get_param(data, pos, 2, modes)
      data[data[pos+3]] = int(first == second)
      pos += 4
    elif opcode == 99:
      return outputs[-1]
      break
    else:
      print opcode
      assert False

print 'a', solve()
print 'b', solve(True)
