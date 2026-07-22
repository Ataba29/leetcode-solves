from typing import List
from collections import deque


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = deque()
        total = 0


        for op in operations:
            if op == "D":
                s.append(s[-1] * 2)
                total += s[-1]
            elif op == "C":
                temp = s.pop()
                total -= temp
            elif op == "+":
                score1 = s[-1]
                score2 = s[-2]
                s.append(score1+score2)
                total += score2 + score1
            else:
                s.append(int(op))
                total += s[-1]
                
        return total