import numpy as np

with open('input.txt') as f:
    m = np.array([[x for x in line.strip()] for line in f.readlines()], dtype=str)

curry, currx = np.argwhere(m == '^')[0]
m[(curry, currx)] = '.'
h, w = m.shape

d = np.array([-1, 0])
dchars = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}
rotmat = np.array([[0, 1], [-1, 0]])

path = set()
dbpath = []


while curry >= 0 and curry < h and currx >= 0 and currx < w:

    path.add((curry, currx))
    dbpath.append((curry, currx, dchars[tuple(d)]))

    pos = np.array([curry, currx])

    # print([pos + d < m.shape, pos + d >= 0])

    # find next direction
    while np.all([pos + d < m.shape, pos + d >= (0, 0)]) and m[tuple(pos + d)] != '.':
        d = rotmat @ d

    curry, currx = pos + d


# for pos in dbpath:
#     x, y, dchar = pos
#     m[(x, y)] = dchar
# print(m)

print(len(path))
# print(path)
