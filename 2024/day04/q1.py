with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

w = len(data[0])
h = len(data)

count = 0


def check(word):
    # print(word)
    if word == 'XMAS' or word == 'SAMX':
        return 1
    return 0


for j in range(h):
    for i in range(w):
        # horizontal
        if i < w - 3:
            count += check(data[j][i : i + 4])
        # vertical
        if j < h - 3:
            count += check(''.join([data[j + x][i] for x in range(4)]))
        # diagonal
        if i < w - 3 and j < h - 3:
            count += check(''.join([data[j + x][i + x] for x in range(4)]))
        # diagonal 2
        if j >= 3 and i < w - 3:
            count += check(''.join([data[j - x][i + x] for x in range(4)]))
print(count)
