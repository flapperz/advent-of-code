import re

with open("input.txt", 'r') as f:
    data = ''.join(f.readlines())

regex = 'mul\\((\\d*,\\d*)\\)'

capture = re.findall(regex, data)

out = 0
for pair in capture:
    x, y = [int(e) for e in pair.split(',')]
    out += x*y

print(out)

