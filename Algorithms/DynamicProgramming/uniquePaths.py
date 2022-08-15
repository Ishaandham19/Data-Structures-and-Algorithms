"""In a m x n grid. Find the number of ways it is possible to go from grid[0][0] to grid[m-1][n-1]
You can only move either down or right at any point in time."""

# Time Complexity: O(m * n)
# Space Complexity : O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        # The (m-1) row and (n-1) col have value 1 in all squares since only one path possible
        for i in range(m-2, -1, -1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]