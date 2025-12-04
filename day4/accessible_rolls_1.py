with open("day4/input.txt") as f:
    lines = f.read().strip().split("\n")
    grid = [list(line) for line in lines]

    accessible = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (-1, 1),
        (0, -1),
        (-1, 0),
        (1, -1),
        (-1, -1),
    ]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            curr_count = 0
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    curr_count += 1
            if curr_count < 4:
                accessible += 1

    print(accessible)
