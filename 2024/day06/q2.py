import numpy as np
from q1path import defaultpath

with open('input.txt') as f:
    m = np.array([[x for x in line.strip()] for line in f.readlines()], dtype=str)

starty, startx = np.argwhere(m == '^')[0]
m[(starty, startx)] = '.'
h, w = m.shape

dchars = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}
rotmat = np.array([[0, 1], [-1, 0]])

def is_stuck(curry, currx):
    d = np.array([-1, 0])

    path = set()

    while curry >= 0 and curry < h and currx >= 0 and currx < w:

        path.add((curry, currx, dchars[tuple(d)]))

        pos = np.array([curry, currx])

        # print([pos + d < m.shape, pos + d >= 0])

        # find next direction
        while np.all([pos + d < m.shape, pos + d >= (0, 0)]) and m[tuple(pos + d)] != '.':
            d = rotmat @ d

        nexty, nextx = pos + d
        if (nexty, nextx, dchars[tuple(d)]) in path:
            return True

        curry, currx = nexty, nextx
    return False


# for pos in dbpath:
#     x, y, dchar = pos
#     m[(x, y)] = dchar
# print(m)
out = 0

it = 0
defaultpath = set(defaultpath)
print(f"path long: {len(defaultpath)}")
maxit = len(defaultpath)
for it, (i, j) in enumerate(defaultpath):
    if m[i,j] == '.':
        m[i,j] = '@'
        if is_stuck(starty, startx):
            # print(i,j)
            out += 1
        m[i,j] = '.'

    if it % 200 == 0:
        print( f'progress {it * 100 // maxit} %')

print(out)
