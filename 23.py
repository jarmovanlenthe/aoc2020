import sys

l = "962713854"

class Node:
    value = None
    next = None
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Part 1
cups_in_game = list(map(int, list(l)))
cups_linked = [Node(c) for c in cups_in_game]
for cur, next in zip(cups_linked, cups_linked[1:]):
    cur.next = next
cups_linked[-1].next = cups_linked[0]

node_mapping = {node.value: node for node in cups_linked}

current_cup = cups_linked[0]

for rounds in range(100):
    # Pick cups
    a = current_cup.next
    b = a.next
    c = b.next
    # Remove from list
    current_cup.next = c.next

    # Find destination cup
    new_cup_cannot_be = {current_cup.value, a.value, b.value, c.value}
    current_value = current_cup.value

    while current_value in new_cup_cannot_be:
        current_value -= 1
        if current_value == 0:
            current_value = 9
    destination_cup = node_mapping[current_value]
    next_node = destination_cup.next

    # Insert removed cups
    destination_cup.next = a
    c.next = next_node

    # New current
    current_cup = current_cup.next

current_cup = node_mapping[1].next
res = ""
while current_cup != node_mapping[1]:
    res += str(current_cup.value)
    current_cup = current_cup.next
print(res)

# Part 2
cups_in_game = list(map(int, list(l)))
cups_linked = [Node(c) for c in cups_in_game]
for val in range(10, 1000001):
    cups_linked.append(Node(val))
for cur, next in zip(cups_linked, cups_linked[1:]):
    cur.next = next
cups_linked[-1].next = cups_linked[0]

node_mapping = {node.value: node for node in cups_linked}

current_cup = cups_linked[0]

for rounds in range(10000000):
    # Pick cups
    a = current_cup.next
    b = a.next
    c = b.next
    # Remove from list
    current_cup.next = c.next

    # Find destination cup
    new_cup_cannot_be = {current_cup.value, a.value, b.value, c.value}
    current_value = current_cup.value

    while current_value in new_cup_cannot_be:
        current_value -= 1
        if current_value == 0:
            current_value = 1000000
    destination_cup = node_mapping[current_value]
    next_node = destination_cup.next

    # Insert removed cups
    destination_cup.next = a
    c.next = next_node

    # New current
    current_cup = current_cup.next

cup1 = node_mapping[1]
a = cup1.next
b = a.next

print(a.value*b.value)
