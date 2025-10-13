from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res = res ^ num

        diff_bit = 1
        while not (res & diff_bit):
            diff_bit <<= 1

        a, b = 0, 0
        for n in nums:
            if diff_bit & n:
                a = a ^ n
            else:
                b = b ^ n
        return [a, b]
