from collections import defaultdict
from typing import List
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        itinerary = []

        def dfs(node):
            while graph[node]:
                next_dest = heapq.heappop(graph[node])
                dfs(next_dest)
            itinerary.append(node)

        dfs("JFK")
        itinerary.reverse()
        return itinerary
