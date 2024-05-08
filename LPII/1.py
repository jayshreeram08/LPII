"""
1.Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a
recursive algorithm for searching all the vertices of a graph or tree data structure.
"""
g={
    0:[1,2],
    1:[0,3,4],
    2:[3,0],
    3:[2,1,4],
    4:[3,1]
}
def dfs(g,s):
    vis[s]=1
    print(s)
    for c in g[s]:
        if not vis[c]:
            dfs(g,c)

vis=[0]*5   #list compression
print("DFS traversal")
dfs(g,0)
def bfs(g,s):
    q=[s]
    vis=[s]
    while q:
        cur=q.pop(0)
        print(cur)
        for c in g[cur]:
            if c not in vis:
                q.append(c)
                vis.append(c)
print("BFS traversal")
bfs(g,0)
