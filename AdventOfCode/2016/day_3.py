def part1():
    with open('day_3.input', 'rb') as fin:
        triangles = [map(int, line.strip().split())
                     for line in fin]

    print sum(1
              if ((a + b) > c and
                  (a + c) > b and
                  (b + c) > a)
              else 0
              for a, b, c in triangles)


def part2():
    with open('day_3.input', 'rb') as fin:
        rows = [map(int, line.strip().split())
                for line in fin]

    valid = 0
    for i in xrange(0, len(rows)-2, 3):
        a, b, c = rows[i:i+3]
        for j in xrange(3):
            if ((a[j] + b[j]) > c[j] and
                (a[j] + c[j]) > b[j] and
                (b[j] + c[j]) > a[j]):
                valid += 1
    
    print valid

part1()
part2()
