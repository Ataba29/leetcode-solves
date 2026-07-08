from typing import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        for ch in list(count):
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]
            if len(set(count.values())) == 1:
                return True
            count[ch] += 1

        return False
