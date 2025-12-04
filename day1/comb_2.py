pos = 50
count0 = 0

with open("day1/input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        dist = int(line[1:])
        step = 1 if direction == "R" else -1

        for _ in range(dist):
            pos = (pos + step) % 100
            if pos == 0:
                count0 += 1

print(count0)
