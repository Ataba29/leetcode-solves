from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            if val > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


sol = Solution()

print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
