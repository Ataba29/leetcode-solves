class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        res = 0
        for i in range(len(s) - 1):
            res += int(s[i] != s[i + 1])
        return res
