from aocd import data

example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def part_1(data):
    rows = data.split("\n")

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]

    pattern = "XMAS"
    count = 0

    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            for direction in directions:
                for k in range(0, len(pattern)):
                    current_i = i + direction[0] * k
                    current_j = j + direction[1] * k
                    
                    if current_i < 0 or current_j < 0 or current_i >= len(rows) or current_j >= len(row):
                        break
                    
                    if rows[current_i][current_j] == pattern[k]:
                        if k == len(pattern) - 1:
                            count += 1
                    else:
                        break
                    
    return count

def part_2(data):
    rows = data.split("\n")
    
    directions = [
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]
    
    xmas_count = 0
        
    for i in range(1, len(rows) - 1):
        row = rows[i]
        for j in range(1, len(row) - 1):
            char = row[j]
            if char == 'A':
                surrounding = [rows[i + direction[0]][j + direction[1]] for direction in directions]
                if set(surrounding[0:2]) == {'M', 'S'}:
                    print(i, j)
                    if set(surrounding[2:]) == {'M', 'S'}:
                        xmas_count += 1
    
    return xmas_count
    
print(part_2(data))