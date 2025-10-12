import math


class Solution:
    def findIntegers(self, n: int) -> int:
        length = int(math.log2(n)) + 1
        if length < 3:
            return length + 1
        dp = [0] * length
        dp[0] = 1
        dp[1] = 2

        for i in range(2, length):
            dp[i] = dp[i - 1] + dp[i - 2]

        k = length - 1
        pre = 0
        ans = 0
        while k >= 0:
            if n & (1 << k) != 0:
                ans += dp[k]
                if pre == 1:
                    return ans
                pre = 1
            else:
                pre = 0
            k -= 1
        return ans + 1
