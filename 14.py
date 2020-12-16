import re
from itertools import permutations

with open("input14.txt") as f:
    lines = f.readlines()

# Part 1
xor_mask = "1" * 36
mem = {}

def apply_mask(inp):
    mask1 = int(mask.replace('X', '0'), 2)
    output = inp | mask1
    mask0 = int(mask.replace('X', '1'), 2)
    output = output & mask0
    return output

for l in lines:
    if l.startswith('mask = '):
        mask = l.strip()[7:]
    else:
        k, v = re.match(r'mem\[(\d+)\] = (\d+)', l).groups()
        mem[k] = apply_mask(int(v))

print(sum(mem.values()))

print()
# Part 2
mem = {}

def get_binary_strings(length):
    res = []
    def _get_binary_strings(s, length):
        if length == 0:
             res.append(s)
        else:
            _get_binary_strings(s + '0', length-1)
            _get_binary_strings(s + '1', length-1)
    _get_binary_strings("", length)
    return res

def get_addresses(inp, mask):
    xs = mask.count('X')
    res = []
    for bs in get_binary_strings(xs):
        o = f'{mask}'
        for b in bs:
            o = o.replace('X', b, 1)
        o = inp | int(o, 2)
        mask_1 = '1' * 36
        cnt = 0
        for i, c in enumerate(mask):
            if c == 'X':
                mask_1 = mask_1[0:i] + bs[cnt] + mask_1[i+1:]
                cnt += 1
        o = o & int(mask_1, 2)
        res.append(o)
    return res

for l in lines:
    if l.startswith('mask = '):
        mask = l.strip()[7:]
    else:
        k, v = re.match(r'mem\[(\d+)\] = (\d+)', l).groups()
        addresses = get_addresses(int(k), mask)
        for a in addresses:
            mem[a] = int(v)

print(sum(mem.values()))