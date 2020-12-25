from collections import defaultdict

with open("input25.txt") as f:
    lines = list(map(int, f.readlines()))

pub_door = lines[0]
pub_card = lines[1]
print(f"Door pubkey: {pub_door}")
print(f"Card pubkey: {pub_card}")

def get_loop_size(pub_key):
    loop_size = 0
    value = 1
    while value != pub_key:
        value = (value * 7) % 20201227
        loop_size += 1
    return loop_size

def get_encryption_key(pub_key, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * pub_key) % 20201227
    return value

loop_door = get_loop_size(pub_door)
loop_card = get_loop_size(pub_card)
print(loop_door, loop_card)

print(get_encryption_key(pub_card, loop_door))
