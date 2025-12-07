with open("day7/input.txt", "r") as f:
    grid = [line.rstrip("\n") for line in f]

rows = len(grid)
cols = len(grid[0])

rs, cs = 0, 0
for r in range(rows):
    if "S" in grid[r]:
        rs, cs = r, grid[r].index("S")
        break

stack = [(rs, cs)]
visited = set(stack)

hit_splitters = set()

while stack:
    start_r, start_c = stack.pop()

    for r in range(start_r + 1, rows):
        cell = grid[r][start_c]

        if cell == ".":
            continue

        if cell == "^":
            if (r, start_c) in hit_splitters:
                break

            hit_splitters.add((r, start_c))

            for nc in (start_c - 1, start_c + 1):
                if 0 <= nc < cols and (r, nc) not in visited:
                    visited.add((r, nc))
                    stack.append((r, nc))
            break
        break

print(len(hit_splitters))
