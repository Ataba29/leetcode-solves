from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if (
                        x + dx >= rows
                        or y + dy >= cols
                        or x + dx < 0
                        or y + dy < 0
                        or grid[x + dx][y + dy] != 1
                    ):
                        continue
                    fresh -= 1
                    grid[x + dx][y + dy] = 2
                    q.append(((x + dx), (y + dy)))

            time += 1

        return time if fresh == 0 else -1
