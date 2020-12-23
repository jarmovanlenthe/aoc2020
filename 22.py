from collections import deque
from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

with open("input22.txt") as f:
    lines = [_.strip() for _ in f.readlines()]

player_1 = deque()
player_2 = deque()
p1 = True
for l in lines:
    if l == '':
        p1 = False
    if l.isalnum():
        if p1:
            player_1.append(int(l))
        else:
            player_2.append(int(l))
part2_1 = deepcopy(player_1)
part2_2 = deepcopy(player_2)

def play():
    p1 = player_1.popleft()
    p2 = player_2.popleft()
    if p1 > p2:
        player_1.append(p1)
        player_1.append(p2)
    else:
        player_2.append(p2)
        player_2.append(p1)

while len(player_1) > 0 and len(player_2) > 0:
    play()

if len(player_1) > 0:
    winner = list(player_1)
else:
    winner = list(player_2)

multiply_list = map(lambda x: x + 1, list(range(len(winner)))[::-1])
print(sum(map(lambda x: x[0]*x[1], zip(winner, multiply_list))))

# Part 2
player_1 = part2_1
player_2 = part2_2

def play_2(player_1: deque, player_2: deque, seen: set):
    if len(player_1) == 0:
        return 2, player_1, player_2
    if len(player_2) == 0:
        return 1, player_1, player_2
    if (tuple(player_1),tuple(player_2)) in seen:
        return 1, player_1, player_2
    seen.add((tuple(player_1), tuple(player_2)))
    p1 = player_1.popleft()
    p2 = player_2.popleft()
    if p1 > p2:
        winner = 1
    else:
        winner = 2
    if len(player_1) >= p1 and len(player_2) >= p2:
        winner, _, _ = play_2(deque(list(deepcopy(player_1))[:p1]), deque(list(deepcopy(player_2))[:p2]), set())
    
    if winner == 1:
        player_1.append(p1)
        player_1.append(p2)
        return play_2(player_1, player_2, seen)
    elif winner == 2:
        player_2.append(p2)
        player_2.append(p1)
        return play_2(player_1, player_2, seen)

winner, player_1, player_2 = play_2(player_1, player_2, set())

if winner == 1:
    winner = list(player_1)
else:
    winner = list(player_2)

multiply_list = list(map(lambda x: x + 1, list(range(len(winner)))[::-1]))
print(sum(map(lambda x: x[0]*x[1], zip(winner, multiply_list))))
