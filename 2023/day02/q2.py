with open('input.txt') as f:
    data = f.readlines()

constraints = {'red': 12, 'green': 13, 'blue': 14}

out = 0

for line in data:
    p1, p2 = line.split(':')
    gnum = int(p1[5:])
    rounds = [
        [e.strip().split() for e in x.strip().split(',')] for x in p2.strip().split(';')
    ]

    count = {'red': [0], 'green': [0], 'blue': [0]}
    for round in rounds:
        for ballnum, color in round:
            count[color].append(int(ballnum))
    # print(count)
    # break
    out += max(count['red']) * max(count['green']) * max(count['blue'])

    # print(gnum)
    # print(sets)
print(out)
