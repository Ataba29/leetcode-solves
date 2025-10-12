from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = (point[0]) ** 2 + (point[1]) ** 2
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for (_, point) in heap]
