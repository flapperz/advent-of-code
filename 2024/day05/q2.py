
# not reorder only find who can be middle
# order directive is complete for each pair

from collections import defaultdict

# data_fname = 'q1test.txt'
data_fname = 'input.txt'

# predecessor
pred2suc = defaultdict(set)
suc2pred = defaultdict(set)

updates = []

with open(data_fname) as f:

    nextline = f.readline()

    nrule = 0
    while nextline != "\n":
        p, c = nextline.strip().split('|')
        pred2suc[p].add(c)
        # nrule += 1
        nextline = f.readline()
    # print(nrule)

    nextline = f.readline()

    while nextline != "":
        updates.append([x for x in nextline.strip().split(",")])
        nextline = f.readline()

def check_order(update):
    before = set()
    for pnum in update:
        for pred in pred2suc[pnum]:
            if pred in before:
                return False

        before.add(pnum)

    return True

def get_middle(update):
    # check dup -> no dup
    # if len(update) != len(set(update)):
    #     print("dup")

    # exact number of member on left or right of mid
    padnum = len(update) // 2
    for i, pnum in enumerate(update):
        others = set(update)
        others.remove(pnum)
        if len(others.intersection(pred2suc[pnum])) == padnum:
            return int(pnum)

    print("find fail, fuck")
    return -1




# check number of unique pnum
# k = set()
# for update in updates:
#     k.update(update)
# print(len(k))

out = 0
for update in updates:
    if not check_order(update):
        res = get_middle(update)
        out += res

print(out)



