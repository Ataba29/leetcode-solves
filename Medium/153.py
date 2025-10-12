from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, n - 1
        res = nums[r]
        while l <= r:
            mid = l + (r - l) // 2
            val = nums[mid]
            if val > nums[r]:
                l = mid + 1
            else:
                res = min(val, res)
                r = mid - 1
        return res
