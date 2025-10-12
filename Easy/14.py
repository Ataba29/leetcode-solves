from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                # Stop if i exceeds length or mismatch found
                if i >= len(s) or s[i] != char:
                    return res
            res += char
        return res
