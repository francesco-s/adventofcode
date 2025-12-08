import math

K = 1000


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


with open("day8/input.txt") as f:
    boxes = [tuple(map(int, line.split(","))) for line in f]

num_boxes = len(boxes)
pairs = []
dsu = UnionFind(num_boxes)


for i in range(num_boxes):
    for j in range(i + 1, num_boxes):
        pairs.append((math.dist(boxes[i], boxes[j]), i, j))

pairs.sort(key=lambda x: x[0])

for k in range(min(K, len(pairs))):
    dist, i, j = pairs[k]
    dsu.union(i, j)

comp = {}
for i in range(num_boxes):
    root = dsu.find(i)
    comp[root] = comp.get(root, 0) + 1

largest = sorted(comp.values(), reverse=True)[:3]
result = largest[0] * largest[1] * largest[2]

print(result)
