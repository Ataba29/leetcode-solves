from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])

                backtrack()

                # Backtrack
                path.pop()
                used.remove(i)

        backtrack()
        return res
