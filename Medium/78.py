from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, path):
            if idx == len(nums):
                res.append(path)
                return

            backtrack(idx + 1, path + [nums[idx]])
            backtrack(idx + 1, path)

        backtrack(0, [])
        return res
