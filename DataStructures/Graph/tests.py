from dijkstraShortestPath import dijkstra_shortest_path
import dfs
import bfs

if __name__ == "__main__":
       # Adjacency list of graph1 with weights
       graph1 = [[(1, 3), (2, 1)], 
              [(0, 3), (2, 7), (3, 5), (4, 1)],
              [(0, 1), (1, 7), (3, 2)],
              [(1, 5), (2, 2), (4, 7)],
              [(1, 1), (3, 7)]]


       graph2 = []

       # Adjacency list of graph1 without weights
       adj_list_1 = [[1, 2], [0, 2, 3, 4], [0, 1, 3], [1, 2, 4], [1, 3]]

       adj_list_2 = []

       # Test for Dijkstra shortest path       
       expected_distances_staring_2 = [1, 4, 0, 2, 5]
       distance_starting_2 = dijkstra_shortest_path(5, graph1, 2)
       assert(expected_distances_staring_2 == distance_starting_2)

       # Test for preoder-dfs
       expected_nodes_1 = [0, 1, 2, 3, 4]
       expected_nodes_2 = []

       nodes1 = dfs.preoder_dfs_rec(5, adj_list_1)
       nodes2 = dfs.preorder_dfs_itr(5, adj_list_1)
       assert expected_nodes_1 == nodes1
       assert expected_nodes_1 == nodes2
       print(dfs.preoder_dfs_rec(5, adj_list_1))

       nodes1 = dfs.preoder_dfs_rec(5, adj_list_2)
       nodes2 = dfs.preorder_dfs_itr(5, adj_list_2)
       assert expected_nodes_2 == nodes1
       assert expected_nodes_2 == nodes2
       print(dfs.preoder_dfs_rec(5, adj_list_2))

       # Test for bfs
       expected_nodes = [0, 1, 2, 3, 4]
       print(bfs.bfs(5, adj_list_1))