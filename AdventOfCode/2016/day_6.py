with open('day_6.input', 'rb') as fin:
    lines = [l.strip() for l in fin]

from collections import Counter

# Part 1
for idx in xrange(8):
    print Counter([c[idx] for c in lines]).most_common(1)[0][0], 

print 

# Part 2
for idx in xrange(8):
    print sorted(Counter([c[idx] for c in lines]).most_common(),
                 key=lambda c: c[1])[0][0],
