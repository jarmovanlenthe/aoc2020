import re

REG = re.compile(r'(\d+)-(\d+) ([a-z]+): (.*)')

with open("input2.txt") as f:
    lines = f.readlines()

valid = 0
positions_valid = 0

for l in lines:
    g = REG.match(l)
    if int(g.group(1)) <= g.group(4).count(g.group(3)) <= int(g.group(2)):
        valid += 1
    if "{}{}".format(g.group(4)[int(g.group(1))-1], g.group(4)[int(g.group(2))-1]).count(g.group(3)) == 1:
        positions_valid += 1

print(valid)
print(positions_valid)

