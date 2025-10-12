from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        graph = defaultdict(list)
        for f, t, c in flights:
            graph[f].append((t, c))
        h = [(0, src, 0)]
        best = {}

        while h:
            cost, node, stops = heapq.heappop(h)
            if node == dst:
                return cost
            if stops > k:
                continue

            for nei, price in graph[node]:
                new_cost = price + cost
                if new_cost < best.get((nei, stops + 1), float("inf")):
                    best[(nei, stops + 1)] = new_cost
                    heapq.heappush(h, (cost + price, nei, stops + 1))

        return -1
