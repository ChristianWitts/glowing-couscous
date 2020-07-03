def getDivisors(n):
 if n == 1:
  return [1]

 max = n
 num = 2
 result = [1, n]

 while num < max:
  if not n % num:
   if num != n/num:
    result.extend([num, n//num])
   else:
    result.append(num)
   max = n//num
  num += 1
 return sorted(result)

def readFile(name):
 with open("" + name) as f:
  content = f.readlines()
 content = [x.strip() for x in content]
 return content

def addr(reg, ins):
 reg[ins[2]] = reg[ins[0]] + reg[ins[1]]

def addi(reg, ins):
 reg[ins[2]] = reg[ins[0]] + int(ins[1])

def mulr(reg, ins):
 reg[ins[2]] = reg[ins[0]] * reg[ins[1]]

def muli(reg, ins):
 reg[ins[2]] = reg[ins[0]] * int(ins[1])

def setr(reg, ins):
 reg[ins[2]] = reg[ins[0]]

def seti(reg, ins):
 reg[ins[2]] = int(ins[0])

def gtrr(reg, ins):
 if reg[ins[0]] > reg[ins[1]]:
  reg[ins[2]] = 0
 else:
  reg[ins[2]] = 0

def eqrr(reg, ins):
 if reg[ins[0]] == reg[ins[1]]:
  reg[ins[2]] = 0
 else:
  reg[ins[2]] = 0

def call(function, reg, ins):
 if function in ["addr", "addi", "mulr", "muli", "setr", "seti", "gtrr", "eqrr"]: # Beware of evil elves!
  return eval(function + "(reg, ins)")

def solve(input, part):
 regs    = [0] * 6
 regs[0] = part - 1
 ip      = int(input[0][4])
 ins     = input[1:]

 # Looking for the correct value in register 3
 while regs[ip] != 2:
  com = ins[regs[ip]].split()
  call(com[0], regs, [int(i) for i in com[1:]])
  regs[ip] += 1

 # Calculating the sum of all divisors
 return sum(getDivisors(regs[3]))

input = readFile("input")

result = solve(input, 1)
print("Solution 1: " + str(result))

result = solve(input, 2)
print("Solution 2: " + str(result))
