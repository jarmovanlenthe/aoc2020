import re

with open("input19.txt") as f:
    lines = [x.strip() for x in f.readlines()]

l_rules = lines[:lines.index('')]
messages = lines[lines.index('')+1:]

rules = {}
for r in l_rules:
    i, rule = r.split(': ')
    rules[i] = rule

def generate_accepted_messages(rule):
    if re.match(r'"."', rules[rule]):
        return rules[rule][1]
    else:
        rule_parts = rules[rule].split(' | ')
        result = []
        for part in rule_parts:
            numbers = part.split()
            result.append("".join(generate_accepted_messages(n) for n in numbers))
        return f"(?:{'|'.join(result)})"

total_matches = 0
for m in messages:
    if re.fullmatch(generate_accepted_messages("0"), m):
        total_matches += 1
print(total_matches)

# Part 2
def generate_accepted_messages_2(rule):
    if rule == "8":
        # 42 | 42 8 -> (42)+
        return f"{generate_accepted_messages_2('42')}+"
    elif rule == "11":
        # 42 31 | 42 11 31 -> (42){n}(31){n} n > 1
        # Just generate 100 (because the n needs to be the same)
        r11 = (f"{generate_accepted_messages_2('42')}{{{n}}}{generate_accepted_messages_2('31')}{{{n}}}" for n in range(1, 100))
        return f"(?:{'|'.join(r11)})"

    if re.match(r'"."', rules[rule]):
        return rules[rule][1]
    else:
        rule_parts = rules[rule].split(' | ')
        result = []
        for part in rule_parts:
            numbers = part.split()
            result.append("".join(generate_accepted_messages_2(n) for n in numbers))
        return f"(?:{'|'.join(result)})"

total_matches = 0
for m in messages:
    if re.fullmatch(generate_accepted_messages_2("0"), m):
        total_matches += 1
print(total_matches)
