from typing import List
from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0
        freq = Counter(power)
        vals = sorted(freq.keys())
        n = len(vals)

        dp = [0] * n
        dp[0] = vals[0] * freq[vals[0]]

        for i in range(1, n):
            damage = vals[i] * freq[vals[i]]
            j = i - 1

            while j >= 0 and vals[i] - vals[j] <= 2:
                j -= 1

            if j >= 0:
                dp[i] = max(dp[i - 1], dp[j] + damage)
            else:
                dp[i] = max(dp[i - 1], damage)

        return dp[-1]
