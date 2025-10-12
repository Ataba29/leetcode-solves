from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(x, y, visited):
            if (x, y) in visited:
                return
            visited.add((x, y))

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and heights[nx][ny] >= heights[x][y]
                ):
                    dfs(nx, ny, visited)

        for r in range(rows):
            dfs(r, 0, pacific)
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        return [list(cell) for cell in pacific & atlantic]
