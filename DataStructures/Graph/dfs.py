from collections import deque

def preoder_dfs_rec(v, adj):
    """
    Traverses the adjacency list ADJ with V vertices in reorder depth first order
    recursively. Returns a list contains all the visited nodes. 
    Time Complexity - O(|V| + |E|)
    Space Complexity - O(|V|)
    """
    processed_nodes = []
    visited = [False] * v
    def helper(x):
        processed_nodes.append(x)  # visit node
        visited[x] = True
        for neigh_v in adj[x]:
            if not visited[neigh_v]:
                helper(neigh_v)
 
    helper(0)
    return processed_nodes


def preorder_dfs_itr(v, adj):
    """
    Traverses the adjacency list ADJ with V vertices in preorder depth first order
    iteratively. Returns a list contains all the visited nodes. 
    Time Complexity - O(|V| + |E|)
    Space Complexity - O(|V|)
    """
    processed_nodes = []
    visited = [False] * v
    stack = deque()
    stack.append(0)

    while len(stack):
        vertex = stack.pop()
        if visited[vertex] == False:
            visited[vertex] = True
            processed_nodes.append(vertex)
            for neigh_v in adj[vertex][::-1]:
                    stack.append(neigh_v)
    
    return processed_nodes