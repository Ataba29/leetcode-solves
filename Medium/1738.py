from typing import List
import heapq


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:

        h = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                currRes = matrix[i][j]
                if j != 0:
                    currRes = currRes ^ matrix[i][j - 1]
                if i != 0:
                    currRes = currRes ^ matrix[i - 1][j]
                if j != 0 and i != 0:
                    currRes = currRes ^ matrix[i - 1][j - 1]

                if len(h) < k:
                    heapq.heappush(h, currRes)
                else:
                    temp = heapq.heappop(h)
                    heapq.heappush(h, max(temp, currRes))
                matrix[i][j] = currRes
        return h[0]


# 5 2
# 1 6

# 5 7
# 4 2

# 7 5 4 0
