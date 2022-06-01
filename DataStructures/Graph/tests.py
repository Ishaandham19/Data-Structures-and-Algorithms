from dijkstra_shortest_path import dijkstra_shortest_path
import dfs
import bfs

if __name__ == "__main__":
       graph1 = [[(1, 3), (2, 1)], 
              [(0, 3), (2, 7), (3, 5), (4, 1)],
              [(0, 1), (1, 7), (3, 2)],
              [(1, 5), (2, 2), (4, 7)],
              [(1, 1), (3, 7)]]


       graph2 = [[]]
       # Test for Dijkstra shortest path       
       expected_distances_staring_2 = [1, 4, 0, 2, 5]
       distance_starting_2 = dijkstra_shortest_path(5, graph1, 2)
       assert(expected_distances_staring_2 == distance_starting_2)

       # Test for preoder-dfs
       expected_nodes = [0, 1, 2, 3, 4]
       print(dfs.preoder_dfs_rec(5, adj_1))

       # Test for bfs
       expected_nodes = [0, 1, 2, 3, 4]
       print(bfs.bfs(5, adj_1))