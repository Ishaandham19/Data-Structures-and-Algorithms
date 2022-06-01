def bfs(v, adj):
    """
    Traverses the adjacency list ADJ with V vertices in breadth first order. 
    Returns a list contains all the visited nodes. 
    Time Complexity - O(|V| + |E|)
    Space Complexity - O(|V|)
    """
    visited_nodes = []
    visited = [False] * v
    queue = [0]
    visited[0] = True
    while len(queue):
        v = queue.pop(0)
        visited_nodes.append(v) # visit node
        for edge in adj[v]:
            vertex = edge[0]
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
    
    return visited_nodes
