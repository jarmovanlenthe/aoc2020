from collections import defaultdict
from itertools import combinations_with_replacement
with open("input17.txt") as f:
    lines = [x.strip() for x in f.readlines()]

state = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == "#":
            state[0][y][x] = True
        else:
            state[0][y][x] = False

neighbors_positions = []
for z in range(-1, 2):
    for y in range(-1, 2):
        for x in range(-1, 2):
            if (z,y,x) != (0,0,0):
                neighbors_positions.append((z,y,x))

def get_active_neighbors(current_state, z, y, x):
    active_neighbors = 0
    for pos in neighbors_positions:
        if current_state[z+pos[0]][y+pos[1]][x+pos[2]]:
            active_neighbors += 1
    return active_neighbors

def get_state_range(d: dict):
    mi = min(d.keys()) if d.keys() else 0
    ma = max(d.keys()) if d.keys() else 0
    return mi, ma

original_state_dimensions = get_state_range(state[0])

def enlarge_state_range(d: dict, current_round):
    mi, ma = get_state_range(d)
    return original_state_dimensions[0] - current_round, original_state_dimensions[1] + current_round + 1

def round_of_3d_GoL(state, current_round):
    new_state = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
    for z in range(*enlarge_state_range(state, current_round)):
        for y in range(*enlarge_state_range(state[z], current_round)):
            for x in range(*enlarge_state_range(state[z][y], current_round)):
                if state[z][y][x] and get_active_neighbors(state, z,y,x) not in [2, 3]:
                    new_state[z][y][x] = False
                elif not state[z][y][x] and get_active_neighbors(state, z,y,x) == 3:
                    new_state[z][y][x] = True
                else:
                    new_state[z][y][x] = state[z][y][x]
    return new_state

rounds = 6
for i in range(1, rounds+1):
    state = round_of_3d_GoL(state, i)

num_active = 0
for z in state:
    for y in state[z]:
        for x in state[z][y]:
            if state[z][y][x]:
                num_active += 1
print(num_active)
