class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ""
        starter = True
        while i < len(word1) and j < len(word2):
            if starter:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1

            starter = not starter

        while i < len(word1):
            res += word1[i]
            i += 1
        while j < len(word2):
            res += word2[j]
            j += 1

        return res
