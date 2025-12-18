from math import sqrt
import subprocess

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_sets = n  # Track number of disjoint sets
    
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
        
        self.num_sets -= 1  # Merged two sets into one
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

# Connect pairs until all are in one circuit
uf = UnionFind(len(boxes))
last_connection = []

for distance, i, j in pairs:
    if uf.union(i, j):
        last_connection = (i, j)
        if uf.num_sets == 1:  # All boxes are now in one circuit
            break

# Get the X coordinates of the last two boxes connected
x1 = boxes[last_connection[0]][0]
x2 = boxes[last_connection[1]][0]
answer = x1 * x2

subprocess.run("pbcopy", text=True, input=str(answer))
print(answer, "(copied to clipboard)")
