from functools import lru_cache

lines = [0]
with open("input10.txt") as f:
    lines.extend([int(x) for x in f.readlines()])
    lines.sort()
    lines.append(lines[len(lines)-1] + 3)

diffs = []
for i in range(1, len(lines)):
    diffs.append(lines[i]-lines[i-1])

print(lines)
print(diffs)
diffs_1 = diffs.count(1)
diffs_3 = diffs.count(3)
print("Diffs 1: {}".format(diffs_1))
print("Diffs 3: {}".format(diffs_3))
print("Product: {}".format(diffs_1 * diffs_3))

@lru_cache()
def calc_adapter_recurse(current, target, adapters):
    if current == target:
        return 1
    options = [i for i in adapters if 1 <= i - current <= 3 ]
    count = 0
    for option in options:
        count += calc_adapter_recurse(option, target, adapters)
    return count

count = calc_adapter_recurse(0, lines[len(lines)-1], tuple(lines))
print(count)