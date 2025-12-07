import math

with open("day6/input.txt") as f:
    lines = [line.rstrip("\n") for line in f]

ops_line = lines[-1]
num_lines = lines[:-1]

width = len(ops_line)
height = len(num_lines)

grid = [list(line.ljust(width)) for line in num_lines]

is_sep = [
    all(row[c] == " " for row in grid) and ops_line[c] == " " for c in range(width)
]

problems = []
start = None
for c in range(width):
    if not is_sep[c] and start is None:
        start = c
    if is_sep[c] and start is not None:
        problems.append((start, c - 1))
        start = None
if start is not None:
    problems.append((start, width - 1))

answers = []
for cs, ce in problems:
    op_col = None
    for c in range(cs, ce + 1):
        if ops_line[c] in "+*":
            op_col = c
            break
    if op_col is None:
        continue
    op = ops_line[op_col]

    nums = []
    for r in range(height):
        segment = "".join(grid[r][cs : ce + 1]).strip()
        if segment:
            nums.append(int(segment))

    if not nums:
        continue

    if op == "+":
        val = sum(nums)
    else:
        val = math.prod(nums)

    answers.append(val)

grand_total = sum(answers)
print(grand_total)
