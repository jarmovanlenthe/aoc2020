from collections import defaultdict

with open("input13.txt") as f:
    lines = f.readlines()

current_timestamp = int(lines[0])
bus_ids = lines[1].strip().split(',')

# Part 1
buses = defaultdict(list)
for bus in bus_ids:
    if bus == 'x':
        continue
    bus = int(bus)
    for at in range(current_timestamp, current_timestamp+100):
        if at % bus == 0:
            buses[at].append(bus)
            break

from pprint import pprint
pprint(buses)

sorted_buses = list(buses.keys())
sorted_buses.sort()
first_bus_at = sorted_buses[0]
print(first_bus_at, buses[first_bus_at])
wait_for = first_bus_at - current_timestamp
print(wait_for)
print(wait_for * buses[first_bus_at][0])

print()
# Part 2
# Below is copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
# n = bus starts
# a = bus_times
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

a = []
n = []
for i, b in enumerate(bus_ids):
    if b != 'x':
        n.append(int(b))
        a.append(int(b) - i)

print(chinese_remainder(n,a))
