TO_SUM = 2020

with open("input1.txt") as f:
    lines = [int(x) for x in f.readlines()]

# Part 1
below = [x for x in lines if x<=1010]
above = [x for x in lines if x>1010]

for x in below:
    for y in above:
        if x + y == TO_SUM:
            print(f"Pair is: {x} and {y}.")
            print("Product is: {}.".format(x*y))

# Part 2
lines.sort()

for i in range(len(lines)):
    for j in range(i, len(lines)):
        for k in range(j, len(lines)):
            if lines[i] + lines[j] + lines[k] == TO_SUM:
                print("Pair is {}, {}, {}".format(lines[i], lines[j], lines[k]))
                print("Product is {}".format(lines[i]*lines[j]*lines[k]))
