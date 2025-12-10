import re
from time import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

"""Using stacks -> TLE:
from collections import deque


def parse_line_part2(line):
    # Extract joltage requirements inside { ... }
    joltage_match = re.search(r"\{([^}]+)\}", line)
    if not joltage_match:
        return None, []

    # Target is now a tuple of integers, not a string of .#
    target = tuple(int(x) for x in joltage_match.group(1).split(","))

    # Extract all button groups inside ( ... )
    buttons_raw = re.findall(r"\(([^)]*)\)", line)

    buttons = []
    for b in buttons_raw:
        if b.strip() == "":
            buttons.append(())
        else:
            buttons.append(tuple(int(x) for x in b.split(",")))

    return target, buttons


def min_presses_part2(target, buttons):
    n = len(target)
    start = (0,) * n  # Start with all registers at 0

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, dist = queue.popleft()

        for b_indices in buttons:
            # Create new state: Add 1 to each index affected by this button
            # Note: Part 2 is addition, not XOR
            new_state_list = list(state)
            possible = True
            for idx in b_indices:
                new_state_list[idx] += 1
                # Optimization: Pruning
                # If we exceed the target at any index, this path is invalid
                if new_state_list[idx] > target[idx]:
                    possible = False
                    break

            if not possible:
                continue

            new_state = tuple(new_state_list)

            if new_state == target:
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

        target, buttons = parse_line_part2(line)
        if target is None:
            continue

        presses = min_presses_part2(target, buttons)

        if presses is not None:
            total += presses
        else:
            print(f"Warning: No solution found for line: {line[:20]}...")

print(total)

"""

# Using ILP -> vibe coded


ts = time()
total = 0

with open("day10/input.txt", "r") as f:
    lines = f.read().strip().splitlines()

machines = []
for line in lines:
    if not line.strip():
        continue

    # Extract buttons: (0,1)(2) -> [[0, 1], [2]]
    button_strs = re.findall(r"\(([^)]*)\)", line)
    buttons = []
    for button in button_strs:
        if not button.strip():  # Handle empty buttons "()"
            buttons.append([])
        else:
            inds = [int(x) for x in button.split(",")]
            buttons.append(inds)

    # Extract jolts: {10,20} -> [10, 20]
    m = re.search(r"\{([^}]*)\}", line)
    if m:
        jolts = [int(x) for x in m.group(1).split(",")]
        machines.append((buttons, jolts))


# Helper function to solve single machine ILP
def solve_machine(buttons, jolts):
    n = len(jolts)
    m = len(buttons)

    # Matrix A: A[i, j] = 1 if button j affects index i
    A = np.zeros((n, m), dtype=int)
    for j, inds in enumerate(buttons):
        for i in inds:
            if i < n:  # Safety check
                A[i, j] = 1

    # Objective: Minimize sum of button presses (c = [1, 1, ..., 1])
    c = np.ones(m, dtype=float)

    # Constraint: A @ x = jolts
    jolts_arr = np.array(jolts, dtype=float)
    lc = LinearConstraint(A, lb=jolts_arr, ub=jolts_arr)

    # Bounds: x >= 0 (cannot press negative times)
    bounds = Bounds(lb=np.zeros(m), ub=np.full(m, np.inf))

    # Integrality: Force solutions to be integers
    integrality = np.ones(m, dtype=int)

    res = milp(c=c, constraints=[lc], integrality=integrality, bounds=bounds)

    if res.status != 0:
        # Status 0 means success.
        # If strictly required to exist, we could raise error, but returning 0 allows continuing.
        # print(f"Warning: ILP failed/infeasible (Status {res.status})")
        return 0

    # res.fun is the minimized objective value (total presses)
    return int(round(res.fun))


# Process all machines
for buttons, jolts in machines:
    total += solve_machine(buttons, jolts)

print(f"Total minimal presses: {total}")
print(f"Runtime: {time() - ts:.4f}s")
