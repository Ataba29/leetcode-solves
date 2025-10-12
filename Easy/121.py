from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_prof, max_prof = prices[0], 0

        for p in prices[1:]:
            if curr_prof > p:
                curr_prof = p
            max_prof = max(max_prof, p - curr_prof)

        return max_prof
