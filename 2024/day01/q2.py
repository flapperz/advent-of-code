from collections import defaultdict

with open('input.txt') as f:
    data = f.readlines()

x = defaultdict(lambda: 0)
y = defaultdict(lambda: 0)


for i, line in enumerate(data):
    xi, yi = line.strip().split()
    x[int(xi)] += 1
    y[int(yi)] += 1

sim = 0
for xi in x:
    if xi in y:
        sim += xi * x[xi] * y[xi]

print(sim)



