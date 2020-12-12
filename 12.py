import math

with open("input12.txt") as f:
    lines = f.readlines()

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.degrees = 90
        self.wpx = 10
        self.wpy = 1

    def parse_line(self, l):
        action, value = l[0], int(l[1:])
        if action == "F":
            actions = ["N", "E", "S", "W"]
            action = actions[int(self.degrees/90)]
        if action == "N":
            self.y += value
        elif action == "E":
            self.x += value
        elif action == "S":
            self.y -= value
        elif action == "W":
            self.x -= value
        elif action == "L":
            self.degrees = (self.degrees - value) % 360
        elif action == "R":
            self.degrees = (self.degrees + value) % 360
    
    def parse_line2(self, l):
        action, value = l[0], int(l[1:])
        if action == "F":
            self.x += value * self.wpx
            self.y += value * self.wpy
        elif action == "N":
            self.wpy += value
        elif action == "S":
            self.wpy -= value
        elif action == "E":
            self.wpx += value
        elif action == "W":
            self.wpx -= value
        elif action == "R":
            value = -value
            action = "L"
        if action == "L":
            # Apply rotation matrix
            x = round(self.wpx * math.cos(2*math.pi*(value/360)) - self.wpy * math.sin(2*math.pi*(value/360)))
            y = round(self.wpx * math.sin(2*math.pi*(value/360)) + self.wpy * math.cos(2*math.pi*(value/360)))
            self.wpx, self.wpy = x, y

# Part 1
s = Ship()
for l in lines:
    s.parse_line(l)
print(abs(s.x), abs(s.y), abs(s.x)+abs(s.y))

print()

# Part 2
s = Ship()
for l in lines:
    s.parse_line2(l)
print(abs(s.x), abs(s.y), abs(s.x)+abs(s.y))
