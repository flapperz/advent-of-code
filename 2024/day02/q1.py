def process_line(rawline):
    xs = [int(x) for x in rawline.strip().split()]

    isincrease = xs[1] - xs[0] > 0

    for i in range(1, len(xs)):
        next = xs[i]
        prev = xs[i-1]
        diff = abs(next - prev)
        if diff < 1 or diff > 3:
            return 0

        if (next - prev < 0 and isincrease) or (next - prev > 0 and not isincrease):
            # print(f'{xs}: {next}-{prev}, {isincrease}')
            return 0

    return 1

out = 0
with open("input.txt") as f:
    for rawline in f:
        out += process_line(rawline)
print(out)
