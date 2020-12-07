from functools import reduce
import operator

with open("input3.txt") as f:
    lines = f.readlines()

SLOPES = [(1,1), (3,1), (5,1), (7,1), (1,2)]

trees_total = []

for a, b in SLOPES:
    pos = 0
    trees = 0
    for i, l in enumerate(lines):
        if i % b != 0:
            continue
        if l[pos] == "#":
            trees += 1
        pos = (pos + a) % len(l.strip())
    
    trees_total.append(trees)
    print(f"Down {a}, right {b}, trees: {trees}")

product = reduce(operator.mul, trees_total)
print(f"Product: {product}")