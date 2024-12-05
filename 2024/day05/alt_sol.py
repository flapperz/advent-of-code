# not working since real input is cyclic I guess

from collections import defaultdict

# data_fname = 'q1test.txt'
data_fname = 'input.txt'

# predecessor
pred_dict = defaultdict(list)
db_dict = []
updates = []

with open(data_fname) as f:
    nextline = f.readline()

    nrule = 0
    while nextline != '\n':
        p, c = nextline.strip().split('|')
        nrule += 1
        pred_dict[c].append(p)
        db_dict.append((c,p))
        nextline = f.readline()
    print(nrule)

    nextline = f.readline()

    while nextline != '':
        updates.append([x for x in nextline.strip().split(',')])
        nextline = f.readline()

ordermap = defaultdict(int)
ordermap.update({k: len(v) for k, v in pred_dict.items()})
# print(ordermap)
# print(pred_dict)

q1out = 0
q2out = 0

member = set()
for update in updates:
    member.update(update)

    sorted_update = sorted(update, key=lambda x: ordermap[x], reverse=True)
    mid = int(sorted_update[len(update) // 2])
    if tuple(sorted_update) == tuple(update):
        q1out += mid
    else:
        q2out += mid
member = sorted(list(member))

print(q1out)
print(q2out)
