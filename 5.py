with open("input5.txt") as f:
    lines = f.readlines()

maximum_seat_id = 0
ABS_MAX = int('1111111', 2) * 8 + int('111', 2)

missing_seats = list(range(ABS_MAX))

for l in lines:
    row = int(l[0:7].replace('F', '0').replace('B', '1'), 2)
    seat = int(l[7:10].replace('L', '0').replace('R', '1'), 2)
    seat_id = row * 8 + seat
    if seat_id > maximum_seat_id:
        maximum_seat_id = seat_id
    missing_seats.remove(seat_id)

print(maximum_seat_id)
print(missing_seats)