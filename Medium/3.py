class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        uni = set()

        for r in range(len(s)):
            while s[r] in uni:
                uni.remove(s[l])
                l += 1
            uni.add(s[r])
            res = max(res, len(uni))
        return res
