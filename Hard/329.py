from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = {}  # (i, j) -> max_path_length

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            best = 1
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                px, py = i + dx, j + dy
                if 0 <= px < rows and 0 <= py < cols and matrix[px][py] > matrix[i][j]:
                    best = max(best, 1 + dfs(px, py))
            dp[(i, j)] = best
            return best

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans
