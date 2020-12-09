from itertools import combinations

with open("input9.txt") as f:
    lines = [int(x) for x in f.readlines()]

pos = 25
finished = False

# Part 1
while not finished:
    combs = combinations(lines[pos-25:pos], 2)
    found = False
    for comb in combs:
        if sum(comb) == lines[pos]:
            found = True
    if not found:
        weakness = lines[pos]
        print(weakness)
        finished = True
    pos += 1

print()

# Part 2
pos = 0
finished = False
while not finished:
    acc = 0
    pos2 = pos
    while acc < weakness:
        acc += lines[pos2]
        if acc == weakness:
            print(min(lines[pos:pos2+1])+max(lines[pos:pos2+1]))
            finished = True
            break
        pos2 += 1
    pos += 1