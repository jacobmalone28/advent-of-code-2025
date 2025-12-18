from math import sqrt
import subprocess

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True  # Successfully united

# Read junction boxes
with open("input") as f:
    boxes = []
    for line in f:
        pos = tuple(map(int, line.strip().split(",")))
        boxes.append(pos)

# Calculate distance between two points
dist = lambda a, b: sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2)

# Generate all pairs with their distances
pairs = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        d = dist(boxes[i], boxes[j])
        pairs.append((d, i, j))

# Sort pairs by distance
pairs.sort()

# Connect the 1000 closest pairs using Union-Find
uf = UnionFind(len(boxes))

for idx, (distance, i, j) in enumerate(pairs):
    uf.union(i, j)  # Try to connect (might already be in same circuit)
    if idx == 999:  # Process first 1000 pairs (0-999)
        break

# Count circuit sizes
circuit_sizes = {}
for i in range(len(boxes)):
    root = uf.find(i)
    circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

# Get the three largest circuits
sizes = sorted(circuit_sizes.values(), reverse=True)
answer = sizes[0] * sizes[1] * sizes[2]

subprocess.run("pbcopy", text=True, input=str(answer))
print(answer, "(copied to clipboard)")