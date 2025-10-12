from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            newStone = y - x
            if newStone > 0:
                heapq.heappush(stones, -newStone)

        return -stones[0] if len(stones) > 0 else 0
