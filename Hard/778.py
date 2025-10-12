from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        h = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while h:
            height, x, y = heapq.heappop(h)

            if x == n - 1 and y == n - 1:
                return height
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if 0 <= newX < n and 0 <= newY < n and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    heapq.heappush(h, (max(height, grid[newX][newY]), newX, newY))
