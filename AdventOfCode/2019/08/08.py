import numpy as np
digits = [int(i) for i in open('input', 'r').read().strip()]

layers = np.array(digits).reshape((-1,6,25))
composite = np.apply_along_axis(lambda x: x[np.where(x != 2)[0][0]], axis=0, arr=layers)

print("Part 2:")
print("\n".join(''.join(u" ♥️"[int(i)] for i in line) for line in composite))

