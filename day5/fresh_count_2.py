intervals = []
fresh_count = 0

with open("day5/input.txt") as f:
    for line in f:
        line: str = line.strip()
        if not line:
            break
        start, end = map(int, line.split("-"))
        intervals.append((start, end))

    intervals.sort()

    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    fresh_count = sum(end - start + 1 for start, end in merged)

    print(fresh_count)
