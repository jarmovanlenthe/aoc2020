from collections import defaultdict

with open("input24.txt") as f:
    lines = [_.strip() for _ in f.readlines()]

# Hex tiles work with [x,y,z] coordinates with x+y+z=0
# https://stackoverflow.com/questions/1838656/how-do-i-represent-a-hextile-hex-grid-in-memory

def parse_tile(direction):
    def parse_tile_recursive(direction, x, y, z):
        if direction == '':
            return x, y, z
        # e, se, sw, w, nw, and ne
        if direction.startswith('se'):
            return parse_tile_recursive(direction[2:], x, y - 1, z + 1)
        elif direction.startswith('sw'):
            return parse_tile_recursive(direction[2:], x - 1, y, z + 1)
        elif direction.startswith('nw'):
            return parse_tile_recursive(direction[2:], x, y + 1, z - 1)
        elif direction.startswith('ne'):
            return parse_tile_recursive(direction[2:], x + 1, y, z - 1)
        elif direction.startswith('e'):
            return parse_tile_recursive(direction[1:], x + 1, y - 1, z)
        elif direction.startswith('w'):
            return parse_tile_recursive(direction[1:], x - 1, y + 1, z)
    return parse_tile_recursive(direction, 0, 0, 0)

tiles = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
for l in lines:
    x, y, z = parse_tile(l)
    tiles[x][y][z] = not tiles[x][y][z]

def amount_of_blacks(tiles):
    blacks = 0
    for x in tiles:
        for y in tiles[x]:
            for z in tiles[x][y]:
                if tiles[x][y][z]:
                    blacks += 1
    return blacks

# Part 1
print(amount_of_blacks(tiles))

# Part 2
neighbors_positions = [parse_tile(x) for x in ['se', 'sw', 'ne', 'nw', 'e', 'w']]

def get_neighbors(x, y, z):
    neighbors = []
    for neighbor in neighbors_positions:
        nx, ny, nz = neighbor
        neighbors.append((x+nx, y+ny, z+nz))
    return neighbors

def get_black_neighbors(state, x, y, z):
    result = 0
    for neighbor in get_neighbors(x, y, z):
        nx, ny, nz = neighbor
        if state[nx][ny][nz]:
            result += 1
    return result

def hex_gol(state):
    new_state = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
    tiles_to_check = []
    for x in state:
        for y in state[x]:
            for z in state[x][y]:
                tiles_to_check.append((x,y,z))
    neighbors = []
    for tile in tiles_to_check:
        neighbors.extend(get_neighbors(*tile))
    
    tiles_to_check.extend(neighbors)

    for tile in tiles_to_check:
        x, y, z = tile
        black_neighbors = get_black_neighbors(state, *tile)
        if state[x][y][z] and (black_neighbors == 0 or black_neighbors > 2):
            new_state[x][y][z] = False
        elif not state[x][y][z] and black_neighbors == 2:
            new_state[x][y][z] = True
        else:
            new_state[x][y][z] = state[x][y][z]
    
    return new_state

for rounds in range(100):
    tiles = hex_gol(tiles)
print(amount_of_blacks(tiles))