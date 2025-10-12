class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = [0] * 26
        for ch in sentence:
            count[ord(ch) - ord("a")] += 1
        return not min(count) == 0
