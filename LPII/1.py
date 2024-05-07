"""
1.Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a
recursive algorithm for searching all the vertices of a graph or tree data structure.
"""
class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs(self, s):
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)

        while queue:
            s = queue.pop(0)
            print(s, end=' ')
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(4, 6)

print("DFS starting from vertex 0:")
g.dfs_recursive(0)
print("\nBFS starting from vertex 0:")
g.bfs(0)