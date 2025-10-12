class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letterFound = False
        res = 0
        for ch in s[::-1]:
            if letterFound:
                if ch != " ":
                    res += 1
                else:
                    return res
            elif ch.isalpha():
                letterFound = True
                res = 1
        return res
