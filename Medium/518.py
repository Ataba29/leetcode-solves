from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        dp = [[0] * (amount + 1) for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for i in range(m):
            for j in range(1, amount + 1):
                val = 0
                if i - 1 >= 0:
                    val += dp[i - 1][j]
                val2 = 0
                if j - coins[i] >= 0:
                    val2 = dp[i][j - coins[i]]
                dp[i][j] = val + val2

        return dp[m - 1][amount]
