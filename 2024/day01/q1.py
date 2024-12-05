with open("input.txt") as f:
    data = f.readlines()

x = [None for i in range(len(data))]
y = [None for i in range(len(data))]

for i,line in enumerate(data):
    xi, yi = line.strip().split()
    x[i] = int(xi)
    y[i] = int(yi)

x.sort()
y.sort()

print( sum([abs(x[i]-y[i]) for i in range(len(data))]))
