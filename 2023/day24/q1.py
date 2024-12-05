import numpy as np

record = []
with open('input.txt', 'r') as f:
    for line in f:
        ll = [int(x) for x in line.strip().replace(',', '').replace('@', '').split()]
        record.append([ll[0], ll[1], ll[3], ll[4]])

# lbound = 7
# ubound = 27
lbound = 200000000000000
ubound = 400000000000000


def check_collide(reci, recj):
    # print(reci, recj)
    A = [[reci[2], -recj[2]], [reci[3], -recj[3]]]
    b = [recj[0] - reci[0], recj[1] - reci[1]]
    if np.linalg.det(A) != 0:
        sol = np.linalg.solve(A, b)
        if sol[0] >= 0 and sol[1] >= 0:
            x = reci[0] + reci[2] * sol[0]
            y = reci[1] + reci[3] * sol[0]
            if x >= lbound and x <= ubound and y >= lbound and y <= ubound:
                return 1
    return 0


out = 0

for i in range(len(record)-1):
    for j in range(i+1, len(record)):
        reci = record[i]
        recj = record[j]

        out += check_collide(reci, recj)
        # break
print(out)
