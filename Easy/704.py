from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = nums[mid]
            if val == target:
                return mid
            if val > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
