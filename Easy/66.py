from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + c
            c = 0
            if digits[i] >= 10:
                digits[i] -= 10
                c = 1

        return digits if c != 1 else [1] + digits
