from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        def backtrack(start: int, path: str):
            if start == len(digits):
                res.append(path)
                return

            for letter in digit_map[digits[start]]:
                backtrack(start + 1, path + letter)

        backtrack(0, "")
        return res
