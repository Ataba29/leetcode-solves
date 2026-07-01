from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float("inf")

        for idx, num in enumerate(nums):
            if num == target:
                res = min(res, abs(idx - start))

        return res
