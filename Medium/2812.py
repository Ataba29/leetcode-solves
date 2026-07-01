from typing import List
from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float("inf")] * n for _ in range(n)]

        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in d:
                if 0 <= r + dr <= n - 1 and 0 <= c + dc <= n - 1:
                    if dist[r + dr][c + dc] == float("inf"):
                        dist[r + dr][c + dc] = dist[r][c] + 1
                        q.append((r + dr, c + dc))

        heap = []
        heapq.heappush(heap, (-dist[0][0], 0, 0))
        visited = set()

        while heap:
            s, r, c = heapq.heappop(heap)
            s = -s

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return s

            for dr, dc in d:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        new_s = min(s, dist[nr][nc])
                        heapq.heappush(heap, (-new_s, nr, nc))
