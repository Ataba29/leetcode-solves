from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev_len = 0
        start = 0
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] <= nums[i - 1]:
                length = i - start
                if prev_len >= k and length >= k or length >= 2 * k:
                    return True
                prev_len = length
                start = i
        return False
