from collections import defaultdict
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        def Dijkstra(start):
            d = {node: float("inf") for node in range(1, n + 1)}
            d[start] = 0

            heap = [(0, start)]
            while heap:
                dist, node = heapq.heappop(heap)
                if dist > d[node]:
                    continue

                for nei, wei in graph[node]:
                    new_dist = wei + dist
                    if new_dist < d[nei]:
                        d[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))
            return d

        max_dist = max(Dijkstra(k).values())
        return max_dist if max_dist != float("inf") else -1
