lines = open('input').read().split('\n')

state = lines[0].split(': ')[1].strip()
start_len = len(state)
rules = {}
for line in lines[2:]:
    if line:
        before, after = line.split('=>')
        rules[before.strip()] = after.strip()

# Important: ..... -> .
zero_idx = 0
print 0, state
for t in xrange(15000):
    state = '..'+state+'..'
    new_state = ['.' for _ in range(len(state))]
    read_state = '..'+state+'..'
    zero_idx += 2
    for i in range(len(state)):
        pat = read_state[i:i+5]
        new_state[i] = rules.get(pat, '.')

    start = 0
    end = len(new_state)-1
    while new_state[start] == '.':
        start += 1
        zero_idx -= 1
    while new_state[end] == '.':
        end -= 1
    state = ''.join(new_state[start:end+1])
    print t+1, zero_idx, state

zero_idx = -int(50e9) + 45
ans = 0
for i in range(len(state)):
    if state[i] == '#':
        ans += i-zero_idx
        print i-zero_idx, ans
print state, len(state), start_len
print ans
