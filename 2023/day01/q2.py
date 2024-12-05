numnames = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
lut = {numnames[i]: str(i + 1) for i in range(len(numnames))}
lut['one'] = 'o1e'
lut['two'] = 't2'
lut['three'] = 't3e'
lut['five'] = '5e'


def processLine(rawline):
    line: str = rawline.strip()

    isrep = False
    for nn in numnames:
        if line.find(nn) != -1:
            isrep = True

    for numname in numnames:
        line = line.replace(numname, lut[numname])
    if isrep:
        print(rawline)
        print(line)
        print('----')

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
