from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_count = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == num:
                curr_count += 1
            else:
                curr_count -= 1

            if curr_count < 0:
                num = nums[i]
                curr_count = 1

        return num
