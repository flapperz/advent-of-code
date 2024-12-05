import re

with open('input.txt', 'r') as f:
    data = ''.join(f.readlines())

# data = "don't()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


regex = 'mul\\((\\d*,\\d*)\\)'


out = 0


def process_chunk(chunk):
    capture = re.findall(regex, chunk)

    out = 0
    for pair in capture:
        x, y = [int(e) for e in pair.split(',')]
        out += x * y

    return out


chunk = ''
do_op = 'do()'
dont_op = "don't()"
is_do = False

stack = ''

for char in data:
    if is_do:
        chunk += char

    if not is_do:
        if char == do_op[len(stack)]:
            stack += char
            if len(stack) == 4:
                is_do = True
                stack = ''

        else:
            stack = ''
    else:
        if char == dont_op[len(stack)]:
            stack += char
            if len(stack) == 7:
                is_do = False
                stack = ''
                print(chunk)
                out += process_chunk(chunk)
                chunk = ''
        else:
            stack = ''
    if stack:
        print(stack)

if is_do:
    out += process_chunk(chunk)

print(out)
