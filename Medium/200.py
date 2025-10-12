from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y):
            if x >= rows or y >= cols or x < 0 or y < 0 or grid[x][y] == "0":
                return

            grid[x][y] = "0"
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(x + dx, y + dy)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res
