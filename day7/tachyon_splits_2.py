import sys

sys.setrecursionlimit(10000)

with open("day7/input.txt", "r") as f:
    grid = [line.rstrip("\n") for line in f]

rows = len(grid)
cols = len(grid[0])

start_r, start_c = 0, 0
for r in range(rows):
    if "S" in grid[r]:
        start_r, start_c = r, grid[r].index("S")
        break

memo = {}


def count_timelines(r, c):
    if not (0 <= c < cols):
        return 1

    state = (r, c)
    if state in memo:
        return memo[state]

    curr_r = r + 1

    while curr_r < rows:
        cell = grid[curr_r][c]

        if cell == "^":
            left_paths = count_timelines(curr_r, c - 1)
            right_paths = count_timelines(curr_r, c + 1)

            total = left_paths + right_paths
            memo[state] = total
            return total

        curr_r += 1

    memo[state] = 1
    return 1


total_timelines = count_timelines(start_r, start_c)
print(total_timelines)
