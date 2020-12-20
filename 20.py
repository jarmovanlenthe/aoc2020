from collections import defaultdict

MONSTER="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')

with open("input20.txt") as f:
    lines = [x.strip() for x in f.readlines()]

# input consists of 144 10*10 tiles

tiles = {}
tile = []
tile_num = 0
for l in lines:
    if l == '':
        tiles[tile_num] = tile
        tile = []
    elif l.startswith('Tile'):
        tile_num = int(l[5:-1])
    else:
        tile.append(l)

def rotations(t):
    res = [t]
    cur = t[:]
    for _ in range(3):
        rot_90 = [''.join(reversed(x)) for x in zip(*cur)]
        res.append(rot_90)
        cur = rot_90[:]
    return res

def flipped(t):
    res = []
    res.append(t)
    res.append(t[::-1])
    res.append([i[::-1] for i in t])
    res.append([i[::-1] for i in t[::-1]])
    return res

def flipped_and_rotated(t):
    opts = []
    for r in flipped(t):
        opts.extend(rotations(r))
    res = []
    for opt in opts:
        if opt not in res:
            res.append(opt)
    return res

def borders(t):
    border = []
    border.append(t[0])
    border.append(t[-1])
    border.append(''.join([i[0] for i in t]))
    border.append(''.join([i[-1] for i in t]))
    border.append(t[0][::-1])
    border.append(t[-1][::-1])
    border.append(''.join([i[0] for i in t][::-1]))
    border.append(''.join([i[-1] for i in t][::-1]))
    return border

def neighbors(tile_num):
    neighbor_num = 0
    for tborder in borders(tiles[tile_num]):
        for k, v in tiles.items():
            if k == tile_num:
                continue
            for oborder in borders(v):
                if tborder == oborder:
                    neighbor_num += 1
    return neighbor_num / 2

def get_tiles_with_n_neighbors(n):
    res = []
    for t in tiles:
        if neighbors(t) == n:
            res.append(t)
    return res

# Part 1
prod = 1
for t in get_tiles_with_n_neighbors(2):
    prod *= t
print(prod)

# Part 2

# Because the total image is also a square, we can calculate the dimension (also with sqrt, but that needs the math import :-))
dimension = int(len(get_tiles_with_n_neighbors(3))/4 + len(get_tiles_with_n_neighbors(2))/2)

def generate_tiling(t_map):
    puzzle = [[None for i in range(dimension)] for j in range(dimension)]
    def generate_tiling_r(puzzle, x, y, added):
        if y == dimension:
            return puzzle
        next_x, next_y = x + 1, y
        if next_x == dimension:
            next_x, next_y = 0, y + 1
        for tile_id, options in t_map.items():
            if tile_id in added:
                continue
            added.add(tile_id)
            for index, borders in options.items():
                top, left = borders[0], borders[2]
                if x > 0:
                    neighbor_id, neighbor_index = puzzle[x-1][y]
                    neighbor_right_border = t_map[neighbor_id][neighbor_index][3]
                    if neighbor_right_border != left:
                        continue
                if y > 0:
                    neighbor_id, neighbor_index = puzzle[x][y-1]
                    neighbor_bottom_border = t_map[neighbor_id][neighbor_index][1]
                    if neighbor_bottom_border != top:
                        continue
                puzzle[x][y] = (tile_id, index)
                answer = generate_tiling_r(puzzle, next_x, next_y, added)
                if answer:
                    return answer
            added.remove(tile_id)
        puzzle[x][y] = None
        return None
    return generate_tiling_r(puzzle, 0, 0, set())

def make_image(tile_options, puzzle_layout):
    res = []
    for row in puzzle_layout:
        grids = []
        for tile_id, index in row:
            grid = tile_options[tile_id][index]
            grid = [i[1:-1] for i in grid[1:-1]]
            grids.append(grid)
        for y in range(len(grids[0][0])):
            res_row = []
            for i in range(len(grids)):
                res_row.extend(grids[i][x][y] for x in range(len(grids[i])))
            res.append("".join(res_row))
    return res

def check_monster(puzzle,x,y):
    for dx, r in enumerate(MONSTER):
        for dy, c in enumerate(r):
            if c == '#' and puzzle[x+dx][y+dy] != '#':
                return 0
    return 1

tile_options = {tile_id: flipped_and_rotated(tile) for tile_id, tile in tiles.items()}
tile_map = defaultdict(dict)
for tile_id, options in tile_options.items():
    for index, tile in enumerate(options):
        tile_map[tile_id][index] = borders(tile)
puzzle_layout = generate_tiling(tile_map)
puzzle = make_image(tile_options, puzzle_layout)
all_puzzles = flipped_and_rotated(puzzle)
num_monsters = 0
for puzzle in all_puzzles:
    for px in range(len(puzzle)-len(MONSTER)+1):
        for py in range(len(puzzle[px])-len(MONSTER[0])+1):
            num_monsters += check_monster(puzzle,px,py)
roughness = "".join(puzzle).count('#') - num_monsters * "".join(MONSTER).count('#')
print(roughness)