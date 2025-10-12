from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start: int, path: List[str]):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if self.isPalindrome(sub):
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res
