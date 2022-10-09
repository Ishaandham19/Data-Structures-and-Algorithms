"""
Cycle Detection Algorithm : Uses DFS to determine wether a graph has a cycle.
The graph can be disconnected hence we start a dfs for every vertex, and keep a "stack" that tracks the vertices visited in that dfs run.
The optimization in this algorithm is to categorize vertices into processing and processed. 
    If a vertex is processed, that means it is visited in a previous dfs and hence we don't call dfs on it again.
    if a vertex is processing, that mean it is visited in the same dfs run, and we have a cycle.

Essentially, we check for back edges. If no back edges, the graph is acyclic.
Time Complexity - O(V + E)
Space Complexity - O(V)


Solution (heavily) inspired from: https://leetcode.com/problems/course-schedule/discuss/441722/Python-99-time-and-100-space.-Collection-of-solutions-with-explanation
"""

def cycleDetection(adj_list):
    visited = [False] * len(adj_list)

    def hasCycle(v, stack):
        if visited[v]:
            if v in stack:
                # This vertex is processing and it means we have a cycle.
                return True
            # This vertex is processed so we pass
            return False

        # mark this vertex as visited
        visited[v] = True
        # add it to the current stack   
        stack.append(v)

        for i in adj_list[v]:
            if hasCycle(i, stack):
                return True

        # once processed, we pop it out of the stack
        stack.pop()
        return False

    # we traverse each vertex using DFS, if we find a cycle, stop and return
    for v in range(len(adj_list)):
        if hasCycle(v, []):
            return False

    return True

