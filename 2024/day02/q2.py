def dampener(rawline):
    xs = [int(x) for x in rawline.strip().split()]

    for i in range(len(xs)):
        if process_line(xs[:i] + xs[i + 1 :]):
            return 1
    return 0


def process_line(xs):
    isincrease = xs[1] - xs[0] > 0

    for i in range(1, len(xs)):
        next = xs[i]
        prev = xs[i - 1]
        diff = abs(next - prev)
        if diff < 1 or diff > 3:
            return 0

        if (next - prev < 0 and isincrease) or (next - prev > 0 and not isincrease):
            # print(f'{xs}: {next}-{prev}, {isincrease}')
            return 0

    return 1


out = 0
with open('input.txt') as f:
    for rawline in f:
        out += dampener(rawline)
print(out)
