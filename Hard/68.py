from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        l = 0
        curr_len = 0

        for r, word in enumerate(words):
            if curr_len + len(word) + (r - l) > maxWidth:
                ans.append(self.constructStr(words[l:r], maxWidth, curr_len))
                l = r
                curr_len = 0
            curr_len += len(word)

        ans.append(" ".join(words[l:]).ljust(maxWidth))
        return ans

    def constructStr(self, words, maxWidth, wordsLength):
        n = len(words)
        if n == 1:
            return words[0] + " " * (maxWidth - wordsLength)

        total_spaces = maxWidth - wordsLength
        space_between = total_spaces // (n - 1)
        extra = total_spaces % (n - 1)

        res = ""
        for i in range(n - 1):
            res += words[i]
            res += " " * (space_between + (1 if i < extra else 0))
        res += words[-1]

        return res
