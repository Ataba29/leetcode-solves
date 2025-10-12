class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # frequency arrays for 26 letters
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in range(n):
            cnt1[ord(s1[i]) - ord("a")] += 1
            cnt2[ord(s2[i]) - ord("a")] += 1

        if cnt1 == cnt2:
            return True

        for i in range(n, m):
            cnt2[ord(s2[i]) - ord("a")] += 1
            cnt2[ord(s2[i - n]) - ord("a")] -= 1
            if cnt1 == cnt2:
                return True

        return False
