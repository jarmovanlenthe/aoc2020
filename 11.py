with open("input11.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def get_seat(state, x, y):
    if x < 0 or y < 0:
        return 'L'
    try:
        return state[x][y]
    except:
        return 'L'
    
def get_occupied_seats_around_seat(state, x, y):
    positions = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    seats = [get_seat(state, a, b) for a, b in positions]
    return seats.count("#")

def get_first_seat(state, x, y, xfunc, yfunc):
    current_seat = get_seat(state, x, y)
    if current_seat == '.':
        return get_first_seat(state, xfunc(x), yfunc(y), xfunc, yfunc)
    else:
        return current_seat

def get_occupied_seats_around_seat_part2(state, x, y):
    plus_f = lambda x: x + 1
    min_f = lambda x: x - 1
    nop_f = lambda x: x
    positions = [
        get_first_seat(state, x-1,y-1,min_f,min_f),
        get_first_seat(state, x,y-1,nop_f,min_f),
        get_first_seat(state, x+1,y-1,plus_f,min_f),
        get_first_seat(state, x-1,y,min_f,nop_f),
        get_first_seat(state, x+1,y,plus_f,nop_f),
        get_first_seat(state, x-1,y+1,min_f,plus_f),
        get_first_seat(state, x,y+1,nop_f,plus_f),
        get_first_seat(state, x+1,y+1,plus_f,plus_f),
        ]
    return positions.count('#')

def seat_round(state, occupy_func, leniency):
    new_state = []
    for i in range(len(state)):
        row = ""
        for j in range(len(state[0])):
            current_seat = state[i][j]
            if current_seat == "L":
                if occupy_func(state, i, j) == 0:
                    row += "#"
                else:
                    row += "L"
            elif current_seat == "#":
                if occupy_func(state, i, j) >= leniency:
                    row += "L"
                else:
                    row += "#"
            else:
                row += '.'
        new_state.append(row)
    return new_state

# Part 1
old_state = []
new_state = lines
while old_state != new_state:
    old_state = new_state
    new_state = seat_round(old_state, get_occupied_seats_around_seat, 4)

print(sum(map(lambda x: x.count('#'), new_state)))


# Part 2
old_state = []
new_state = lines
while old_state != new_state:
    old_state = new_state
    new_state = seat_round(old_state, get_occupied_seats_around_seat_part2, 5)

print(sum(map(lambda x: x.count('#'), new_state)))