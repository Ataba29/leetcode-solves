from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        temp = 1
        for i in range(1, n + 1):
            if temp * 2 == i:
                temp = i
            res[i] = 1 + res[i - temp]
        return res
