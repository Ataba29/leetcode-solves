from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        m = len(s)
        n = len(t)
        if m < n:
            return res
        l = 0
        min_freq = float("inf")
        map_t = Counter(t)
        map_s = Counter()

        for r in range(m):
            map_s[s[r]] += 1

            while self.checkMaps(map_t, map_s):
                if r - l + 1 < min_freq:
                    min_freq = r - l + 1
                    res = s[l : r + 1]
                map_s[s[l]] -= 1
                l += 1
        return res

    def checkMaps(self, map_t: Counter, map_s: Counter) -> bool:
        for ch, freq in map_t.items():
            if freq > map_s[ch]:
                return False
        return True
