from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stk = []
        n = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                idx, height = stk.pop()
                maxArea = max(maxArea, (i - idx) * height)
                start = idx
            stk.append([start, h])

        for i, h in stk:
            maxArea = max(maxArea, (n - i) * h)

        return maxArea
