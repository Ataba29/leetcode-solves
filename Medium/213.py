from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def robLinear(house):
            dp = [0] * (n - 1)
            dp[0] = house[0]
            dp[1] = max(house[0], house[1])

            for i in range(2, n - 1):
                dp[i] = max(dp[i - 2] + house[i], dp[i - 1])
            return dp[-1]

        return max(robLinear(nums[1:]), robLinear(nums[:n]))
