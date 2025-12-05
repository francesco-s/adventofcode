intervals = []
fresh_count = 0

with open("day5/input.txt") as f:
    for line in f:
        line: str = line.strip()
        if not line:
            break
        start, end = map(int, line.split("-"))
        intervals.append((start, end))

    for line in f:
        line = line.strip()
        if line:
            id_ = int(line)
            if any(start <= id_ <= end for start, end in intervals):
                fresh_count += 1

    print(fresh_count)
