from collections import Counter


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        res = 0
        for word in words:
            word = set(word)
            canFrom = True
            for ch in brokenLetters:
                if ch in word:
                    canFrom = False
            if canFrom:
                res += 1

        return res
