from collections import defaultdict

with open("input6.txt") as f:
    lines = f.readlines()

answers = []
group_answers = []
for l in lines:
    if l == '\n':
        answers.append(group_answers)
        group_answers = []
        continue
    a = defaultdict(lambda : False)
    for q in l.strip():
        a[q] = True
    group_answers.append(a)
answers.append(group_answers)

summ = 0
summ_2 = 0
for groups in answers:
    g = {}
    for d in groups:
        g.update(d)
    summ += len(g.keys())
    
    g2 = {}
    for k in g.keys():
        if all(x[k] for x in groups):
            g2[k] = True

    summ_2 += len(g2.keys())

print(summ)
print(summ_2)

