bags = []

class Bag:
    def __init__(self, color):
        self.color = color
        self.children = []
        bags.append(self)

    def add_child(self, amount, bag):
        self.children.append((amount, bag))
    
    def __str__(self):
        childstr = ""
        if self.children:
            childrenstr = "[" + ", ".join([str(a) + " of " + str(c) for a, c in self.children]) + "]"
            return f"{self.color} -> {childrenstr}"
        return f"{self.color}"
    
    def amount_of_children(self):
        if not self.children:
            return 0
        return sum([a for a, c in self.children]) + sum(a * c.amount_of_children() for a, c in self.children)

    @staticmethod
    def find(color):
        for bag in bags:
            if bag.color == color:
                return bag
    
    @staticmethod
    def find_or_create(color):
        bag = Bag.find(color)
        if bag:
            return bag
        return Bag(color)

def preprocess_data():
    with open("input7.txt") as f:
        lines = f.readlines()
    lines = [x.replace('.', '').replace('bags', '').replace('bag', '') for x in lines]
    for l in lines:
        node, children = l.split(' contain ')
        node = node.strip()
        node = Bag.find_or_create(node)
        for child in children.split(','):
            child = child.strip()
            amount, color = child.split(' ', 1)
            if amount == "no":
                continue
            amount = int(amount)
            node.add_child(amount, Bag.find_or_create(color.strip()))

preprocess_data()
amount = 0
for bag in bags:
    if bag.color == "shiny gold":
        continue
    if "shiny gold" in str(bag):
        amount += 1
print(amount)

shiny = Bag.find("shiny gold")
print(shiny.amount_of_children())