with open("day4/input.txt") as f:
    lines = f.read().strip().split("\n")
    grid = [list(line) for line in lines]

    accessible = 0
    rows = len(grid)
    cols = len(grid[0])
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

    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "@":
                    continue
                neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "@":
                            neighbors += 1
                if neighbors < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = "."

        total_removed += len(to_remove)

    print(total_removed)

# TODO: use stacks
