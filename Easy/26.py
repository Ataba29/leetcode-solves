from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[k] = nums[i]
                k += 1
                seen.add(nums[i])

        return k
