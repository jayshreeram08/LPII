#Implement depth first search algorithm and Breadth First Search algorithm,
# Use an undirected graph and develop a recursive algorithm for searching all the vertices of a 
# graph or tree data structure

def bfs(visited, graph, queue):
    if not queue:
        return
    node = queue.pop(0)
    print(node, end=' ')
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited and neighbour not in queue:
            queue.append(neighbour)
    bfs(visited, graph, queue)

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def main():
    graph = {}
    print("Enter the number of vertices:")
    n = int(input())
    print("Enter the adjacency list for each vertex (node: neighbours, separated by spaces):")
    for i in range(n):
        node, *neighbours = input().split()
        graph[node] = neighbours
    start_node = input("Enter the starting node: ")

    print("\nFollowing is the Breadth First Search:")
    bfs_visited = set()
    bfs_queue = [start_node]
    bfs(bfs_visited, graph, bfs_queue)

    print("\n\nFollowing is the Depth First Search:")
    dfs_visited = set()
    dfs(dfs_visited, graph, start_node)

if __name__ == "__main__":
    main()
