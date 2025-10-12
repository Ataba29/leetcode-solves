from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        times = [[p, s] for p, s in zip(position, speed)]
        stk = []
        for p, s in sorted(times)[::-1]:
            timeTaken = (target - p) / s
            if not stk or timeTaken > stk[-1]:
                stk.append(timeTaken)
        return len(stk)
