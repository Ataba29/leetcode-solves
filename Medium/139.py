from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # empty string can always be segmented

        for i in range(1, n + 1):
            for word in wordDict:
                if len(word) <= i and s[i - len(word) : i] == word:
                    dp[i] = dp[i] or dp[i - len(word)]

        return dp[n]
