from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        n = len(nums)
        res = []
        for r in range(n):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

        return res
