with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

w = len(data[0])
h = len(data)

count = 0


def check(middle, diag_down, diag_up):
    if middle == 'A' and (diag_down == 'MS' or diag_down == 'SM') and (diag_up == 'MS' or diag_up == 'SM'):
        return 1
    return 0





for j in range(h - 2):
    for i in range(w - 2):
        count += check(
            data[j + 1][i + 1],
            data[j][i] + data[j + 2][i + 2],
            data[j + 2][i] + data[j][i + 2],
        )
print(count)
