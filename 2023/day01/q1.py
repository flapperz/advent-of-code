def processLine(line):
    num = None
    last = None
    for a in line.strip():
        if a.isnumeric():
            if not num:
                num = a
            last = a
    num += last
    return int(num)


out = 0
with open('input.txt') as f:
    for line in f:
        out += processLine(line)

print(out)
