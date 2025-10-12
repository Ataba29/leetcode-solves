from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        for ch in ransomCounter.keys():
            if ch not in magazineCounter or ransomCounter[ch] > magazineCounter[ch]:
                return False
        return True
