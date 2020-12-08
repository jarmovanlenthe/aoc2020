import copy

with open("input8.txt") as f:
    lines = [l.strip() for l in f.readlines()]

class Proc:

    def __init__(self, instructions):
        self.instructions = instructions
        self.ip = 0
        self.acc = 0

    def handle_instruction(self):
        try:
            command, operand = self.instructions[self.ip].split(' ')
        except:
            print("Finished!")
            raise
        if command == "acc":
            self.acc += int(operand)
            self.ip += 1
        if command == "jmp":
            self.ip += int(operand)
        if command == "nop":
            self.ip += 1

# Part 1
p = Proc(lines)
instructions_seen = []
while True:

    if p.ip in instructions_seen:
        print(p.acc)
        break
    instructions_seen.append(p.ip)

    p.handle_instruction()

# Part 2
for i in range(len(lines)):
    instructions = copy.deepcopy(lines)
    l = instructions[i]
    command, operand = l.split(' ')
    if command == "jmp":
        instructions[i] = f"nop {operand}"
    elif command == "nop":
        instructions[i] = f"jmp {operand}"
    
    instructions_seen = []
    p = Proc(instructions)
    while p.ip not in instructions_seen:
        if p.ip in instructions_seen:
            print(p.acc)
            break
        instructions_seen.append(p.ip)
        try:
            p.handle_instruction()
        except:
            print(f"Finished on IP: {p.ip}")
            print(f"Changed line: {i}")
            print(f"Accumulator value: {p.acc}")
