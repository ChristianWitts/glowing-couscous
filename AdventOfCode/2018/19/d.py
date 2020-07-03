from copy import copy
import re

with open('input') as fin:
    d = [line.strip() for line in fin.readlines()]

def gen_op(op):
  def opr(inputs, a, b, c):
    outputs = inputs
    if any(x > len(inputs) for x in (a, b, c)):
      return []
    outputs[c] = op(outputs[a], outputs[b])
    return outputs

  def opi(inputs, a, b, c):
    outputs = inputs
    if any(x > len(inputs) for x in (a, c)):
      return []
    outputs[c] = op(outputs[a], b)
    return outputs
  return opr, opi

def gen_comp_op(op):
  oprr, opri = gen_op(op)
  def opir(inputs, a, b, c):
    outputs = inputs
    if any(x > len(inputs) for x in (b, c)):
      return []
    outputs[c] = int(op(a, outputs[b]))
    return outputs
  return oprr, opri, opir

addr, addi = gen_op(lambda x,y: x + y)
mulr, muli = gen_op(lambda x,y: x * y)
banr, bani = gen_op(lambda x,y: x & y)
borr, bori = gen_op(lambda x,y: x | y)

def setr(inputs, a, b, c):
  outputs = inputs
  if any(x >= len(inputs) for x in  (a, c)):
    return []
  outputs[c] = outputs[a]
  return outputs
def seti(inputs, a, b, c):
  outputs = inputs
  if c >= len(inputs):
    return []
  outputs[c] = a
  return outputs

gtrr, gtri, gtir = gen_comp_op(lambda x,y: x > y)
eqrr, eqri, eqir = gen_comp_op(lambda x,y: x == y)

operations = {
  'addr': addr, 'addi': addi,
  'mulr': mulr, 'muli': muli,
  'banr': banr, 'bani': bani,
  'borr': borr, 'bori': bori,
  'setr': setr, 'seti': seti,
  'gtrr': gtrr, 'gtri': gtri, 'gtir': gtir,
  'eqrr': eqrr, 'eqri': eqri, 'eqir': eqir
}

ip_register = int(re.findall(r'(\d+)', d[0])[0])
d = d[1:]
for part in xrange(2):
  registers = [part, 0, 0, 0, 0, 0]

  while 0 <= registers[ip_register] < len(d):
    ip = registers[ip_register]
    if ip == 1:
      print "ab"[part], sum([x for x in xrange(1, registers[5]+1) if registers[5] % x == 0])
      break
    code = d[ip].split()
    args = map(int, code[1:])
    instr = code[0]
    registers = operations[instr](registers, *args)
    registers[ip_register] += 1
