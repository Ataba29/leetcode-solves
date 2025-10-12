from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        pairs = [0] * len(spells)
        potions.sort()
        m = len(potions)

        for i in range(len(pairs)):
            idx = self.binarySearch(success, spells[i], potions)
            pairs[i] = m - idx

        return pairs

    def binarySearch(self, target, mult, arr):
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (r + l) // 2
            if arr[mid] * mult >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l
