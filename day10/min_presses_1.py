import re
from collections import deque


def parse_line(line):
    # Extract target pattern inside [ ... ]
    target = re.search(r"\[([.#]+)\]", line).group(1)

    # Extract all button groups inside ( ... )
    buttons_raw = re.findall(r"\(([^)]*)\)", line)

    buttons = []
    for b in buttons_raw:
        if b.strip() == "":
            buttons.append(())
        else:
            buttons.append(tuple(int(x) for x in b.split(",")))

    return target, buttons


def min_presses(target, buttons):
    n = len(target)
    target_state = tuple(1 if c == "#" else 0 for c in target)

    masks = []
    for b in buttons:
        mask = [0] * n
        for i in b:
            mask[i] ^= 1
        masks.append(tuple(mask))

    start = (0,) * n
    if start == target_state:
        return 0

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, dist = queue.popleft()

        for mask in masks:
            new_state = tuple(state[i] ^ mask[i] for i in range(n))
            if new_state == target_state:
                return dist + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, dist + 1))

    return None


total = 0
with open("day10/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        target, buttons = parse_line(line)
        presses = min_presses(target, buttons)
        total += presses if presses else 0

print(total)
