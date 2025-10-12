class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = ""
        reslen = 0

        def expand(l, r):
            nonlocal res, reslen
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > reslen:
                    res = s[l : r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i - 1)

        return res
