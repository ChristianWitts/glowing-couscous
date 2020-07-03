i = [*zip(*[iter(map(int,open('input').read().strip()))]*150)]
print(min([(l.count(0),l.count(1)*l.count(2)) for l in i])[1])
print(*map(lambda p:(' ','*')[next(filter(lambda x:x<2,p))],zip(*i)))
