import re
from collections import defaultdict

with open('input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

gearloc2num = defaultdict(list)


def add_gearloc(j, span, num):
    i0, i1 = span

    y = j
    x = max(0, i0 - 1)
    if data[y][x] == '*':
        gearloc2num[(y, x)].append(num)

    y = j
    x = min(w - 1, i1)
    if data[y][x] == '*':
        gearloc2num[(y, x)].append(num)

    for jj in (j - 1, j + 1):
        if jj >= 0 and jj < w:
            for ii in range(max(0, i0 - 1) , min(w, i1 + 1)):
                char = data[jj][ii]
                if char == '*':
                    gearloc2num[(jj, ii)].append(num)


exp = r'(\d+)'
w = len(data[0])
h = len(data)

out = 0
for j, line in enumerate(data):
    for match in re.finditer(exp, data[j]):
        # print(match.span(), match.group())
        span = match.span()

        # num = int(match.group)
        add_gearloc(j, span, int(match.group()))

for k,v in gearloc2num.items():
    if len(v) == 2:
        out += v[0] * v[1]

# print(gearloc2num)
print(out)
