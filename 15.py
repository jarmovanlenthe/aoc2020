from collections import defaultdict

with open("input15.txt") as f:
    lines = [x.strip() for x in f.readlines()]

class Game:
    def __init__(self, starting_numbers):
        self.last = defaultdict(lambda: None)
        self.before_last = defaultdict(lambda: None)
        self.last_num = 0
        self.times = 1
        for i, n in enumerate(starting_numbers):
            self.last[n] = i + 1
            self.last_num = n
            self.times += 1

    def do_game(self):
        if not self.before_last[self.last_num]:
            self.before_last[0] = self.last[0]
            self.last[0] = self.times
            self.last_num = 0
        else:
            prev = self.last[self.last_num] - self.before_last[self.last_num]
            self.before_last[prev] = self.last[prev]
            self.last[prev] = self.times
            self.last_num = prev
        self.times += 1

for l in lines:
    starting_numbers = [int(x) for x in l.split(',')]
    g = Game(starting_numbers)
    rounds = 30000000
    for times in range(len(starting_numbers), rounds):
        g.do_game()
    print(g.last_num)
    