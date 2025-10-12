import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        h = [(0, 0)]
        mst_cost = 0
        count = 0
        while h and count < n:
            weight, u = heapq.heappop(h)
            if visited[u]:
                continue
            visited[u] = True
            mst_cost += weight
            count += 1

            for v in range(n):
                if not visited[v]:
                    val = abs(points[u][0] - points[v][0]) + abs(
                        points[u][1] - points[v][1]
                    )
                    heapq.heappush(h, (val, v))
        return mst_cost
