from typing import List


class Solution:
    def calcTime(self, piles: List[int], k: int) -> int:
        h = 0
        for p in piles:
            h += (p + k - 1) // k
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            hours = self.calcTime(piles, mid)
            if hours <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


sol = Solution()
print(sol.minEatingSpeed([312884470], 312884469))
