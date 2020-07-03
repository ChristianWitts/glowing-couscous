seen = set()
CS = set()
final = None

C = 7041048
D = 65536
while True:
    E = D % 256
    C += E
    C = (C%(2**24) * 65899) % (2**24)
    if D < 256:
        if not CS:
            print C
        if C not in CS:
            final = C
        CS.add(C)
        D = C | (2**16)
        if D in seen:
            print final
            break
        seen.add(D)
        C = 7041048
        continue

    D = D/256
