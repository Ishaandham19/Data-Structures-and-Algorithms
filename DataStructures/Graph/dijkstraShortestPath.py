"""
 Brief Description- Dijkstra's shortest path algorithm computes the shortest path from
 the starting node to all the nodes of the graph.
 Assumption - No negative weights. (doesn't work with negative weights - use Bellman Ford.)
"""

import heapq

def dijkstra_shortest_path(v, adj, x):
    """ Computes the shortest distances from vertex X to all other vertices in graph.
     Argument ADJ represents a adjacency list - [[(v1,w1), (v2,w2)], [(),()...]...]
     and V the number of vertices.

     Time Complexity - Theta(|V| + |E| * log |E|)
     Space Complexity: Theta(|V|) - size of heap is |V|

    Alternate implementation - 
        Add all the vertices in the heap - start heap with V vertices. 
        Change heappush to decreasePriority operation. 
        Time Complexity - Theta((|V| + |E|) * log |V|)
    """
    distances = [float('inf')] * v
    distances[x] = 0
    processed = [False] * v
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, x))
    while len(heap):
        w0, v0 = heapq.heappop(heap)
        if processed[v0]:
            continue
        processed[v0] = True
        for edge in adj[v0]:
            v1, w1 = edge
            if (distances[v0] + w1) < distances[v1]:
                distances[v1] = distances[v0] + w1
                heapq.heappush(heap, (distances[v1], v1))

    return distances
