import re
with open("input16.txt") as f:
    lines = [x.strip() for x in f.readlines()]

ranges = {}
your_ticket = []
nearby_tickets = []
next_line = ""
for l in lines:
    ticket_range = re.match(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', l)
    if ticket_range:
        name, s1, e1, s2, e2 = ticket_range.groups()
        s1, e1, s2, e2 = [int(x) for x in [s1, e1, s2, e2]]
        ranges[name] = lambda x, s1=s1, e1=e1, s2=s2, e2=e2: s1 <= x <= e1 or s2 <= x <= e2
    elif l == "your ticket:":
        next_line = "y"
    elif l == "nearby tickets:":
        next_line = "n"
    elif next_line == "y":
        your_ticket = [int(x) for x in l.split(',')]
        next_line = ""
    elif next_line == "n":
        nearby_tickets.append([int(x) for x in l.split(',')])

valid_tickets = [your_ticket]
# Part 1
invalid = 0
for t in nearby_tickets:
    valid = True
    for r in t:
        if not any(ranges[x](r) for x in ranges.keys()):
            invalid += r
            valid = False
    if valid:
        valid_tickets.append(t)

print(invalid)

# Part 2
print(len(valid_tickets))
transposed_tickets = list(zip(*valid_tickets))
possible_values = dict()
for r in ranges.keys():
    possible_values[r] = list(range(len(ranges.keys())))
for i, t in enumerate(transposed_tickets):
    for r in ranges.keys():
        if not all([ranges[r](x) for x in t]):
            possible_values[r].remove(i)

while sum([len(v) for v in possible_values.values()]) > len(your_ticket):
    for i, v in [(i, v) for i, v in possible_values.items() if len(v) > 1]:
        for v2 in [v2 for v2 in possible_values.values() if len(v2) == 1]:
            try:
                possible_values[i].remove(v2[0])
            except:
                pass

print(possible_values)

depart = 1
for k, v in possible_values.items():
    possible_values[k] = v[0]
    if k.startswith('departure '):
        depart *= your_ticket[v[0]]
print(possible_values)
print(depart)

# too low: 673920