class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List to store edges (u, v, weight)

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))  # Add edge with weight

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def kruskal_mst(self):
        # Step 1: Sort edges by weight
        self.edges.sort()
        mst = []  # Store the resulting MST
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        for weight, u, v in self.edges:
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                mst.append((u, v, weight))

        return mst


# Example:
g = Graph(4)  # Create a graph with 4 vertices
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = g.kruskal_mst()
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"Edge: {u} - {v}, Weight: {weight}")
