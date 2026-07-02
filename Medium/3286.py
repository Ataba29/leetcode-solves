from typing import List
from collections import deque


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        startH = health - grid[0][0]
        if startH <= 0:
            return False
        m, n = len(grid), len(grid[0])
        bestH = [[-1] * n for _ in range(m)]
        bestH[0][0] = startH

        q = deque([(0, 0)])
        while q:
            r, c = q.popleft()
            currH = bestH[r][c]
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    nextH = currH - grid[nr][nc]

                    if nextH <= 0:
                        continue

                    if nextH > bestH[nr][nc]:
                        bestH[nr][nc] = nextH
                        q.append((nr, nc))

        return bestH[-1][-1] >= 1
