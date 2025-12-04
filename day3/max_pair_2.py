K = 12

with open("day3/input.txt") as f:
    total = 0
    for line in f:
        digits = line.strip()
        stack = []
        removals = len(digits) - K

        for d in digits:
            while stack and removals > 0 and stack[-1] < d:
                stack.pop()
                removals -= 1
            stack.append(d)

        best = int("".join(stack[:K]))
        total += best

    print(total)
