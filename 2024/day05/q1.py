from collections import defaultdict

data_fname = 'input.txt'

# predecessor
pred_dict = defaultdict(list)
updates = []

with open(data_fname) as f:

    nextline = f.readline()

    while nextline != "\n":
        p, c = nextline.strip().split('|')
        pred_dict[p].append(c)
        nextline = f.readline()

    nextline = f.readline()

    while nextline != "":
        updates.append([x for x in nextline.strip().split(",")])
        nextline = f.readline()

# print(pred_dict)
# print(updates)

def get_middle(update):
    return int(update[len(update) // 2])

def check_order(update):

    before = set()
    for pnum in update:
        for pred in pred_dict[pnum]:
            if pred in before:
                return False

        before.add(pnum)

    return True

out = 0
for update in updates:
    if check_order(update):
        out += get_middle(update)

print(out)



