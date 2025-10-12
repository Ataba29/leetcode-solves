from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] + [amount + 1] * amount

        for i in range(1, amount + 1):
            for c in coins:
                if not i - c < 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return -1 if dp[amount] == amount + 1 else dp[amount]
