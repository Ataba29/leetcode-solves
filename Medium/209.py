from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        curr_len = 0
        res = len(nums)
        for r in range(len(nums)):
            curr_len += 1
            curr_sum += nums[r]

            while target <= curr_sum:
                res = min(res, curr_len)
                curr_sum -= nums[l]
                l += 1
                curr_len -= 1
        return res if sum(nums) >= target else 0
