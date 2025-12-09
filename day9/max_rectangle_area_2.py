tiles = []
with open("day9/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(","))
        tiles.append((x, y))

n = len(tiles)
perimeter = set()
for i in range(n):
    p = tiles[i]
    q = tiles[(i + 1) % n]

    a1, a2 = min(p[0], q[0]), max(p[0], q[0])
    b1, b2 = min(p[1], q[1]), max(p[1], q[1])

    for a in range(a1, a2 + 1):
        for b in range(b1, b2 + 1):
            perimeter.add((a, b))

candidates = []
for i in range(n):
    p = tiles[i]
    for j in range(i + 1, n):
        q = tiles[j]

        width = abs(p[0] - q[0]) + 1
        height = abs(p[1] - q[1]) + 1
        area = width * height
        candidates.append((area, p, q))

candidates.sort(key=lambda x: x[0], reverse=True)

solution_found = 0
for area_val, p, q in candidates:
    a1, a2 = min(p[0], q[0]), max(p[0], q[0])
    b1, b2 = min(p[1], q[1]), max(p[1], q[1])

    contains_perimeter = False
    for px, py in perimeter:
        if a1 < px < a2 and b1 < py < b2:
            contains_perimeter = True
            break

    if not contains_perimeter:
        solution_found = area_val
        break

print(solution_found)
