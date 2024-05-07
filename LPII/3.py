"""
3.Implement Greedy search algorithm for any of the following application:
Prim's Minimal Spanning Tree Algorithm
"""
import heapq
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        # Priority queue: (weight, vertex)
        pq = [(0, 0)]
        mst_cost = 0
        in_mst = [False] * self.V
        result = []

        while pq:
            weight, u = heapq.heappop(pq)
            if in_mst[u]:
                continue

            in_mst[u] = True
            mst_cost += weight
            result.append((u, weight))

            for v, cost in self.graph[u]:
                if not in_mst[v]:
                    heapq.heappush(pq, (cost, v))

        return result, mst_cost

# Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
result, mst_cost = g.prim_mst()
print("Edges in MST with their weights:", result)
print("Cost of MST:", mst_cost)