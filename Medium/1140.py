from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def dfs(player, i, M):
            if i == len(piles):
                return 0

            if (player, i, M) in memo:
                return memo[(player, i, M)]

            res = 0 if player else float("inf")
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                total += piles[i + X - 1]
                if player:
                    res = max(res, total + dfs(not player, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not player, i + X, max(M, X)))
            memo[(player, i, M)] = res
            return res

        return dfs(True, 0, 1)
