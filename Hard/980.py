from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        start_r = start_c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total += 1
                if grid[i][j] == 1:
                    start_r, start_c = i, j

        res = 0
        visited = set()

        def dfs(r, c, count):
            nonlocal res

            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid[r][c] == -1 or (r, c) in visited:
                return

            if grid[r][c] == 2 and count == total:
                res += 1
                return

            visited.add((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, count + 1)

            visited.remove((r, c))

        dfs(start_r, start_c, 1)
        return res
