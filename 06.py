from aocd import get_data

data = get_data(day=6, year=2024)

example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def part_1(rows: list[list[str]]):
    guard_pos = None
    for j, row in enumerate(rows):
        if "^" in row:
            guard_pos = (row.index('^'), j)
            break
        
    directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]
    
    direction_index = 0
    
    unique_positions = set()
        
    for i in range(len(rows) * len(rows[0])):
        direction = directions[direction_index]
        
        guard_pos = (
            guard_pos[0] + direction[0],
            guard_pos[1] + direction[1]
        )
        
        try:
            if rows[guard_pos[1]][guard_pos[0]] == "#":
                direction_index = (direction_index + 1) % len(directions)
                
                guard_pos = (
                    guard_pos[0] - direction[0],
                    guard_pos[1] - direction[1]
                )
        # IndexError when guard walks out of bounds
        except IndexError:
            return unique_positions

        unique_positions.add(guard_pos)

    # Guard never walked out of bounds = stuck in cycle
    print(unique_positions)
    return set()

def part_2(rows: list[list[str]]):
    cycles = 0
    
    for unique_position in part_1(rows):
        new_blockage = rows
        
        if new_blockage[unique_position[1]][unique_position[0]] == "^":
            continue
        
        new_blockage[unique_position[1]][unique_position[0]] = "#"
        
        if len(part_1(new_blockage)) == 0:
            # print(unique_position)
            cycles += 1
        
    return cycles

rows = example.strip().split("\n")
rows = [list(row) for row in rows]
print(part_2(rows))