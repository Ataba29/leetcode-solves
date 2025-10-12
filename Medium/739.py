from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []

        for idx, temp in enumerate(temperatures):
            while stk:
                x = stk[-1]
                if temp - x[1] > 0:
                    res[x[0]] = idx - x[0]
                    stk.pop()
                else:
                    break
            stk.append([idx, temp])

        return res


sol = Solution()


print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
