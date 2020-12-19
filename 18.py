import re

with open("input18.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def calc(tokens, part):
    while '(' in tokens:
        count = 1
        index = tokens.index('(')
        for c in range(index + 1, len(tokens)):
            if tokens[c] == '(':
                count += 1
            elif tokens[c] == ')':
                count -= 1
            if count == 0:
                break
        else:
            # Shouldn't happen
            print("No ()")
            return
        tokens = tokens[:index] + [calc(tokens[index+1:c], part)] + tokens[c + 1:]

    if part == 2:
        while '+' in tokens:
            index = tokens.index('+')
            tokens = tokens[:index-1] + [str(int(tokens[index-1])+int(tokens[index+1]))] + tokens[index+2:]

    
    total = int(tokens[0])    
    for pos in range(1, len(tokens), 2):
        operator = tokens[pos]
        if operator == '+':
            total += int(tokens[pos+1])
        elif operator == '*':
            total *= int(tokens[pos+1])
    return total

total_sum = 0
for l in lines:
    res = calc(l.replace('(', '( ').replace(')', ' )').split(), 1)
    total_sum += res
print(total_sum)

total_sum = 0
for l in lines:
    res = calc(l.replace('(', '( ').replace(')', ' )').split(), 2)
    total_sum += res
print(total_sum)