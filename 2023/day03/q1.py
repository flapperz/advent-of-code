import re

with open('input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

def is_special(char):
    return char != '.' and not char.isnumeric()

def check_num(j, span):
    i0, i1 = span
    if is_special(data[j][max(0, i0 - 1)]):
        return 1
    if is_special(data[j][min(w - 1, i1)]):
        return 1
    patch = ''
    if j != 0:
        patch += data[j - 1][max(0, i0 - 1) : min(w, i1 + 1)]
    if j != w - 1:
        patch += data[j + 1][max(0, i0 - 1) : min(w, i1 + 1)]
    for char in patch:
        if is_special(char):
            return 1
    return 0


exp = r'(\d+)'
w = len(data[0])
h = len(data)

out = 0
for j, line in enumerate(data):
    for match in re.finditer(exp, data[j]):
        # print(match.span(), match.group())
        span = match.span()

        if check_num(j, span):
            # print(int(match.group()))
            out += int(match.group())
print(out)
