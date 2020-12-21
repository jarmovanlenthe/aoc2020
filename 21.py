import re
from collections import defaultdict

with open("input21.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def parse_line(l):
    g = re.match(r'([a-z ]+)(\(contains [a-z, ]+\))?', l).groups()
    ingreds = g[0].strip().split()
    allergens = []
    if g[1]:
        allergens = g[1][10:-1].split(', ')
    return ingreds, allergens

all_ingredients = set()
allergen_ingred_map = defaultdict(set)
for l in lines:
    ingreds, allergens = parse_line(l)
    all_ingredients |= set(ingreds)
    for a in allergens:
        if a not in allergen_ingred_map:
            for i in ingreds:
                if i not in allergen_ingred_map[a]:
                    allergen_ingred_map[a].add(i)
        else:
            allergen_ingred_map[a] = allergen_ingred_map[a].intersection(set(ingreds))

while any([len(x) > 1 for x in allergen_ingred_map.values()]):
    len_1 = [i for i, a in allergen_ingred_map.items() if len(a) == 1]
    len_more = [i for i, a in allergen_ingred_map.items() if len(a) > 1]
    for i in len_more:
        for single_i in len_1:
            allergen_ingred_map[i] -= allergen_ingred_map[single_i]

# Part 1
num_ingreds = 0
ingreds_with_allergens = [next(iter(x)) for x in allergen_ingred_map.values()]
ingreds_without_allergens = all_ingredients - set(ingreds_with_allergens)
for i in ingreds_without_allergens:
    for l in lines:
        num_ingreds += l.count(" " + i + " ")
        num_ingreds += 1 if l.startswith(i + " ") else 0
print(num_ingreds)

# Part 2
sorted_ingreds = sorted(allergen_ingred_map.keys())
print(','.join([next(iter(allergen_ingred_map[x])) for x in sorted_ingreds]))