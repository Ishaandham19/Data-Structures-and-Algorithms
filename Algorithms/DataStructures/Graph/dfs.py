def preoder_dfs_rec(v, adj):
    """
    Traverses the adjacency list ADJ with V vertices in preorder depth first order
    recursively. Returns a list contains all the visited nodes. 
    Time Complexity - O(|V| + |E|)
    Space Complexity - O(|V|)
    """
    visited_nodes = []
    visited = [False] * v
    def helper(x):
        if visited[x]:
            return
        visited_nodes.append(x)  # visit node
        visited[x] = True
        for edge in adj[x]:
            v = edge[0]
            helper(v)

    helper(0)
    return visited_nodes


def preorder_dfs_itr(v, adj):
    """
    Traverses the adjacency list ADJ with V vertices in preorder depth first order
    iteratively. Returns a list contains all the visited nodes. 
    Time Complexity - O(|V| + |E|)
    Space Complexity - O(|V|)
    """