from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, summ):
            if summ == target:
                res.append(path[:])
                return
            if summ > target or start == len(candidates):
                return
            backtrack(start, path + [candidates[start]], summ + candidates[start])
            backtrack(start + 1, path, summ)

        backtrack(0, [], 0)
        return res
