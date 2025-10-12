from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = max([dp[j] + 1 for j in range(i) if nums[j] < nums[i]], default=1)
        return max(dp)
