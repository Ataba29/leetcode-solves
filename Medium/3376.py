from typing import List


class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:

        memo = {}

        def backtrack(visited: set, x: int) -> int:
            key = tuple(sorted(visited))
            if key in memo:
                return memo[key]

            if len(visited) == len(strength):
                return 0

            res = float("inf")

            for idx, stren in enumerate(strength):
                if idx not in visited:
                    visited.add(idx)
                    need = stren
                    wait = (need + x - 1) // x
                    res = min(res, wait + backtrack(visited, x + k))
                    visited.remove(idx)

            memo[key] = res
            return int(res)

        return backtrack(set(), 1)