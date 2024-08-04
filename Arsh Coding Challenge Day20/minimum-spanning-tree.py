import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Solution:
    
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # Step 1: Create a list of all edges with their weights
        edges = []
        for u in range(V):
            for neighbor in adj[u]:
                v, weight = neighbor
                edges.append((weight, u, v))
        
        # Step 2: Create a priority queue (min-heap) of all edges
        heapq.heapify(edges)
    
        # Step 3: Initialize Union-Find structure
        uf = UnionFind(V)
    
        mst = []
        total_cost = 0
    
        # Step 4: Process edges in order of their weights
        while edges and len(mst) < V - 1:
            weight, u, v = heapq.heappop(edges)
        
            # Check if the current edge forms a cycle
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst.append((u, v, weight))
                total_cost += weight
    
        if len(mst) != V - 1:
            return None  # MST not possible (disconnected graph)
    
        return total_cost

# Example usage:
# Number of vertices
V = 4
# Adjacency list representation: adj[u] is a list of (v, weight) pairs
adj = [
    [(1, 10), (2, 15), (3, 20)], # Edges from vertex 0
    [(0, 10), (2, 25), (3, 25)], # Edges from vertex 1
    [(0, 15), (1, 25), (3, 30)], # Edges from vertex 2
    [(0, 20), (1, 25), (2, 30)]  # Edges from vertex 3
]

solution = Solution()
total_cost = solution.spanningTree(V, adj)
if total_cost is not None:
    print(f"Total cost of the Minimum Spanning Tree: {total_cost}")
else:
    print("Minimum Spanning Tree not possible")
