def dfs(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return 1

    visited.add(start)

    total_paths = 0

    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                total_paths += dfs(graph, neighbor, end, visited)

    visited.remove(start)

    return total_paths


graph = {}
total_path = 0

with open("day11/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line or ":" not in line:
            continue

        node, adjacents = line.split(":")
        graph[node.strip()] = adjacents.strip().split()

total_path = dfs(graph, "you", "out")
print(total_path)
