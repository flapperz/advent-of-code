# still wrong
with open('q1test.txt', 'r') as f:
    data = ''.join(f.readlines())

out = 0
isopen = False
stack = ''
prev = '.'
whatprev = ''
for i,char in enumerate(data):
    if not isopen:
        if char.isnumeric() and (prev == '.' or prev == '\n'):
            isopen = True
            stack += char
            whatprev = prev
    else:
        if char.isnumeric():
            stack += char
        elif char == '.' or char == '\n':
            num = int(stack)
            out += num
            print(whatprev + stack + char)
            stack = ''
            isopen = False
        else:
            # print(whatprev + stack + char)
            stack = ''
            isopen = False
    prev = char

print(out)
# print(sum([int(x) for x in capture]))
