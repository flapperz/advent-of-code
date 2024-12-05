with open('input.txt') as f:
    data = f.readlines()

constraints = {
    'red': 12,
    'green': 13,
    'blue': 14
}

out = 0

for line in data:
    p1, p2 = line.split(':')
    gnum = int(p1[5:])
    rounds = [[e.strip().split() for e in x.strip().split(',')] for x in p2.strip().split(';')]

    isvalid = True
    for round in rounds:
        for ballnum, color in round:
            if int(ballnum) > constraints[color]:
                isvalid = False
                break
        if not isvalid:
            break
    else:
        out += gnum

    # print(gnum)
    # print(sets)
print(out)
