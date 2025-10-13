from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:  # check for empty list
            return []
        res = []
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1] + 1:
                res.append(
                    f"{nums[l]}->{nums[r - 1]}" if l != r - 1 else f"{nums[r - 1]}"
                )
                l = r
        res.append(f"{nums[l]}->{nums[-1]}" if l != len(nums) - 1 else f"{nums[-1]}")
        return res
