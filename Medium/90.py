from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(idx, path):
            res.append(path)

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res
