from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        steps = 0
        start = 0

        while steps < n:
            idx = start
            temp = nums[idx]
            while True:
                nxt = (idx + k) % n
                nums[nxt], temp = temp, nums[nxt]
                idx = nxt
                steps += 1
                if idx == start:
                    break
            start += 1
