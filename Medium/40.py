from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(idx, path, total):
            if total == target:
                res.append(path)
                return
            if idx >= len(candidates) or total > target:
                return

            for i in range(idx, len(candidates)):
                val = candidates[i]
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [val], total + val)

        backtrack(0, [], 0)
        return res
